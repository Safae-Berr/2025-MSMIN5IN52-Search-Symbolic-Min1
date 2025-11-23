# 🚀 COMMENT DÉMARRER LE PROJET

## ⚠️ IMPORTANT : 2 TERMINAUX REQUIS

Le projet nécessite **2 terminaux séparés** :
- **Terminal 1** → Backend (API)
- **Terminal 2** → Frontend (Interface Web)

---

## 📺 Guide Visuel

```
┌─────────────────────────────────────────────────────────────┐
│  TERMINAL 1 : BACKEND                                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  $ cd backend                                               │
│  $ pip install -r requirements.txt                          │
│  $ pip install -r ../requirements.txt                       │
│  $ python main.py                                           │
│                                                             │
│  INFO: Uvicorn running on http://0.0.0.0:8000 ✅           │
│                                                             │
│  ⚠️  NE PAS FERMER CE TERMINAL                              │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│  TERMINAL 2 : FRONTEND                                      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  $ cd frontend                                              │
│  $ npm install                                              │
│  $ npm run dev                                              │
│                                                             │
│  ➜ Local: http://localhost:3000/ ✅                        │
│                                                             │
│  ⚠️  NE PAS FERMER CE TERMINAL                              │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│  NAVIGATEUR                                                 │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Ouvrir : http://localhost:3000                            │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 🎬 Étapes Détaillées

### Étape 1 : Prérequis

Vérifiez que vous avez :

```bash
# Python 3.8+
python3 --version

# Node.js 16+
node --version

# npm
npm --version
```

Si quelque chose manque, installez-le :
- Python : https://www.python.org/downloads/
- Node.js : https://nodejs.org/

---

### Étape 2 : Terminal 1 - Backend

```bash
# 1. Ouvrir un terminal
# 2. Aller dans le dossier backend
cd wordle-solver/backend

# 3. Installer les dépendances (PREMIÈRE FOIS SEULEMENT)
pip install -r requirements.txt
pip install -r ../requirements.txt

# 4. Démarrer le backend
python main.py
```

**✅ Vous devez voir :**
```
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [xxxxx]
INFO:     Started server process [xxxxx]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

**⚠️ IMPORTANT : Laissez ce terminal ouvert !**

---

### Étape 3 : Terminal 2 - Frontend

```bash
# 1. Ouvrir UN NOUVEAU terminal (pas le même)
# 2. Aller dans le dossier frontend
cd wordle-solver/frontend

# 3. Installer les dépendances (PREMIÈRE FOIS SEULEMENT)
npm install

# 4. Démarrer le frontend
npm run dev
```

**✅ Vous devez voir :**
```
  VITE v5.x.x  ready in 500 ms

  ➜  Local:   http://localhost:3000/
  ➜  Network: use --host to expose
  ➜  press h to show help
```

**⚠️ IMPORTANT : Laissez ce terminal ouvert aussi !**

---

### Étape 4 : Navigateur

Ouvrez votre navigateur sur :

```
http://localhost:3000
```

**✅ Vous devez voir :**
- L'interface Wordle Solver
- Bouton "Démarrer"
- Menu de configuration
- **PAS d'erreur "Backend non accessible"**

---

## ❌ Problème : "Backend non accessible"

Si vous voyez ce message d'erreur rouge, cela signifie que :

**Le backend (Terminal 1) n'est PAS démarré !**

### Solution :

1. Vérifiez le Terminal 1
2. Vous devez voir : `Uvicorn running on http://0.0.0.0:8000`
3. Si ce n'est pas le cas, redémarrez le backend :
   ```bash
   cd backend
   python main.py
   ```
4. Rafraîchissez la page dans le navigateur

---

## 🔍 Test Rapide

Pour vérifier que le backend fonctionne :

```bash
# Dans un 3ème terminal
curl http://localhost:8000/

# Vous devez voir quelque chose comme :
# {"message":"Wordle Solver API", ...}
```

Si cette commande ne fonctionne pas, le backend n'est pas démarré.

---

## 📝 Ordre de Démarrage

**TOUJOURS DANS CET ORDRE :**

1. ✅ Backend d'abord (Terminal 1)
2. ✅ Frontend ensuite (Terminal 2)
3. ✅ Navigateur en dernier

❌ **NE PAS** démarrer le frontend avant le backend !

---

## 🛑 Arrêt du Projet

Pour arrêter proprement :

1. **Terminal 2 (Frontend)** : Appuyez sur `Ctrl+C`
2. **Terminal 1 (Backend)** : Appuyez sur `Ctrl+C`

---

## 🚀 Script Automatique (Alternatif)

Si vous voulez tout démarrer automatiquement :

### Linux / macOS
```bash
./start.sh
```

### Windows
```bash
start.bat
```

**Note :** Ces scripts peuvent ne pas fonctionner sur tous les systèmes.
En cas de problème, utilisez la méthode manuelle (2 terminaux).

---

## 💡 Astuces

### Terminal 1 (Backend)
- Port par défaut : 8000
- API documentation : http://localhost:8000/docs
- Ne fermez jamais ce terminal pendant l'utilisation

### Terminal 2 (Frontend)
- Port par défaut : 3000
- Hot reload activé (modifications détectées automatiquement)
- Ne fermez jamais ce terminal pendant l'utilisation

### Développement
- Vous pouvez modifier le code et voir les changements en direct
- Le backend recharge automatiquement (uvicorn --reload)
- Le frontend recharge automatiquement (Vite HMR)

---

## 🆘 Aide

Si vous avez toujours des problèmes :

1. **Exécutez le diagnostic :**
   ```bash
   ./diagnose.sh
   ```

2. **Consultez la documentation :**
   - `TROUBLESHOOTING.md` - Guide de dépannage complet
   - `QUICKSTART.md` - Guide rapide
   - `backend/README.md` - Documentation backend
   - `frontend/README.md` - Documentation frontend

3. **Vérifiez les logs :**
   - Regardez les messages dans Terminal 1 et Terminal 2
   - Ouvrez la console du navigateur (F12)

---

## ✅ Checklist

Avant de commencer :

- [ ] Python 3.8+ installé
- [ ] Node.js 16+ installé
- [ ] Archive extraite
- [ ] Dépendances backend installées
- [ ] Dépendances frontend installées

Pendant l'exécution :

- [ ] Terminal 1 : Backend actif (port 8000)
- [ ] Terminal 2 : Frontend actif (port 3000)
- [ ] Navigateur : http://localhost:3000 ouvert
- [ ] Aucune erreur "Backend non accessible"

---

**🎯 Résumé : 2 terminaux, backend d'abord, frontend ensuite !**
