#!/bin/bash

# Script de démarrage du Wordle Solver
# Lance le backend et le frontend en parallèle

echo "🚀 Démarrage du Wordle Solver..."
echo ""

# Vérifier si Python est installé
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 n'est pas installé. Veuillez l'installer d'abord."
    exit 1
fi

# Vérifier si Node.js est installé
if ! command -v node &> /dev/null; then
    echo "❌ Node.js n'est pas installé. Veuillez l'installer d'abord."
    exit 1
fi

# Vérifier si npm est installé
if ! command -v npm &> /dev/null; then
    echo "❌ npm n'est pas installé. Veuillez l'installer d'abord."
    exit 1
fi

# Fonction de nettoyage
cleanup() {
    echo ""
    echo "🛑 Arrêt des serveurs..."
    kill $BACKEND_PID $FRONTEND_PID 2>/dev/null
    exit
}

trap cleanup SIGINT SIGTERM

# Installer les dépendances si nécessaire
if [ ! -d "backend/venv" ]; then
    echo "📦 Installation des dépendances Python..."
    cd backend
    python3 -m venv venv
    source venv/bin/activate
    pip install -q -r requirements.txt
    pip install -q -r ../requirements.txt
    cd ..
    echo "✅ Dépendances Python installées"
fi

if [ ! -d "frontend/node_modules" ]; then
    echo "📦 Installation des dépendances Node.js..."
    cd frontend
    npm install --silent
    cd ..
    echo "✅ Dépendances Node.js installées"
fi

# Démarrer le backend
echo ""
echo "🔧 Démarrage du backend API (port 8000)..."
cd backend
source venv/bin/activate 2>/dev/null || true
python main.py &
BACKEND_PID=$!
cd ..

# Attendre que le backend soit prêt
echo "⏳ Attente du démarrage du backend..."
sleep 3

# Démarrer le frontend
echo ""
echo "🎨 Démarrage du frontend React (port 3000)..."
cd frontend
npm run dev &
FRONTEND_PID=$!
cd ..

# Attendre que le frontend soit prêt
sleep 3

echo ""
echo "✅ Wordle Solver est prêt !"
echo ""
echo "🌐 Frontend : http://localhost:3000"
echo "🔌 Backend API : http://localhost:8000"
echo "📚 Documentation API : http://localhost:8000/docs"
echo ""
echo "Appuyez sur Ctrl+C pour arrêter les serveurs"
echo ""

# Attendre que les processus se terminent
wait $BACKEND_PID $FRONTEND_PID
