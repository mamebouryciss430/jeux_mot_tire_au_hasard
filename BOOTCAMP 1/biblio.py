import random
import time



def choix_niveau(n):
    '''
   Objectifs :Choisir le mot en fonction du niveau
   Methodes :utilisation de condition If/Else
   Besoins:niveau
   Entrees:niveau
   Sorties:le mot a deviner , le nombre de mots charges
   Connus:////
   Resultat:le mot a deviner , le nombre de mots charges
   Hypotheses:n=1 ou n=2 ou n=3

    '''



    if n == 1:
        print("Vous avez choisi le Niveau 1")
        lignes = []  # future liste des lignes
        with open("mots.txt", "r", encoding="utf-8") as f:
            for ligne in f:
                ligne = ligne.rstrip()  # supprime la fin de ligne
                if len(ligne) <= 4:
                    lignes.append(ligne)  # ajoute la ligne à la liste
        return random.choice(lignes), lignes
    else:
        if n == 2:
            print("Vous avez choisi le Niveau 2")
            lignes = []  # future liste des lignes
            with open("mots.txt", "r", encoding="utf-8") as f:
                for ligne in f:
                    ligne = ligne.rstrip()  # supprime la fin de ligne
                    if len(ligne) > 4 and len(ligne) <= 7:
                        lignes.append(ligne)  # ajoute la ligne à la liste
            return random.choice(lignes), lignes
        else:
            if n == 3:
                print("Vous avez choisi le Niveau 3")
                lignes = []  # future liste des lignes
                with open("mots.txt", "r", encoding="utf-8") as f:
                    for ligne in f:
                        ligne = ligne.rstrip()  # supprime la fin de ligne
                        if len(ligne) > 7:
                            lignes.append(ligne)  # ajoute la ligne à la liste
                return random.choice(lignes), lignes
            else:
                print("Les niveaux varient de 1 à 3")

def verif_lettre(pe, t, m, lettres_trouvees):
    '''
      Objectifs : verifier la validite de la lettre saisie
      Methodes  : utilisation de condition While et Boucle If/Else
      Besoins   :le nombre de points d'erreur , le nombre de tentative , le mot a deviner , une liste devant contenir les lettres trouvees
      Entrees   :le nombre de points d'erreur , le nombre de tentative , le mot a deviner , une liste devant contenir les lettres trouvees
      Sorties   :le temps decremente et le score
      Connus    :////
      Resultats :le temps decremente et le score
      Hypotheses: lettres trouvees different du mot a devenir , tentative superieur a 0 , temps inferieur a 5minutes

       '''
    nbre = 0
    partie = 0
    temps = 0
    score=0
    start = time.time()
    while set(lettres_trouvees) != set(m) and t > 0 and temps < start + 300:
        temps = time.time()
        print(f"\nla partie se termine apres 5minutes\ntemps restant:{(((start+300)-temps)/60)} minutes")
        l = str(input("\nSaisir une lettre: "))
        l=l.lower()
        liste = [chr(i) for i in range(ord('a'), ord('z') + 1)]

        if l not in liste:
            print("Vous devrez saisir que des lettres de l'alphabet")
            if pe != 0:
                pe -= 1
                print("Il vous reste " + str(pe) + " points erreurs")
            else:
                if t != 0:
                    t -= 1
                    print("Il vous reste " + str(t) + " tentatives")
                else:
                    if t <= 0:
                        print("Vous avez perdu")
        else:
            mot_masque = ""
            if l in m:
                lettres_trouvees += l
                for trouve in m:
                    if trouve in lettres_trouvees:
                        mot_masque =mot_masque+ trouve

                    else:
                        mot_masque += "_"
                print(mot_masque)
                print("Bravo, lettre correcte")
                t += 1
                if mot_masque == m:
                    score = t * len(lettres_trouvees)
                    print(f"nombre de tentative restant:{t}\n")
                    print(f"felicitations: Vous avez devine le mot.\nVotre score est : {score} ")


            else:
                voyelle = ['a', 'e', 'i', 'o', 'u', 'y']
                if l in voyelle:
                    t -= 2
                    print(
                        "Vous avez saisie une voyelle qui n'est pas dans le mot\nvous perdez deux tentatives\n#####################################\nIl vous reste " + str(
                            t) + " tentatives")
                    if t >= 6:
                        print(" +---+\n |    |\n      |\n      |\n      |\n      |\n==========\n")
                    if t == 5:
                        print(" +---+\n |    |\n O    |\n      |\n      |\n      |\n==========\n")
                    if t == 4:
                        print(" +---+\n |    |\n O    |\n/     |\n      |\n      |\n==========\n")
                    if t == 3:
                        print(" +---+\n |    |\n O    |\n/|    |\n      |\n      |\n==========\n")
                    if t == 2:
                        print(" +---+\n |    |\n O    |\n/|\   |\n      |\n      |\n==========\n")
                    if t == 1:
                        print(" +---+\n |    |\n O    |\n/|\   |\n/     |\n      |\n==========\n")
                    if t <= 0:
                        print(" +---+\n |    |\n O    |\n/|\   |\n/ \   |\n      |\n==========\n")

                else:
                    t -= 1
                    print(
                        "Vous avez saisie une consonne qui n'est pas dans le mot\nvous perdez une tentative\n#####################################\nIl vous reste " + str(
                            t) + " tentatives")
                    if t >= 6:
                        print(" +---+\n |    |\n      |\n      |\n      |\n      |\n==========\n")
                    if t == 5:
                        print(" +---+\n |    |\n O    |\n      |\n      |\n      |\n==========\n")
                    if t == 4:
                        print(" +---+\n |    |\n O    |\n/     |\n      |\n      |\n==========\n")
                    if t == 3:
                        print(" +---+\n |    |\n O    |\n/|    |\n      |\n      |\n==========\n")
                    if t ==2:
                        print(" +---+\n |    |\n O    |\n/|\   |\n      |\n      |\n==========\n")
                    if t == 1:
                        print(" +---+\n |    |\n O    |\n/|\   |\n/     |\n      |\n==========\n")
                    if t <= 0:
                        print(" +---+\n |    |\n O    |\n/|\   |\n/ \   |\n      |\n==========\n")
        nbre += 1
        temps = time.time()
    if temps > start + 300:
        print(f"temps ecoule (Vous avez fait plus de 5 minutes) !\nLe mot a deviner etait: {m}Votre score :{score}")

    return t,score
def affichage(m, lignes):
    '''
      Objectifs :Afficher le nombre de mots charges ,Afficher la longueur du mot a deviner
      Methodes :boucle for
      Besoins:le mot a deviner ,
      Entrees:m (le mot a deviner ) , lignes (nombre de mots charges)
      Sorties:///
      Connus:///
      Resultats:///
      Hypotheses:///

       '''
    print("Chargement des données ...\n" + str(len(lignes)) + " mots chargés\nJe vous propose un mot de " + str(
        len(m)) + " lettres. De quel mot s'agit-il?")
    print("################################")
    for lettre in m:
        lettre = lettre.rstrip()
        print("_", end="")