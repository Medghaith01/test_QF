"""
Plan d'alignement — Test Technique The Quantic Factory
=======================================================
Lecture du PDF et analyse des écarts avec l'état actuel.

À lire avant toute modification des notebooks.
"""

# ============================================================
# RAPPEL DES EXIGENCES DU PDF
# ============================================================
"""
1. HYPOTHÈSE CLAIRE avant de creuser
   - "Formuler une hypothèse claire avant de creuser"
   - "Prouver quelque chose de concret, pas seulement décrire"
   - → Une question de recherche ne suffit PAS

2. HONNÊTETÉ SCIENTIFIQUE
   - "Rester dans la véracité : ne pas forcer une conclusion"
   - "Si vous testez plusieurs hypothèses, dites-le"
   - "Distinguer explicitement corrélation et causalité"
   - "Mentionner la taille d'échantillon et les limites/incertitudes"

3. DATAVIZ
   - "Immédiatement compréhensible par un non-spécialiste"
   - "Privilégier simplicité et pertinence"
   - Pas de graphique trivial (ex: évolution mois par mois seule)
   - Pas de visualisation surchargée sans valeur ajoutée

4. RENDU
   - Code + Présentation (PDF/PPT)
   - Présentation : sujet, hypothèse, méthode, résultats, dataviz clés,
     conclusions AVEC limites et incertitudes
"""

# ============================================================
# ÉTAT ACTUEL DU NARRATIF
# ============================================================
"""
EDA actuel : structure en "enquête"
  1. Hypothèse initiale : jeunes 2RM à risque
  2. Section 1, 2, 3 : réfutation progressive
  3. Section 3 (heatmap) : découverte des piétons âgés
  4. Section 9 : conclusion → piétons âgés = vrai groupe à risque

Problème : la question de recherche "Comment âge × mode influence gravité ?"
est exploratoire, pas une hypothèse testable. Le PDF exige une HYPOTHÈSE.
"""

# ============================================================
# HYPOTHÈSE RECOMMANDÉE
# ============================================================
"""
Proposition : reformuler en hypothèse testable.

H1 : Les piétons âgés de 65 ans et plus présentent une probabilité
     de blessure grave (hospitalisé ou tué) significativement plus élevée
     que les autres usagers, même après contrôle des facteurs contextuels
     (éclairage, météo, genre).

Justification :
  - Testable : comparaison piétons 65+ vs tous les autres
  - Précise : "65 ans et plus", "blessure grave", "contrôle des covariables"
  - Supportée par les données : OR=1.46, IC 95% [1.23-1.74]
  - Laisse place aux limites et à la distinction corrélation/causalité

H0 : L'âge n'a pas d'effet sur la gravité chez les piétons après
     contrôle des covariables.
"""

# ============================================================
# CE QUI DOIT CHANGER DANS CHAQUE NOTEBOOK
# ============================================================

# ---- data_cleaning.ipynb ----
"""
✅ DÉJÀ FAIT : nettoyage VMA (48 artifacts → NaN)
✅ OK : colonnes créées, types corrigés, CSV exporté

À VÉRIFIER :
  - Ajouter une cellule narrative qui décrit le nettoyage effectué
  - Mentionner la taille finale (33 551 lignes, 26 colonnes)
  - Mentionner le traitement des valeurs manquantes
"""

# ---- eda_patterns.ipynb ----
"""
CHANGEMENTS NÉCESSAIRES :

A. INTRODUCTION (cellule titre, lignes 20-37)
   AVANT : "L'hypothèse initiale était erronée → le vrai groupe à risque est..."
   APRÈS : Reformuler sous forme d'hypothèse claire + narration d'honnêteté
           "Nous formulons l'hypothèse H1 : les piétons 65+ ont une gravité
            accrue. Avant de la tester, explorons les données...
            Note : cette hypothèse n'est pas la première que nous avons testée
            — nous avons d'abord exploré l'hypothèse jeunes 2RM, qui n'a pas
            été confirmée par les données. C'est ce qui nous a menés à H1."

B. SECTION 2 (âge) - lignes 571-605
   AVANT : "Première faille dans notre hypothèse"
   APRÈS : Reformuler pour montrer que c'est l'exploration qui guide
           l'affinement de l'hypothèse, pas une "réfutation"

C. SECTION 3 (interaction) - lignes 860-873
   AVANT : "L'hypothèse initiale n'est pas confirmée"
   APRÈS : Reformuler comme "Exploration ayant conduit à la formulation de H1"
           Ajouter mention de l'honnêteté scientifique (plusieurs hypothèses
           testées)

D. SECTION 9 (synthèse)
   Reformuler pour :
   - Rappeler H1 explicitement
   - Lister les analyses qui soutiennent H1
   - Lister les limites / incertitudes
   - Distinguer corrélation et causalité

E. MENTIONS OBLIGATOIRES À AJOUTER (quelque part dans l'EDA) :
   1. "Ceci est une analyse corrélationnelle, pas causale"
   2. "Nous avons testé plusieurs hypothèses avant de retenir H1"
   3. Taille d'échantillon : n=33 551
   4. Limites : base OpenData Paris (déclaratif ?), biais de sélection,
      absence de données médicales, pas de suivi longitudinal
"""

