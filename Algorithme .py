""" 
I. Algorithme de Traitement Linéaire (Approche Procédurale)
Nom : Calcul_Moyennes_Direct
Description : Traite les données de manière séquentielle pour un affichage immédiat.
ALGORITHME :

    Variable ligne : Chaîne de caractères
    Variable valeurs : Tableau de réels
    Ouvrir eleves.csv en accès LECTURE
    Sauter l'en-tête du fichier
    TANT QUE le curseur n'est pas à la fin du fichier (EOF) :
        ligne ← Lire ligne suivante
        données ← Scinder ligne par le séparateur ","
        nom ← données[0]
        valeurs ← Convertir données[1...n] en Nombres
        moyenne ← Somme(valeurs) / Taille(valeurs)
        AFFICHER nom, moyenne
    Fermer le fichier
    FIN

II. Algorithme de Modélisation (Approche POO)
Nom : Gestion_Classe_Objets
Description : Découple la structure des données de la logique de traitement pour permettre la réutilisation.
1. Structure de l'Entité Eleve

    PROPRIÉTÉS : identifiant, notes (Tableau de réels)
    FONCTION calculerMoyenne() :
        SI Taille(notes) == 0 RETOURNER 0
        RETOURNER Somme(notes) / Taille(notes)

2. Processus Principal

    Initialiser ListeClasse : Liste d'objets Eleve
    CHARGEMENT :
        POUR CHAQUE enregistrement dans eleves.csv :
            e ← Nouvelle Instance de Eleve avec les données brutes
            Ajouter e à ListeClasse
    TRAITEMENT :
        POUR CHAQUE e DANS ListeClasse :
            résultat ← e.calculerMoyenne()
            AFFICHER e.identifiant, résultat
    FIN"""
