Algorithme (Filtrage & Dictionnaires)
DÉBUT

    INITIALISER deux listes : valides et invalides.
    OUVRIR eleves.csv.
    CONFIGURER DictReader pour qu'il nettoie automatiquement les espaces des clés et valeurs.
    POUR CHAQUE ligne (dictionnaire) lue :
        VÉRIFIER la conformité :
            Le Code est-il unique et bien formaté ?
            Le Nom et Prénom commencent-ils par une lettre ?
            La Date_Naissance est-elle convertible en format date ?
            Les Notes sont-elles toutes numériques et entre 0 et 20 ?
        SI toutes les conditions sont VRAIES :
            Ajouter le dictionnaire à valides.
        SINON :
            Ajouter le dictionnaire à invalides avec la cause du rejet.
    RAPPORT D'AUDIT : Afficher la liste invalides pour signaler les erreurs détectées dans le fichier source.
    MENU INTERACTIF : Proposer les opérations (Affichage, Modification, Recherche) sur la liste valides.
        Note : La modification permet de corriger les erreurs de saisie détectées.
    PERSISTANCE : Sauvegarder la liste valides (contenant les données saines et corrigées) dans donnees.json.

FIN

Algorithme En POO (Modélisation & Persistance JSON)

DÉBUT

A. Définition de l'Objet Eleve

    PROPRIÉTÉS : code, nom, prenom, date, classe, notes.
    MÉTHODE calculer_moyenne() : Logique de calcul interne.
    MÉTHODE to_dict() : Prépare l'objet pour l'export JSON.

B. Processus Principal (Le Pilotage)

    PRÉ-TRAITEMENT (Audit) :
        Exécuter le filtrage du CSV (identique à la version Sans POO).
        AFFICHER le rapport des données invalides pour information.
        INSTANCIER un objet Eleve pour chaque ligne de la liste valides.
        Stocker ces objets dans une liste MaClasse.
    CHARGEMENT HYBRIDE :
        SI donnees.json existe : Charger et recréer les objets directement (priorité à la sauvegarde précédente).
        SINON : Utiliser les objets créés à partir du CSV filtré.
    MENU INTERACTIF :
        L'utilisateur interagit avec les méthodes des objets (Modifier, Calculer).
        MODIFICATION : Permet de mettre à jour les informations. Chaque modification déclenche une re-validation immédiate pour garantir l'intégrité.
    SAUVEGARDE FINALE :
        Parcourir MaClasse, transformer chaque objet via to_dict() et enregistrer le tout en JSON (le format JSON devient la base de données corrigée).

FIN
