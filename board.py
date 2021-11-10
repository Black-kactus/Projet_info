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

def mouvement(piece,case):
  if piece._couleur==CouleurQuiJoue: #cf interface
    if type(piece).mouvementpossible==True:
      on bouge la pièce
    else:
      print("Ce mouvement n'est pas autorisé pour ce type de pièce.")
  else:
    print("Vous ne pouvez pas déplacer une pièce de l'adversaire.")
    
  
