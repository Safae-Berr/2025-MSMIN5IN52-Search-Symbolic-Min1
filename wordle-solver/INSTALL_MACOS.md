# 🍎 Guide d'Installation macOS

## 📋 Problèmes Rencontrés

Si vous voyez ces erreurs :
```
ERROR: No matching distribution found for python-cors>=1.0.0
ModuleNotFoundError: No module named 'fastapi'
```

C'est résolu ! Suivez ce guide.

---

## ✅ Installation Correcte (Recommandée)

### Méthode 1 : Avec Environnement Virtuel (RECOMMANDÉ)

```bash
# 1. Aller dans le dossier backend
cd backend

# 2. Créer un environnement virtuel
python3 -m venv venv

# 3. Activer l'environnement virtuel
source venv/bin/activate

# 4. Installer les dépendances
pip install -r requirements.txt
pip install -r ../requirements.txt

# 5. Démarrer le backend
python main.py
```

**✅ Vous devriez voir :**
```
INFO:     Uvicorn running on http://0.0.0.0:8000
```

---

### Méthode 2 : Installation Système (Alternative)

Si la méthode 1 ne fonctionne pas :

```bash
# 1. Mettre à jour pip
python3 -m pip install --upgrade pip --user

# 2. Installer les dépendances
cd backend
pip3 install -r requirements.txt --user
pip3 install -r ../requirements.txt --user

# 3. Démarrer avec python3
python3 main.py
```

---

## 🔧 Si FastAPI n'est Toujours Pas Trouvé

### Option A : Forcer le chemin Python

```bash
# Trouver où les packages sont installés
python3 -m site

# Vous verrez quelque chose comme :
# /Users/ivancocusse/Library/Python/3.9/lib/python/site-packages

# Vérifier que fastapi est bien là
ls ~/Library/Python/3.9/lib/python/site-packages | grep fastapi

# Si fastapi est là, utiliser directement python3 -m pour lancer
cd backend
python3 -m uvicorn main:app --host 0.0.0.0 --port 8000
```

### Option B : Réinstaller Complètement avec Environnement Virtuel

```bash
# Nettoyer
cd backend
rm -rf venv

# Créer un nouvel environnement virtuel
python3 -m venv venv

# Activer
source venv/bin/activate

# Vérifier que vous êtes dans le venv
which python
# Devrait afficher : .../backend/venv/bin/python

# Installer
pip install --upgrade pip
pip install -r requirements.txt
pip install -r ../requirements.txt

# Lancer
python main.py
```

---

## 🎯 Vérification

Pour vérifier que tout est installé :

```bash
# Activer le venv si nécessaire
source venv/bin/activate

# Vérifier fastapi
python -c "import fastapi; print(fastapi.__version__)"

# Vérifier uvicorn
python -c "import uvicorn; print(uvicorn.__version__)"

# Si ces commandes fonctionnent, vous êtes prêt !
```

---

## 🚀 Démarrage Complet (2 Terminaux)

### Terminal 1 : Backend

```bash
cd wordle-solver/backend

# Si vous utilisez un venv
source venv/bin/activate

# Démarrer
python main.py
# OU si ça ne marche pas :
python3 -m uvicorn main:app --host 0.0.0.0 --port 8000
```

### Terminal 2 : Frontend

```bash
cd wordle-solver/frontend

# Installer (première fois)
npm install

# Démarrer
npm run dev
```

---

## 🐛 Problèmes Spécifiques macOS

### Problème : "pip: command not found"

```bash
# Utiliser python3 -m pip à la place
python3 -m pip install -r requirements.txt
```

### Problème : "Permission denied"

```bash
# Utiliser --user
pip3 install -r requirements.txt --user
```

### Problème : "ssl certificate verify failed"

```bash
# Mettre à jour les certificats
/Applications/Python\ 3.9/Install\ Certificates.command
```

### Problème : Python 3.9 vs Python 3.x

Vous utilisez Python 3.9. C'est OK, mais vérifiez :

```bash
# Version de Python
python3 --version

# Si < 3.8, mettre à jour Python
# Télécharger depuis : https://www.python.org/downloads/macos/
```

---

## 📝 Commandes Complètes pour macOS

Copier-coller ces commandes :

```bash
# Étape 1 : Backend
cd ~/Desktop/EPF-5A/IA\ 2/wordle-solver\ 5/backend
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
pip install -r ../requirements.txt
python main.py
```

Laissez tourner, puis dans un **nouveau terminal** :

```bash
# Étape 2 : Frontend
cd ~/Desktop/EPF-5A/IA\ 2/wordle-solver\ 5/frontend
npm install
npm run dev
```

Puis ouvrir dans le navigateur :
```
http://localhost:3000
```

---

## 💡 Astuce : Alias pour Démarrage Rapide

Ajoutez dans votre `~/.zshrc` ou `~/.bash_profile` :

```bash
alias wordle-backend="cd ~/Desktop/EPF-5A/IA\ 2/wordle-solver\ 5/backend && source venv/bin/activate && python main.py"
alias wordle-frontend="cd ~/Desktop/EPF-5A/IA\ 2/wordle-solver\ 5/frontend && npm run dev"
```

Puis dans le terminal :
```bash
source ~/.zshrc  # ou ~/.bash_profile

# Démarrer facilement
wordle-backend    # Terminal 1
wordle-frontend   # Terminal 2
```

---

## ✅ Checklist macOS

- [ ] Python 3.8+ installé : `python3 --version`
- [ ] pip installé : `python3 -m pip --version`
- [ ] Node.js installé : `node --version`
- [ ] npm installé : `npm --version`
- [ ] Environnement virtuel créé : `python3 -m venv venv`
- [ ] Environnement virtuel activé : `source venv/bin/activate`
- [ ] Dépendances installées sans erreur
- [ ] Backend démarre : `python main.py`
- [ ] Frontend démarre : `npm run dev`

---

## 🆘 Toujours des Problèmes ?

1. **Assurez-vous d'être dans le bon dossier** :
   ```bash
   pwd
   # Devrait afficher quelque chose comme :
   # /Users/ivancocusse/Desktop/EPF-5A/IA 2/wordle-solver 5/backend
   ```

2. **Utilisez un environnement virtuel** :
   C'est la solution la plus fiable pour éviter les conflits.

3. **Vérifiez les versions** :
   ```bash
   python3 --version  # 3.8+
   pip3 --version     # 21+
   node --version     # 16+
   ```

---

**Le problème `python-cors` a été corrigé dans la nouvelle version du projet !**
