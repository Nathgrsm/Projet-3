plateau = [" " for _ in range(9)]

def afficherPlateau(p, gagnant=None):
     print(" " + p[0] + " | " + p[1] + " | " + p[2] + " ")
     print("---+---+---")
     print(" " + p[3] + " | " + p[4] + " | " + p[5] + " ")
     print("---+---+---")
     print(" " + p[6] + " | " + p[7] + " | " + p[8] + " ")
     if gagnant:
         print("""* Terminé ! Le joueur {0} a gagné la partie. *""".format(gagnant))

def morpion():
        joueur = "X"
        tour = 0
        while True:
         afficherPlateau(plateau)
         print("Tour du joueur " + joueur + ". Entrez un nombre de 1 à 9.")
         move = int(input()) - 1
         if plateau[move] == " ":
            plateau[move] = joueur
            tour += 1
         else:
            print("Cette case est déjà occupée, choisissez-en une autre.")
            continue
        
         if plateau[0] == plateau[1] == plateau[2] != " " \
         or plateau[3] == plateau[4] == plateau[5] != " " \
         or plateau[6] == plateau[7] == plateau[8] != " " \
         or plateau[0] == plateau[3] == plateau[6] != " " \
         or plateau[1] == plateau[4] == plateau[7] != " " \
         or plateau[2] == plateau[5] == plateau[8] != " " \
         or plateau[0] == plateau[4] == plateau[8] != " " \
         or plateau[2] == plateau[4] == plateau[6] != " ":
             afficherPlateau(plateau, joueur)
             break
               
         if tour == 9:
             print("Personne n'a gagné !")
             break
               
         joueur = "O" if joueur == "X" else "X"
           

if __name__ == "__main__":
    morpion()
