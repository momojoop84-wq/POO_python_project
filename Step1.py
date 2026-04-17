"""
Étape 1:

    Ouvir le fichier.
    Boucler sur chaque ligne.
    Utilise .strip() pour enlever le \n (saut de ligne) invisible à la fin.
    Utilise .split(";") pour séparer les colonnes.
    Affiche le résultat des 5 premières lignes seulement.
"""
# lignes=[]
# with open ("Donnees_Projet_Python_Dev_Data.csv","r", encoding="utf-8") as fichier:
    # lignes = fichier.readlines()
    # lignes = [x.strip() for x in lignes ]
    # print(lignes[:5])
import csv 

Data_Base=[ ]

with open ("Donnees_Projet_Python_Dev_Data.csv","r", encoding="utf-8") as Data:
    lines = csv.DictReader(Data, delimiter=';')
    for i in lines :
        Data_Base.append(i)
print(Data_Base[:5])

"""
 TON ACTION (Étape 2.1) :
Je veux que tu essaies d'écrire une fonction est_valide_code(code).
Elle doit :

    Vérifier si la longueur est égale à 6.
    Vérifier si les 3 premiers sont des lettres MAJUSCULES.
    Vérifier si les 3 derniers sont des chiffres.
    Retourner True si tout est bon, sinon False.
    
"""

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
    CODE[3:].isnumeric() :
        return True
    else : 
        return False 

def validation_Code(CODE):
    if LongueurCode(CODE) and AlphaUpperCode(CODE) and CODE[:3].isupper() and NumCode(CODE) :
        return True
    return False  
        
"""
Passons à la règle suivante pour le Numéro :

    Règle : Composé de lettres majuscules ET de chiffres.
    Longueur : Exactement 7 caractères.
    Exemples valides : H5G32YR ou 54YTG5T.

Comment faire ?
Ici, les lettres et les chiffres sont mélangés. On ne peut pas couper en deux comme pour le code.
On doit vérifier que chaque caractère est soit une lettre majuscule, soit un chiffre.
Pour la fonction :

    Vérifier la longueur (7).
    Utilise .isalnum() (Vérifie si c'est alphanumérique : lettre ou chiffre).
    Utilise .isupper() sur toute la chaîne pour être sûr qu'il n'y a pas de minuscules.
"""
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


"""
Prénom
• Commence par une lettre
• Contient au moins 3 lettres
"""
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
"""
Nom
• Commence par une lettre
• Contient au moins 2 lettres
"""

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
 
"""
Date de naissance
Doit être une date valide
Vous devez :
o Choisir un format
o Convertir toutes les dates dans ce format
"""

def formater_date(chaine):
    # On remplace tous les séparateurs par des "/"
    for sep in [" ", "-", ".", ":", "_"]:
        chaine = chaine.replace(sep, "/")
    return chaine

def est_date_valide(date_propre):
    parties = date_propre.split("/")
    
    # 1. Structure
    if len(parties) != 3: return False
    
    # 2. Type (que des chiffres)
    if not all(p.isdigit() for p in parties): return False
    
    # 3. Valeurs (Logique métier)
    j, m, a = int(parties[0]), int(parties[1]), parties[2]
    return 1 <= j <= 31 and 1 <= m <= 12 and len(a) == 4


# def validation_Date(Date) :
    # Date = date.replace(" ","/").replace("-","/").replace(".","/")
    
    # dateFormat = date.split("/")
    # if len(dateFormat) != 3 :
        # return False
    # if not dateFormat[0].isnumeric() and  dateFormat[1].isnumeric() and dateFormat[3].isnumeric()
        # return False    
        
        # Day = int(dateFormat[0])
        # Month = int(dateFormat[1])
        # Year = int(dateFormat[2])
        
    # if 1 >= Day<= 31 and 1 >= Month <= 12 and len(Year) == 4 :
        # return True
    # else :
        # return False

"""
Classe
Valeurs possibles : de 6em à 3em avec A, B, C ou D
Exemples possibles : 4emA, 4 em a, 4iem A, etc.
Vous devez :
Choisir un format unique
Convertir toutes les classes dans ce format
"""

def formateur_classe(c):
    c = c.upper().replace(" ", "")
    # On ne garde que le premier et le dernier caractère
    return c[0] + c[-1]

def est_classe_valide(c_propre):
    # Le chiffre doit être entre 6 et 3, la lettre entre A et D
    chiffre = c_propre[0] in ["6", "5", "4", "3"]
    lettre = c_propre[1] in ["A", "B", "C", "D"]
    return chiffre and lettre


 def validation_Classe(Classe):    
    if formateur_classe(Classe)and est_classe_valide(Classe) :
        return True 
    return False

"""
Notes
Les notes sont sous forme de chaîne de caractères.
Format :
•Les matières sont séparées par #
•Les notes sont entre crochets []
•Les devoirs sont séparés par |
•La note d’examen est séparée par :
Pour chaque matière, vous devez extraire :
les notes de devoir
la note d’examen
calculer la moyenne selon la formule donnée
moyenne = (moyenne_devoirs + 2×examen)/3
"""
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
        # --- ETAPE A : Découpage (Parsing pur) ---
        nom = m.split("[")[0]
        
        # On récupère ce qu'il y a entre [ et ]
        contenu = m.split("[")[1].replace("]", "")
        parties = contenu.split(":")
        
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


# def parsing(GlobalNote):
    # notes = GlobalNote.split("#") # on sépare chaque matière 
    # for i in notes: # on boucle pour séparer les notes des matières par le séparateur "[" puis affecter les notes et matière chacune à une varible
        # note = notes.split("[")
        # nomMatière = note[0]
        # Gnote_matière = note[1] .replace("]", "") # en affectant les notes à une varible on enlève le crochet fermant à la fin "]" par replace 
        # Difnote = Gnote_matière.split(:)
        # noteDevoir_str = Difnote[0]
        # notecomposition = Difnote[1]
        # noteDevoir = noteDevoir_str.split("|")


# def verfyNote(note) :
    # if 0 >= note <= 20 :
        # return True
    # else :
        # return False



# def moyenne(moyenne):
    # noteDevoir = noteDevoir.replace(",",".")
    # noteDevoir = [float(i) for i in noteDevoir]
    # notecomposition = notecomposition.replace(",",".")
    # notecomposition = float(notecomposition) 
    # somme = noteDevoir[0]+noteDevoir[1]
    # moyenne = 