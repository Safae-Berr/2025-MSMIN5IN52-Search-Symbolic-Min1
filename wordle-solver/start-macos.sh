#!/bin/bash

# Script de démarrage pour macOS

echo "🍎 Démarrage Wordle Solver - macOS"
echo "==================================="
echo ""

# Vérifier Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 n'est pas installé"
    echo "   Télécharger : https://www.python.org/downloads/macos/"
    exit 1
fi

echo "✅ Python 3 installé : $(python3 --version)"

# Vérifier Node.js
if ! command -v node &> /dev/null; then
    echo "❌ Node.js n'est pas installé"
    echo "   Télécharger : https://nodejs.org/"
    exit 1
fi

echo "✅ Node.js installé : $(node --version)"
echo ""

# Backend
echo "🔧 Configuration du Backend..."
cd backend

# Créer environnement virtuel si nécessaire
if [ ! -d "venv" ]; then
    echo "   Création de l'environnement virtuel..."
    python3 -m venv venv
fi

# Activer l'environnement virtuel
echo "   Activation de l'environnement virtuel..."
source venv/bin/activate

# Installer les dépendances
echo "   Installation des dépendances..."
pip install --upgrade pip -q
pip install -r requirements.txt -q
pip install -r ../requirements.txt -q

echo "✅ Backend configuré"
echo ""

# Frontend
echo "🎨 Configuration du Frontend..."
cd ../frontend

if [ ! -d "node_modules" ]; then
    echo "   Installation des dépendances npm..."
    npm install --silent
fi

echo "✅ Frontend configuré"
echo ""

# Démarrer
echo "🚀 Démarrage des serveurs..."
echo ""
echo "Pour démarrer, ouvrez 2 terminaux et exécutez :"
echo ""
echo "Terminal 1 (Backend) :"
echo "  cd backend"
echo "  source venv/bin/activate"
echo "  python main.py"
echo ""
echo "Terminal 2 (Frontend) :"
echo "  cd frontend"
echo "  npm run dev"
echo ""
echo "Puis ouvrez : http://localhost:3000"
echo ""
