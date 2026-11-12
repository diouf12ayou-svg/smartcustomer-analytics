# SmartCustomer Analytics 🚀
> **Plateforme web intelligente d'analyse comportementale, de segmentation et de prédiction du comportement client.**

---

## 📋 Table des Matières
- [1. Présentation du Projet](#1-présentation-du-projet)
- [2. Fonctionnalités Principales](#2-fonctionnalités-principales)
- [3. Analyse comportementale](#3-analyse-comportementale)
  - [3.1 Score comportemental](#31-score-comportemental)
  - [3.2 Segmentation par IA](#32-segmentation-par-ia)
- [4. Guide d'Installation et de Lancement](#4-guide-dinstallation-et-de-lancement)
- [5. Architecture et diagrammes UML](#5-architecture-et-diagrammes-uml)
- [6. Évolutions Futures](#6-évolutions-futures)

---

## 1. 🎯 Présentation du Projet

**SmartCustomer Analytics** est une solution web d'analyse décisionnelle (Business Intelligence) et d'intelligence artificielle conçue pour les équipes marketing, commerciales et analystes de données.

L'application permet de :
- Collecter et centraliser les données de navigation et d'achats des clients.
- Évaluer automatiquement la valeur et l'engagement de chaque client grâce à un score heuristique.
- Classifier les clients en 4 catégories métiers (VIP, Fidèle, Potentiel, Nouveau).
- Réaliser une **segmentation non surveillée par Machine Learning** (Clustering K-Means) pour identifier des groupes de comportements homogènes.
- Offrir des tableaux de bord interactifs pour piloter les actions marketing et exporter les données.

---

## 2. ✨ Fonctionnalités Principales

| Module | Description |
| :--- | :--- |
| **📊 Dashboard Principal** | Vue d'ensemble des KPIs (ventes totales, score moyen, nombre de VIP, répartition sectorielle et top clients). |
| **👤 Gestion des Clients (CRUD)** | Ajout, modification, suppression, recherche instantanée et filtrage par catégorie de clients. |
| **📥 Exportation CSV** | Téléchargement en 1 clic d'un fichier CSV formaté avec les scores et statuts recalculés. |
| **🤖 Comportement client et IA** | Score comportemental et segmentation K-Means ($K=3$) basés sur les données d'achat et de navigation. |
| **📈 Business Intelligence (BI)** | Analyse dynamique de la répartition du portefeuille client et des métriques de navigation. |
| **📐 Documentation technique** | Architecture du projet et diagrammes UML disponibles dans le document séparé [`Architecture_UML.md`](./Architecture_UML.md). |

---

## 3. 🧠 Analyse comportementale

### 3.1 Score comportemental
Le score individuel d'un client est calculé via la méthode `calculer_score()` du modèle `Customer` :

$$\text{Score} = \left(\frac{\text{total\_achats}}{10000} \times 40\right) + (\text{nombre\_visites} \times 10) + (\text{pages\_visitees} \times 5) + (\text{produits\_consultes} \times 3) + (\text{temps\_navigation} \times 2)$$

#### Grille de Catégorisation :
- 🟢 **VIP** : Score $\ge 80$
- 🔵 **Fidèle** : Score $\ge 50$
- 🟠 **Potentiel** : Score $\ge 20$
- ⚪ **Nouveau** : Score $< 20$

### 3.2 Segmentation par IA
L'analyse IA complète l'évaluation comportementale par un algorithme de clustering $K$-Means ($K=3$) :
1. **Feature Extraction** : Extraction de `total_achats` et `nombre_visites`.
2. **Normalisation $Z$-score** : $\frac{X - \mu}{\sigma}$ pour équilibrer le poids des variables.
3. **Clustering K-Means** : Regroupement automatique en 3 segments :
   - *Segment 0 (Économique / Nouveau)* : Faibles achats, visites occasionnelles.
   - *Segment 1 (Régulier / Potentiel)* : Achats moyens, visites régulières.
   - *Segment 2 (Premium / VIP)* : Forte valeur d'achat et fréquence élevée.

---

## 4. 🚀 Guide d'Installation et de Lancement

### Prérequis
- Python 3.10 ou supérieur installé.

### Étape 1 : Cloner / Accéder au projet
```bash
cd SmartCustomer_Analytics
```

### Étape 2 : Activer l'environnement virtuel
Sur Windows (PowerShell) :
```powershell
.\env\Scripts\activate
```

### Étape 3 : Installer les dépendances (si nécessaire)
```bash
pip install django numpy scikit-learn
```

### Étape 4 : Appliquer les migrations de base de données
```bash
python Analyse_intelligente_des_clients/manage.py migrate
```

### Étape 5 : Lancer le serveur de développement
```bash
python Analyse_intelligente_des_clients/manage.py runserver
```

L'application sera accessible à l'adresse : **`http://127.0.0.1:8000/`**

---

## 5. 📐 Architecture et diagrammes UML

L'architecture technique, l'organisation des fichiers et les diagrammes UML sont regroupés dans le document séparé [`Architecture_UML.md`](./Architecture_UML.md). Ces changements concernent la documentation uniquement : l'application reste inchangée.

---

## 6. 🔮 Évolutions Futures
- 🔮 **Algorithme de prédiction du Churn (Attrition)** via de la régression logistique ou Random Forest.
- 🔮 **Système de Recommandation de Produits** par filtrage collaboratif.
- 🔮 **Génération de rapports PDF** personnalisés pour les réunions de direction.
