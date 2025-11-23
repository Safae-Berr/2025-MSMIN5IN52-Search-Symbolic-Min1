# Wordle Solver - Solveur Intelligent CSP + IA avec Interface Web

Un solveur de Wordle avancé combinant la **programmation par contraintes (CSP)** avec **OR-Tools**, des **stratégies d'optimisation intelligentes**, et une **interface web React interactive**.

## 🎯 Caractéristiques

- ✅ **Moteur CSP** : Résolution efficace avec OR-Tools CP-SAT
- 🧠 **Stratégies intelligentes** : Fréquence, Entropie, Minimax
- 🌐 **Interface Web** : Application React moderne et responsive
- 🚀 **API REST** : Backend FastAPI performant
- 🌍 **Multilingue** : Support FR/EN
- 📊 **Statistiques** : Analyse en temps réel
- 🎮 **Modes multiples** : Manuel avec assistance IA

## 🚀 Installation et Démarrage Rapide

### Prérequis
- Python 3.8+
- Node.js 16+
- npm ou yarn

### 1. Installation du Backend

```bash
# Depuis le dossier racine
cd backend

# Installer les dépendances Python
pip install -r requirements.txt
pip install -r ../requirements.txt

# Démarrer le serveur API
python main.py
```

Le backend sera accessible sur `http://localhost:8000`

### 2. Installation du Frontend

```bash
# Dans un nouveau terminal, depuis le dossier racine
cd frontend

# Installer les dépendances Node.js
npm install

# Démarrer le serveur de développement
npm run dev
```

L'interface web sera accessible sur `http://localhost:3000`

### 3. Utilisation

1. Ouvrez votre navigateur sur `http://localhost:3000`
2. Configurez la langue et la stratégie dans les paramètres
3. Cliquez sur "Démarrer" pour commencer une partie
4. Utilisez le clavier virtuel ou physique pour entrer vos tentatives
5. Obtenez des suggestions intelligentes en temps réel
6. Visualisez les mots possibles et les contraintes

## 🏗️ Architecture du Projet

```
wordle-solver/
├── backend/                 # API FastAPI
│   ├── main.py             # Serveur API
│   ├── requirements.txt    # Dépendances backend
│   └── README.md           # Documentation backend
├── frontend/                # Application React
│   ├── src/
│   │   ├── components/     # Composants React
│   │   ├── services/       # Client API
│   │   └── App.jsx         # Application principale
│   ├── package.json        # Dépendances frontend
│   └── README.md           # Documentation frontend
├── wordle_solver/           # Package Python principal
│   ├── csp/                # Module CSP (moteur)
│   ├── strategies/         # Stratégies d'optimisation
│   ├── game/               # Simulation Wordle
│   └── dictionaries/       # Dictionnaires FR/EN
├── examples/               # Exemples d'utilisation
├── tests/                  # Tests unitaires
└── docs/                   # Documentation

## 📦 Dépendances principales

- `ortools` : Moteur CSP
- `anthropic` : API Claude pour LLM
- `numpy`, `scipy` : Calculs numériques
- `rich`, `click` : Interface CLI

## 🎮 Utilisation

### 🌐 Interface Web (Recommandé)

L'interface web offre la meilleure expérience utilisateur :

1. **Démarrer le backend** : `cd backend && python main.py`
2. **Démarrer le frontend** : `cd frontend && npm run dev`
3. Accéder à `http://localhost:3000`

**Fonctionnalités** :
- Interface de jeu intuitive avec clavier virtuel
- Suggestions IA en temps réel
- Visualisation des mots possibles
- Statistiques et contraintes en direct
- Support multi-langues et multi-stratégies

### 📚 Mode Python (Programmation)

```python
from wordle_solver import WordleGame, HybridSolver, ConstraintManager, DictionaryLoader
from wordle_solver.strategies import FrequencyStrategy

# Charger le dictionnaire
dictionary = DictionaryLoader.load_english()

# Créer le solveur avec une stratégie
solver = HybridSolver(dictionary)
strategy = FrequencyStrategy()
constraint_manager = ConstraintManager()

# Créer une partie
game = WordleGame("ROBOT")

# Première tentative
guess = strategy.get_first_guess("en")  # "SOARE"
feedback = game.make_guess(guess)
print(feedback)  # Affiche le feedback coloré

# Appliquer les contraintes
constraint_manager.apply_feedback(feedback)

# Trouver les mots possibles
possible_words = solver.get_possible_words(constraint_manager)
print(f"Mots possibles : {len(possible_words)}")

# Choisir le meilleur mot avec la stratégie
next_guess = strategy.choose_word(possible_words, constraint_manager, 2)
print(f"Meilleur choix : {next_guess}")
```

### 🔌 API REST

L'API backend peut être utilisée indépendamment :

```bash
# Documentation interactive
http://localhost:8000/docs

# Exemples de requêtes
curl -X POST "http://localhost:8000/api/game/new" \
  -H "Content-Type: application/json" \
  -d '{"language":"en","strategy":"frequency"}'
```

## 🏗️ Architecture

```
wordle_solver/
├── csp/                 # Module CSP (cœur)
│   ├── constraint_manager.py
│   ├── word_filter.py
│   └── solver.py
├── llm/                 # Intégration LLM (à venir)
├── strategies/          # Stratégies de jeu (à venir)
├── game/                # Simulation Wordle
└── dictionaries/        # Dictionnaires FR/EN
```

## 📖 Exemples

Consultez le dossier `examples/` pour des cas d'usage :

- `basic_solver.py` : Résolution basique sans LLM
- `llm_assisted.py` : Résolution avec stratégies adaptatives (à venir)
- `batch_analysis.py` : Analyse de performance (à venir)

## 🧪 Tests

```bash
# Installer les dépendances de dev
pip install -e ".[dev]"

# Lancer les tests
pytest

# Avec couverture
pytest --cov=wordle_solver
```

## 🔑 Configuration

Créer un fichier `.env` :

```bash
cp .env.example .env
# Éditer .env avec votre clé API Anthropic
```

## 📝 Statut du projet

**Phase 1 : Module CSP de base** ✅ TERMINÉ
- [x] Gestionnaire de contraintes
- [x] Filtrage de dictionnaire
- [x] Solveur OR-Tools
- [x] Simulation de jeu

**Phase 2 : Stratégies d'optimisation** ✅ TERMINÉ
- [x] Stratégie par fréquence
- [x] Stratégie par entropie
- [x] Stratégie minimax
- [x] Tests et benchmarks
- [x] Comparateur de stratégies

**Phase 3 : Interface Web** ✅ TERMINÉ
- [x] API REST FastAPI
- [x] Application React interactive
- [x] Intégration des stratégies
- [x] Suggestions en temps réel
- [x] Support multi-langues

**Phase 4 : Améliorations futures** 🔮
- [ ] Intégration LLM (Claude API)
- [ ] Mode auto-solve visualisé
- [ ] Statistiques avancées
- [ ] Historique des parties
- [ ] Thèmes personnalisables

## 🤝 Contribution

Les contributions sont bienvenues ! N'hésitez pas à ouvrir une issue ou un PR.

## 📄 Licence

MIT License - voir le fichier LICENSE

## 🙏 Remerciements

- Google OR-Tools pour le moteur CSP
- Anthropic pour l'API Claude
- La communauté Wordle

---

**Note** : Ce projet est à but éducatif et démontre l'utilisation de CSP + LLM pour la résolution de puzzles.
