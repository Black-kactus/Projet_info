from piece import cavalier, dame, fou, pion, roi, tour

#echiquier

#cooordonées de chaques cases
#possibilité d'avoir une seule case
#règles du jeu d'échec
#savoir si une pièces est attaquée

#attribut: quel camp joue/droit au roque


L=[[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8]]
#echiquier en liste de listes L[0][5] pour dire qu'on ait en A6 par exemple


#initialisation du plateau:
#T,C,F,Q,K,P = tour, cavalier, fou, reine(queen), roi(king), pion
#N,B = noir, blanc
TB1=tour("Blanc",0,0,1)
TB2=tour("Blanc",7,0,2)
CB1=cavalier("Blanc",1,0,1)
CB2=cavalier("Blanc",6,0,2)
FB1=fou("Blanc",2,0,1)
FB2=fou("Blanc",5,0,2)
QB1=dame("Blanc",3,0,1)
KB1=roi("Blanc",4,0,1)
PB1=pion("Blanc",0,1,1)
PB2=pion("Blanc",1,1,2)
PB3=pion("Blanc",2,1,3)
PB4=pion("Blanc",3,1,4)
PB5=pion("Blanc",4,1,5)
PB6=pion("Blanc",5,1,6)
PB7=pion("Blanc",6,1,7)
PB8=pion("Blanc",7,1,8)

TN1=tour("Noir",0,7,1)
TN2=tour("Noir",7,7,2)
CN1=cavalier("Noir",1,7,1)
CN2=cavalier("Noir",6,7,2)
FN1=fou("Noir",2,7,1)
FN2=fou("Noir",5,7,2)
QN1=dame("Noir",3,7,1)
KN1=roi("Noir",4,7,1)
PN1=pion("Noir",0,6,1)
PN2=pion("Noir",1,6,2)
PN3=pion("Noir",2,6,3)
PN4=pion("Noir",3,6,4)
PN5=pion("Noir",4,6,5)
PN6=pion("Noir",5,6,6)
PN7=pion("Noir",6,6,7)
PN8=pion("Noir",7,6,8)

#position = [a[1,2,...,8], b[1,...,8],...,h[1,...,8]]
position=[[TB1,PB1,0,0,0,0,PN1,TN1],[CB1,PB2,0,0,0,0,PN2,CN1],[FB1,PB3,0,0,0,0,PN3,FN1],[QB1,PB4,0,0,0,0,PN4,QN1],[KB1,PB5,0,0,0,0,PN5,KN1],[FB2,PB6,0,0,0,0,PN6,FN2],[CB2,PB7,0,0,0,0,PN7,CN2],[TB2,PB8,0,0,0,0,PN8,TN2]]
prises=[] #pièces prises

def mouvement(piece,case): #case = liste des 2 coordonées de la case : [colonne,ligne]
  if piece._couleur==CouleurQuiJoue: #cf interface
    a=type(piece)
    ligne=case[1]
    colonne=case[0]
    if ligne==piece.ligne and colonne==piece.colonne:
      print("Votre pièce est déjà à cette position.")
    else:
      if a.mouvementpossible(piece,case)==True:
        if position[colonne][ligne]!=0: #s'il y a déjà une pièce sur la case
          if position[colonne][ligne]._couleur!=CouleurQuiJoue: #si la pièce est de la couleur opposée, on la mange
            prise.append(position[colonne][ligne])
            piece.ligne=ligne
            piece.colonne=colonne
            position[colonne][ligne]=piece
          else:
            print("Il y a déjà une de vos pièces sur cette case.")
        else: #s'il n'y a pas d'autre pièce sur la case
            piece.ligne=ligne
            piece.colonne=colonne
            position[colonne][ligne]=piece
      else:
        print("Vous ne pouvez pas déplacer la pièce à cet endroit là.")
  else:
    print("Vous ne pouvez pas déplacer une pièce de l'adversaire.")
    

