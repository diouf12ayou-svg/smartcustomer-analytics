# Architecture et modélisation UML - SmartCustomer Analytics

Ce document rassemble l'architecture technique, l'organisation du code et les diagrammes UML de l'application **SmartCustomer Analytics (Analyse intelligente des clients)**. Il décrit le projet sans en modifier le fonctionnement.

## 1. Architecture technique

- **Backend** : Python 3 et Django 5+ (architecture MVT : Model-View-Template).
- **Machine Learning et traitement des données** : `scikit-learn` (K-Means) et `numpy`.
- **Base de données** : SQLite 3 (`db.sqlite3`).
- **Interface** : HTML5, CSS3 et JavaScript (ES6+).
- **Visualisation** : Chart.js et Mermaid.js pour les diagrammes UML.

### Organisation des fichiers

```text
SmartCustomer_Analytics/
├── README.md
├── Architecture_UML.md
└── Analyse_intelligente_des_clients/
    ├── manage.py
    ├── db.sqlite3
    ├── main/
    │   ├── models.py
    │   ├── views.py
    │   ├── urls.py
    │   ├── tests.py
    │   └── templates/
    │       ├── base.html
    │       ├── analyse.html
    │       └── principal/
    │           ├── dashboard.html
    │           ├── clients.html
    │           ├── ia.html
    │           ├── powerbi.html
    │           └── uml.html
    └── Analyse_intelligente_des_comportements_clients/
        ├── settings.py
        └── urls.py
```

---

## 2. Diagramme des Cas d'Utilisation (Use Case Diagram)

Ce diagramme modélise les exigences fonctionnelles de la plateforme. Il délimite le périmètre du système en définissant les acteurs métiers (**Responsable Marketing**, **Client**, **Data Analyst**, **Responsable Commercial**, **Data Scientist**, et **Administrateur**) ainsi que leurs cas d'utilisation associés au sein de la plateforme IA.

```mermaid
graph LR
    %% Acteurs
    RM["👤 Responsable Marketing"]
    CL["👤 Client"]
    DA["👤 Data Analyst"]
    RC["👤 Responsable Commercial"]
    DS["👤 Data Scientist"]
    AD["⚙️ Administrateur"]

    %% Frontière du Système
    subgraph Plateforme["Plateforme IA de prédiction du comportement client"]
        UC_Recomm("Générer des recommandations<br/>personnalisées")
        UC_Export("Exporter les rapports")
        UC_Collect("Collecter les données<br/>de navigation")
        UC_Analyse("Analyser le comportement<br/>client")
        UC_PowerBI("Visualiser le tableau<br/>de bord Power BI")
        UC_Clean("Nettoyer et préparer<br/>les données")
        UC_ConsulPred("Consulter les prédictions")
        UC_Predict("Prédire le comportement<br/>client")
        UC_Train("Entraîner le modèle<br/>Machine Learning")
        UC_GereAcc("Gérer les utilisateurs<br/>et les accès")
    end

    %% Relations Acteurs -> Use Cases
    RM --> UC_Recomm
    RM --> UC_Export
    RM --> UC_PowerBI

    CL --> UC_Collect

    DA --> UC_Collect
    DA --> UC_Analyse
    DA --> UC_PowerBI
    DA --> UC_Clean

    RC --> UC_PowerBI
    RC --> UC_ConsulPred

    DS --> UC_Predict
    DS --> UC_Train

    AD --> UC_GereAcc

    %% Relations inter-Use Cases (utilise)
    UC_Recomm -.->|utilise| UC_PowerBI
    UC_ConsulPred -.->|utilise| UC_PowerBI
    UC_Predict -.->|utilise| UC_PowerBI
    UC_Predict -.->|utilise| UC_Train

    %% Styles Personnalisés Premium
    style RM fill:#eff6ff,stroke:#2563eb,stroke-width:2px,rx:8px
    style CL fill:#eff6ff,stroke:#2563eb,stroke-width:2px,rx:8px
    style DA fill:#eff6ff,stroke:#2563eb,stroke-width:2px,rx:8px
    style RC fill:#eff6ff,stroke:#2563eb,stroke-width:2px,rx:8px
    style DS fill:#eff6ff,stroke:#2563eb,stroke-width:2px,rx:8px
    style AD fill:#fff5f5,stroke:#e53e3e,stroke-width:2px,rx:8px

    style UC_Recomm fill:#ffffff,stroke:#475569,stroke-width:1px
    style UC_Export fill:#ffffff,stroke:#475569,stroke-width:1px
    style UC_Collect fill:#ffffff,stroke:#475569,stroke-width:1px
    style UC_Analyse fill:#ffffff,stroke:#475569,stroke-width:1px
    style UC_PowerBI fill:#fffbeb,stroke:#d97706,stroke-width:2px
    style UC_Clean fill:#ffffff,stroke:#475569,stroke-width:1px
    style UC_ConsulPred fill:#ffffff,stroke:#475569,stroke-width:1px
    style UC_Predict fill:#ffffff,stroke:#475569,stroke-width:1px
    style UC_Train fill:#ffffff,stroke:#475569,stroke-width:1px
    style UC_GereAcc fill:#ffffff,stroke:#475569,stroke-width:1px

    style Plateforme fill:#f8fafc,stroke:#94a3b8,stroke-width:2px,stroke-dasharray: 5 5
```

