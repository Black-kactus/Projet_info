from piece import Cavalier, Dame, Fou, Pion, Roi, Tour


#attribut: quel camp joue/droit au roque

#échiquier=[a[1,2,3,4,5,6,7,8],b[1,2,3,4,5,6,7,8],c[1,2,3,4,5,6,7,8],d[1,2,3,4,5,6,7,8],e[1,2,3,4,5,6,7,8],f[1,2,3,4,5,6,7,8],g[1,2,3,4,5,6,7,8],h[1,2,3,4,5,6,7,8]]
#echiquier en liste de listes L[0][5] pour dire qu'on ait en A6 par exemple

#initialisation du plateau et des pièces:
#T,C,F,Q,K,P = tour, cavalier, fou, reine(queen), roi(king), pion
#N,B = noir, blanc
TB1=Tour("Blanc",0,0,1)
TB2=Tour("Blanc",7,0,2)
CB1=Cavalier("Blanc",1,0,1)
CB2=Cavalier("Blanc",6,0,2)
FB1=Fou("Blanc",2,0,1)
FB2=Fou("Blanc",5,0,2)
QB1=Dame("Blanc",3,0,1)
KB1=Roi("Blanc",4,0,1)
PB1=Pion("Blanc",0,1,1)
PB2=Pion("Blanc",1,1,2)
PB3=Pion("Blanc",2,1,3)
PB4=Pion("Blanc",3,1,4)
PB5=Pion("Blanc",4,1,5)
PB6=Pion("Blanc",5,1,6)
PB7=Pion("Blanc",6,1,7)
PB8=Pion("Blanc",7,1,8)

TN1=Tour("Noir",0,7,1)
TN2=Tour("Noir",7,7,2)
CN1=Cavalier("Noir",1,7,1)
CN2=Cavalier("Noir",6,7,2)
FN1=Fou("Noir",2,7,1)
FN2=Fou("Noir",5,7,2)
QN1=Dame("Noir",3,7,1)
KN1=Roi("Noir",4,7,1)
PN1=Pion("Noir",0,6,1)
PN2=Pion("Noir",1,6,2)
PN3=Pion("Noir",2,6,3)
PN4=Pion("Noir",3,6,4)
PN5=Pion("Noir",4,6,5)
PN6=Pion("Noir",5,6,6)
PN7=Pion("Noir",6,6,7)
PN8=Pion("Noir",7,6,8)

position=[[TB1,PB1,0,0,0,0,PN1,TN1],[CB1,PB2,0,0,0,0,PN2,CN1],[FB1,PB3,0,0,0,0,PN3,FN1],[QB1,PB4,0,0,0,0,PN4,QN1],[KB1,PB5,0,0,0,0,PN5,KN1],[FB2,PB6,0,0,0,0,PN6,FN2],[CB2,PB7,0,0,0,0,PN7,CN2],[TB2,PB8,0,0,0,0,PN8,TN2]]
prises_Noir=[] #pièces prises par les noirs
prises_Blanc=[] #pièces prises par les blancs



