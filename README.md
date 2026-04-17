PROJET PYTHON – DEV DATA P8
Gestion et traitement de données
Objectif du projet
Ce projet consiste à :
•
•
•
•
Récupérer et analyser un fichier de données
Valider et structurer les informations
Manipuler les données avec Python
Créer un programme interactif (menu)
1. Traitement des données
Étape 1 : Récupération des données
Vous devez récupérer le fichier : « Donnees_Projet_Python_Dev_Data »
Étape 2 : Traitement des données
Après lecture du fichier :
•
•
Traiter les informations contenues dans chaque ligne
Stocker les données dans une structure de votre choix :
o Liste
o Tuple
o Dictionnaire
o Ou combinaison
Étape 3 : Validation des données
Vous devez :
•
Séparer les données en deux groupes :
o Données valides
o Données invalides
Une ligne est invalide si au moins une information est incorrecte.
Étape 4 : Gestion des données invalides
Pour chaque ligne invalide, vous devez :
•
•
•
Conserver les informations
Indiquer les éléments incorrects
Expliquer pourquoi ils sont invalides2. Règles de validation des données
Chaque champ doit respecter des règles précises.
CODE
•
•
•
3 lettres majuscules suivies de 3 chiffres
Longueur : 6 caractères
Exemple AAD004
Numéro
•
•
•
Composé de lettres majuscules et de chiffres
Longueur : 7 caractères
Exemples : H5G32YR ou 54YTG5T
Prénom
•
•
Commence par une lettre
Contient au moins 3 lettres
Nom
•
•
Commence par une lettre
Contient au moins 2 lettres
Date de naissance
•
•
Doit être une date valide
Vous devez :
o Choisir un format
o Convertir toutes les dates dans ce format
Classe
•
Valeurs possibles : de 6em à 3em avec A, B, C ou D
Exemples possibles : 4emA, 4 em a, 4iem A, etc.
Vous devez :
•
•
Choisir un format unique
Convertir toutes les classes dans ce formatNotes
Les notes sont sous forme de chaîne de caractères.
Format :
•Les matières sont séparées par #
•Les notes sont entre crochets []
•Les devoirs sont séparés par |
•La note d’examen est séparée par :
Exemple :
•
Math[12|11:13]#Francais[4|11|8:13]#Anglais[13,5|11:15]#PC[11:9]#SVT[1
2|9|16|11:12]#HG[10:13]
•
Francais[4|11:13]#Anglais[13,5:15]#PC[11:9]#SVT[12|9|16|11:12]#HG[10:
13]#Math[12|14,5|11:13]
Pour chaque matière, vous devez extraire :
•
•
•
les notes de devoir
la note d’examen
calculer la moyenne selon la formule donnée
moyenne = (moyenne_devoirs + 2×examen)/3
3. Fonctionnalités du programme
Vous devez créer un menu interactif permettant :
Affichage des données
•
•
•
Afficher les données valides ou invalides (au choix)
Afficher une information à partir de son numéro
Afficher les cinq premières entrées
Ajout de données
•
•
Permettre d’ajouter une nouvelle information
Vérifier la validité des données saisies
Modification
•
•
Modifier une information invalide
Transférer une information corrigée vers les données validesRecherche
•
•
Afficher les informations d’une personne à partir de son Numéro
Afficher les lignes saisies par une personne à partir de son code en affichant le
pourcentage de données valides et invalides données par cette personne.
4. Pagination
L’affichage des données doit être paginé :
•
•
Afficher par défaut 5 lignes par page
Permettre à l’utilisateur de choisir le nombre de lignes par page
Consignes importantes
•
•
•
Vous devez écrire l’algorithme détaillé avant de coder
Vous devez utiliser uniquement les modules Python de base
Le code doit être clair, structuré et organisé
Compétences visées
Ce projet permet de travailler :
•
•
•
•
•
•
la logique algorithmique
la validation des données
les structures de données
les chaînes de caractères
la manipulation de fichiers
la conception de programme
