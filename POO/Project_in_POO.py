"""
ÉTAPE 5 — Introduction au fichier
À faire
• Lire le fichier du projet
• Créer des objets Etudiant à partir des données valide du fichier
Résultat attendu
Passage vers le projet
"""
"""
ÉTAPE 6 — Simplification du projet original
À faire
Créer une classe :
Personne
Attributs :
• code
• nom
• prenom
• classe
Créer une classe :
GestionDonnees
Méthodes :
• charger_fichier()
• valider_donnees()
• afficher_valides()
"""
import csv
from datetime import datetime
import json

class Etudiant:
    def __init__(self, nom, prenom, code, date_naiss, classe, age):
        self.nom = nom
        self.prenom = prenom
        self.code = code
        self.date_naiss = date_naiss # La date propre (ex: 01/01/2000)
        self.notes = {} # Contiendra les moyennes par matière
        self.classe = classe 
        self.age = age 

    def calculer_moyenne_generale(self):
        if not self.notes:
            return 0
        # On additionne toutes les moyennes de matières (les valeurs du dictionnaire)
        somme = sum(self.notes.values())
        nombre_matieres = len(self.notes)
        return round(somme / nombre_matieres, 2)
    
class GestionDonnees:
    def __init__(self):
        self.liste_valides = []
        self.liste_invalides = []

    # --- BRIQUE 1 : VALIDATION DU CODE ---
    
    def code_est_valide(self, code):
        if len(code) == 6 and code[:3].isalpha() and code[:3].isupper() and code[3:].isnumeric():
            return True
        return False

    # --- BRIQUE 2 : VALIDATION DU NOM/PRENOM ---
    
    def identite_est_valide(self, nom, prenom):
        if len(nom) >= 2 and nom[0].isalpha() and len(prenom) >= 3 and prenom[0].isalpha():
            return True
        return False

    # --- BRIQUE 3 : VALIDATION DE LA CLASSE ---
    
    def classe_est_valide(self, classe):
        c = classe.upper().replace(" ", "")
        if len(c) < 2: return False
        
        propre = c[0] + c[-1] # Ex: "6A"
        
        # On vérifie la validité
        if propre[0] in "6543" and propre[1] in "ABCD":
            return propre # On retourne "6A" (C'est ça qui sera stocké dans res_classe)
        return False
    
    # --- BRIQUE 4 : PARSING DES NOTES ---
    
    def parser_notes(self, chaine_globale):
        
        
        
        """Transforme le texte du CSV en dictionnaire de moyennes"""
        
        dictionnaire_moyennes = {}
        
        # On découpe par matière avec le séparateur "#"
        
        matieres = chaine_globale.split("#")

        for m in matieres:
            if "[" in m and "]" in m:
                
                # 1. Extraction du nom et des notes
                
                nom_matiere, reste = m.split("[")
                notes_brutes = reste.replace("]", "")
                
                # 2. Séparation Devoirs / Examen
                
                parties = notes_brutes.split(":")
                if len(parties) == 2:
                    dev_str = parties[0].split("|")
                    ex_str = parties[1]
                    
                    # 3. Conversion en nombres (float)
                    
                    try:
                        devoirs = [float(d.replace(",", ".")) for d in dev_str]
                        examen = float(ex_str.replace(",", "."))
                        
                        if not (0 <= examen <= 20) or any(not (0 <= d <= 20) for d in devoirs):
                            return False # Si une note dépasse 20, la brique renvoie False
                        
                        # 4. Calcul de la moyenne de la matière (pondérée)
                        
                        moy_dev = sum(devoirs) / len(devoirs)
                        moyenne_finale = (moy_dev + 2 * examen) / 3
                        
                        # On range le résultat dans le dictionnaire
                        
                        dictionnaire_moyennes[nom_matiere] = round(moyenne_finale, 2)
                        
                    except ValueError:
                        
                        continue # Si une note n'est pas un nombre, on passe

        return dictionnaire_moyennes

    # --- BRIQUE 5 : VALIDATION DATE ---
    
    def date_est_valide(self, date_brute):
        for sep in [" ", "-", ".", ":", "_",",","|"]:
            date_brute = date_brute.replace(sep, "/")
        
        parties = date_brute.split("/")
        if len(parties) != 3: return False
        
        try:
            # Gestion des mois en lettres ---
            mois_dict = {
                "janvier": 1, "fevrier": 2, "mars": 3, "avril": 4, "mai": 5, "juin": 6,
                "juillet": 7, "aout": 8, "septembre": 9, "octobre": 10, "novembre": 11, "decembre": 12
            }
            
            m_saisi = parties[1].lower()
            m = mois_dict[m_saisi] if m_saisi in mois_dict else int(parties[1])
            j = int(parties[0])
            a = int(parties[2])
            
            # Gestion des années à 2 chiffres (ex: 92) ---
            if a < 100:
                a += 1900 if a > 25 else 2000

            # --- LA SUITE DE TON CODE (Vérification mois/année) ---
            if not (1 <= m <= 12 and 1900 <= a <= 2025): return False
            
            jours_max = 31
            if m in [4, 6, 9, 11]: jours_max = 30
            elif m == 2:
                if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
                    jours_max = 29
                else:
                    jours_max = 28
            
            if 1 <= j <= jours_max:
                # Retourne un format unifié 00/00/0000 (plus propre pour l'affichage)
                return f"{j:02d}/{m:02d}/{a}"
                
            return False
            
        except ValueError:
            return False

