from test import coup,deplacement
from board import mouvement,position

def interpreteur(coup,deplacement):
    global position
    coup=coup.get()
    deplacement=deplacement.get()
    colonne_P=ord(coup[0])-97 #position de la pièce à bouger
    ligne_P=coup[1]-1 #position de la pièce à bouger
    colonne_A=ord(deplacement[0])-97 #position de la case d'arrivée
    ligne_A=deplacement[1]-1 #position de la case d'arrivée
    mouvement(position[colonne_P][ligne_P],[colonne_A,ligne_A]) #case = liste des 2 coordonées de la case : [colonne,ligne]
