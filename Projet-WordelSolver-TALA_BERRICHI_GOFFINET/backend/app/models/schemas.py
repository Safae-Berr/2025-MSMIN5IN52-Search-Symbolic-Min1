# backend/app/models/schemas.py
from typing import Dict, List
from pydantic import BaseModel, Field

class Feedback(BaseModel):
    """
    Schéma représentant le feedback d'une proposition Wordle.
    """
    green: Dict[str, str] = Field(default_factory=dict)
    yellow: Dict[str, List[str]] = Field(default_factory=dict)
    grey: List[str] = Field(default_factory=list)

class WordGuessRequest(BaseModel):
    """
    Requête envoyée pour proposer un mot ou demander une suggestion.
    """
    word: str = Field(..., description="Le mot proposé par l'utilisateur")

class WordSuggestionsRequest(BaseModel):
    """
    Requête pour obtenir des suggestions de mots depuis le solveur.
    """
    feedback: Feedback = Field(..., description="Feedback des tentatives précédentes")
    language: str = Field("fr", description="Langue du jeu ('fr' ou 'en')")
    previous_guesses: List[str] = Field(
        default_factory=list,
        description="Liste des mots déjà essayés pour éviter les répétitions"
    )

class WordSuggestionsResponse(BaseModel):
    """
    Réponse du solveur Wordle avec liste de mots candidats.
    """
    suggestions: List[str] = Field(..., description="Liste de mots candidats proposés")