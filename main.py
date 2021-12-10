#from test import coup, piece_a_bouger


def interpreteur(coup,piece_a_bouger):
    from board import mouvement,position
    #global position
    coup=coup.get()
    piece_a_bouger=piece_a_bouger.get()
    colonne_P=ord(coup[0])-97 #position de la pièce à bouger
    ligne_P=int(coup[1])-1 #position de la pièce à bouger
    colonne_A=ord(piece_a_bouger[0])-97 #position de la case d'arrivée
    ligne_A=int(piece_a_bouger[1])-1 #position de la case d'arrivée
    mouvement(position[colonne_P][ligne_P],[colonne_A,ligne_A]) #case = liste des 2 coordonées de la case : [colonne,ligne]

#from board import position
#from piece import*
#from test import fonction_lecture

#print(fonction_lecture(position))

#P1 = input("coup?")
#P2 = input("piece à bouger?")

#interpreteur(P1,P2)

#for i in fonction_lecture(position):
#    print(i)

