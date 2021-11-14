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

  def mouvementpossible(self,case): #indique si la tour peut bouger jusqu'à la case indiquée
    ligne=case[1]
    colonne=case[0]
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
#il faut importer la variable position du fichier board



  
#à faire pour chaque pièce :
  #def mouvementpossible (self,case) :
	  #if dans les règles :
		  #return True 
	  #else:
		  #return False


