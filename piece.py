class Piece():
    def __init__(self, couleur, colonne, ligne, numero):
        self._couleur = couleur
        self.ligne = ligne
        self.colonne = colonne
        self._numero = numero

    def __str__(self):
        nom = ""
        if self._couleur == "Blanc":
            nom += "B"
        else:
            nom += "N"
        nom += str(self._numero)
        if type(self) == Pion:
            nom = "P" + nom
        elif type(self) == Fou:
            nom = "F" + nom
        elif type(self) == Dame:
            nom = "Q" + nom
        elif type(self) == Roi:
            nom = "K" + nom
        elif type(self) == Cavalier:
            nom = "C" + nom
        elif type(self) == Tour:
            nom = "T" + nom
        return nom
        # on a un nom du type "PN3" pour le pion noir 3

    # attributs de chaque piece :
    # couleur
    # coordonées sur le board (ou -1,-1 si mangée par les blancs et -2,-2 si mangée par les noirs)
    # valeur
    # numéro de piece (ex : 1 pour le pion 1 ou le cavalier 1..)


class Fou(Piece):
    def __init__(self, couleur, colonne, ligne, numero):
        super().__init__(couleur, colonne, ligne, numero)
        self._valeur = 3

    def mouvement_possible(self, colonne, ligne):  # indique si le fou peut bouger jusqu'à la case indiquée
        from board import position
        if ligne > 7 or colonne > 7 or ligne < 0 or colonne < 0:  # sortie de l'échiquier
            return False
        elif colonne == self.colonne and ligne == self.ligne:  # si le fou ne bouge pas
            return True
        else:
            k=abs(colonne-self.colonne)
            if k != abs(ligne-self.ligne):
                return False #pas le bon motif de déplacement
            
            elif (colonne == self.colonne + k and ligne == self.ligne + k):  # si le fou bouge sur la diagonale de bas gauche à haut droit (/)
                for i in range(1, k):
                        if position[self.colonne + i][self.ligne + i] != 0:  # s'il y a une autre piece en travers du chemin
                            return False

            elif (colonne == self.colonne - k and ligne == self.ligne - k):  # si le fou bouge sur la diagonale de haut droite à bas gauche (/)
                for i in range(1, -(k - 1)):
                    if position[self.colonne - i][self.ligne - i] != 0:  # s'il y a une autre piece en travers du chemin
                        return False

            elif (colonne == self.colonne - k and ligne == self.ligne + k):  # si le fou bouge sur la diagonale de bas droit à haut gauche (\)
                for i in range(1, k):
                    if position[self.colonne - i][self.ligne + i] != 0:  # s'il y a une autre piece en travers du chemin
                        return False

            else:  # si le fou bouge sur la diagonale de haut gauche à bas droit (\)
                for i in range(1, -(k - 1)):
                    if position[self.colonne + i][self.ligne - i] != 0:  # s'il y a une autre piece en travers du chemin
                        return False

            #K = 0
            #cpt = 0
            #for k in range(-8, 9):  # motif de déplacement du fou
                #if (colonne == self.colonne + k and ligne == self.ligne + k) or (colonne == self.colonne - k and ligne == self.ligne + k):
                    #cpt += 1
                    #K = k
            #if cpt != 1:  # pas le bon "motif" de déplacement
                #return False

            #elif (colonne == self.colonne + K and ligne == self.ligne + K):  # si le fou bouge sur la diagonale de bas gauche à haut droit (/)
                #if K > 0:  # si le fou va vers le haut gauche
                    #for k in range(1, K):
                        #if position[self.colonne + k][self.ligne + k] != 0:  # s'il y a une autre piece en travers du chemin
                            #return False
                #else:  # si le fou va vers le bas droit
                    #for k in range(1, -(K - 1)):
                        #if position[self.colonne - k][self.ligne - k] != 0:  # s'il y a une autre piece en travers du chemin
                            #return False

            #elif (colonne == self.colonne - K and ligne == self.ligne + K):  # si le fou bouge sur la diagonale de haut gauche à bas droit (\)
                #if K > 0:  # si le fou va vers le haut droit
                    #for k in range(1, K):
                        #if position[self.colonne - k][self.ligne + k] != 0:  # s'il y a une autre piece en travers du chemin
                            #return False
                #else:  # si la tour va vers le bas gauche
                    #for k in range(1, -(K - 1)):
                        #if position[self.colonne + k][self.ligne - k] != 0:  # s'il y a une autre piece en travers du chemin
                            #return False
        return True

