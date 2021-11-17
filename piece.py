from board import position

#OPP pour instancier les différentes pieces
class piece():
  def __str__(self):
    nom=""
    if self._couleur=="Blanc":
      nom+="B"
    else:
      nom+="N"
    nom+=str(self._numero)
    if type(self)==pion:
      nom="P"+nom
    elif type(self)==fou:
      nom="F"+nom
    elif type(self)==dame:
      nom="Q"+nom
    elif type(self)==roi:
      nom="K"+nom
    elif type(self)==cavalier:
      nom="C"+nom
    elif type(self)==tour:
      nom="T"+nom
    return nom
    #on a un nom du type "PN3" pour le pion noir 3

	
#attributs de chaque piece :
  #couleur
  #coordonées sur le board
  #valeur
  #numéro de piece (ex : 1 pour le pion 1 ou le cavalier 1..)

class fou(piece):
  def __init__ (self,couleur,colonne,ligne,numero,valeur=3):
    self._couleur=couleur
    self._valeur=valeur
    self.ligne=ligne
    self.colonne=colonne
    self._numero=numero

  def mouvementpossible(self,colonne,ligne): #indique si le fou peut bouger jusqu'à la case indiquée
    if ligne>7 or colonne>7 or ligne<0 or colonne<0: # sortie de l'échiquier
	    return False
    elif colonne==self.colonne and ligne==self.ligne: #si le fou ne bouge pas
	    return True
    else:
      K=0
      cpt=0
      for k in range(-8,9): #motif de déplacement du fou
        if (colonne==self.colonne+k and ligne==self.ligne+k) or (colonne==self.colonne-k and ligne==self.ligne+k):
          cpt+=1
          K=k
      if cpt!=1: #pas le bon "motif" de déplacement
	      return False

      elif (colonne==self.colonne+K and ligne==self.ligne+K): #si le fou bouge sur la diagonale de bas gauche à haut droit (/)
        if K>0: #si le fou va vers le haut gauche
          for k in range(1,K):
            if position[self.colonne+k][self.ligne+k]!=0: #s'il y a une autre piece en travers du chemin
              return False
        else: #si le fou va vers le bas droit
	        for k in range(1,-(K-1)):
        	  if position[self.colonne-k][self.ligne-k]!=0: #s'il y a une autre piece en travers du chemin
		          return False
    
      elif (colonne==self.colonne-K and ligne==self.ligne+K): #si le fou bouge sur la diagonale de haut gauche à bas droit (\)
        if K > 0: #si le fou va vers le haut droit
          for k in range(1,K):
            if position[self.colonne-k][self.ligne+k]!=0: #s'il y a une autre piece en travers du chemin
              return False
        else: #si la tour va vers le bas gauche 
          for k in range(1,-(K-1)):
            if position[self.colonne+k][self.ligne-k]!=0: #s'il y a une autre piece en travers du chemin
              return False
    return True


class roi(piece):
  def __init__ (self,couleur,colonne,ligne,numero,valeur=0):
    self._couleur=couleur
    self._valeur=valeur
    self.ligne=ligne
    self.colonne=colonne
    self._numero=numero

class dame (piece):
  def __init__ (self,couleur,colonne,ligne,numero,valeur=9):
    self._couleur=couleur
    self._valeur=valeur
    self.ligne=ligne
    self.colonne=colonne
    self._numero=numero

class cavalier (piece):
  def __init__ (self,couleur,colonne,ligne,numero,valeur=3):
    self._couleur=couleur
    self._valeur=valeur
    self.ligne=ligne
    self.colonne=colonne
    self._numero=numero

class pion (piece):
  def __init__ (self,couleur,colonne,ligne,numero,valeur=1):
    self._couleur=couleur
    self._valeur=valeur
    self.ligne=ligne
    self.colonne=colonne
    self._numero=numero

class tour (piece):
  def __init__ (self,couleur,colonne,ligne,numero,valeur=5):
    self._couleur=couleur
    self._valeur=valeur
    self.ligne=ligne
    self.colonne=colonne
    self._numero=numero

  def mouvementpossible(self,colonne,ligne): #indique si la tour peut bouger jusqu'à la case indiquée
    if ((ligne != self.ligne) and (colonne != self.colonne)) or ligne>7 or colonne>7 or ligne<0 or colonne<0: #pas le bon "motif" de déplacement ou sortie de l'échiquier
	    return False
    elif colonne==self.colonne and ligne==self.ligne: #si la tour ne bouge pas
	    return True
    elif ligne==self.ligne: #si la tour bouge en horizontal
	    if colonne > self.colonne: #si la tour va vers le haut
	      for c in range(self.colonne,colonne):
		      if position[c][ligne]!=0: #s'il y a une autre piece en travers du chemin
		        return False
	    else: #si la tour va vers le bas
	      for c in range(colonne,self.colonne):
        	if position[c][ligne]!=0: #s'il y a une autre piece en travers du chemin
		        return False
    elif colonne==self.colonne: #si la tour bouge en vertical
	    if ligne > self.ligne: #si la tour va vers la droite
	      for l in range(self.ligne,ligne):
		      if position[colonne][l]!=0: #s'il y a une autre piece en travers du chemin
		        return False
	    else: #si la tour va vers la gauche 
	      for l in range(ligne,self.ligne):
        	if position[colonne][l]!=0: #s'il y a une autre piece en travers du chemin
		        return False
    return True


  
#à faire pour chaque pièce :
  #def mouvementpossible (self,case) :
	  #if dans les règles :
		  #return True 
	  #else:
		  #return False


