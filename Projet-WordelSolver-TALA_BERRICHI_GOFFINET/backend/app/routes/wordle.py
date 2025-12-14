from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from app.data.load_fr_word import load_fr_words
from app.data.load_en_word import load_en_words
from app.services.wordle_solver import HybridWordleSolver
from app.models.schemas import Feedback
from app.services.llm_service import GeminiLLM
from app.models.schemas import Feedback, WordSuggestionsRequest


router = APIRouter()

# Charger dictionnaires
words_fr = load_fr_words()
words_en = load_en_words()

solver_fr = HybridWordleSolver(words_fr)
solver_en = HybridWordleSolver(words_en)
llm_service = GeminiLLM()

class WordleRequest(BaseModel):
    feedback: Feedback
    language: Optional[str] = "fr"
    use_llm: Optional[bool] = False

@router.post("/guess")
def make_guess(req: WordleRequest):
    lang = (req.language or "fr").lower()
    solver = solver_fr if lang == "fr" else solver_en if lang == "en" else None
    if solver is None:
        raise HTTPException(status_code=400, detail="Langue non supportée.")

    solver.update_constraints(req.feedback.dict())
    next_guess, explanation = solver.get_next_guess(language=lang)

    # Si LLM demandé
    if req.use_llm:
        try:
            llm_word, llm_explanation = llm_service.suggest_word(
                candidates=solver.csp.filter_candidates(solver.constraints),
                feedback_history=[solver.constraints_dict()],
                word_length=5,
                language=lang
            )
            return {"next_guess": llm_word, "explanation": llm_explanation}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Erreur LLM Gemini : {str(e)}")

    return {"next_guess": next_guess, "explanation": explanation}

@router.post("/suggest-ai")
def suggest_with_ai(req: WordSuggestionsRequest):
    """Route dédiée pour obtenir une suggestion IA basée sur les contraintes actuelles"""
    print(f"📥 Requête reçue - Language: {req.language}")
    print(f"📥 Feedback: {req.feedback.dict()}")
    
    lang = req.language.lower()
    solver = solver_fr if lang == "fr" else solver_en if lang == "en" else None
    if solver is None:
        raise HTTPException(status_code=400, detail="Langue non supportée.")

    try:
        # Étape 1: Mettre à jour les contraintes
        print("🔄 Étape 1: Mise à jour des contraintes...")
        solver.update_constraints(req.feedback.dict())
        print("✅ Contraintes mises à jour")
        
        # Étape 2: Obtenir les candidats du CSP
        print("🔍 Étape 2: Filtrage des candidats...")
        candidates = solver.csp.filter_candidates(solver.constraints)
        print(f"✅ {len(candidates)} candidats trouvés")
        
        if not candidates:
            raise HTTPException(status_code=400, detail="Aucun candidat trouvé avec ces contraintes")
        
        # Étape 3: Appel au LLM
        print(f"🤖 Étape 3: Appel au LLM avec {min(50, len(candidates))} candidats...")
        candidates_list = list(candidates)[:50]
        print(f"Candidats envoyés au LLM: {candidates_list[:10]}...")
        
        llm_word, llm_explanation = llm_service.suggest_word(
            candidates=candidates_list,
            feedback_history=[],
            word_length=5,
            language=lang
        )
        
        print(f"✅ LLM a répondu: {llm_word}")
        
        return {
            "suggested_word": llm_word.upper(), 
            "explanation": llm_explanation,
            "candidates_count": len(candidates)
        }
        
    except HTTPException:
        raise
    except Exception as e:
        print(f"❌ ERREUR DÉTAILLÉE:")
        print(f"Type: {type(e).__name__}")
        print(f"Message: {str(e)}")
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Erreur : {str(e)}")