class Tour(Piece):
    def __init__(self, couleur, colonne, ligne, numero):
        super().__init__(couleur, colonne, ligne, numero)
        self._valeur = 5

    def mouvement_possible(self, colonne, ligne):  # indique si la tour peut bouger jusqu'à la case indiquée
        from board import position
        if ((ligne != self.ligne) and (colonne != self.colonne)) or ligne > 7 or colonne > 7 or ligne < 0 or colonne < 0:  # pas le bon "motif" de déplacement ou sortie de l'échiquier
            return False
        elif colonne == self.colonne and ligne == self.ligne:  # si la tour ne bouge pas
            return True
        elif ligne == self.ligne:  # si la tour bouge en horizontal
            if colonne > self.colonne:  # si la tour va vers le haut
                for c in range(self.colonne, colonne):
                    if position[c][ligne] != 0:  # s'il y a une autre piece en travers du chemin   ##1
                        return False
            else:  # si la tour va vers le bas
                for c in range(colonne, self.colonne):
                    if position[c][ligne] != 0:  # s'il y a une autre piece en travers du chemin  ##2
                        return False
        elif colonne == self.colonne:  # si la tour bouge en vertical
            if ligne > self.ligne:  # si la tour va vers la droite
                for l in range(self.ligne, ligne):
                    if position[colonne][l] != 0:  # s'il y a une autre piece en travers du chemin  ##3
                        return False
            else:  # si la tour va vers la gauche
                for l in range(ligne, self.ligne):
                    if position[colonne][l] != 0:  # s'il y a une autre piece en travers du chemin  ##4
                        return False
        return True

class Dame(Fou,Tour):
    def __init__(self, couleur, colonne, ligne, numero):
        super().__init__(couleur, colonne, ligne, numero)
        self._valeur = 9

    def mouvement_possible(self,colonne,ligne):
            if Fou(self._couleur, self.colonne, self.ligne, self._numero).mouvement_possible(colonne,ligne) or Tour(self._couleur, self.colonne, self.ligne, self._numero).mouvement_possible(colonne,ligne):
                return True
            else :
                return False


class Cavalier(Piece):
    def __init__(self, couleur, colonne, ligne, numero):
        super().__init__(couleur, colonne, ligne, numero)
        self._valeur = 3

    def mouvement_possible(self, colonne, ligne):  # indique si le cavalier peut bouger jusqu'à la case indiquée
        from board import position
        if colonne == self.colonne and ligne == self.ligne:  # si le cavalier ne bouge pas
            return True
        elif ((colonne != self.colonne - 2 and ligne != self.ligne + 1) or (colonne != self.colonne - 2 and ligne != self.ligne - 1) or (colonne != self.colonne - 1 and ligne != self.ligne + 2) or (colonne != self.colonne - 1 and ligne != self.ligne - 2) or (colonne != self.colonne + 1 and ligne != self.ligne + 2) or (colonne != self.colonne + 1 and ligne != self.ligne - 2) or (colonne != self.colonne + 2 and ligne != self.ligne + 1) or (colonne != self.colonne + 2 and ligne != self.ligne - 1)) or ligne > 7 or colonne > 7 or ligne < 0 or colonne < 0:  # pas le bon "motif" de déplacement ou sortie de l'échiquier
            return False
        else:
            return True


class Pion(Piece):
    def __init__(self, couleur, colonne, ligne, numero):
        super().__init__(couleur, colonne, ligne, numero)
        self._valeur = 1
        self.Move1 = True

    def mouvement_possible(self, colonne, ligne):  # indique si le pion peut bouger jusqu'à la case indiquée
        from board import position
        if ligne > 7 or colonne > 7 or ligne < 0 or colonne < 0:  # pas le bon "motif" de déplacement ou sortie de l'échiquier
            return False
        elif colonne == self.colonne and ligne == self.ligne:  # si le pion ne bouge pas
            return True
        if colonne != self.colonne and ligne == self.ligne:
            return False
        else:
            if colonne == self.colonne:
                if ligne == (self.ligne + 1) and self._couleur == "Blanc":
                    if position[colonne][ligne] == 0:  # s'il n'y a pas de piece sur la case d'arrivée
                        return True
                if ligne == (self.ligne + 2) and self._couleur == "Blanc":
                    if self.Move1:  # premier mouvement du pion ?
                        if position[colonne][ligne - 1] == 0 and position[colonne][ligne] == 0:  # s'il n'y a pas de piece sur la case d'arrivée
                            return True
                if ligne == (self.ligne - 1) and self._couleur != "Blanc":
                    if position[colonne][ligne] == 0:  # s'il n'y a pas de piece sur la case d'arrivée
                        return True
                if ligne == (self.ligne - 2) and self._couleur != "Blanc":
                    if self.Move1:  # premier mouvement du pion ?
                        if position[colonne][ligne + 1] == 0 and position[colonne][ligne] == 0:  # s'il n'y a pas de piece sur la case d'arrivée
                            return True
                # else:
                # return False
            if colonne == (self.colonne + 1) or colonne == (self.colonne - 1):  # mouvement diagonal
                if ligne == (self.ligne + 1) and self._couleur == "Blanc":
                    return True
                if ligne == (self.ligne - 1) and self._couleur != "Blanc":
                    return True
                # else:
                # return False
            else:
                return False


