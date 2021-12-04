#ce fichier est ouvert à tout le monde pour faire des tests


#test des fonctions mouvement piece

#position = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,PB1,0,0,0,0,0],[0,PB2,PB3,PB4,0,0,0,0],[0,0,PB5,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
#P = pion("Blanc",3,1,2)
#print(pion.mouvementpossible(P,5,6))


#from board import mouvement






#tests d'héritage de classes :

#class Piece():
    #def __init__(self,case):
        #self.position=case

#class Fou(Piece):

    #def __init__(self,case):
        #super().__init__(case)

    #def mouvement_posssible(self,colonne,ligne):
            #if [colonne-1,ligne-1]==self.position:
                #return True
            #else :
                #return False

#class Tour(Piece):
    #def __init__(self,case):
        #super().__init__(case)
    #def mouvement_posssible(self,colonne,ligne):
            #if [colonne-1,ligne]==self.position:
                #return True
            #else :
                #return False

#class Dame(Fou,Tour):
    #def __init__(self,case,echec):
        #super().__init__(case)
        #self._mort=echec
        #self.valeur=5
    #def mouvement_posssible(self,colonne,ligne):
            #if Fou(self.position).mouvement_posssible(colonne,ligne) or Tour(self.position).mouvement_posssible(colonne,ligne):
                #return True
            #else :
                #return False

#reine=Dame([1,1],True)
#print(reine.mouvement_posssible(1,1))
#print(reine.position,reine._mort,reine.valeur)