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





def update_coord_piece(piece,ligne,colonne): # on met à jour les coordonnées de la pièce
  piece.ligne = ligne
  piece.colonne = colonne

def eaten_Noir(colonne,ligne):
  prises_Noir.append(position[colonne][ligne]) #on ajoute la pièce à la liste des pièces mangées
  position[colonne][ligne].colonne = -2  # on change les coordonées de la pièce mangée
  position[colonne][ligne].ligne = -2

def eaten_Blanc(colonne,ligne):
  prises_Blanc.append(position[colonne][ligne])  #on ajoute la pièce à la liste des pièces mangées
  position[colonne][ligne].colonne = -1  # on change les coordonées de la pièce mangée
  position[colonne][ligne].ligne = -1

def eat_Piece(piece, colonne, ligne):
  pass
  position[piece.colonne][piece.ligne] = 0  # on enlève la pièce de son ancienne case
  possible_prise = position[colonne][ligne]
  position[colonne][ligne] = piece  # on met à jour la liste position

def annuler_Mouvement(piece, ligne, colonne, arg):
  position[piece.colonne][piece.ligne] = piece  # on annule le mouvement
  position[colonne][ligne] = arg  # on annule le mouvement


def ROQUEB(): #grand roque blanc
  if KB1.echec==True or KB1.Move1 or TB2.Move1: #déjà échec ou bougé
    return (False,"Vous ne pouvez plus roquer.")
  elif position[3][0]!=0 or position[2][0]!=0 or position[1][0]!=0: #chemin pas libre
    return (False,"Il y a des pièces sur le chemin.")
  position[3][0]=KN1
  l=KN1.ligne
  c=KN1.colonne
  update_coord_piece(KN1,0,3)
  A=KN1.Echec2()
  position[3][0]=0
  position[2][0]=KN1
  update_coord_piece(KN1,0,2)
  B=KN1.Echec2()
  position[2][0]=0
  update_coord_piece(KN1,l,c)
  if A or B : #attaques en chemin
    return (False,"Vous ne pouvez pas roquer sans mettre votre roi en échec.")
  elif position[4][0]==KB1 and position[0][0]==TB1: #tout bon, roque
    update_coord_piece(KB1,0,2)
    position[2][0]=KB1
    update_coord_piece(TB1,0,3)
    position[3][0]=TB1
    position[4][0]=0 #on enlève les pièces de leur ancienne case
    position[0][0]=0
    return (True,0)
  else:
    return (False,"Vous ne pouvez pas roquer.")



def ROQUEN(): #grand roque noir
  if KN1.echec==True or KN1.Move1 or TN2.Move1:
    return (False,"Vous ne pouvez plus roquer.")
  elif position[3][7]!=0 or position[2][7]!=0 or position[1][7]!=0:
    return (False,"Il y a des pièces sur le chemin.")
  position[3][7]=KN1
  l=KN1.ligne
  c=KN1.colonne
  update_coord_piece(KN1,7,3)
  A=KN1.Echec2()
  position[3][7]=0
  position[2][7]=KN1
  update_coord_piece(KN1,7,2)
  B=KN1.Echec2()
  position[2][7]=0
  update_coord_piece(KN1,l,c)
  if A or B:
    return (False,"Vous ne pouvez pas roquer sans mettre votre roi en échec.")
  elif position[4][7]==KN1 and position[0][7]==TN1: #tout bon, roque
    update_coord_piece(KN1,7,2) #on met à jour les coordonnées des pièces
    position[2][7]=KN1
    update_coord_piece(TN2,7,3)
    position[3][7]=TN1
    position[4][7]=0 #on enlève les pièces de leur ancienne case
    position[0][7]=0
    return (True,0)
  else:
    return (False,"Vous ne pouvez pas roquer.")



