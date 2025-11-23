# Frontend React - Wordle Solver

Interface web interactive pour le Wordle Solver.

## 🚀 Installation

```bash
cd frontend

# Installer les dépendances
npm install
# ou
yarn install
```

## ▶️ Démarrage

```bash
# Mode développement
npm run dev
# ou
yarn dev
```

L'application sera accessible sur `http://localhost:3000`

## 🏗️ Build pour production

```bash
# Créer un build de production
npm run build
# ou
yarn build

# Prévisualiser le build
npm run preview
# ou
yarn preview
```

## 🎨 Fonctionnalités

### Interface de jeu
- ✅ Grille Wordle interactive (6 tentatives)
- ✅ Clavier virtuel avec état des lettres
- ✅ Support du clavier physique
- ✅ Animations et transitions fluides

### Assistance IA
- ✅ Suggestions intelligentes en temps réel
- ✅ Affichage des mots possibles
- ✅ Choix de stratégie (Fréquence, Entropie, Minimax, Simple)
- ✅ Explications des choix de l'IA

### Configuration
- ✅ Support multilingue (EN, FR)
- ✅ Choix de la stratégie de résolution
- ✅ Statistiques en temps réel

## 🧩 Architecture des composants

```
src/
├── App.jsx                 # Composant principal
├── components/
│   ├── WordleGrid.jsx      # Grille de jeu
│   ├── Keyboard.jsx        # Clavier virtuel
│   ├── SuggestionsPanel.jsx # Panel de suggestions
│   ├── GameControls.jsx    # Contrôles de jeu
│   └── GameStats.jsx       # Statistiques
├── services/
│   └── api.js              # Client API
└── index.css               # Styles Tailwind
```

## 🎨 Technologies utilisées

- **React 18** - Framework UI
- **Vite** - Build tool et dev server
- **Tailwind CSS** - Framework CSS utility-first
- **Lucide React** - Icônes
- **Axios** - Client HTTP

## 🔧 Configuration

Le frontend communique avec l'API backend via proxy Vite :

```javascript
// vite.config.js
server: {
  proxy: {
    '/api': 'http://localhost:8000'
  }
}
```

## 🐛 Dépannage

### L'application ne démarre pas
1. Vérifiez que Node.js 16+ est installé
2. Supprimez `node_modules` et réinstallez : `rm -rf node_modules && npm install`
3. Vérifiez que le port 3000 n'est pas déjà utilisé

### Erreurs de connexion à l'API
1. Vérifiez que le backend est démarré sur le port 8000
2. Vérifiez la configuration du proxy dans `vite.config.js`
3. Consultez la console du navigateur pour les erreurs CORS

### Problèmes de style
1. Vérifiez que Tailwind CSS est correctement configuré
2. Relancez le serveur de développement
3. Videz le cache du navigateur

## 📱 Responsive Design

L'interface est entièrement responsive et s'adapte aux écrans :
- 📱 Mobile (< 768px)
- 💻 Tablette (768px - 1024px)
- 🖥️ Desktop (> 1024px)

## 🎯 Prochaines fonctionnalités

- [ ] Mode "Auto-solve" pour voir l'IA jouer
- [ ] Historique des parties
- [ ] Statistiques avancées
- [ ] Thèmes personnalisables
- [ ] Mode multijoueur
