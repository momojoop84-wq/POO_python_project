import csv 

Data_Base=[ ]

with open ("Donnees_Projet_Python_Dev_Data.csv","r", encoding="utf-8") as Data:
    lines = csv.DictReader(Data, delimiter=';')
    for i in lines :
        Data_Base.append(i)
print(Data_Base[:5])




#Validation Code----------------------------------------------------------------------------------------------------
def LongueurCode(CODE) :
    if len (CODE) == 6 :
        return True
    else : 
        return False 

def AlphaUpperCode(CODE) :
    if CODE[:3].isalpha() and CODE[:3].isupper() :
        return True
    else : 
        return False 

def NumCode(CODE) :
    if CODE[3:].isnumeric() :
        return True
    else : 
        return False 

def validation_Code(CODE):
    if LongueurCode(CODE) and AlphaUpperCode(CODE) and CODE[:3].isupper() and NumCode(CODE) :
        return True
    return False  




#Validation du numéro --------------------------------------------------------------------------------------
def longueurNumero(Numero):
    if len(Numero) == 7 :
        return True
    else :
        return False

def contenuNumero(Numero):
    if Numero.isalnum() and Numero.isupper() :
       return True
    else :
        return False

def est_valide_numero(numero):
    #on appelle les deux briques
    if longueurNumero(numero) and contenuNumero(numero):
        return True
    return False



#----------------Prénom-------------------------
def LongueurPrenom(Prénom):
    if len(Prénom) >= 3 :
        return True
    else :
        return False 

def AlphaPrenom(Prénom):
    if Prénom[0].isalpha() :
           return True
    else :
        return False

def est_valide_Prenom(Prénom) :
    # On appelle les deux briques
    if LongueurPrenom(Prénom) and AlphaPrenom(Prénom) :
        return True
    return False



#-----------------Nom-----------------------------------------------
def LongueurNom(Nom) :
    if len(Nom) >= 2:
        return True
    else :
        return False 

def AlphaNom(Nom) :    
    if Nom[0].isalpha() :
        return True
    else :
        return False 

def est_valide_Nom(Nom) :
    # On appelle les deux briques
    if LongueurNom(Nom) and AlphaNom(Nom) :
        return True
    return False

#-----------------Date---------------------------------------------
def formater_date(chaine):
    # On remplace tous les séparateurs par des "/"
    for sep in [" ", "-", ".", ":", "_"]:
        chaine = chaine.replace(sep, "/")
    return chaine

def nb_jours_max(mois, annee):
    # Mois à 30 jours
    if mois in [4, 6, 9, 11]:
        return 30
    # Février
    if mois == 2:
        # Règle mathématique pour les années bissextiles
        if (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0):
            return 29
        return 28
    # Tous les autres sont à 31
    return 31


def est_date_valide(date_propre):
    parties = date_propre.split("/")
    
    # 1. Structure
    if len(parties) != 3: return False
    
    # 2. Type (que des chiffres)
    if not all(p.isdigit() for p in parties): return False
    
    # 3. Valeurs (Logique métier)
    j, m, a = int(parties[0]), int(parties[1]), int(parties[2])
    
    # 1. On vérifie d'abord que le mois et l'année sont cohérents
    if not (1 <= m <= 12 and 1900 <= a <= 2025): 
        return False
        
    # 2. On vérifie que le jour ne dépasse pas le MAX de ce mois-là
    if not (1 <= j <= nb_jours_max(m, a)):
        return False
        
    return True




#-------------Classe----------------------------
def formateur_classe(c):
    c = c.upper().replace(" ", "")
    if len(c) < 2:
        return "XX"
    # On ne garde que le premier et le dernier caractère
    return c[0] + c[-1]

def est_classe_valide(c_propre):
    # Le chiffre doit être entre 6 et 3, la lettre entre A et D
    chiffre = c_propre[0] in ["6", "5", "4", "3"]
    lettre = c_propre[1] in ["A", "B", "C", "D"]
    return chiffre and lettre

def validation_Classe(Classe) :
    classe_p = formateur_classe(Classe)
    if est_classe_valide(classe_p) : 
        return True 
    return False


#-----------------Notes : Parsing----et-----Moyenne-----------------------------------------------
def nettoyer_note(chaine) :
    return chaine.replace(",", ".")

def est_note_valide(n_str) :
    try:
        valeur = float(n_str)
        return 0 <= valeur <= 20
    except ValueError:
        return False

def calculer_moyenne_matiere(devoirs, examen) :
    moy_dev = sum(devoirs) / len(devoirs)
    return (moy_dev + 2 * examen) / 3