def roqueB(): #petit roque blanc
  global position
  global KB1,TB2
  if KB1.echec==True or KB1.Move1 or TB2.Move1: #si echec ou déjà bougé
    return (False,"Vous ne pouvez plus roquer.")
  elif position[5][0]!=0 or position[6][0]!=0 : #si chemin pas dégegé
    return (False,"La case d'arrivée est déjà occupée.")
  position[5][0]=KB1
  l=KB1.ligne
  c=KB1.colonne
  update_coord_piece(KB1,0,5)
  A=KB1.Echec2()
  position[5][0]=0
  position[6][0]=KB1
  update_coord_piece(KB1,0,6)
  B=KB1.Echec2()
  position[6][0]=0
  update_coord_piece(KB1,l,c)
  if A or B: #si attaque sur le chemin
    return (False,"Vous ne pouvez pas roquer sans mettre votre roi en échec.")
  elif position[4][0]==KB1 and position[7][0]==TB2: #tout bon, roque
    update_coord_piece(KB1,0,6) #on met les coordonnées à jour
    position[6][0]=KB1
    update_coord_piece(TB2,0,5)
    position[5][0]=TB2
    position[4][0]=0 #on enlève les pièces de leur ancienne case
    position[7][0]=0
    return (True,0)
  else:
    return (False,"Vous ne pouvez pas roquer.")


def roqueN(): #petit roque noir
  global position
  global KN1, TN2
  if KN1.echec==True or KN1.Move1 or TN2.Move1: # déjà échec ou bougé
    return (False,"Vous ne pouvez plus roquer.")
  elif position[5][7]!=0 or position[6][7]!=0: #chemin pas libre
    return (False,"La case d'arrivée est déjà occupée.")
  position[5][7]=KN1
  l=KN1.ligne
  c=KN1.colonne
  update_coord_piece(KN1,7,5)
  A=KN1.Echec2()
  position[5][7]=0
  position[6][7]=KN1
  update_coord_piece(KN1,7,6)
  B=KN1.Echec2()
  position[6][7]=0
  update_coord_piece(KN1,l,c)
  if A or B: #attaque sur le chemin
    return (False,"Vous ne pouvez pas roquer sans mettre votre roi en échec.")
  elif position[4][7]==KN1 and position[7][7]==TN2: #tout bon, roque
    update_coord_piece(KN1,7,7)
    position[6][7]=KN1
    update_coord_piece(TN2,7,5)
    position[5][7]=TN2
    position[4][7]=0 #on enlève les pièces de leur ancienne case
    position[7][7]=0
    return (True,0)
  else:
    return (False,"Vous ne pouvez pas roquer.")





