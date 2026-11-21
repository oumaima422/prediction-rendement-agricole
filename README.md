# 🌱 Prédiction du rendement agricole à partir des données climatiques et des caractéristiques du sol

## 📌 Présentation du projet

L'agriculture est fortement influencée par les conditions climatiques et les caractéristiques pédologiques. Ce projet vise à étudier et à prédire le rendement agricole à partir de variables climatiques et de caractéristiques du sol, en utilisant des techniques de **Machine Learning**.

L'étude porte principalement sur l'influence de la température, des précipitations, de l'humidité et du type de sol (*Soil Type*) sur le rendement agricole.

Deux algorithmes de Machine Learning sont étudiés et comparés : **Random Forest** et **XGBoost**.

## 🎯 Objectifs du projet

- Étudier l'influence des variables climatiques sur le rendement agricole.
- Analyser le rôle du type de sol dans la prédiction du rendement.
- Comparer les performances de Random Forest et XGBoost.
- Optimiser les hyperparamètres des modèles.
- Développer une application web interactive permettant d'estimer le rendement agricole.

## 📊 Jeu de données

Le projet exploite un jeu de données provenant de Kaggle comprenant **1 000 observations**.

Les données ne contiennent aucune valeur manquante ni aucun doublon.

Les principales variables utilisées sont :

| Variable | Description |
|---|---|
| Temperature | Température |
| Rainfall | Précipitations |
| Humidity | Humidité |
| Soil Type | Type de sol |
| Crop Type | Type de culture |
| Yield | Rendement agricole (t/ha) |

**Remarque :** Le type de sol constitue la seule information pédologique disponible dans le jeu de données.

## ⚙️ Méthodologie

Le travail a été réalisé selon les étapes suivantes :

1. **Étude bibliographique et bibliométrique :** analyse des travaux scientifiques sur la prédiction du rendement agricole et les méthodes de Machine Learning.
2. **Exploration des données :** analyse de la structure, des variables et de la qualité du jeu de données.
3. **Prétraitement :** encodage des variables catégorielles avec `OneHotEncoder`.
4. **Construction des modèles :** développement de modèles Random Forest et XGBoost à l'aide de pipelines Scikit-learn.
5. **Évaluation :** séparation des données en 80 % pour l'entraînement et 20 % pour le test, avec une validation croisée à 5 folds.
6. **Comparaison :** évaluation des modèles par rapport à un modèle de référence `DummyRegressor`.
7. **Optimisation :** recherche des meilleurs hyperparamètres avec `RandomizedSearchCV`.
8. **Déploiement :** sauvegarde du pipeline final et développement d'une application web avec Streamlit.

## 🤖 Modèles utilisés

- **Random Forest Regressor :** modèle d'ensemble basé sur plusieurs arbres de décision.
- **XGBoost Regressor :** algorithme de boosting basé sur des arbres de décision.
- **Dummy Regressor :** modèle de référence qui prédit la moyenne des valeurs de rendement.

## 📈 Résultats expérimentaux

Les performances des modèles initiaux et optimisés ont été évaluées à l'aide des métriques R², RMSE et MAE.

### Résultats des modèles initiaux

| Modèle | R² | RMSE |
|---|---:|---:|
| Random Forest | -0,0166 | 2,2676 |
| XGBoost | -0,0813 | 2,3386 |
| Dummy Regressor | — | 2,2490 |

### Résultats du modèle final optimisé

**XGBoost optimisé :**

| Métrique | Résultat |
|---|---:|
| R² | 0,0031 |
| RMSE (test) | 2,2455 t/ha |
| MAE (test) | 1,9326 t/ha |
| RMSE moyenne (validation croisée) | 2,3965 |

### Interprétation

Après optimisation, XGBoost présente la RMSE la plus faible sur l'ensemble de test et la meilleure RMSE moyenne en validation croisée parmi les modèles étudiés.

Cependant, l'amélioration par rapport au modèle de référence reste très faible. Le coefficient R² proche de zéro indique que le modèle explique très peu la variabilité du rendement agricole.

Ces résultats doivent donc être interprétés avec prudence et montrent les limites prédictives du jeu de données utilisé.

## 🖥️ Application web interactive

Une application web a été développée avec **Streamlit** afin de permettre aux utilisateurs de saisir les paramètres climatiques et le type de sol, puis d'obtenir une estimation du rendement agricole.

### Fonctionnalités

- Saisie des paramètres climatiques.
- Sélection du type de sol.
- Sélection du type de culture.
- Estimation du rendement agricole à l'aide du modèle XGBoost optimisé.

### Technologies utilisées

- Python
- Streamlit
- Pandas
- Scikit-learn
- XGBoost
- Joblib
- JSON

## 📁 Structure du projet

```text
Prediction-Rendement-Agricole/
│
├── app.py
├── modele_rendement_agricole.pkl
├── categories.json
├── requirements.txt
├── README.md
│
├── notebooks/
│   └── analyse_modelisation.ipynb
│
└── images/
    └── interface_application.png
```

*La structure est indicative et peut être adaptée aux fichiers réellement présents dans le dépôt.*

## 🚀 Installation et exécution

### 1. Cloner le dépôt

```bash
git clone URL_DU_DEPOT
```

### 2. Accéder au dossier

```bash
cd Prediction-Rendement-Agricole
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Lancer l'application

```bash
streamlit run app.py
```

L'application sera accessible localement à l'adresse :

```text
http://localhost:8501
```

## 📦 Fichiers importants

- `app.py` : code source de l'application Streamlit.
- `modele_rendement_agricole.pkl` : pipeline XGBoost optimisé sauvegardé.
- `categories.json` : catégories des variables qualitatives utilisées par l'application.
- `requirements.txt` : liste des dépendances Python.

## 🔬 Conclusion

Ce projet met en œuvre une démarche complète de prédiction du rendement agricole, allant de l'étude bibliographique et bibliométrique jusqu'au développement d'une application web interactive.

Les expérimentations montrent que l'optimisation de XGBoost permet d'obtenir une légère amélioration des performances. Toutefois, les résultats soulignent également l'importance de la qualité, de la diversité et de la richesse des données pour construire des modèles prédictifs fiables.

## 🔑 Mots-clés

Rendement agricole · Machine Learning · Random Forest · XGBoost · Données climatiques · Type de sol · OneHotEncoder · Validation croisée · Streamlit · Agriculture intelligente
