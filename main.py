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



#from board import position
#from piece import*
#from new_interface import fonction_lecture

#print(fonction_lecture(position))

#def demander_utilisateur():
    #lettres = "a,b,c,d,e,f,g,h"
    #chiffres = "1,2,3,4,5,6,7,8"
    #P1 = input("ou aller?")
    #while len(P1)!=2 or (P1[0] not in lettres) or (P1[1] not in chiffres):
        #print("Syntaxe incorrecte.")
        #P1 = input("ou aller?")
    #P2 = input("piece à bouger?")
    #while len(P2)!=2 or (P2[0] not in lettres) or (P2[1] not in chiffres):
        #print("Syntaxe incorrecte.")
        #P2 = input("piece à bouger?")
    #return P1,P2

#P1,P2 = demander_utilisateur()
#interpreteur(P1,P2,couleurA)

#if interpreteur(P1,P2,couleurA) == False:
    #print("Faux")
    #coup, piece_a_bouger = demander_utilisateur()

#for i in fonction_lecture(position):
    #print(i)