class Roi(Fou,Tour):
    def __init__(self, couleur, colonne, ligne, numero,echec=False):
        self._valeur = 0
        self._echec=echec
        self._couleur = couleur
        self.ligne = ligne
        self.colonne = colonne
        self._numero = numero

    def mouvement_possible(self,colonne,ligne):
            if (Fou(self._couleur, self.colonne, self.ligne, self._numero).mouvement_possible(colonne,ligne) or Tour(self._couleur, self.colonne, self.ligne, self._numero).mouvement_possible(colonne,ligne)) and (abs(ligne-self.ligne<1) and abs(colonne-self.colonne<1)):
                return True
            else :
                return False

    def Echec1(self): #attention : complexité élevée
        from board import position
        for piece in position:
            if piece !=0 and piece._couleur == self._couleur and piece.mouvement_possible(self.colonne,self.ligne):
                    return True
        return False
    
    def Echec2(self):
        from board import position
        #diagonales
        A=1
        for i in range(max(self.colonne,7-self.colonne), 8):
            a,b,c,d=True,True,True,True
            if not(self.colonne+i>7) and not(self.ligne+i>7) and position[self.colonne+i][self.ligne+i] != 0 and a:
                A= position[self.colonne+i][self.ligne+i]
                if (type(A)==Fou or type(A)==Dame) and A._couleur!=self._couleur:
                    return True
                else:
                    A=False
            elif not(self.ligne-i<0) and not(self.colonne-i<0) and position[self.colonne-i][self.ligne-i] != 0 and b:
                A= position[self.colonne-i][self.ligne-i]
                if (type(A)==Fou or type(A)==Dame) and A._couleur!=self._couleur:
                    return True
                else:
                    b=False
            elif not(self.colonne+i>7) and not(self.ligne-i<0) and position[self.colonne+i][self.ligne-i] != 0 and c:
                A=position[self.colonne+i][self.ligne-i]
                if (type(A)==Fou or type(A)==Dame) and A._couleur!=self._couleur:
                    return True
                else:
                    c= False
            elif not(self.colonne-i<0) and not(self.ligne+i>7) and position[self.colonne-i][self.ligne+i] != 0 and d:   
                A=position[self.colonne-i][self.ligne+i]
                if (type(A)==Fou or type(A)==Dame) and A._couleur!=self._couleur:
                    return True
                else:
                    d = False
                
        #Pion
        if self._couleur=="Blanc" and self.ligne!=7:
            if (self.colonne!=7 and type(position[self.colonne+1][self.ligne+1])==Pion and position[self.colonne+1][self.ligne+1]._couleur=="Noir")or (self.colonne!=0 and type(position[self.colonne-1][self.ligne+1])==Pion and position[self.colonne-1][self.ligne+1]._couleur=="Noir") :
                return True
        elif self._couleur=="Noir" and self.ligne!=0:
            if (self.colonne!=7 and type(position[self.colonne+1][self.ligne-1])==Pion and position[self.colonne+1][self.ligne-1]._couleur=="Blanc") or (self.colonne!=0 and type(position[self.colonne-1][self.ligne-1])==Pion and position[self.colonne-1][self.ligne-1]._couleur=="Blanc") :
                return True

        #cavalier
        if (not(self.colonne - 2 < 0) and not(self.ligne + 1 > 7) and type(position[self.colonne - 2][self.ligne + 1])==Cavalier and position[self.colonne - 2][self.ligne + 1]._couleur != self._couleur) or (not(self.colonne - 2 < 0) and not(self.ligne - 1 <  0) and type(position[self.colonne - 2][self.ligne - 1]) == Cavalier and position[self.colonne - 2][self.ligne - 1]._couleur!=self._couleur) or (not(self.colonne - 1 < 0) and not(self.ligne + 2 > 7) and type(position[self.colonne - 1][self.ligne + 2])==Cavalier and position[self.colonne - 1][self.ligne + 2]._couleur!=self._couleur) or (not(self.colonne - 1 < 0) and not(self.ligne - 2 < 0) and type(position[self.colonne - 1][self.ligne - 2])==Cavalier and position[self.colonne - 1][self.ligne - 2]._couleur!=self._couleur) or (not(self.colonne + 1 > 7) and not(self.ligne + 2 > 7) and type(position[self.colonne + 1][self.ligne + 2])==Cavalier and position[self.colonne + 1][self.ligne + 2]._couleur!=self._couleur) or (not(self.colonne + 1 > 7) and not(self.ligne - 2 < 0) and type(position[self.colonne + 1][self.ligne - 2])==Cavalier and position[self.colonne + 1][self.ligne - 2]._couleur!=self._couleur) or (not(self.colonne + 2 > 7) and not(self.ligne + 1 > 7) and type(position[self.colonne + 2][self.ligne + 1])==Cavalier and position[self.colonne + 2][self.ligne + 1]._couleur!=self._couleur) or (not(self.colonne + 2 > 7) and not(self.ligne - 1 < 0) and type(position[self.colonne + 2][self.ligne - 1])==Cavalier and position[self.colonne + 2][self.ligne - 1]._couleur!=self._couleur) :
            return True

        #colonnes/lignes
        A=1
        for i in range(max(self.colonne,7-self.colonne), 8): #colonne
            a,b=True,True
            if not(self.colonne+i>7) and position[self.colonne+i][self.ligne] != 0 and a:
                A=position[self.colonne+i][self.ligne]
                if (type(A)==Tour or type(A)==Dame) and A._couleur!=self._couleur:
                    return True
                else:
                    a=False
            elif not(self.colonne-i<0) and position[self.colonne-i][self.ligne] != 0 and b: 
                A= position[self.colonne-i][self.ligne]
                if (type(A)==Tour or type(A)==Dame) and A._couleur!=self._couleur:
                    return True
                else:
                    b=False
        A=1
        for i in range(max(self.ligne,7-self.ligne), 8): #ligne
            c,d=True,True
            if not(self.ligne+i>7) and position[self.colonne][self.ligne+i] != 0 and c:
                A=position[self.colonne][self.ligne+i]
                if (type(A)==Tour or type(A)==Dame) and A._couleur!=self._couleur:
                    return True
                else:
                    c=False
            elif not(self.ligne-i<0) and position[self.colonne][self.ligne-i] != 0 and d:
                A=position[self.colonne][self.ligne-i]
                if (type(A)==Tour or type(A)==Dame) and A._couleur!=self._couleur:
                    return True
                else:
                    d=False
        #Roi
        if (not(self.ligne+1 > 7) and type(position[self.colonne][self.ligne+1])==Roi and position[self.colonne][self.ligne+1]._couleur!=self._couleur) or (not(self.ligne-1 < 0) and type(position[self.colonne][self.ligne-1])==Roi and position[self.colonne][self.ligne-1]._couleur!=self._couleur) or (not (self.colonne+1 > 7) and type(position[self.colonne+1][self.ligne])==Roi and position[self.colonne+1][self.ligne]._couleur!=self._couleur) or (not(self.colonne-1 < 0) and not(self.ligne-1 < 0) and type(position[self.colonne-1][self.ligne-1])==Roi and position[self.colonne-1][self.ligne-1]._couleur!=self._couleur) or (not(self.colonne+1 > 7) and not(self.ligne+1 > 7) and type(position[self.colonne+1][self.ligne+1])==Roi and position[self.colonne+1][self.ligne+1]._couleur!=self._couleur) or (not (self.colonne-1 < 0) and not(self.ligne+1 > 7) and type(position[self.colonne-1][self.ligne+1])==Roi and position[self.colonne-1][self.ligne+1]._couleur!=self._couleur) or (not(self.colonne-1 < 0) and type(position[self.colonne-1][self.ligne])==Roi and position[self.colonne-1][self.ligne]._couleur!=self._couleur) or (not(self.colonne+1 > 7) and not(self.ligne-1 < 0) and type(position[self.colonne+1][self.ligne-1])==Roi and position[self.colonne+1][self.ligne-1]._couleur!=self._couleur):
            return True

        return False
        
        



# à faire pour chaque pièce :
# def mouvementpossible (self,case) :
# if dans les règles (pas de sortie de l'échiqiuer, bonne forme de déplacement, pas d'autre pièce sur le chemin):
# return True
# elif piece ne bouge pas:
# return True
# else:
# return False
