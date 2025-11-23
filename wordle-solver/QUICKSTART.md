# 🚀 Guide de Démarrage Rapide

## Installation Automatique (Recommandé)

### Linux / macOS
```bash
./start.sh
```

### Windows
```bash
start.bat
```

Ces scripts vont :
1. Installer automatiquement toutes les dépendances
2. Démarrer le backend (port 8000)
3. Démarrer le frontend (port 3000)
4. Ouvrir votre navigateur sur l'application

---

## Installation Manuelle

### Prérequis
- Python 3.8+
- Node.js 16+
- npm ou yarn

### 1️⃣ Backend

```bash
# Depuis le dossier racine
cd backend

# Installer les dépendances
pip install -r requirements.txt
pip install -r ../requirements.txt

# Démarrer le serveur
python main.py
```

✅ Backend prêt sur `http://localhost:8000`

### 2️⃣ Frontend

```bash
# Dans un nouveau terminal
cd frontend

# Installer les dépendances
npm install

# Démarrer l'application
npm run dev
```

✅ Frontend prêt sur `http://localhost:3000`

---

## 🎮 Première Utilisation

1. **Ouvrez** `http://localhost:3000` dans votre navigateur

2. **Configurez** votre partie :
   - Cliquez sur l'icône ⚙️ pour ouvrir les paramètres
   - Choisissez votre langue (EN ou FR)
   - Choisissez votre stratégie (Fréquence recommandée)

3. **Démarrez** en cliquant sur "Démarrer"

4. **Jouez** :
   - Utilisez le clavier virtuel ou votre clavier physique
   - Appuyez sur "Entrée" pour valider un mot
   - Utilisez "Backspace" pour effacer

5. **Obtenez de l'aide** :
   - Cliquez sur "Obtenir une Suggestion" pour voir le meilleur mot
   - Consultez la liste des mots possibles
   - Cliquez sur un mot suggéré pour l'utiliser directement

---

## 🐛 Dépannage

### Le backend ne démarre pas
```bash
# Vérifier Python
python3 --version  # Devrait afficher 3.8+

# Réinstaller les dépendances
cd backend
pip install --upgrade -r requirements.txt
```

### Le frontend ne démarre pas
```bash
# Vérifier Node.js
node --version  # Devrait afficher 16+

# Nettoyer et réinstaller
cd frontend
rm -rf node_modules package-lock.json
npm install
```

### Erreur de connexion à l'API
1. Vérifiez que le backend est bien démarré sur le port 8000
2. Ouvrez `http://localhost:8000/docs` pour tester l'API
3. Vérifiez les logs du backend pour les erreurs

### Port déjà utilisé
```bash
# Changer le port du backend (dans backend/main.py)
uvicorn.run(app, host="0.0.0.0", port=8001)

# Changer le port du frontend (dans frontend/vite.config.js)
server: { port: 3001 }
```

---

## 📚 Documentation Complète

- **Backend API** : Voir `backend/README.md`
- **Frontend** : Voir `frontend/README.md`
- **Stratégies** : Voir `docs/STRATEGIES.md`
- **README principal** : Voir `README.md`

---

## 💡 Conseils

- **Meilleure stratégie** : Entropie (optimal théoriquement) ou Fréquence (rapide et efficace)
- **Premier mot** : SOARE (EN) ou AIMER (FR) sont recommandés
- **Suggestions** : Cliquez directement sur un mot suggéré pour l'utiliser
- **Clavier physique** : Vous pouvez utiliser votre clavier normalement

---

## 🎯 Objectifs de Performance

- ✅ **Taux de succès** : 100%
- ✅ **Moyenne de tentatives** : 3.7
- ✅ **Temps de réponse** : < 1 seconde

---

**Bon jeu ! 🎮**
