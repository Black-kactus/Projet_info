def interpreteur(coup,piece_a_bouger,couleurA,coup_special):
    from board import mouvement,position
    position_ou_aller=coup.get()
    piece_bougee=piece_a_bouger.get()
    print(coup_special)
    if coup_special != "roque" and coup_special != "ROQUE":
        colonne_P=ord(position_ou_aller[0])-97 #position de la case d'arrivée
        ligne_P=int(position_ou_aller[1])-1 #position de la case d'arrivée
        colonne_A=ord(piece_bougee[0])-97 #position de la piece à bouger
        ligne_A=int(piece_bougee[1])-1 #position de la pièce à bouger
    else:
        colonne_P=1 #position de la case d'arrivée
        ligne_P=1 #position de la case d'arrivée
        colonne_A=1 #position de la piece à bouger
        ligne_A=1 #position de la pièce à bouger
    if mouvement(position[colonne_A][ligne_A],[colonne_P,ligne_P],couleurA,coup_special)[0]==False: #case = liste des 2 coordonées de la case : [colonne,ligne]
        return (False,mouvement(position[colonne_A][ligne_A],[colonne_P,ligne_P],couleurA,coup_special)[1])
    return (True,0)



def interpreteur_script(script):
    import time
    from new_interface import coup_special,coup,piece_a_bouger
    from new_interface import LPOSITION, fonction_lecture, couleurA,nbcoup,message_erreur,afficherPiece
    #from new_interface import cmd_bouton_valider
    script = script.split(' ')
    #L=[]
    #for i in range(0,len(script),2):
        #L.append([script[i].split("-"),script[i+1].split("-")])
    for i in range(len(script)):
        time.sleep(4)
        coup_script=script[i].split("-")
        #L.append(script[i].split("-"))
        if len(coup_script)==1:
            coup_special.set(coup_script)
        elif len(coup_script)==2:
            piece_a_bouger.set(coup_script[0])
            coup.set(coup_script[1])
        #cmd_bouton_valider()
    
        from board import position #
        if not(interpreteur(coup,piece_a_bouger,couleurA,coup_special.get())[0]==False): #
            global LPOSITION #
            LPOSITION=fonction_lecture(position) #
        
            nbcoup.set(str(int(nbcoup.get())+1))
            coup.set("")
            piece_a_bouger.set("")
            message_erreur.set("")
            coup_special.set("")

            if couleurA.get() == "Blanc": 
                couleurA.set("Noir")
            else:
                couleurA.set("Blanc")
            afficherPiece()
        else:
            message_erreur.set(interpreteur(coup,piece_a_bouger,couleurA,coup_special.get())[1])
interpreteur_script("e2-e4 c7-c5 c2-c3 d7-d5 e4-d5 d8-d5 d2-d4 g8-f6 g1-f3 c8-g4 f1-e2 e7-e6 h2-h3 g4-h5 roque b8-c6 c1-e3 c5-d4 c3-d4 f8-b4")





    
    



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