def mouvement(piece,case): #case = liste des 2 coordonées de la case : [colonne,ligne]
  if piece==0:
    print("Vous n'avez pas de pièce à cet endroit.")
  else :
    global position
    from new_interface import couleurA
    CouleurQuiJoue=couleurA.get()
    if piece._couleur==CouleurQuiJoue:
      a=type(piece)
      ligne=case[1]
      colonne=case[0]
      if ligne==piece.ligne and colonne==piece.colonne:
        print("Votre pièce est déjà à cette position.")
      else:
        if piece.mouvement_possible(colonne,ligne):
          if CouleurQuiJoue == "Blanc" and KB1.Echec2():
            print("Vous ne pouvez pas bouger votre pièce à cet endroit sans mettre votre roi en échec.")
          elif CouleurQuiJoue=="Noir" and KN1.Echec2():
            print("Vous ne pouvez pas bouger votre pièce à cet endroit sans mettre votre roi en échec.")
          elif a!=Pion:
            if position[colonne][ligne]!=0: #s'il y a déjà une pièce sur la case
              if position[colonne][ligne]._couleur!=CouleurQuiJoue: #si la pièce est de la couleur opposée, on la mange
                if CouleurQuiJoue=='Blanc':
                  prises_Blanc.append(position[colonne][ligne]) #on met à jour la liste des prises
                  position[colonne][ligne].colonne=-1 #on change les coordonées de la pièce mangée
                  position[colonne][ligne].ligne=-1
                else:
                  prises_Noir.append(position[colonne][ligne])
                  position[colonne][ligne].colonne=-2 #on change les coordonées de la pièce mangée
                  position[colonne][ligne].ligne=-2
                position[piece.colonne][piece.ligne]=0 #on enlève la pièce de son ancienne case
                piece.ligne=ligne #on met à jour les coordonnées de la pièce
                piece.colonne=colonne
                position[colonne][ligne]=piece #on met à jour la liste position
                
              else:
                print("Il y a déjà une de vos pièces sur cette case.")
            else: #s'il n'y a pas d'autre pièce sur la case
                position[piece.colonne][piece.ligne]=0 #on enlève la pièce de son ancienne case
                piece.ligne=ligne #on met à jour les coordonnées de la pièce
                piece.colonne=colonne
                position[colonne][ligne]=piece #on met à jour la liste position 
          
          else: #cas spécial du pion
            if CouleurQuiJoue=="Blanc": #si les blancs jouent
              if ligne==piece.ligne+1 and colonne==piece.colonne:
                if position[colonne][ligne]!=0: #s'il y a déjà une pièce sur la case
                  print("Cette case est déjà occupée.")
                else:
                  position[piece.colonne][piece.ligne]=0 #on enlève la pièce de son ancienne case
                  piece.ligne=ligne #on met à jour les coordonnées de la pièce
                  piece.colonne=colonne
                  position[colonne][ligne]=piece #on met à jour la liste position
              elif ligne==piece.ligne+2 and colonne==piece.colonne:
                if position[colonne][ligne]!=0: #s'il y a déjà une pièce sur la case
                  print("Cette case est déjà occupée.")
                elif not(piece.Move1): #ne peut plus déplacer de 2
                  print("Vous ne pouvez plus jouer ce coup")
                else:
                  position[piece.colonne][piece.ligne]=0 #on enlève la pièce de son ancienne case
                  piece.ligne=ligne #on met à jour les coordonnées de la pièce
                  piece.colonne=colonne
                  position[colonne][ligne]=piece #on met à jour la liste position
              else:
                if position[colonne][ligne]._couleur!=CouleurQuiJoue: #si la pièce est de la couleur opposée, on la mange
                  if CouleurQuiJoue=='Blanc':
                    prises_Blanc.append(position[colonne][ligne]) #on met à jour la liste des prises
                    position[colonne][ligne].colonne=-1 #on change les coordonées de la pièce mangée
                    position[colonne][ligne].ligne=-1
                  else:
                    prises_Noir.append(position[colonne][ligne])
                    position[colonne][ligne].colonne=-2 #on change les coordonées de la pièce mangée
                    position[colonne][ligne].ligne=-2
                if position[colonne][ligne]==0: #s'il n'y a pas de pièce sur la case
                  print("Vous ne pouvez déplacer votre pion en diagonale que pour manger une pièce.")
                else:
                  if position[colonne][ligne]._couleur!=CouleurQuiJoue: #si la pièce est de la couleur opposée, on la mange
                    if CouleurQuiJoue=='Blanc':
                      prises_Blanc.append(position[colonne][ligne]) #on met à jour la liste des prises
                      position[colonne][ligne].colonne=-1 #on change les coordonées de la pièce mangée
                      position[colonne][ligne].ligne=-1
                    else:
                      prises_Noir.append(position[colonne][ligne])
                      position[colonne][ligne].colonne=-2 #on change les coordonées de la pièce mangée
                      position[colonne][ligne].ligne=-2
                    position[piece.colonne][piece.ligne]=0 #on enlève la pièce de son ancienne case
                    piece.ligne=ligne #on met à jour les coordonnées de la pièce
                    piece.colonne=colonne
                    position[colonne][ligne]=piece #on met à jour la liste position
                  else:
                    print("Il y a déjà une de vos pièces sur cette case.")
            else: #si les noirs jouent
              if ligne==piece.ligne-1 and colonne==piece.colonne:
                if position[colonne][ligne]!=0: #s'il y a déjà une pièce sur la case
                  print("Cette case est déjà occupée.")
                else:
                  position[piece.colonne][piece.ligne]=0 #on enlève la pièce de son ancienne case
                  piece.ligne=ligne #on met à jour les coordonnées de la pièce
                  piece.colonne=colonne
                  position[colonne][ligne]=piece #on met à jour la liste position
              else:
                if position[colonne][ligne]==0: #s'il n'y a pas de pièce sur la case
                  print("Vous ne pouvez déplacer votre pion en diagonale que pour manger une pièce.")
                else:
                  if position[colonne][ligne]._couleur!=CouleurQuiJoue: #si la pièce est de la couleur opposée, on la mange
                    if CouleurQuiJoue=='Blanc':
                      prises_Blanc.append(position[colonne][ligne]) #on met à jour la liste des prises
                      position[colonne][ligne].colonne=-1 #on change les coordonées de la pièce mangée
                      position[colonne][ligne].ligne=-1
                    else:
                      prises_Noir.append(position[colonne][ligne])
                      position[colonne][ligne].colonne=-2 #on change les coordonées de la pièce mangée
                      position[colonne][ligne].ligne=-2
                    position[piece.colonne][piece.ligne]=0 #on enlève la pièce de son ancienne case
                    piece.ligne=ligne #on met à jour les coordonnées de la pièce
                    piece.colonne=colonne
                    position[colonne][ligne]=piece #on met à jour la liste position
                  else:
                    print("Il y a déjà une de vos pièces sur cette case.")
        else:
          print("Vous ne pouvez pas déplacer la pièce à cet endroit là.")
    else:
      print("Vous ne pouvez pas déplacer une pièce de l'adversaire.")
    