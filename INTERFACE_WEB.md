# Interface Web pour l'Optimisation VRP

## Description

Interface web interactive permettant de configurer et visualiser en temps réel les solutions du problème de tournées de véhicules (VRP).

## Fonctionnalités

- **Placement interactif des points** : Cliquez sur la carte pour placer le dépôt, les clients et les stations de recharge
- **Configuration flexible** : Choisissez le nombre de véhicules, la capacité, le type de VRP (classique ou vert)
- **Visualisation en temps réel** : Suivez la progression de l'optimisation avec des mises à jour en direct
- **Affichage des tournées** : Visualisez les chemins optimaux sur la carte avec des couleurs différentes par véhicule

## Installation

1. Installer les dépendances :
```bash
pip install -r requirements.txt
```

2. Lancer l'application :
```bash
python app.py
```

3. Ouvrir votre navigateur à l'adresse :
```
http://localhost:5000
```

## Utilisation

### 1. Placer les points sur la carte

- Sélectionnez le mode de placement (Dépôt, Client, ou Station)
- Cliquez sur la carte pour placer les points
- Le dépôt est marqué en rouge
- Les clients sont marqués en bleu
- Les stations de recharge sont marquées en vert

### 2. Configurer les paramètres

- **Nombre de véhicules** : Nombre de véhicules disponibles (1-10)
- **Capacité par véhicule** : Capacité maximale de chaque véhicule
- **Type de VRP** :
  - **Classique** : VRP standard avec contraintes de capacité
  - **Vert** : VRP pour véhicules électriques avec stations de recharge
- **Temps limite** : Temps maximum pour la résolution (5-300 secondes)

### 3. Lancer la résolution

- Cliquez sur le bouton "Résoudre"
- Suivez la progression en temps réel :
  - Barre de progression
  - Distance actuelle
  - Tournées partielles qui se construisent progressivement
- Une fois terminé, les résultats finaux s'affichent :
  - Statut de la solution (optimal, feasible, infeasible)
  - Distance totale
  - Nombre de véhicules utilisés
  - Tournées complètes sur la carte

### 4. Visualiser les résultats

- Les tournées sont affichées sur la carte avec des couleurs différentes
- Cliquez sur une ligne pour voir le véhicule correspondant
- Les résultats détaillés apparaissent dans le panneau latéral

## Exemple d'utilisation

1. Placez un dépôt (mode "Dépôt") à Paris (48.8566, 2.3522)
2. Placez 5-6 clients autour du dépôt
3. Si vous utilisez le VRP vert, placez 2-3 stations de recharge
4. Configurez : 2 véhicules, capacité 50
5. Cliquez sur "Résoudre"
6. Observez la construction progressive des tournées optimales

## Notes techniques

- L'interface utilise **Leaflet** pour la carte interactive
- Les mises à jour en temps réel utilisent **Server-Sent Events (SSE)**
- La résolution utilise **OR-Tools CP-SAT** en arrière-plan
- Les tournées partielles sont simulées pendant la résolution pour donner un feedback visuel

## Dépannage

- **La carte ne s'affiche pas** : Vérifiez votre connexion internet (Leaflet nécessite un accès CDN)
- **La résolution ne démarre pas** : Vérifiez que vous avez placé au moins un dépôt et un client
- **Erreur "infeasible"** : Le problème peut être trop contraint, essayez d'augmenter la capacité ou le nombre de véhicules