---

## 3. Diagramme de Classes (Class Diagram - Architecture MVT)

Ce diagramme représente la structure statique de l'application en adaptant le patron de conception **MVT (Model-View-Template)** de Django. Il montre la structure du modèle `Customer`, la logique des vues, le routage des URL et les pages de rendu.

```mermaid
classDiagram
    direction TB

    class URLs {
        +path("admin/", admin.site.urls)
        +path("", views.dashboard)
        +path("dashboard/", views.dashboard)
        +path("clients/", views.liste_clients)
        +path("analyse/", views.analyse)
    }

    class Views {
        +dashboard(request: HttpRequest) HttpResponse
        +liste_clients(request: HttpRequest) HttpResponse
        +analyse(request: HttpRequest) HttpResponse
        +ancien_dashboard_inutilise(request: HttpRequest) HttpResponse
    }

    class Customer {
        +int id
        +string name
        +string email
        +float total_achats
        +int nombre_visites
        +int pages_visitees
        +float temps_navigation
        +int produits_consultes
        +datetime created_at
        +calculer_score() int
        +categorie() string
        +__str__() string
    }

    class Templates {
        <<Folder>>
        +principal/dashboard.html
        +principal/clients.html
        +analyse.html
    }

    %% Relations de routage et flux de données
    URLs --> Views : route les requêtes vers
    Views --> Customer : interroge et modifie
    Views --> Templates : transmet le contexte de données à
```

### Détails des attributs du modèle `Customer` :
- **`total_achats`** : Somme cumulée dépensée par le client (sert de base de calcul pour 40% du score).
- **`nombre_visites`** : Nombre de fois que le client est venu sur le site (sert de base pour 10 points par visite).
- **`pages_visitees`** : Nombre total de pages consultées (5 points par page).
- **`temps_navigation`** : Temps total passé en secondes (2 points par seconde).
- **`produits_consultes`** : Nombre de produits consultés (3 points par produit).

### Calcul du score et de la catégorie :
Le score est calculé par la méthode `calculer_score()` :
$$\text{Score} = \left(\frac{\text{total\_achats}}{10000} \times 40\right) + (\text{nombre\_visites} \times 10) + (\text{pages\_visitees} \times 5) + (\text{produits\_consultes} \times 3) + (\text{temps\_navigation} \times 2)$$

La méthode `categorie()` renvoie le profil du client en fonction de son score :
- **VIP** : Score $\ge 80$
- **Fidele** : Score $\ge 50$
- **Potentiel** : Score $\ge 20$
- **Nouveau** : Score $< 20$

---

## 4. Diagramme de Séquence (Sequence Diagram)

Ce diagramme illustre le flux dynamique d'une requête de création ou de mise à jour de client via l'interface, montrant comment les vues interagissent avec le modèle, la base de données et le template.

```mermaid
sequenceDiagram
    autonumber
    actor User as Utilisateur
    participant Browser as Navigateur Web
    participant URL as Router (urls.py)
    participant View as View (liste_clients)
    participant Model as Model (Customer)
    participant DB as SQLite DB (db.sqlite3)
    participant Template as Template (clients.html)

    User->>Browser: Saisit les infos client & clique sur Valider
    Browser->>URL: HTTP POST /clients/ (nom, email, achats, visites, ...)
    URL->>View: appelle liste_clients(request)
    
    alt Action "update" (Modification)
        View->>Model: Récupère Customer via edit_id
    else Action "create" (Ajout)
        View->>Model: Instantie un nouveau Customer
    end

    View->>Model: Met à jour les attributs
    View->>Model: appelle save()
    Model->>DB: Exécute la requête SQL (INSERT/UPDATE)
    DB-->>Model: Retourne le statut SQL OK
    
    View->>URL: Redirige vers /clients/ (HTTP 302 Redirect)
    URL->>View: appelle liste_clients(request) (HTTP GET)
    
    View->>Model: Query : Customer.objects.all().order_by("-created_at")
    Model->>DB: SELECT * FROM main_customer ...
    DB-->>Model: Liste des clients bruts
    
    View->>View: Calcule les scores, segments & statistiques globales
    View->>Template: Rend le template principal/clients.html
    Template-->>Browser: Retourne le code HTML généré
    Browser-->>User: Affiche l'interface mise à jour avec le client
```