#----------BRIQUE 6 : DETERMINER L'ÂGE -----------------------------

    def calculer_age(self, date_propre):
        
        # 1. On récupère l'année système actuelle
        
        annee_actuelle = datetime.now().year
        
        # 2. On extrait l'année de naissance de la date propre (ex: "15/04/2008")
        
        segments = date_propre.split("/")
        annee_naissance = int(segments[2]) # Le 3ème élément est l'année
        
        # 3. Calcul
        
        return annee_actuelle - annee_naissance

    
    def charger_fichier(self, chemin):
        
        import csv
        
        try:
            
            with open(chemin, "r", encoding="utf-8") as file:
                    
                    # On utilise DictReader pour avoir les noms de colonnes
                    
                    lecteur = csv.DictReader(file, delimiter=';')
                    
                    for ligne in lecteur:
                    
                    # On récupère les résultats de chaque validation
                        
                        res_date = self.date_est_valide(ligne['Date de naissance'])
                        res_classe = self.classe_est_valide(ligne['Classe'])
                        code_ok = self.code_est_valide(ligne['CODE'])
                        moyennes_dict = self.parser_notes(ligne['Note'])
                        nom_ok = self.identite_est_valide(ligne['Nom'], ligne['Prénom'])
                        
                        # L'AIGUILLAGE FINAL : Tout doit être différent de False
                        
                        if all([res_date, res_classe, code_ok, moyennes_dict, nom_ok]):
                            # Calcul de l'âge avant la naissance de l'objet
                            age_calcule = self.calculer_age(res_date) 
                            
                            nouvel_etudiant = Etudiant(
                                nom=ligne['Nom'],
                                prenom=ligne['Prénom'],
                                code=ligne['CODE'],
                                date_naiss=res_date,
                                classe=res_classe, # On stocke la classe propre (ex: "6A")
                                age=age_calcule
                            )
                            
                            nouvel_etudiant.notes = moyennes_dict
                            
                            self.liste_valides.append(nouvel_etudiant)
                        
                        else:
                                motifs = []
                                
                                # Test du Code
                                if not code_ok: 
                                    motifs.append("CODE (3 MAJ + 3 chiffres)")
                                
                                # Test du Nom et Prénom (Brique identite_est_valide)
                                if not nom_ok:
                                    motifs.append("NOM/PRENOM (Lettres uniquement, Nom >= 2, Prénom >= 3)")
                                
                                # Test de la Date
                                if not res_date: 
                                    motifs.append("DATE (Format JJ/MM/AAAA, 1900-2025)")
                                
                                # Test de la Classe
                                if not res_classe: 
                                    motifs.append("CLASSE (ex: 6A, 3B, 4C, 5D)")
                                
                                # Test des Notes (si le dictionnaire est vide ou False)
                                if not moyennes_dict:
                                    motifs.append("NOTES (Format Matière[note|note:exam] ou notes > 20)")
                                
                                # On enregistre tout dans la ligne
                                ligne['MOTIFS'] = motifs
                                self.liste_invalides.append(ligne)
                            
            print(f"Chargement terminé : {len(self.liste_valides)} valides.")

        except FileNotFoundError:
            
            print("Erreur : Fichier introuvable.")
    

    def detecter_erreurs(self, ligne):
        fautes = []
        if not self.code_est_valide(ligne['CODE']): fautes.append("CODE")
        if not self.identite_est_valide(ligne['Nom'], ligne['Prénom']): fautes.append("IDENTITE")
        if not self.date_est_valide(ligne['Date de naissance']): fautes.append("DATE")
        if not self.classe_est_valide(ligne['Classe']): fautes.append("CLASSE")
        if not self.parser_notes(ligne['Note']): fautes.append("NOTES")
        return fautes

    def traiter_saisie_correction(self, ligne, liste_fautes, choix_index):
        try:
            index = int(choix_index) - 1
            faute_choisie = liste_fautes[index]
            
            if faute_choisie == "CODE":
                print("\n[RÈGLE] 3 Lettres MAJ + 3 Chiffres. Ex: ABC123")
                valeur = input(f"Ancien ({ligne['CODE']}) -> Nouveau : ").upper()
                if self.code_est_valide(valeur): ligne['CODE'] = valeur
                
            elif faute_choisie == "DATE":
                print("\n[RÈGLE] Format JJ/MM/AAAA (Ex: 12/05/2010). Année entre 1900 et 2025.")
                valeur = input(f"Ancien ({ligne['Date de naissance']}) -> Nouveau : ")
                if self.date_est_valide(valeur): ligne['Date de naissance'] = valeur
                
            elif faute_choisie == "IDENTITE":
                print("\n[RÈGLE] Nom (min 2 lettres), Prénom (min 3 lettres). Pas de chiffres.")
                n_nom = input(f"Nom [{ligne['Nom']}] : ") or ligne['Nom']
                n_pre = input(f"Prénom [{ligne['Prénom']}] : ") or ligne['Prénom']
                if self.identite_est_valide(n_nom, n_pre):
                    ligne['Nom'], ligne['Prénom'] = n_nom, n_pre

            elif faute_choisie == "NOTES":
                print("\n[RÈGLE] Format: Matiere[note|note:exam]#... (Notes de 0 à 20)")
                valeur = input("Entrez la chaîne de notes complète : ")
                if self.parser_notes(valeur): ligne['Note'] = valeur

            # Si la validation échoue après la saisie
            else:
                print("❌ Format toujours incorrect. Réessayez.")

        except (ValueError, IndexError):
            print("Choix invalide.")
    
    
    def re_valider_eleve(self, index):
        ligne = self.liste_invalides[index]
        # On refait les tests
        d = self.date_est_valide(ligne['Date de naissance'])
        cl = self.classe_est_valide(ligne['Classe'])
        co = self.code_est_valide(ligne['CODE'])
        no = self.identite_est_valide(ligne['Nom'], ligne['Prénom'])
        m = self.parser_notes(ligne['Note'])

        if all([d, cl, co, no, m]):
            # On crée l'objet final
            nouvel_e = Etudiant(ligne['Nom'], ligne['Prénom'], ligne['CODE'], d, cl, self.calculer_age(d))
            nouvel_e.notes = m
            self.liste_valides.append(nouvel_e)
            self.liste_invalides.pop(index) # On l'enlève des erreurs
            print("L'élève a été transféré vers les valides !")
    
    def corriger_invalide(self, index_invalide):
        if not (0 <= index_invalide < len(self.liste_invalides)): 
            return

        ligne = self.liste_invalides[index_invalide]
        
        while True:
            
            # 1. On recalcule les erreurs actuelles pour voir où on en est
            erreurs = self.detecter_erreurs(ligne) # Une petite méthode qui renvoie la liste des fautes
            
            if not erreurs:
                print("\n✨ Bravo ! Toutes les erreurs sont corrigées.")
                self.re_valider_eleve(index_invalide)
                break

            print(f"\n--- Correction de : {ligne['Nom']} {ligne['Prénom']} ---")
            print("Champs à corriger :")
            for i, err in enumerate(erreurs, 1):
                print(f"{i}. {err}")
            print("Q. Quitter la modification")

            choix = input("\nQuel champ voulez-vous corriger ? ").upper()
            
            if choix == 'Q': break
            
            # 2. Logique de modification selon le choix
            # Si l'utilisateur choisit 1, on regarde quelle est la 1ère erreur de la liste
            # et on lui demande la nouvelle valeur avec le message d'AIDE associé.
            self.traiter_saisie_correction(ligne, erreurs, choix)
    
    def afficher_pagination(self, liste_a_afficher, type_donnees="valide"):
        if not liste_a_afficher:
            print("\nAucune donnée à afficher.")
            return

        taille_page = 5
        total_pages = (len(liste_a_afficher) + taille_page - 1) // taille_page
        page_actuelle = 0

        while True:
            # Calcul du début et de la fin pour la page actuelle
            debut = page_actuelle * taille_page
            fin = debut + taille_page
            donnees_page = liste_a_afficher[debut:fin]

            print(f"\n--- Page {page_actuelle + 1} / {total_pages} ---")
            print(f"{'IDX':<4} | {'NOM':<12} | {'PRENOM':<12} | {'INFOS'}")
            print("-" * 75)

            for i, item in enumerate(donnees_page):
                idx_reel = debut + i
                if type_donnees == "valide":
                    # On récupère la moyenne via la méthode de l'objet
                    moy = item.calculer_moyenne_generale()
                    
                    # On transforme le dictionnaire de notes en texte lisible
                    # Ex: {'Math': 12, 'PC': 15} -> "Math:12, PC:15"
                    txt_notes = ", ".join([f"{m}:{n}" for m, n in item.notes.items()])
                    
                    # On construit la ligne avec TOUTES les infos
                    infos = f"{item.classe} | {item.age}ans | MOY: {moy} | {txt_notes}"
                    print(f"{idx_reel:<4} | {item.nom:<12} | {item.prenom:<12} | {infos}")
                else:
                    # Style Dictionnaire
                    motifs = ", ".join(item.get('MOTIFS', []))
                    print(f"{idx_reel:<4} | {item['Nom']:<12} | {item['Prénom']:<12} | ERR: {motifs}")

            # Menu de navigation
            print(f"\n[S]uivant | [P]récédent | [Q]uitter")
            choix = input("Action : ").upper()

            if choix == "S" and page_actuelle < total_pages - 1:
                page_actuelle += 1
            elif choix == "P" and page_actuelle > 0:
                page_actuelle -= 1
            elif choix == "Q":
                break

    def afficher_joli_json(self, donnees):
        """Affiche une liste (objets ou dictionnaires) au format JSON propre"""
        if not donnees:
            print("Rien à afficher.")
            return

        # 1. On s'assure d'avoir une liste (même si on n'a qu'un seul étudiant)
        if not isinstance(donnees, list):
            items_a_traiter = [donnees]
        else:
            items_a_traiter = donnees

        print(f"\n--- AFFICHAGE DE {len(items_a_traiter)} ÉLÉMENT(S) ---")

        # 2. On boucle pour transformer ET afficher avec le numéro
        for i, item in enumerate(items_a_traiter):
            # Transformation en dictionnaire 
            if hasattr(item, '__dict__'):
                d = item.__dict__.copy()
            else:
                d = item

            # 3. On génère le "rendu_beau" pour cet élément précis
            rendu_beau = json.dumps(d, indent=4, ensure_ascii=False)
            
            # 4. On affiche l'index (pour que l'utilisateur sache quel numéro taper)
            print(f"\n[ ligne : {i} ]") 
            print(rendu_beau)
            print("-" * 20)
    
    def rechercher_etudiant(self, code_cherche):
        # On parcourt la liste des objets valides
        for etudiant in self.liste_valides:
            if etudiant.code == code_cherche:
                print(f"\n✅ Étudiant trouvé !")
                # On utilise ta superbe méthode JSON pour l'affichage détaillé
                self.afficher_joli_json(etudiant)
                return etudiant
        
        print(f"\n❌ Aucun étudiant trouvé avec le code : {code_cherche}")
        return None
    
    def afficher_statistiques(self):
        total = len(self.liste_valides) + len(self.liste_invalides)
        if total == 0:
            print("Aucune donnée chargée.")
            return

        p_valide = (len(self.liste_valides) / total) * 100
        p_invalide = (len(self.liste_invalides) / total) * 100

        print("\n" + "="*35)
        print(f"📊 BILAN DU FICHIER CSV")
        print(f"Total de lignes traitées : {total}")
        print(f"Élèves Valides (Objets)  : {len(self.liste_valides)} ({p_valide:.1f}%)")
        print(f"Lignes Invalides (Dict)  : {len(self.liste_invalides)} ({p_invalide:.1f}%)")
        print("="*35)
    
    def moyenne_de_la_classe(self):
        if not self.liste_valides:
            return 0
        # On appelle la méthode qu'on vient de créer pour chaque objet
        total_moyennes = sum(e.calculer_moyenne_generale() for e in self.liste_valides)
        return round(total_moyennes / len(self.liste_valides), 2)

    def trouver_major(self):
        if not self.liste_valides:
            return None
        # On cherche l'objet qui a la plus grande moyenne générale
        meilleur = max(self.liste_valides, key=lambda e: e.calculer_moyenne_generale())
        return meilleur
    
