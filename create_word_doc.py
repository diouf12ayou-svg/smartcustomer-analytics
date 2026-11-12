import sys
import subprocess

try:
    import docx
    from docx.shared import Inches, Pt, RGBColor
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.enum.table import WD_TABLE_ALIGNMENT
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "python-docx"])
    import docx
    from docx.shared import Inches, Pt, RGBColor
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.enum.table import WD_TABLE_ALIGNMENT
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn

def set_cell_background(cell, fill_color):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), fill_color)
    tcPr.append(shd)

def create_document():
    doc = docx.Document()

    # Define styles
    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Calibri'
    normal_style.font.size = Pt(11)
    normal_style.font.color.rgb = RGBColor(0x33, 0x33, 0x33)

    # Page Margins
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(1)
        section.bottom_margin = Inches(1)
        section.left_margin = Inches(1)
        section.right_margin = Inches(1)

    # Header / Title Page
    title_p = doc.add_paragraph()
    title_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    title_run = title_p.add_run("DOCUMENT DE SPÉCIFICATION ET DE DOCUMENTATION TECHNIQUE\n")
    title_run.bold = True
    title_run.font.size = Pt(20)
    title_run.font.color.rgb = RGBColor(0x1E, 0x3A, 0x8A)

    subtitle_p = doc.add_paragraph()
    subtitle_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    sub_run = subtitle_p.add_run("SmartCustomer Analytics — Analyse Intelligente & Clustering Client\n")
    sub_run.font.size = Pt(14)
    sub_run.font.italic = True
    sub_run.font.color.rgb = RGBColor(0x4B, 0x55, 0x63)

    doc.add_paragraph("—" * 45).alignment = WD_ALIGN_PARAGRAPH.CENTER

    meta_p = doc.add_paragraph()
    meta_p.add_run("Auteur : ").bold = True
    meta_p.add_run("Équipe de Développement SmartCustomer Analytics\n")
    meta_p.add_run("Framework & Technologies : ").bold = True
    meta_p.add_run("Python 3.10, Django 5 (MVT), scikit-learn, SQLite, Chart.js, HTML5/CSS3\n")
    meta_p.add_run("Statut : ").bold = True
    meta_p.add_run("Fonctionnel & Opérationnel | Date : Octobre 2026\n")

    doc.add_heading("1. 🎯 INTRODUCTION ET CONTEXTE DU PROJET", level=1)
    
    doc.add_heading("1.1 Contexte et Problématique Métier", level=2)
    doc.add_paragraph(
        "Dans le secteur du e-commerce et des services en ligne, les entreprises accumulent des volumes massifs de données comportementales (achats, sessions, navigation, consultations de produits). Sans outil automatisé de synthèse, ces données restent inexploitées, empêchant les équipes marketing de proposer des offres adaptées à la valeur réelle de chaque client."
    )
    doc.add_paragraph(
        "SmartCustomer Analytics répond directement à cette problématique en convertissant les données brutes en indicateurs décisionnels actionnables et en segments comportementaux intelligents."
    )

    doc.add_heading("1.2 Objectifs Stratégiques", level=2)
    p = doc.add_paragraph()
    p.add_run("• Évaluer et Qualifier : ").bold = True
    p.add_run("Calculer un score synthétique d'engagement pour chaque profil client.\n")
    p.add_run("• Segmenter : ").bold = True
    p.add_run("Combiner des catégories métriques explicites à des algorithmes de Machine Learning (K-Means).\n")
    p.add_run("• Décider : ").bold = True
    p.add_run("Fournir un tableau de bord visuel et simplifier l'exportation des données CSV pour les campagnes marketing.\n")
    p.add_run("• Modéliser : ").bold = True
    p.add_run("Garantir une architecture logicielle robuste et modélisée en UML (MVT Django).")

    doc.add_heading("1.3 Acteurs et Profils Utilisateurs", level=2)
    table_acteurs = doc.add_table(rows=6, cols=2)
    table_acteurs.alignment = WD_TABLE_ALIGNMENT.CENTER
    table_acteurs.style = 'Table Grid'
    
    headers = ["Acteur / Rôle", "Missions sur la Plateforme"]
    for i, h in enumerate(headers):
        cell = table_acteurs.rows[0].cells[i]
        cell.paragraphs[0].add_run(h).bold = True
        set_cell_background(cell, "1E3A8A")
        cell.paragraphs[0].runs[0].font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

    data_acteurs = [
        ("👤 Responsable Marketing", "Consulte les dashboards, extrait les listes de cibles (VIP, Fidèles) et génère des exports CSV."),
        ("👤 Data Analyst / BI", "Analyse les performances globales, vérifie la cohérence des catégories et des visualisations."),
        ("👤 Data Scientist", "Vérifie l'efficacité du modèle de clustering K-Means et l'ajustement des descripteurs."),
        ("👤 Responsable Commercial", "Identifie les clients VIP à privilégier et les comptes à fort potentiel."),
        ("⚙️ Administrateur Système", "Gère l'application, les migrations de base de données et la sécurité des accès.")
    ]
    for row_idx, (r_role, r_miss) in enumerate(data_acteurs, start=1):
        row = table_acteurs.rows[row_idx]
        row.cells[0].paragraphs[0].add_run(r_role).bold = True
        row.cells[1].paragraphs[0].add_run(r_miss)
        if row_idx % 2 == 0:
            set_cell_background(row.cells[0], "F3F4F6")
            set_cell_background(row.cells[1], "F3F4F6")

    doc.add_heading("2. 💻 ARCHITECTURE ET STACK TECHNIQUE", level=1)
    doc.add_paragraph(
        "L'application repose sur le framework web Django en appliquant le patron de conception MVT (Model-View-Template) :"
    )
    
    p = doc.add_paragraph()
    p.add_run("• Model (main/models.py) : ").bold = True
    p.add_run("Définit la structure de données Customer (total_achats, nombre_visites, pages_visitees, temps_navigation, produits_consultes) et les méthodes métier de calcul du score.\n")
    p.add_run("• View (main/views.py) : ").bold = True
    p.add_run("Gère le traitement des requêtes HTTP, le CRUD, le filtrage, les requêtes d'agrégation ORM et l'entraînement du modèle K-Means.\n")
    p.add_run("• Template (main/templates/) : ").bold = True
    p.add_run("Gabarits d'affichage dynamiques HTML/CSS avec intégration de Chart.js et Mermaid.js.")

    doc.add_heading("3. 🧠 ALGORITHMES ET DATA SCIENCE", level=1)
    
    doc.add_heading("3.1 Système de Scoring Comportemental Heuristique", level=2)
    doc.add_paragraph(
        "Le score de chaque client est évalué selon la formule suivante :\n"
        "Score = (total_achats / 10000 * 40) + (nombre_visites * 10) + (pages_visitees * 5) + (produits_consultes * 3) + (temps_navigation * 2)"
    )

    table_cat = doc.add_table(rows=5, cols=3)
    table_cat.style = 'Table Grid'
    cat_headers = ["Catégorie", "Condition du Score", "Profil du Client"]
    for i, h in enumerate(cat_headers):
        cell = table_cat.rows[0].cells[i]
        cell.paragraphs[0].add_run(h).bold = True
        set_cell_background(cell, "2563EB")
        cell.paragraphs[0].runs[0].font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

    cats_data = [
        ("🟢 VIP", "Score >= 80", "Clients très très engagés et à fort pouvoir d'achat."),
        ("🔵 Fidèle", "Score >= 50", "Clients réguliers avec un bon volume d'achats."),
        ("🟠 Potentiel", "Score >= 20", "Clients en cours de découverte avec un potentiel d'évolution."),
        ("⚪ Nouveau", "Score < 20", "Clients récents ou inactifs à stimuler par des offres.")
    ]
    for row_idx, (cat, cond, desc) in enumerate(cats_data, start=1):
        row = table_cat.rows[row_idx]
        row.cells[0].paragraphs[0].add_run(cat).bold = True
        row.cells[1].paragraphs[0].add_run(cond)
        row.cells[2].paragraphs[0].add_run(desc)

    doc.add_heading("3.2 Segmentation Machine Learning (K-Means Clustering)", level=2)
    doc.add_paragraph(
        "Dans le module /ia/, un modèle de Clustering K-Means (K=3) effectue un découpage non surveillé :\n"
        "1. Standardisation Z-Score : X_scaled = (X - mean) / std pour équilibrer le poids de total_achats et nombre_visites.\n"
        "2. Entraînement K-Means : Calcul des centres de gravité (centroids) dans l'espace des descripteurs.\n"
        "3. Tri cohérent des clusters par niveau d'achat moyen (0: Économique, 1: Régulier, 2: Premium/VIP)."
    )

    doc.add_heading("4. 🖥️ DESCRIPTION DES MODULES FONCTIONNELS", level=1)
    
    p = doc.add_paragraph()
    p.add_run("1. Dashboard Principal (/dashboard/) : ").bold = True
    p.add_run("Cartes KPIs (Total clients, Achats globaux, Score moyen, Décompte VIP), graphiques sectoriels et classements des meilleurs clients.\n")
    p.add_run("2. Gestion des Clients (/clients/) : ").bold = True
    p.add_run("Recherche textuelle instantanée, filtrage par catégorie et formulaires d'ajout/modification/suppression.\n")
    p.add_run("3. Exportation CSV (/clients/export-csv/) : ").bold = True
    p.add_run("Génération et téléchargement d'un fichier CSV récapitulatif encodé en UTF-8 with BOM.\n")
    p.add_run("4. Module d'IA (/ia/) : ").bold = True
    p.add_run("Visualisation 2D interactives du nuage de points et des centres de gravité des clusters K-Means.\n")
    p.add_run("5. Documentation UML (/uml/) : ").bold = True
    p.add_run("Rendu dynamique des diagrammes des Cas d'Utilisation, de Classes MVT et de Séquence.")

    doc.add_heading("5. 🛠️ GUIDE D'INSTALLATION ET DE DÉPLOIEMENT", level=1)
    doc.add_paragraph("Pour exécuter l'application sur votre machine localement :")
    
    p_cmd = doc.add_paragraph()
    p_cmd.add_run("1. Activer l'environnement virtuel :\n").bold = True
    p_cmd.add_run("   .\\env\\Scripts\\activate\n")
    p_cmd.add_run("2. Lancer le serveur Django :\n").bold = True
    p_cmd.add_run("   python Analyse_intelligente_des_clients/manage.py runserver\n")
    p_cmd.add_run("3. Accéder à l'application :\n").bold = True
    p_cmd.add_run("   http://127.0.0.1:8000/")

    doc.add_heading("6. 🔮 PERSPECTIVES ET ÉVOLUTIONS FUTURES", level=1)
    p_fut = doc.add_paragraph()
    p_fut.add_run("• Prédiction du Churn Rate : ").bold = True
    p_fut.add_run("Intégrer une classification supervisée (Random Forest / Régression Logistique) pour anticiper les départs clients.\n")
    p_fut.add_run("• Recommandation de Produits : ").bold = True
    p_fut.add_run("Moteur de filtrage collaboratif basé sur la similarité des profils d'achats.\n")
    p_fut.add_run("• Rapports PDF Automatisés : ").bold = True
    p_fut.add_run("Exportation de bilans exécutifs formatés pour les réunions de direction.")

    filename = "DOCUMENTATION_COMPLETE_SMARTCUSTOMER_ANALYTICS.docx"
    doc.save(filename)
    print(f"Document Word créé avec succès : {filename}")

if __name__ == "__main__":
    create_document()
