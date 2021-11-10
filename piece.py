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
class tour (piece):
  def __init__ (self,couleur,colonne,ligne,numero,valeur=5):
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
#attributs de chaque piece :
  #couleur
  #coordonées sur le board
  #valeur
  #numéro de piece (ex : 1 pour le pion 1 ou le cavalier 1..)

  

  #def mouvement (self) :
	  #if dans les règles :
		  #mettre à jour les coordonnées et le tableau récapitulatif des positions des pièces 
	  #else:
		  #print("vous ne pouvez pas jouer ce coup") 

