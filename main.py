# Fonction qui transforme les entrées de l'utilisateur en données lisibles par la fonction mouvement

def interpreteur(coup, piece_a_bouger, couleurA, coup_special, nbcoup):

    from board import mouvement,position
    position_ou_aller = coup.get()
    piece_bougee = piece_a_bouger.get()

    if coup_special != "roque" and coup_special != "ROQUE":
        colonne_arrivee = ord(position_ou_aller[0])-97  # position de la case d'arrivée
        ligne_arrivee = int(position_ou_aller[1])-1  # position de la case d'arrivée
        colonne_depart = ord(piece_bougee[0])-97  # position de la piece à bouger
        ligne_depart = int(piece_bougee[1])-1  # position de la pièce à bouger

    else:
        colonne_arrivee = 1  # position de la case d'arrivée
        ligne_arrivee = 1  # position de la case d'arrivée
        colonne_depart = 1  # position de la piece à bouger
        ligne_depart = 1  # position de la pièce à bouger
        
    move = mouvement(position[colonne_depart][ligne_depart], [colonne_arrivee,ligne_arrivee], couleurA, coup_special, nbcoup)
    return (move[0], move[1], position[colonne_arrivee][ligne_arrivee])
    #renvoie (le mouvement est-il possible?, message d'erreur éventuel, pièce qu'on vient de bouger)