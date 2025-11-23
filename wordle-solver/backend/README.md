# Backend API - Wordle Solver

API FastAPI pour exposer les fonctionnalités du Wordle Solver.

## 🚀 Installation

```bash
cd backend

# Créer un environnement virtuel (optionnel mais recommandé)
python -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate

# Installer les dépendances
pip install -r requirements.txt

# Installer également les dépendances du projet principal
pip install -r ../requirements.txt
```

## ▶️ Démarrage

```bash
# Depuis le dossier backend
python main.py
```

L'API sera accessible sur `http://localhost:8000`

## 📚 Documentation API

Une fois le serveur démarré, accédez à :
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## 🔌 Endpoints principaux

### Jeu
- `POST /api/game/new` - Créer une nouvelle partie
- `POST /api/game/guess` - Faire une tentative
- `POST /api/game/suggest` - Obtenir des suggestions
- `GET /api/game/state/{game_id}` - Obtenir l'état d'une partie
- `DELETE /api/game/{game_id}` - Supprimer une partie

### Configuration
- `GET /api/languages` - Langues disponibles
- `GET /api/strategies` - Stratégies disponibles
- `GET /api/stats` - Statistiques globales

## 🧪 Test rapide

```bash
# Test avec curl
curl http://localhost:8000/api/languages
curl http://localhost:8000/api/strategies
```

## 🔧 Configuration

Le serveur écoute sur le port 8000 par défaut. Pour changer :

```python
# Dans main.py
uvicorn.run(app, host="0.0.0.0", port=VOTRE_PORT)
```

## 🐛 Dépannage

Si l'API ne démarre pas :
1. Vérifiez que Python 3.8+ est installé
2. Vérifiez que toutes les dépendances sont installées
3. Vérifiez que le port 8000 n'est pas déjà utilisé
4. Consultez les logs pour plus d'informations
