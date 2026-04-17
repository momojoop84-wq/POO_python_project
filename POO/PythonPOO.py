"""
ÉTAPE 1 — Classe simple
Créer une classe : Etudiant
Attributs :
• nom
• prenom
• age
Méthodes :
• afficher_info()
Résultat attendu
Créer 2 ou 3 étudiants et afficher leurs infos
#-------------------------------------------------------------------------------------------------------------------------
ÉTAPE 2 — Ajouter la logique métier
Ajouter :
Attribut :
• notes (liste)
Méthodes :
• ajouter_note()
• calculer_moyenne()
Résultat attendu
Chaque étudiant peut :
• avoir plusieurs notes
• calculer sa moyenne
"""
class Etudiant:
    def __init__(self, nom, prenom, age):
        # Attributs de base (Étape 1)
        self.nom = nom
        self.prenom = prenom
        self.age = age
        # Attribut pour la logique métier (Étape 2)
        self.notes = []

    def afficher_info(self):
        print(f"Étudiant: {self.prenom} {self.nom}, Age: {self.age} ans")

    def ajouter_note(self, note):
        if 0 <= note <= 20:
            self.notes.append(note)
        else:
            print("Note invalide ! Elle doit être entre 0 et 20.")

    def calculer_moyenne(self):
        if not self.notes:
            return 0
        return sum(self.notes) / len(self.notes)

# Création des objets (Instances)
e1 = Etudiant("Sarr", "Modou", 20)
e2 = Etudiant("Diop", "Aminata", 19)

# Utilisation des méthodes
e1.ajouter_note(15)
e1.ajouter_note(12)
e2.ajouter_note(18)

e1.afficher_info()
print(f"Moyenne de {e1.prenom} : {e1.calculer_moyenne():.2f}")

"""
ÉTAPE 3 — Classe de gestion
Créer une classe :
GestionEtudiants
Attribut :
• liste_etudiants
Méthodes :
• ajouter_etudiant()
• afficher_etudiants()
• meilleur_etudiant()
• moyenne_classe()
Résultat attendu
Gérer plusieurs étudiants
"""
class GestionEtudiants:
    def __init__(self):
        # L'attribut est une liste qui contiendra nos objets "Etudiant"
        self.liste_etudiants = []

    def ajouter_etudiant(self, etudiant):
        self.liste_etudiants.append(etudiant)

    def afficher_etudiants(self):
        print("\n--- LISTE DES ÉTUDIANTS ---")
        for e in self.liste_etudiants:
            # On appelle la méthode de l'objet Etudiant lui-même !
            moyenne = e.calculer_moyenne()
            print(f"{e.prenom} {e.nom} | Moyenne: {moyenne:.2f}")

    def meilleur_etudiant(self):
        if not self.liste_etudiants:
            return None
        # On cherche l'étudiant qui a la plus grande moyenne
        return max(self.liste_etudiants, key=lambda e: e.calculer_moyenne())

    def moyenne_classe(self):
        if not self.liste_etudiants:
            return 0
        total_moyennes = sum(e.calculer_moyenne() for e in self.liste_etudiants)
        return total_moyennes / len(self.liste_etudiants)

"""
ÉTAPE 4 — Menu (programme complet)
À faire
Menu :
1. Ajouter étudiant
2. Ajouter note
3. Afficher étudiants
4. Afficher moyenne classe
5. Meilleur étudiant
Résultat attendu
Programme interactif
"""
gestion = GestionEtudiants()

while True:
    print("\n1. Ajouter étudiant | 2. Ajouter note | 3. Afficher | 4. Moyenne Classe | 5. Meilleur | 6. Quitter")
    choix = input("Votre choix : ")

    if choix == "1":
        nom = input("Nom : ")
        prenom = input("Prénom : ")
        age = input("Age : ")
        nouvel_e = Etudiant(nom, prenom, age)
        gestion.ajouter_etudiant(nouvel_e)

    elif choix == "2":
        if not gestion.liste_etudiants:
            print("Erreur : Aucun étudiant dans la base.")
        else:
            print("\n--- CHOISIR UN ÉTUDIANT ---")
            # enumerate crée les numéros (i) automatiquement
            for i, etudiant in enumerate(gestion.liste_etudiants):
                print(f"{i}. {etudiant.prenom} {etudiant.nom}")

            try:
                index = int(input("\nEntrez le numéro de l'étudiant : "))
                
                # On vérifie que le numéro existe dans la liste
                if 0 <= index < len(gestion.liste_etudiants):
                    note = float(input(f"Note pour {gestion.liste_etudiants[index].prenom} : "))
                    # On appelle la méthode de l'objet choisi
                    gestion.liste_etudiants[index].ajouter_note(note)
                    print("Note ajoutée avec succès !")
                else:
                    print("Ce numéro n'existe pas.")
            except ValueError:
                print("Veuillez entrer un chiffre valide.")


    elif choix == "3":
        gestion.afficher_etudiants()

    elif choix == "4":
        print(f"Moyenne de la classe : {gestion.moyenne_classe():.2f}")

    elif choix == "5":
        top = gestion.meilleur_etudiant()
        if top:
            print(f"Le meilleur est {top.prenom} {top.nom}")

    elif choix == "6":
        break


"""
ÉTAPE 7 — BONUS
Vous revenez à votre projet initial :
• validation complète
• parsing des notes
"""