#!/usr/bin/env python3
"""Script de débogage pour le problème COURT vs ROBOT."""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

from wordle_solver import (
    ConstraintManager,
    generate_feedback,
    DictionaryLoader,
    HybridSolver
)

def debug_court_problem():
    print("="*70)
    print("DEBUG: Problème COURT vs ROBOT")
    print("="*70)
    
    # Initialiser
    dictionary = DictionaryLoader.load_english()
    solver = HybridSolver(dictionary)
    cm = ConstraintManager()
    
    # Feedback 1: AROSE vs ROBOT
    print("\n1️⃣ Feedback: AROSE vs ROBOT")
    fb1 = generate_feedback("AROSE", "ROBOT")
    print(f"   Résultat: {fb1}")
    cm.apply_feedback(fb1)
    
    summary1 = cm.get_constraint_summary()
    print(f"   Contraintes:")
    print(f"     - Positions correctes: {summary1['correct_positions']}")
    print(f"     - Lettres présentes: {summary1['present_letters']}")
    print(f"     - Lettres absentes: {summary1['absent_letters']}")
    print(f"     - Compteurs: {summary1['letter_counts']}")
    
    possible1 = solver.get_possible_words(cm, limit=20)
    print(f"   Mots possibles ({len(possible1)}): {sorted(possible1)[:10]}")
    print(f"   ROBOT dans les possibles? {' ROBOT' in possible1}")
    
    # Feedback 2: COURT vs ROBOT
    print("\n2️⃣ Feedback: COURT vs ROBOT")
    fb2 = generate_feedback("COURT", "ROBOT")
    print(f"   Résultat: {fb2}")
    
    # Détailler le feedback
    for i, (letter, fb) in enumerate(zip("COURT", fb2.feedbacks)):
        print(f"     {i}: {letter} → {fb.value}")
    
    cm.apply_feedback(fb2)
    
    summary2 = cm.get_constraint_summary()
    print(f"   Contraintes après COURT:")
    print(f"     - Positions correctes: {summary2['correct_positions']}")
    print(f"     - Lettres présentes: {summary2['present_letters']}")
    print(f"     - Lettres absentes: {summary2['absent_letters']}")
    print(f"     - Compteurs: {summary2['letter_counts']}")
    
    # Vérifier ROBOT manuellement
    print("\n3️⃣ Vérification manuelle de ROBOT")
    print("   ROBOT = R(0) O(1) B(2) O(3) T(4)")
    
    # Test position par position
    word = "ROBOT"
    for pos, letter in enumerate(word):
        if pos in summary2['correct_positions']:
            expected = summary2['correct_positions'][pos]
            match = "✓" if letter == expected else "✗"
            print(f"     Pos {pos}: {letter} - attendu {expected} {match}")
        else:
            print(f"     Pos {pos}: {letter} - pas de contrainte")
    
    # Test lettres présentes
    print("\n   Lettres présentes:")
    for letter, forbidden_pos in summary2['present_letters'].items():
        if letter in word:
            positions_in_word = [i for i, l in enumerate(word) if l == letter]
            conflicts = set(positions_in_word) & set(forbidden_pos)
            status = "✗ CONFLIT" if conflicts else "✓"
            print(f"     {letter}: doit être présent, pas aux pos {forbidden_pos}")
            print(f"        → dans ROBOT aux pos {positions_in_word} {status}")
        else:
            print(f"     {letter}: MANQUANT dans ROBOT ✗")
    
    # Test lettres absentes
    print("\n   Lettres absentes:")
    for letter in summary2['absent_letters']:
        present = "✗ PRÉSENT" if letter in word else "✓"
        print(f"     {letter}: ne doit pas être présent {present}")
    
    # Test contraintes de fréquence
    print("\n   Contraintes de fréquence:")
    from collections import Counter
    word_counts = Counter(word)
    for letter, (min_count, max_count) in summary2['letter_counts'].items():
        actual_count = word_counts.get(letter, 0)
        min_ok = actual_count >= min_count
        max_ok = max_count is None or actual_count <= max_count
        status = "✓" if (min_ok and max_ok) else "✗"
        print(f"     {letter}: min={min_count}, max={max_count}, actual={actual_count} {status}")
    
    # Test final avec is_word_valid
    print("\n4️⃣ Test is_word_valid('ROBOT')")
    is_valid = cm.is_word_valid("ROBOT")
    print(f"   Résultat: {is_valid}")
    
    if not is_valid:
        print("   ❌ ROBOT est considéré invalide alors qu'il devrait être valide!")
    else:
        print("   ✓ ROBOT est valide")
    
    # Chercher les mots possibles
    possible2 = solver.get_possible_words(cm, limit=20)
    print(f"\n   Mots possibles ({len(possible2)}): {sorted(possible2)}")
    
    print("\n" + "="*70)

if __name__ == "__main__":
    debug_court_problem()
