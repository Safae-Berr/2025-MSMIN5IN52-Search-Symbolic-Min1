"""
Exemple basique d'utilisation du solveur Wordle CSP.

Cet exemple montre comment :
1. Charger un dictionnaire
2. Créer une partie de Wordle
3. Utiliser le solveur CSP pour trouver des mots possibles
4. Résoudre progressivement le puzzle
"""

import sys
from pathlib import Path

# Ajouter le dossier parent au path
sys.path.insert(0, str(Path(__file__).parent.parent))

from wordle_solver import (
    WordleGame,
    HybridSolver,
    ConstraintManager,
    DictionaryLoader,
    generate_feedback
)


def print_separator():
    """Affiche un séparateur visuel."""
    print("\n" + "="*70 + "\n")


def display_feedback(feedback):
    """Affiche le feedback de manière lisible."""
    print(f"  {feedback.to_string()}")
    

def solve_wordle_step_by_step(target_word: str, language: str = "en"):
    """
    Résout un Wordle étape par étape en affichant chaque décision.
    
    Args:
        target_word: Le mot à deviner
        language: Langue du dictionnaire ('en' ou 'fr')
    """
    print_separator()
    print(f"🎮 WORDLE SOLVER - Résolution de : {target_word}")
    print_separator()
    
    # Charger le dictionnaire
    print(f"📚 Chargement du dictionnaire {language.upper()}...")
    dictionary = DictionaryLoader.load_language(language)
    print(f"   ✓ {len(dictionary)} mots chargés")
    
    # Initialiser le solveur et le gestionnaire de contraintes
    print("\n🔧 Initialisation du solveur CSP...")
    solver = HybridSolver(dictionary)
    constraint_manager = ConstraintManager()
    print("   ✓ Solveur prêt")
    
    # Créer la partie
    game = WordleGame(target_word)
    
    # Liste de mots de départ recommandés
    starter_words = {
        'en': ['AROSE', 'SLATE', 'CRANE', 'ADIEU'],
        'fr': ['AIMER', 'ARBRE', 'AUTRE', 'FAIRE']
    }
    
    print(f"\n🎯 Partie initialisée - Mot cible : {'*' * len(target_word)}")
    print(f"📊 Nombre de mots possibles initialement : {len(dictionary)}")
    
    attempt = 1
    
    while not game.is_over:
        print_separator()
        print(f"🎲 TENTATIVE {attempt}/6")
        print_separator()
        
        # Obtenir les mots possibles
        possible_words = solver.get_possible_words(constraint_manager)
        
        print(f"📊 Mots possibles : {len(possible_words)}")
        
        if len(possible_words) <= 10:
            print(f"   Candidats : {', '.join(sorted(possible_words)[:10])}")
        else:
            print(f"   Échantillon : {', '.join(sorted(possible_words)[:10])}...")
        
        # Choisir un mot
        if attempt == 1:
            # Utiliser un mot de départ recommandé
            guess = starter_words[language][0]
            print(f"\n💡 Utilisation d'un mot de départ optimal : {guess}")
        else:
            # Choisir le premier mot alphabétiquement (stratégie simple)
            if possible_words:
                guess = sorted(possible_words)[0]
                print(f"\n💭 Choix du mot : {guess}")
            else:
                print("\n❌ Aucun mot possible trouvé !")
                break
        
        # Faire la tentative
        try:
            feedback = game.make_guess(guess)
            display_feedback(feedback)
            
            # Afficher les détails du feedback
            correct_positions = feedback.get_correct_positions()
            present_letters = feedback.get_present_letters()
            absent_letters = feedback.get_absent_letters()
            
            if correct_positions:
                print(f"   ✅ Lettres correctes : {correct_positions}")
            if present_letters:
                print(f"   🟡 Lettres présentes : {present_letters}")
            if absent_letters:
                print(f"   ⬜ Lettres absentes : {absent_letters}")
            
            # Appliquer les contraintes
            constraint_manager.apply_feedback(feedback)
            
            # Afficher l'état des contraintes
            summary = constraint_manager.get_constraint_summary()
            print(f"\n📋 État des contraintes :")
            print(f"   - Positions connues : {len(summary['correct_positions'])}/5")
            print(f"   - Lettres présentes : {len(summary['present_letters'])}")
            print(f"   - Lettres absentes : {len(summary['absent_letters'])}")
            
            attempt += 1
            
        except ValueError as e:
            print(f"   ❌ Erreur : {e}")
            break
    
    # Résultat final
    print_separator()
    if game.is_won:
        print(f"🎉 VICTOIRE ! Mot trouvé en {len(game.attempts)} tentative(s)")
    else:
        print(f"😞 DÉFAITE ! Le mot était : {target_word}")
    print_separator()
    
    # Afficher l'historique
    print("\n📜 Historique des tentatives :")
    for i, fb in enumerate(game.get_history(), 1):
        print(f"   {i}. {fb.to_string()}")
    
    return game.is_won, len(game.attempts)


def demonstrate_constraint_system():
    """Démontre le système de contraintes étape par étape."""
    print_separator()
    print("🔬 DÉMONSTRATION DU SYSTÈME DE CONTRAINTES")
    print_separator()
    
    # Créer un scénario simple
    target = "ROBOT"
    guess1 = "AROSE"
    
    print(f"Mot cible : {target}")
    print(f"Tentative : {guess1}")
    
    # Générer le feedback
    feedback = generate_feedback(guess1, target)
    print(f"Feedback : {feedback.to_string()}")
    
    # Créer et appliquer les contraintes
    cm = ConstraintManager()
    cm.apply_feedback(feedback)
    
    # Afficher les contraintes
    summary = cm.get_constraint_summary()
    print(f"\n📋 Contraintes extraites :")
    print(f"   Positions correctes : {summary['correct_positions']}")
    print(f"   Lettres présentes : {summary['present_letters']}")
    print(f"   Lettres absentes : {summary['absent_letters']}")
    print(f"   Contraintes de fréquence : {summary['letter_counts']}")
    
    # Tester quelques mots
    test_words = ["ROBOT", "ROOST", "RUMOR", "ROVER"]
    print(f"\n🧪 Test de validité des mots :")
    for word in test_words:
        is_valid = cm.is_word_valid(word)
        status = "✅" if is_valid else "❌"
        print(f"   {status} {word}: {'valide' if is_valid else 'invalide'}")


def main():
    """Fonction principale."""
    print("\n" + "="*70)
    print(" "*20 + "WORDLE SOLVER - DEMO")
    print("="*70 + "\n")
    
    # Démonstration 1 : Système de contraintes
    demonstrate_constraint_system()
    
    input("\n\nAppuyez sur Entrée pour continuer vers la résolution complète...")
    
    # Démonstration 2 : Résolution complète (anglais)
    solve_wordle_step_by_step("ROBOT", language="en")
    
    input("\n\nAppuyez sur Entrée pour essayer un exemple en français...")
    
    # Démonstration 3 : Résolution complète (français)
    solve_wordle_step_by_step("ARBRE", language="fr")
    
    print("\n" + "="*70)
    print(" "*25 + "FIN DE LA DEMO")
    print("="*70 + "\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Interruption par l'utilisateur")
    except Exception as e:
        print(f"\n\n❌ Erreur : {e}")
        import traceback
        traceback.print_exc()