# --- INITIALISATION ---
gestion = GestionDonnees()
gestion.charger_fichier("Donnees_Projet_Python_Dev_Data.csv")

while True:
    print("\n" + "═"*40)
    print("       SYSTÈME DE GESTION SCOLAIRE")
    print("═"*40)
    print("1. Afficher Valides (Tableau)")
    print("2. Afficher Invalides (JSON)")
    print("3. Rechercher un étudiant (par CODE)")
    print("4. Corriger une ligne invalide")
    print("5. Voir les Statistiques globales")
    print("6. Performance (Moyenne classe & Major)")
    print("Q. Quitter")
    
    choix = input("\n👉 Votre choix : ").upper()

    if choix == "1":
        # Utilise ta méthode de pagination
        gestion.afficher_pagination(gestion.liste_valides, type_donnees="valide")

    elif choix == "2":
        # Utilise ton affichage JSON pour voir les détails des fautes
        gestion.afficher_joli_json(gestion.liste_invalides)

    elif choix == "3":
        code = input("Entrez le CODE de l'étudiant : ").upper()
        gestion.rechercher_etudiant(code)

    elif choix == "4":
        if not gestion.liste_invalides:
            print("Aucune erreur à corriger.")
        else:
            try:
                idx = int(input("Numéro de l'index à corriger : "))
                gestion.corriger_invalide(idx)
            except (ValueError, IndexError):
                print("Index invalide.")

    elif choix == "5":
        gestion.afficher_statistiques()

    elif choix == "6":
        # Ici on utilise tes nouvelles méthodes de calcul
        moy_cl = gestion.moyenne_de_la_classe()
        major = gestion.trouver_major()
        
        print(f"\n📊 MOYENNE DE LA CLASSE : {moy_cl}/20")
        if major:
            print(f"🏆 MAJOR DE PROMO : {major.prenom} {major.nom} ({major.calculer_moyenne_generale()}/20)")

    elif choix == "Q":
        print("Fin du programme. À bientôt !")
        break