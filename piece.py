#OPP pour instancier les différentes pieces
class piece():
  class fou(piece):
    def __init__ (self,couleur,colonne,ligne,numero,valeur=3):
      self._couleur=couleur
      self._valeur=valeur
      self.ligne=ligne
      self.colonne=colonne
      self.numero=numero
  class roi(piece):
     def __init__ (self,couleur,colonne,ligne,numero,valeur=0):
      self._couleur=couleur
      self._valeur=valeur
      self.ligne=ligne
      self.colonne=colonne
      self.numero=numero
  class dame (piece):
     def __init__ (self,couleur,colonne,ligne,numero,valeur=9):
      self._couleur=couleur
      self._valeur=valeur
      self.ligne=ligne
      self.colonne=colonne
      self.numero=numero
  class cavalier (piece):
     def __init__ (self,couleur,colonne,ligne,numero,valeur=3):
      self._couleur=couleur
      self._valeur=valeur
      self.ligne=ligne
      self.colonne=colonne
      self.numero=numero
  class tour (piece):
     def __init__ (self,couleur,colonne,ligne,numero,valeur=5):
      self._couleur=couleur
      self._valeur=valeur
      self.ligne=ligne
      self.colonne=colonne
      self.numero=numero
  class pion (piece):
     def __init__ (self,couleur,colonne,ligne,numero,valeur=1):
      self._couleur=couleur
      self._valeur=valeur
      self.ligne=ligne
      self.colonne=colonne
      self.numero=numero
  #attributs de chaque piece :
    #couleur
    #coordonées sur le board
    #valeur
    #numéro de piece (ex : 1 pour le pion 1 ou le cavalier 1..)