def traiter_notes_eleve(chaine_globale) :
    matieres = chaine_globale.split("#")
    dictionnaire_moyennes = {}

    for m in matieres :
        if "[" not in m or "]" not in m :
            return False # Sécurité : si la structure est cassée, on rejette
            
        # --- ETAPE A : Découpage (Parsing pur) ---
        # On fait le split une seule fois et on stocke le résultat dans une variable
        decoupe = m.split("[") 

        nom = decoupe[0]
        # On prend la partie de droite et on nettoie juste le "]"
        contenu = decoupe[1].replace("]", "") 

        parties = contenu.split(":")
        if len(parties) < 2:
            return False # Sécurité si pas de ":" (note d'examen manquante)
        
        dev_str = parties[0].split("|")
        ex_str = parties[1]
        
        dev_floats = []
        for d in dev_str :
            # 1. ON NETTOIE (Responsabilité Unique)
            propre = nettoyer_note(d)
            
            # 2. ON VALIDE
            if not est_note_valide(propre): 
                return False # On arrête tout si une note est fausse
                
            # 3. ON STOCKE POUR LE CALCUL
            dev_floats.append(float(propre))

        # --- Pareil pour l'examen ---
        examen_propre = nettoyer_note(ex_str)
        if not est_note_valide(examen_propre): return False
        examen_final = float(examen_propre)


        # --- ETAPE B: Calcul (Appel au Calculateur) ---
        moyenne = calculer_moyenne_matiere(dev_floats, examen_final)
        dictionnaire_moyennes[nom] = round(moyenne, 2)
    
    # --- On ne retourne le dictionnaire qu'une fois TOUTES les matières traitées ---
    return dictionnaire_moyennes


VALIDE = []
INVALIDE = []
for eleve in Data_Base:
    # On crée un petit carnet de notes pour cet élève précis
    erreurs_eleve = []

    # --- TEST 1 : LE CODE ---
    if not validation_Code(eleve['CODE']):
        erreurs_eleve.append("CODE : doit être 3 MAJ suivies de 3 chiffres")

    # --- TEST 2 : LE NUMÉRO ---
    # if not est_valide_numero(eleve['Numero']):
        # erreurs_eleve.append("Numéro : format 7 caractères (MAJ+Chiffres) invalide")
    
    # On transforme en majuscules AVANT de tester
    numero_propre = eleve['Numero'].upper() 

    if not est_valide_numero(numero_propre):
        erreurs_eleve.append("Numéro : format invalide")
    else:
        # IMPORTANT : on enregistre la version MAJUSCULE dans la base
        eleve['Numero'] = numero_propre 

    
    # --- TEST 3 : LE NOM / PRÉNOM ---
    if not est_valide_Nom(eleve['Nom']) or not est_valide_Prenom(eleve['Prénom']):
        erreurs_eleve.append("Nom/Prénom : doit commencer par une lettre et être assez long")

    # --- TEST 4 : LA DATE (On nettoie avant !) ---
    date_propre = formater_date(eleve['Date de naissance'])
    if not est_date_valide(date_propre):
        erreurs_eleve.append("Date : inexistante ou format incorrect")

    # --- TEST 5 : LES NOTES ---
    moyennes = traiter_notes_eleve(eleve['Note'])
    if moyennes is False:
        erreurs_eleve.append("Notes : format invalide ou notes hors barème")
    
    # --- TEST 6 : LES CLASSE ---
    if not validation_Classe(eleve['Classe']) :
        erreurs_eleve.append("Classe : format invalide ou notes hors barème")

    # --- L'AIGUILLAGE FINAL ---
    if len(erreurs_eleve) == 0:
        # L'élève n'a AUCUNE erreur : il va dans VALIDE
        # On en profite pour enregistrer les données propres (date, moyennes)
        eleve['Date'] = date_propre
        eleve['MOYENNES'] = moyennes
        VALIDE.append(eleve)
    else:
        # L'élève a des erreurs : il va dans INVALIDE
        # On enregistre ses erreurs dans son dictionnaire pour le menu plus tard
        eleve['MOTIFS'] = erreurs_eleve
        INVALIDE.append(eleve)

print(f"Nombre d'élèves valides : {len(VALIDE)}")
print(f"Nombre d'élèves invalides : {len(INVALIDE)}")

# Optionnel : voir les erreurs du premier élève invalide
if INVALIDE:
    print(f"Exemple d'erreur : {INVALIDE[0]['MOTIFS']}")

total = len(VALIDE) + len(INVALIDE)
if total > 0:
    p_valide = (len(VALIDE) / total) * 100
    p_invalide = (len(INVALIDE) / total) * 100
    
    print("\n" + "="*50)
    print(f"BILAN DU TRAITEMENT")
    print(f"Total d'élèves : {total}")
    print(f"Valides        : {len(VALIDE)} ({p_valide:.1f}%)")
    print(f"Invalides      : {len(INVALIDE)} ({p_invalide:.1f}%)")
    print("="*50 + "\n")

