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
position=[[TB1,CB1,FB1,QB1,KB1,FB2,CB2,TB2],[PB1,PB2,PB3,PB4,PB5,PB6,PB7,PB8],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[PN1,PN2,PN3,PN4,PN5,PN6,PN7,PN8],[TN1,CN1,FN1,QN1,KN1,FN2,CN2,TN2]]
prises=[] #pièces prises

def mouvement(piece,case): #case = liste des 2 coordonées de la case : [colonne,ligne]
  if piece._couleur==CouleurQuiJoue: #cf interface
    a=type(piece)
    ligne=case[1]
    colonne=case[0]
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
    
  
