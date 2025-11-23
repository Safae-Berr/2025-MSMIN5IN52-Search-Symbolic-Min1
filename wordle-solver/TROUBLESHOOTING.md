# 🔧 Guide de Dépannage

## ❌ Erreur : "Could not connect to the server"

Cette erreur signifie que le **frontend ne peut pas se connecter au backend**.

### 🎯 Solution

**Vous devez démarrer le backend ET le frontend séparément dans 2 terminaux différents.**

---

## ✅ Démarrage Correct (2 Terminaux)

### Terminal 1 : Backend

```bash
# Depuis le dossier racine du projet
cd backend

# Installer les dépendances (première fois seulement)
pip install -r requirements.txt
pip install -r ../requirements.txt

# Démarrer le backend
python main.py
```

**Attendez de voir :**
```
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

✅ Le backend est prêt !

---

### Terminal 2 : Frontend

```bash
# Depuis le dossier racine du projet (NOUVEAU TERMINAL)
cd frontend

# Installer les dépendances (première fois seulement)
npm install

# Démarrer le frontend
npm run dev
```

**Attendez de voir :**
```
  VITE v5.x.x  ready in xxx ms

  ➜  Local:   http://localhost:3000/
  ➜  Network: use --host to expose
```

✅ Le frontend est prêt !

---

## 🚀 Ordre Important

**TOUJOURS dans cet ordre :**

1. **D'ABORD** → Démarrer le backend (Terminal 1)
2. **ENSUITE** → Démarrer le frontend (Terminal 2)
3. **ENFIN** → Ouvrir http://localhost:3000

---

## 🔍 Diagnostic Automatique

Utilisez le script de diagnostic :

```bash
./diagnose.sh
```

Ce script vérifie :
- ✅ Python installé
- ✅ Node.js installé
- ✅ Backend actif sur port 8000
- ✅ Frontend actif sur port 3000
- ✅ Connexion backend fonctionnelle

---

## 🐛 Problèmes Courants

### 1. "Port already in use" (8000)

**Problème :** Le port 8000 est déjà utilisé.

**Solution :**
```bash
# Tuer le processus sur le port 8000
lsof -ti:8000 | xargs kill -9

# Ou changer le port dans backend/main.py
uvicorn.run(app, host="0.0.0.0", port=8001)  # Utiliser 8001
```

### 2. "Port already in use" (3000)

**Problème :** Le port 3000 est déjà utilisé.

**Solution :**
```bash
# Tuer le processus sur le port 3000
lsof -ti:3000 | xargs kill -9

# Ou le frontend proposera automatiquement le port 3001
```

### 3. Backend ne démarre pas

**Problème :** Erreur lors du démarrage du backend.

**Solution :**
```bash
# Vérifier Python
python3 --version  # Doit être 3.8+

# Réinstaller les dépendances
cd backend
pip install --upgrade -r requirements.txt
pip install --upgrade -r ../requirements.txt

# Tester manuellement
python main.py
```

### 4. Frontend ne démarre pas

**Problème :** Erreur lors du démarrage du frontend.

**Solution :**
```bash
# Vérifier Node.js
node --version  # Doit être 16+

# Nettoyer et réinstaller
cd frontend
rm -rf node_modules package-lock.json
npm install

# Démarrer
npm run dev
```

### 5. "Module not found"

**Problème :** Dépendances manquantes.

**Solution Backend :**
```bash
cd backend
pip install -r requirements.txt
pip install -r ../requirements.txt
cd ..
pip install -e .  # Installer le package wordle_solver
```

**Solution Frontend :**
```bash
cd frontend
npm install
```

### 6. Erreur CORS

**Problème :** Le backend refuse les connexions du frontend.

**Vérification :**
```bash
# Le backend doit afficher au démarrage :
# "allow_origins=['http://localhost:3000', ...]"
```

**Solution :** Le backend est déjà configuré correctement. Vérifiez juste qu'il est bien démarré.

---

## 📝 Checklist de Vérification

Avant de lancer l'application :

- [ ] Python 3.8+ installé : `python3 --version`
- [ ] Node.js 16+ installé : `node --version`
- [ ] npm installé : `npm --version`
- [ ] Dépendances backend installées
- [ ] Dépendances frontend installées
- [ ] Backend démarré (Terminal 1)
- [ ] Frontend démarré (Terminal 2)
- [ ] Backend accessible : `curl http://localhost:8000`
- [ ] Frontend accessible : Ouvrir `http://localhost:3000`

---

## 💡 Test Manuel du Backend

Pour vérifier que le backend fonctionne :

```bash
# Test 1 : Endpoint racine
curl http://localhost:8000/

# Test 2 : Langues disponibles
curl http://localhost:8000/api/languages

# Test 3 : Stratégies disponibles
curl http://localhost:8000/api/strategies

# Test 4 : Créer une partie
curl -X POST http://localhost:8000/api/game/new \
  -H "Content-Type: application/json" \
  -d '{"language":"en","strategy":"frequency"}'
```

Si ces commandes fonctionnent, le backend est OK !

---

## 🖥️ Workflow Recommandé

### Option A : 2 Terminaux (Recommandé pour Dev)

**Terminal 1 :**
```bash
cd backend
python main.py
# Laissez tourner
```

**Terminal 2 :**
```bash
cd frontend
npm run dev
# Laissez tourner
```

### Option B : Screen/Tmux (Linux/macOS)

```bash
# Démarrer une session screen
screen -S wordle

# Terminal 1
cd backend && python main.py
# Ctrl+A puis D pour détacher

# Terminal 2
screen -S wordle-frontend
cd frontend && npm run dev
# Ctrl+A puis D pour détacher

# Pour revenir : screen -r wordle
```

### Option C : Script Automatique

Le script `start.sh` lance les deux automatiquement :

```bash
./start.sh
```

**Note :** Sur certains systèmes, vous devrez quand même les lancer manuellement.

---

## 🆘 Toujours des Problèmes ?

1. Exécutez `./diagnose.sh` pour un diagnostic complet
2. Vérifiez les logs dans les terminaux backend et frontend
3. Assurez-vous que les ports 8000 et 3000 sont libres
4. Essayez de redémarrer en mode manuel (2 terminaux)

---

## 📞 Messages d'Erreur Communs

### Frontend

```
AxiosError: Network Error
→ Backend non démarré. Démarrez-le dans Terminal 1.

Could not connect to the server
→ Backend non accessible. Vérifiez qu'il tourne sur port 8000.

XMLHttpRequest cannot load ... due to access control checks
→ Problème CORS. Le backend doit être démarré AVANT le frontend.
```

### Backend

```
Address already in use
→ Port 8000 occupé. Tuez le processus ou changez de port.

ModuleNotFoundError: No module named 'wordle_solver'
→ Installez le package : pip install -e .

ModuleNotFoundError: No module named 'fastapi'
→ Installez les dépendances : pip install -r requirements.txt
```

---

## ✅ Tout Fonctionne Quand Vous Voyez

**Backend (Terminal 1) :**
```
INFO:     Uvicorn running on http://0.0.0.0:8000
```

**Frontend (Terminal 2) :**
```
➜  Local:   http://localhost:3000/
```

**Navigateur :**
```
Interface Wordle Solver chargée avec :
- Bouton "Démarrer"
- Sélection langue/stratégie
- Aucune erreur dans la console
```

---

**🎯 Résumé : Backend d'abord, Frontend ensuite, dans 2 terminaux séparés !**