def mouvement(piece,case,CouleurQuiJoue,coup_special,nbcoup): #case = liste des 2 coordonées de la case : [colonne,ligne]
  global position
  if coup_special != "":

    if coup_special=="roque": #petit roque
      if CouleurQuiJoue=="Blanc": #blancs
        return roqueB()
      else: #noirs
        return roqueN()

    elif coup_special == "ROQUE": #grand roque
      if CouleurQuiJoue=="Blanc": #blancs
        return ROQUEB()
      else: #noirs
        return ROQUEN()

    elif coup_special == "PEP":
      return prise_en_passant(piece, case, CouleurQuiJoue, nbcoup)

  elif piece==0:
    message_erreur=("Vous n'avez pas de pièce à cet endroit.")
    #print("Vous n'avez pas de pièce à cet endroit.")
    return (False,message_erreur)
  else:
    if piece._couleur==CouleurQuiJoue:
      a=type(piece)
      ligne=case[1]
      colonne=case[0]
      if ligne==piece.ligne and colonne==piece.colonne:
        message_erreur="Votre pièce est déjà à cette position."
        return (False,message_erreur)
      else:
        if a!=Pion:
          if piece.mouvement_possible(colonne,ligne):
            if position[colonne][ligne]!=0: #s'il y a déjà une pièce sur la case
              if position[colonne][ligne]._couleur!=CouleurQuiJoue: #si la pièce est de la couleur opposée, on la mange
                position[piece.colonne][piece.ligne]=0 #on enlève la pièce de son ancienne case
                possible_prise=position[colonne][ligne]
                position[colonne][ligne]=piece #on met à jour la liste position
                if (CouleurQuiJoue == "Blanc" and KB1.Echec2()) or (CouleurQuiJoue=="Noir" and KN1.Echec2()): #si clouage
                  message_erreur="Vous ne pouvez pas bouger votre pièce à cet endroit sans mettre votre roi en échec."
                  #annuler_Mouvement(piece, ligne, colonne, possible_prise)
                  position[piece.colonne][piece.ligne]=piece #on annule le mouvement
                  position[colonne][ligne]=possible_prise
                  return (False,message_erreur)
                update_coord_piece(piece, ligne, colonne)#on met à jour les coordonnées de la pièce
                if (a==Tour or a==Roi):
                  piece.Move1=True
                if CouleurQuiJoue=='Blanc':
                  #eaten_Blanc(colonne,ligne)
                  prises_Blanc.append(possible_prise) #on met à jour la liste des prises
                  possible_prise.colonne=-1 #on change les coordonées de la pièce mangée
                  possible_prise.ligne=-1
                else: #noirs
                  # eaten_Noir(colonne,ligne)
                  prises_Noir.append(possible_prise)
                  possible_prise.colonne=-2 #on change les coordonées de la pièce mangée
                  possible_prise.ligne=-2
              else:
                message_erreur="Il y a déjà une de vos pièces sur cette case."
                return (False,message_erreur)
            else: #s'il n'y a pas d'autre pièce sur la case
              position[piece.colonne][piece.ligne]=0 #on enlève la pièce de son ancienne case
              position[colonne][ligne]=piece #on met à jour la liste position
              if (CouleurQuiJoue == "Blanc" and KB1.Echec2()) or (CouleurQuiJoue=="Noir" and KN1.Echec2()): #si clouage
                message_erreur="Vous ne pouvez pas bouger votre pièce à cet endroit sans mettre votre roi en échec."
                #annuler_Mouvement(piece, ligne, colonne, 0)
                position[piece.colonne][piece.ligne]=piece #on annule le mouvement
                position[colonne][ligne]=0 #on annule le mouvement
                return (False,message_erreur)
              if (a==Tour or a==Roi):
                  piece.Move1=True
              update_coord_piece(piece, ligne, colonne)#on met à jour les coordonnées de la pièce
          else:
            message_erreur="Vous ne pouvez pas déplacer la pièce à cet endroit là."
            return (False,message_erreur)

        else: #cas spécial du pion
          legalite = piece.mouvement_possible(colonne,ligne)[0]
          type_de_mouvement = piece.mouvement_possible(colonne,ligne)[1]
          if legalite:
            if CouleurQuiJoue=="Blanc": #si les blancs jouent
              if type_de_mouvement == "tout_droit":
                if position[colonne][ligne]!=0: #s'il y a déjà une pièce sur la case
                  message_erreur="Cette case est déjà occupée."
                  return (False,message_erreur)
                else:
                  position[piece.colonne][piece.ligne]=0 #on enlève la pièce de son ancienne case
                  position[colonne][ligne]=piece #on met à jour la liste position
                  if KB1.Echec2(): #si clouage
                    message_erreur="Vous ne pouvez pas bouger votre pièce à cet endroit sans mettre votre roi en échec."
                    #annuler_Mouvement(piece, ligne, colonne, 0)
                    position[piece.colonne][piece.ligne]=piece #on annule le mouvement
                    position[colonne][ligne]=0 #on annule le mouvement
                    return (False,message_erreur)
                  update_coord_piece(piece, ligne, colonne)#on met à jour les coordonnées de la pièce
              elif type_de_mouvement == "tout_droit_2":
                if position[colonne][ligne]!=0: #s'il y a déjà une pièce sur la case
                  message_erreur="Cette case est déjà occupée."
                  return (False,message_erreur)
                else:
                  position[piece.colonne][piece.ligne]=0 #on enlève la pièce de son ancienne case
                  position[colonne][ligne]=piece #on met à jour la liste position
                  if KB1.Echec2(): #si clouage
                    message_erreur="Vous ne pouvez pas bouger votre pièce à cet endroit sans mettre votre roi en échec."
                    #annuler_Mouvement(piece, ligne, colonne, 0)
                    position[piece.colonne][piece.ligne]=piece #on annule le mouvement
                    position[colonne][ligne]=0 #on annule le mouvement
                    return (False,message_erreur)
                  update_coord_piece(piece, ligne, colonne)  # on met à jour les coordonnées de la pièce
                  piece._condition2 = int(nbcoup.get())

              else:
                if position[colonne][ligne]==0:#s'il n'y a pas de pièce sur la case
                    message_erreur="Vous ne pouvez déplacer votre pion en diagonale que pour manger une pièce."
                    return (False,message_erreur)
                elif position[colonne][ligne]._couleur!=CouleurQuiJoue: #si la pièce est de la couleur opposée, on la mange
                  position[piece.colonne][piece.ligne]=0 #on enlève la pièce de son ancienne case
                  possible_prise=position[colonne][ligne]
                  position[colonne][ligne]=piece #on met à jour la liste position
                  if KB1.Echec2(): #si clouage
                    message_erreur="Vous ne pouvez pas bouger votre pièce à cet endroit sans mettre votre roi en échec."
                    #annuler_Mouvement(piece, ligne, colonne, possible_prise)
                    position[piece.colonne][piece.ligne]=piece #on annule le mouvement
                    position[colonne][ligne]=possible_prise #on annule le mouvement
                    return (False,message_erreur)
                  eaten_Blanc(colonne, ligne)
                  update_coord_piece(piece, ligne, colonne)#on met à jour les coordonnées de la pièce
                else:
                  message_erreur="Il y a déjà une de vos pièces sur cette case."
                  return (False,message_erreur)

            else: #si les noirs jouent
              if type_de_mouvement == "tout_droit":
                if position[colonne][ligne]!=0: #s'il y a déjà une pièce sur la case
                  message_erreur="Cette case est déjà occupée."
                  return (False,message_erreur)
                else:
                  position[piece.colonne][piece.ligne]=0 #on enlève la pièce de son ancienne case
                  position[colonne][ligne]=piece #on met à jour la liste position
                  if KN1.Echec2(): #si clouage
                      message_erreur="Vous ne pouvez pas bouger votre pièce à cet endroit sans mettre votre roi en échec."
                      #annuler_Mouvement(piece, ligne, colonne, 0)
                      position[piece.colonne][piece.ligne]=piece #on annule le mouvement
                      position[colonne][ligne]=0 #on annule le mouvement
                      return (False,message_erreur)
                  update_coord_piece(piece, ligne, colonne)  # on met à jour les coordonnées de la pièce
              elif type_de_mouvement == "tout_droit_2":
                if position[colonne][ligne]!=0: #s'il y a déjà une pièce sur la case
                  message_erreur="Cette case est déjà occupée."
                  return (False,message_erreur)
                else:
                  position[piece.colonne][piece.ligne]=0 #on enlève la pièce de son ancienne case
                  position[colonne][ligne]=piece #on met à jour la liste position
                  if KN1.Echec2(): #si clouage
                    message_erreur="Vous ne pouvez pas bouger votre pièce à cet endroit sans mettre votre roi en échec."
                    #annuler_Mouvement(piece, ligne, colonne, 0)
                    position[piece.colonne][piece.ligne]=piece #on annule le mouvement
                    position[colonne][ligne]=0 #on annule le mouvement
                    return (False,message_erreur)
                update_coord_piece(piece, ligne, colonne)#on met à jour les coordonnées de la pièce
                piece._condition2 = int(nbcoup.get())

              else:
                if position[colonne][ligne]==0: #s'il n'y a pas de pièce sur la case
                  message_erreur="Vous ne pouvez déplacer votre pion en diagonale que pour manger une pièce."
                  return (False,message_erreur)
                elif position[colonne][ligne]._couleur!=CouleurQuiJoue: #si la pièce est de la couleur opposée, on la mange
                  position[piece.colonne][piece.ligne]=0 #on enlève la pièce de son ancienne case
                  possible_prise=position[colonne][ligne]
                  position[colonne][ligne]=piece #on met à jour la liste position
                  if KN1.Echec2(): #si clouage
                    message_erreur="Vous ne pouvez pas bouger votre pièce à cet endroit sans mettre votre roi en échec."
                    #annuler_Mouvement(piece, ligne, colonne, possible_prise)
                    position[piece.colonne][piece.ligne]=piece #on annule le mouvement
                    position[colonne][ligne]=possible_prise #on annule le mouvement
                    return (False,message_erreur)
                  else:
                    eaten_Noir(colonne,ligne)#on ajoute la pièce à la liste des pièces mangées
                    update_coord_piece(piece, ligne, colonne)#on met à jour les coordonnées de la pièce
                else:
                  message_erreur="Il y a déjà une de vos pièces sur cette case."
                  return (False,message_erreur)
          else:
            message_erreur="Vous ne pouvez pas déplacer la pièce à cet endroit là."
            return (False,message_erreur)
    else:
      message_erreur="Vous ne pouvez pas déplacer une pièce de l'adversaire."
      return (False,message_erreur)
  #if (a==Tour or a==Roi):
  if (type(piece) == Tour or type(piece)== Roi):
    piece.Move1=True

  return (True,0)


