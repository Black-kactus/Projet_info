def interpreteur(coup,piece_a_bouger,couleurA):
    from board import mouvement,position
    #global position
    position_ou_aller=coup.get()
    piece_bougee=piece_a_bouger.get()
    colonne_P=ord(position_ou_aller[0])-97 #position de la case d'arrivée
    ligne_P=int(position_ou_aller[1])-1 #position de la case d'arrivée
    colonne_A=ord(piece_bougee[0])-97 #position de la piece à bouger
    ligne_A=int(piece_bougee[1])-1 #position de la pièce à bouger
    if mouvement(position[colonne_A][ligne_A],[colonne_P,ligne_P],couleurA)[0]==False: #case = liste des 2 coordonées de la case : [colonne,ligne]
        return (False,mouvement(position[colonne_A][ligne_A],[colonne_P,ligne_P],couleurA)[1])
    return (True,0)