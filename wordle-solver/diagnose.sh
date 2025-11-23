#!/bin/bash

# Script de diagnostic pour Wordle Solver

echo "🔍 Diagnostic Wordle Solver"
echo "================================"
echo ""

# Vérifier Python
echo "1️⃣ Python :"
if command -v python3 &> /dev/null; then
    python3 --version
    echo "✅ Python installé"
else
    echo "❌ Python non trouvé"
fi
echo ""

# Vérifier Node.js
echo "2️⃣ Node.js :"
if command -v node &> /dev/null; then
    node --version
    echo "✅ Node.js installé"
else
    echo "❌ Node.js non trouvé"
fi
echo ""

# Vérifier npm
echo "3️⃣ npm :"
if command -v npm &> /dev/null; then
    npm --version
    echo "✅ npm installé"
else
    echo "❌ npm non trouvé"
fi
echo ""

# Vérifier les ports
echo "4️⃣ Ports :"
echo "Port 8000 (Backend) :"
if lsof -Pi :8000 -sTCP:LISTEN -t >/dev/null 2>&1 ; then
    echo "✅ Backend actif sur port 8000"
else
    echo "❌ Backend non actif sur port 8000"
fi

echo "Port 3000 (Frontend) :"
if lsof -Pi :3000 -sTCP:LISTEN -t >/dev/null 2>&1 ; then
    echo "✅ Frontend actif sur port 3000"
else
    echo "❌ Frontend non actif sur port 3000"
fi
echo ""

# Tester la connexion au backend
echo "5️⃣ Test de connexion au backend :"
if curl -s http://localhost:8000/ >/dev/null 2>&1; then
    echo "✅ Backend accessible"
    curl -s http://localhost:8000/ | head -n 3
else
    echo "❌ Backend non accessible"
    echo "   → Le backend doit être démarré !"
fi
echo ""

# Vérifier les dépendances
echo "6️⃣ Dépendances :"
if [ -d "backend/venv" ]; then
    echo "✅ Environnement virtuel Python créé"
else
    echo "⚠️  Environnement virtuel Python non créé"
fi

if [ -d "frontend/node_modules" ]; then
    echo "✅ node_modules installés"
else
    echo "⚠️  node_modules non installés"
fi
echo ""

echo "================================"
echo ""
echo "💡 Recommandations :"
echo ""
if ! curl -s http://localhost:8000/ >/dev/null 2>&1; then
    echo "⚠️  PROBLÈME DÉTECTÉ : Backend non actif"
    echo ""
    echo "Solution :"
    echo "  1. Ouvrir un terminal"
    echo "  2. cd wordle-solver/backend"
    echo "  3. python main.py"
    echo ""
    echo "Puis dans un autre terminal :"
    echo "  1. cd wordle-solver/frontend"
    echo "  2. npm run dev"
fi