def annuler_Mouvement(piece, ligne, colonne, arg):
  position[piece.colonne][piece.ligne] = piece  # on annule le mouvement
  position[colonne][ligne] = arg  # on annule le mouvement

def prise_en_passant(piece, case, CouleurQuiJoue, nbcoup):
  ligne = case[1]
  colonne = case[0]
  if CouleurQuiJoue == "Blanc":  # si les blancs jouent
    if piece.ligne == 4:
      if type(position[piece.colonne - 1][piece.ligne]) == Pion and position[piece.colonne - 1][piece.ligne]._couleur != CouleurQuiJoue:
        if position[piece.colonne - 1][piece.ligne]._condition2 == int(nbcoup.get())-1 :
          position[piece.colonne][piece.ligne] = 0  # on enlève la pièce de son ancienne case
          position[colonne][ligne] = piece  # on la met sur la nouvelle case
          eaten_Blanc(piece.colonne - 1, piece.ligne)
          position[piece.colonne - 1][piece.ligne] = 0  # on enlève le pion adversaire du board
          update_coord_piece(piece, ligne, colonne)
          return (True, 0)
        else:
          return (False, "PEP only possible directly after move pion N.")
      if type(position[piece.colonne + 1][piece.ligne]) == Pion and position[piece.colonne + 1][piece.ligne]._couleur != CouleurQuiJoue:
        if position[piece.colonne + 1][piece.ligne]._condition2 == int(nbcoup.get())-1 :
          position[piece.colonne][piece.ligne] = 0  # on enlève la pièce de son ancienne case
          position[colonne][ligne] = piece  # on la met sur la nouvelle case
          eaten_Blanc(piece.colonne + 1,piece.ligne) #on l'ajoute aux prises des Blancs
          position[piece.colonne + 1][piece.ligne] = 0  # on enlève le pion adversaire du board
          update_coord_piece(piece, ligne, colonne)
          return (True, 0)
        else:
          return (False, "PEP only possible directly after move pion N.")
      else:
        return (False,"PEP impossible car pion noir au mauvais endroit.")
    else:
      return (False,"PEP impossible car pion blanc au mauvais endroit.")
  else: #pour les noirs
    if piece.ligne == 3:
      if type(position[piece.colonne - 1][piece.ligne]) == Pion and position[piece.colonne - 1][piece.ligne]._couleur != CouleurQuiJoue:
        if position[piece.colonne - 1][piece.ligne]._condition2 == int(nbcoup.get())-1 :
          position[piece.colonne][piece.ligne] = 0  # on enlève la pièce de son ancienne case
          position[colonne][ligne] = piece  # on la met sur la nouvelle case
          eaten_Blanc(piece.colonne - 1, piece.ligne)
          position[piece.colonne - 1][piece.ligne] = 0
          update_coord_piece(piece, ligne, colonne)
          return (True, 0)
        else:
          return (False, "PEP only possible directly after move pion B.")
      if type(position[colonne + 1][ligne]) == Pion and position[colonne + 1][ligne]._couleur != CouleurQuiJoue:
        if position[piece.colonne + 1][piece.ligne]._condition2 == int(nbcoup.get())-1 :
          position[piece.colonne][piece.ligne] = 0  # on enlève la pièce de son ancienne case
          position[colonne][ligne] = piece  # on la met sur la nouvelle case
          eaten_Blanc(piece.colonne + 1, piece.ligne)
          position[piece.colonne + 1][piece.ligne] = 0
          update_coord_piece(piece, ligne, colonne)
          return (True, 0)
        else:
          return (False, "PEP only possible directly after move pion B.")
      else:
        return (False,"PEP impossible car pion blanc au mauvais endroit.")
    else:
      return (False,"PEP impossible car pion noir au mauvais endroit.")