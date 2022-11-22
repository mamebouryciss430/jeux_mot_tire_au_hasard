import random
import time
import biblio
from datetime import datetime

if __name__ == '__main__':
    '''
    les Membres du projet : Fatima Binta Traore et Mame Boury Cisse 
    Nous avons effectue tout le travail ensemble allant de l'etude de couplage , de l'implementation des fonctions et des tests 
    '''
    print("Partie 1\n Bienvenue dans le jeu LET-GET\n#####################################\n Vous avez 3 point-erreur\n#####################################\nVous avez 6 tentatives\n##########################################")
    print("+---+\n | |\n   |\n   |\n   |\n   |\n==========\n")
    rejouer=1
    nombre_partie = 0
    lesScores=[]
    while rejouer==1 :

        t = 6
        pe = 3
        partie = 0
        score = 0
        nombre_partie +=1
        while t != 0 and partie == 0:
            n = int(input("Choisir un niveau de 1 a 3 :"))

            m, lignes = biblio.choix_niveau(n)
            m=m.lower()


            if n == 1 or n == 2 or n == 3:
                lettres_trouvees = []
                biblio.affichage(m, lignes)
                t,score = biblio.verif_lettre(pe, t, m, lettres_trouvees)
                lesScores.append(score)
                if t <= 0:
                    t == 0
                    print("Vous avez perdu.\nLe mot était :" + m)

            partie = 1  # pour montrer que le mot a ete trouve

        print(f"la partie { nombre_partie} est finie pour vous ")
        file = open("log_game.txt", "w")
        file.write(
            f"Numero partie: {nombre_partie}\nNombre de tentatives: {t}\nScore Obtenu: {score}\nPlus grand Score: {max(lesScores)}")
        file.close()
        rejouer = int(input("1-Pour rejouer une autre partie\n2-Pour quitter\n"))

    print("vous venez de quitter le jeu !\nA la prochaine")


