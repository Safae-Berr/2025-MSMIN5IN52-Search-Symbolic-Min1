# 🟩 Wordle CSP & LLM Solver

Réalisé par: 
- Safae BERRICHI
- Pauline GOFFINET
- Lamyae TALA


## 🔹 Description

Ce projet propose un **solveur de Wordle** combinant **programmation par contraintes (CSP)** et **LLM (Language Model)**.

Le jeu Wordle consiste à deviner un mot de 5 lettres. Après chaque tentative, le joueur reçoit des indices :

- 🟩 **Vert** → lettre correcte et bien placée
- 🟨 **Jaune** → lettre présente mais mal placée
- ⬜ **Gris** → lettre absente

Ces indices définissent des **contraintes sur le mot secret**, que le solveur CSP utilise pour filtrer les mots possibles.  
Le LLM est intégré pour **proposer des coups optimisés** à partir des contraintes déjà appliquées.

---

## 🔹 Fonctionnalités

- 🎯 Génération d’un **mot secret aléatoire** côté backend
- ✅ Évaluation des propositions du joueur (**vert / jaune / gris**) côté backend
- 🤖 **Suggestions IA** basées sur les contraintes actuelles via le solveur hybride CSP + LLM
- 💻 Interface web interactive avec **React** :
    - Plateau de jeu (`GameBoard`)
    - Clavier interactif (`Keyboard`)
    - Panel de suggestions IA (`SolverPanel`)
    - Statistiques et modal de fin de partie (`GameStats`)
- 🌐 Support des langues **français et anglais**

---

## 🔹 Architecture

### Backend (FastAPI)
- Endpoints principaux:
    - `POST /new` → démarrer une nouvelle partie
    - `POST /guess` → soumettre un mot et recevoir le feedback
    - `POST /suggest-ai` → obtenir la suggestion IA selon les contraintes actuelles

- Solveur hybride `HybridWordleSolver` :
    - 🟢 **CSP** pour filtrer les candidats selon les contraintes
    - 🤖 **LLM** pour proposer le meilleur mot suivant

### Frontend (React)
- `WordleGame.jsx` : logique du jeu, gestion du clavier, affichage du plateau et des résultats
- `SolverPanel.jsx` : affichage des suggestions IA
- `GameStats.jsx` : modal de fin de partie
- Communication avec le backend via **Axios**

---

## 🔹 Technologies

- **Backend** : Python 3.11, FastAPI, OR-Tools / python-constraint, Pydantic
- **Frontend** : React, Tailwind CSS, Axios
- **LLM** : OpenAI API ou modèle local via GeminiLLM
- **Dictionnaires** : français et anglais
- **Notifications** : Sonner (toast messages)

---

## 🔹 Installation & Démarrage

### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```
### Frontend
```bash
cd frontend
npm install
npm run dev
```