def afficher_pagination(liste_a_afficher):
    if not liste_a_afficher:
        print("Aucune donnée à afficher.")
        return

    taille_page = 5
    total_pages = (len(liste_a_afficher) + taille_page - 1) // taille_page
    page_actuelle = 0

    while True:
        debut = page_actuelle * taille_page
        fin = debut + taille_page
        page_donnees = liste_a_afficher[debut:fin]

        print(f"\n--- Page {page_actuelle + 1} / {total_pages} ---")
        print(f"{'NUMERO':<10} | {'NOM':<15} | {'PRENOM':<15} | {'CLASSE':<6} | {'INFOS/MOYENNES'}")
        print("-" * 110)
        for e in page_donnees:
            classe_p = formateur_classe(e['Classe'])
            
            # 2. On prépare la colonne de droite (Moyennes OU Erreurs)
            if 'MOYENNES' in e:
                # On affiche les moyennes car l'élève est valide
                infos = ", ".join([f"{m}:{n}" for m, n in e['MOYENNES'].items()])
            else:
                # On affiche les motifs car l'élève est invalide
                infos = "ERREURS: " + ", ".join(e.get('MOTIFS', ["Inconnu"]))

            # 3. L'AFFICHAGE UNIQUE (Toutes les données sur une ligne)
            print(f"{e['Numero']:<10} | {e['Nom']:<15} | {e['Prénom']:<15} | {classe_p:<6} | {infos}")

        print("\n[S]uivant | [P]récédent | [Q]uitter le menu")
        action = input("Action : ").upper()

        if action == 'S' and page_actuelle < total_pages - 1:
            page_actuelle += 1
        elif action == 'P' and page_actuelle > 0:
            page_actuelle -= 1
        elif action == 'Q':
            break

# --- PROGRAMME PRINCIPAL (MENU) ---
while True:
    print("\n========== GESTION ÉLÈVES ==========")
    print("1. Afficher les données valides")
    print("2. Afficher les données invalides")
    print("3. Rechercher par Numéro")
    print("4. Modifier une information invalide") 
    print("5. Quitter")
    
    choix = input("Votre choix (1-5) : ")

    if choix == "1":
        #On appelle la fonction de pagination 
        print("\n--- LISTE DES ÉLÈVES VALIDES ---")
        afficher_pagination(VALIDE)

    elif choix == "2":
        # On affiche les invalides (la pagination affichera aussi leurs motifs d'erreurs)
        print("\n--- LISTE DES ÉLÈVES INVALIDES ---")
        afficher_pagination(INVALIDE)

    elif choix == "3":
        num_rech = input("Entrez le numéro de l'élève à rechercher : ").upper()
        trouve = False
        #  On cherche dans les deux listes pour être complet
        for e in VALIDE + INVALIDE:
            if e['Numero'] == num_rech:
                print(f"\n✅ TROUVÉ : {e['Nom']} {e['Prénom']}")
                print(f"Détails : {e}")
                trouve = True
                break
        if not trouve: print("❌ Aucun élève ne possède ce numéro.")

    elif choix == "4": 
        if not INVALIDE:
            print("Aucune donnée invalide à corriger.")
        else:
            # 1. On affiche la liste des fautifs avec un numéro simple (1, 2, 3...)
            print("\n--- CHOISISSEZ LA LIGNE À CORRIGER ---")
            for i in range(len(INVALIDE)):
                print(f"{i+1}. {INVALIDE[i]['Nom']} {INVALIDE[i]['Prénom']}")

            # 2. L'utilisateur choisit le numéro de la ligne
            try:
                index = int(input("\nEntrez le chiffre de la ligne à modifier (0 pour annuler) : "))
                if 1 <= index <= len(INVALIDE):
                    cible = INVALIDE[index - 1] # -1 car l'index commence à 0 en Python
                    
                    # 3. RAPPEL DES ERREURS (On aide l'utilisateur)
                    print(f"\n>>> MODIFICATION DE : {cible['Nom']} {cible['Prénom']}")
                    print(f"Erreurs à corriger : {cible['MOTIFS']}")

                    # 4. On demande quel champ modifier
                    # On affiche les clés possibles pour l'aider
                    champ = input("Champ à modifier (Nom, Prénom, Date de naissance, Classe, Note) : ")
                    if champ in cible:
                        nouvelle_valeur = input(f"Nouvelle valeur pour {champ} : ")
                        cible[champ] = nouvelle_valeur
                        print("✅ Modifié ! (Pensez à relancer pour re-valider)")
                    else:
                        print("❌ Champ inexistant.")
            except ValueError:
                print("❌ Entrez un chiffre valide.")

    elif choix == "5":
        print("Fermeture du programme. Au revoir !")
        break

