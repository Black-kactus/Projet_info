def interpreteur(coup, piece_a_bouger, couleurA, coup_special, nbcoup):

    from board import mouvement,position
    position_ou_aller = coup.get()
    piece_bougee = piece_a_bouger.get()

    if coup_special != "roque" and coup_special != "ROQUE":
        colonne_P = ord(position_ou_aller[0])-97  # position de la case d'arrivée
        ligne_P = int(position_ou_aller[1])-1  # position de la case d'arrivée
        colonne_A = ord(piece_bougee[0])-97  # position de la piece à bouger
        ligne_A = int(piece_bougee[1])-1  # position de la pièce à bouger

    else:
        colonne_P = 1  # position de la case d'arrivée
        ligne_P = 1  # position de la case d'arrivée
        colonne_A = 1  # position de la piece à bouger
        ligne_A = 1  # position de la pièce à bouger
        
    move = mouvement(position[colonne_A][ligne_A], [colonne_P,ligne_P], couleurA, coup_special, nbcoup)
    return (move[0], move[1], position[colonne_P][ligne_P])


# def fonction_attente():
#     # global attente
#     # attente=True
#     return True