# ---- hypothesis_testing.ipynb ----
"""
CHANGEMENTS NÉCESSAIRES :

A. INTRODUCTION
   - Rappeler H1 explicitement
   - Structure : trois méthodes indépendantes pour confirmer

B. AJOUTS NÉCESSAIRES :
   1. Limites et incertitudes dans la conclusion
   2. Distinction corrélation/causalité
   3. Taille d'échantillon rappelée
   4. Note sur les hypothèses testées avant H1

C. STRUCTURE ACTUELLE (déjà bonne) :
   - Chi² + OR (Section 1-3)
   - Régression logistique (Section 4-7)
   - XGBoost + SHAP (Section 8-10)
"""

# ---- rapport_analyse.ipynb ----
"""
CHANGEMENTS NÉCESSAIRES :

A. INTRODUCTION
   - Sujet + hypothèse de départ explicites
   - Méthode résumée

B. RÉSULTATS CLÉS
   - Les dataviz essentielles
   - Les chiffres clés (OR, p-values, importance SHAP)

C. CONCLUSIONS
   - AVEC limites et incertitudes
   - Distinction corrélation/causalité
   - "Ce que les données montrent / ne montrent pas"

D. SUGGESTION : ajouter une slide "Mise en garde" ou "Limites"
"""

# ============================================================
# DATAVIZ À CONSERVER / SUPPRIMER
# ============================================================
"""
CONSERVER (supportent H1 directement) :
  - 03_mode_age_heatmap.png (interaction centrale)
  - 02b_age_u_curve.png (courbe en J, montre le pic 75+)
  - 01_mode_severity.png (montre que Piétons = mode le plus grave)

CONSERVER (covariables de contrôle) :
  - 05_environmental_severity.png (contextualise)
  - 10_vma_severity.png (avec labels, montre absence de gradient)

À SUPPRIMER OU SIMPLIFIER (trop triviaux ou surchargés) :
  - 07_monthly_trends.png (évolution mois par mois = trivial si seul)
  - 08_covid_severity.png (intéressant mais périphérique)
  - 09_dayofweek_patterns.png (montre juste fréquence, pas de conclusion)
  - 06_arrondissement_hotspots.png (corrélation faible, peu conclusive)

À GARDER MAIS DÉPLACER EN ANNEXE :
  - 04_gender_mode_severity.png
  - 02_age_severity.png (graphique en barres, redondant avec 02b)
"""

# ============================================================
# ORDRE DE TRAVAIL PROPOSÉ
# ============================================================
"""
1. [x] Nettoyage VMA dans data_cleaning.ipynb
2. [ ] Ajustements narratifs eda_patterns.ipynb
3. [ ] Ajustements narratifs hypothesis_testing.ipynb
4. [ ] Ajustements narratifs rapport_analyse.ipynb
5. [ ] Re-exécuter tous les notebooks
6. [ ] Décider quels outputs conserver
7. [ ] Générer la présentation (PDF)
"""

# ============================================================
# NOTE SUR LA PRÉSENTATION
# ============================================================
"""
Le PDF exige une PRÉSENTATION (PowerPoint, Google Slides ou PDF)
qui résume la démarche et sert de support à l'oral.

Contenu minimum :
  - Sujet et hypothèse de départ
  - Méthode (données, traitements, outils)
  - Résultats et dataviz clés
  - Conclusions AVEC limites et incertitudes

À PRÉVOIR APRÈS validation des notebooks.
"""
