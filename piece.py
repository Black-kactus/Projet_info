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
        return True

class Tour(Piece):
    def __init__(self, couleur, colonne, ligne, numero,Move1=False):
        super().__init__(couleur, colonne, ligne, numero)
        self._valeur = 5
        self.Move1=Move1

    def mouvement_possible(self, colonne, ligne):  # indique si la tour peut bouger jusqu'à la case indiquée
        from board import position
        if ((ligne != self.ligne) and (colonne != self.colonne)) or ligne > 7 or colonne > 7 or ligne < 0 or colonne < 0:  # pas le bon "motif" de déplacement ou sortie de l'échiquier
            return False
        elif colonne == self.colonne and ligne == self.ligne:  # si la tour ne bouge pas
            return True
        elif ligne == self.ligne:  # si la tour bouge en horizontal
            if colonne > self.colonne:  # si la tour va vers la droite
                for c in range(self.colonne+1, colonne):
                    if position[c][ligne] != 0:  # s'il y a une autre piece en travers du chemin   ##1
                        return False
            else:  # si la tour va vers la gauche
                for c in range(colonne+1, self.colonne):
                    if position[c][ligne] != 0:  # s'il y a une autre piece en travers du chemin  ##2
                        return False
        elif colonne == self.colonne:  # si la tour bouge en vertical
            if ligne > self.ligne:  # si la tour va vers le haut
                for l in range(self.ligne+1, ligne):
                    if position[colonne][l] != 0:  # s'il y a une autre piece en travers du chemin  ##3
                        return False
            else:  # si la tour va vers le bas
                for l in range(ligne+1, self.ligne):
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
        if ligne > 7 or colonne > 7 or ligne < 0 or colonne < 0:  # sortie de l'échiquier
            return False
        elif (colonne == self.colonne - 2 and ligne == self.ligne + 1) or (colonne == self.colonne - 2 and ligne == self.ligne - 1) or (colonne == self.colonne - 1 and ligne == self.ligne + 2) or (colonne == self.colonne - 1 and ligne == self.ligne - 2) or (colonne == self.colonne + 1 and ligne == self.ligne + 2) or (colonne == self.colonne + 1 and ligne == self.ligne - 2) or (colonne == self.colonne + 2 and ligne == self.ligne + 1) or (colonne == self.colonne + 2 and ligne == self.ligne - 1) or (colonne == self.colonne and ligne == self.ligne) :  # bon "motif" de déplacement ou cavalier ne bouge pas
            print("bah là c'est bon")
            return True
        else: #pas bon déplacement
            return False


class Pion(Piece):
    def __init__(self, couleur, colonne, ligne, numero):
        super().__init__(couleur, colonne, ligne, numero)
        self._valeur = 1
        self._condition2 = 5

    def mouvement_possible(self, colonne, ligne):  # indique si le pion peut bouger jusqu'à la case indiquée
        from board import position
        if ligne > 7 or colonne > 7 or ligne < 0 or colonne < 0:  # pas le bon "motif" de déplacement ou sortie de l'échiquier
            return (False,0)
        elif colonne == self.colonne and ligne == self.ligne:  # si le pion ne bouge pas
            return (True,"statique")
        elif colonne != self.colonne and ligne == self.ligne: #mouvement horizontal
            return (False,0)
        else:
            if colonne == self.colonne: #mouvement vertical
                if ligne == (self.ligne + 1) and self._couleur == "Blanc" :
                    if position[colonne][ligne] == 0:  # s'il n'y a pas de piece sur la case d'arrivée
                        return (True,"tout_droit")
                    else:
                        return (False,0)
                elif self.ligne == 1 and ligne == 3 and self._couleur == "Blanc": # premier mouvement du pion
                    if position[colonne][ligne - 1] == 0 and position[colonne][ligne] == 0:  # s'il n'y a pas de piece sur la case d'arrivée
                        return (True,"tout_droit_2")
                    else:
                        return (False,0)
                elif ligne == (self.ligne - 1) and self._couleur == "Noir":
                    if position[colonne][ligne] == 0:  # s'il n'y a pas de piece sur la case d'arrivée
                        return (True,"tout_droit")
                    else:
                        return (False,0)
                elif ligne == 4 and self.ligne == 6 and self._couleur == "Noir": # premier mouvement du pion
                    if position[colonne][ligne + 1] == 0 and position[colonne][ligne] == 0:  # s'il n'y a pas de piece sur la case d'arrivée
                        return (True,"tout_droit_2")
                    else:
                        return (False,0)
                else:
                    return (False,0)
            elif colonne == (self.colonne + 1) or colonne == (self.colonne - 1):# mouvement diagonal
                if ligne == (self.ligne + 1) and self._couleur == "Blanc":
                    return (True,"diagonale")

                elif ligne == (self.ligne - 1) and self._couleur == "Noir":
                    return (True,"diagonale")
                else:
                    return (False,0)
            else:
                return (False,0)


class Roi(Fou,Tour):
    def __init__(self, couleur, colonne, ligne, numero, echec=False):
        super().__init__(couleur, colonne, ligne, numero)
        self._valeur = 0
        self.echec=echec
        self.Move1=False

    def mouvement_possible(self,colonne,ligne):
            if (Fou(self._couleur, self.colonne, self.ligne, self._numero).mouvement_possible(colonne,ligne) or Tour(self._couleur, self.colonne, self.ligne, self._numero).mouvement_possible(colonne,ligne)) and (abs(ligne-self.ligne<=1) and abs(colonne-self.colonne<=1)):
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
        a,b,c,d=True,True,True,True
        for i in range(1,min(max(self.colonne,7-self.colonne),max(self.ligne,7-self.ligne))+1):
            if not(self.colonne+i>7) and not(self.ligne+i>7) and position[self.colonne+i][self.ligne+i] != 0 and a:
                A= position[self.colonne+i][self.ligne+i]
                if (type(A)==Fou or type(A)==Dame) and A._couleur!=self._couleur:
                    self.echec=True
                    print("diago")#
                    return True
                else:
                    a=False
            if not(self.ligne-i<0) and not(self.colonne-i<0) and position[self.colonne-i][self.ligne-i] != 0 and b:
                A= position[self.colonne-i][self.ligne-i]
                if (type(A)==Fou or type(A)==Dame) and A._couleur!=self._couleur:
                    self.echec=True
                    print("diago")#
                    return True
                else:
                    b=False
            if self.colonne+i<=7 and self.ligne-i>=0 and position[self.colonne+i][self.ligne-i] != 0 and c:
                A=position[self.colonne+i][self.ligne-i]
                if (type(A)==Fou or type(A)==Dame) and A._couleur!=self._couleur:
                    self.echec=True
                    print("diago")#
                    return True
                else:
                    c= False
            if not(self.colonne-i<0) and not(self.ligne+i>7) and position[self.colonne-i][self.ligne+i] != 0 and d:   
                A=position[self.colonne-i][self.ligne+i]
                if (type(A)==Fou or type(A)==Dame) and A._couleur!=self._couleur:
                    self.echec=True
                    print("diago")#
                    return True
                else:
                    d = False
                
        #Pion
        if self._couleur=="Blanc" and self.ligne!=7:
            if (self.colonne!=7 and type(position[self.colonne+1][self.ligne+1])==Pion and position[self.colonne+1][self.ligne+1]._couleur=="Noir")or (self.colonne!=0 and type(position[self.colonne-1][self.ligne+1])==Pion and position[self.colonne-1][self.ligne+1]._couleur=="Noir") :
                print("pion")#
                return True
        elif self._couleur=="Noir" and self.ligne!=0:
            if (self.colonne!=7 and type(position[self.colonne+1][self.ligne-1])==Pion and position[self.colonne+1][self.ligne-1]._couleur=="Blanc") or (self.colonne!=0 and type(position[self.colonne-1][self.ligne-1])==Pion and position[self.colonne-1][self.ligne-1]._couleur=="Blanc") :
                print("pion")#
                return True

        #cavalier
        if (not(self.colonne - 2 < 0) and not(self.ligne + 1 > 7) and type(position[self.colonne - 2][self.ligne + 1])==Cavalier and position[self.colonne - 2][self.ligne + 1]._couleur != self._couleur) or (not(self.colonne - 2 < 0) and not(self.ligne - 1 <  0) and type(position[self.colonne - 2][self.ligne - 1]) == Cavalier and position[self.colonne - 2][self.ligne - 1]._couleur!=self._couleur) or (not(self.colonne - 1 < 0) and not(self.ligne + 2 > 7) and type(position[self.colonne - 1][self.ligne + 2])==Cavalier and position[self.colonne - 1][self.ligne + 2]._couleur!=self._couleur) or (not(self.colonne - 1 < 0) and not(self.ligne - 2 < 0) and type(position[self.colonne - 1][self.ligne - 2])==Cavalier and position[self.colonne - 1][self.ligne - 2]._couleur!=self._couleur) or (not(self.colonne + 1 > 7) and not(self.ligne + 2 > 7) and type(position[self.colonne + 1][self.ligne + 2])==Cavalier and position[self.colonne + 1][self.ligne + 2]._couleur!=self._couleur) or (not(self.colonne + 1 > 7) and not(self.ligne - 2 < 0) and type(position[self.colonne + 1][self.ligne - 2])==Cavalier and position[self.colonne + 1][self.ligne - 2]._couleur!=self._couleur) or (not(self.colonne + 2 > 7) and not(self.ligne + 1 > 7) and type(position[self.colonne + 2][self.ligne + 1])==Cavalier and position[self.colonne + 2][self.ligne + 1]._couleur!=self._couleur) or (not(self.colonne + 2 > 7) and not(self.ligne - 1 < 0) and type(position[self.colonne + 2][self.ligne - 1])==Cavalier and position[self.colonne + 2][self.ligne - 1]._couleur!=self._couleur) :
            print("cavalier") #
            return True

        #colonnes/lignes
        A=1
        a,b=True,True
        for i in range(1,max(self.colonne,7-self.colonne)+1): #lignes
            if self.colonne+i<=7 and position[self.colonne+i][self.ligne] != 0 and a:
                A=position[self.colonne+i][self.ligne]
                if (type(A)==Tour or type(A)==Dame) and A._couleur!=self._couleur:
                    print("lignes")#
                    return True
                else:
                    a=False
            if self.colonne-i>=0 and position[self.colonne-i][self.ligne] != 0 and b: 
                A= position[self.colonne-i][self.ligne]
                if (type(A)==Tour or type(A)==Dame) and A._couleur!=self._couleur:
                    print("lignes")
                    return True
                else:
                    b=False
        A=1
        c,d=True,True
        for i in range(1,max(self.ligne,7-self.ligne)+1): #colonnes
            if self.ligne+i<=7 and position[self.colonne][self.ligne+i] != 0 and c:
                A=position[self.colonne][self.ligne+i]
                if (type(A)==Tour or type(A)==Dame) and A._couleur!=self._couleur:
                    print("colonne")
                    return True
                else:
                    c=False
            if not(self.ligne-i<0) and position[self.colonne][self.ligne-i] != 0 and d:
                A=position[self.colonne][self.ligne-i]
                if (type(A)==Tour or type(A)==Dame) and A._couleur!=self._couleur:
                    print("colonne")
                    return True
                else:
                    d=False
        #Roi
        if (self.ligne+1 <= 7 and type(position[self.colonne][self.ligne+1])==Roi and position[self.colonne][self.ligne+1]._couleur!=self._couleur) or (self.ligne-1 >= 0 and type(position[self.colonne][self.ligne-1])==Roi and position[self.colonne][self.ligne-1]._couleur!=self._couleur) or (self.colonne+1 <= 7 and type(position[self.colonne+1][self.ligne])==Roi and position[self.colonne+1][self.ligne]._couleur!=self._couleur) or (self.colonne-1 >= 0 and self.ligne-1 >= 0 and type(position[self.colonne-1][self.ligne-1])==Roi and position[self.colonne-1][self.ligne-1]._couleur!=self._couleur) or (self.colonne+1 <= 7 and self.ligne+1 <= 7 and type(position[self.colonne+1][self.ligne+1])==Roi and position[self.colonne+1][self.ligne+1]._couleur!=self._couleur) or (self.colonne-1 >= 0 and self.ligne+1 <= 7 and type(position[self.colonne-1][self.ligne+1])==Roi and position[self.colonne-1][self.ligne+1]._couleur!=self._couleur) or (self.colonne-1 >= 0 and type(position[self.colonne-1][self.ligne])==Roi and position[self.colonne-1][self.ligne]._couleur!=self._couleur) or (self.colonne+1 <= 7 and self.ligne-1 >= 0 and type(position[self.colonne+1][self.ligne-1])==Roi and position[self.colonne+1][self.ligne-1]._couleur!=self._couleur):
            print("roi")
            return True

        return False
    

    def Echec_et_mat(self,nbcoup):
        from board import position,mouvement,prises_Blanc,prises_Noir
        archive_pos=position[:] #on enregistre les positions car la fonction mouvement change la liste position
        archive_prisesB=prises_Blanc[:]
        archive_prisesN=prises_Noir[:]
        ligne=self.ligne
        colonne=self.colonne
        for colonne in position: #on regarde chaque piece encore sur le plateau, pour cela on parcours la liste position
            for piece in colonne:
                if piece!=0 and piece._couleur == self._couleur: #si on trouve une piece de notre couleur, alors on essaye de la bouger
                    if type(piece)==Roi:
                        L=[[colonne,ligne+1],[colonne,ligne-1],[colonne+1,ligne],[colonne-1,ligne-1],[colonne+1,ligne+1],[colonne-1,ligne+1],[colonne-1,ligne],[colonne+1,ligne-1]]
                        for case in L: #on teste tous les mouvements possibles du roi
                            a=0 
                            if case[0]<=7 and case[0]>=0 and case[1]<=7 and case[1]>=0: #si on reste dans l'échiquier
                                if position[case[0]][case[1]]!=0: #s'il y a une piece sur la case d'arrivée
                                    a=1
                                    mangee=position[case[0]][case[1]] #on garde tout en mémoire pour annuler le mouvement
                                    #coordL=mangee.ligne
                                    #coordC=mangee.colonne
                                #print(piece,case,self._couleur,self.Echec2(),mouvement(piece,case,self._couleur,"",nbcoup)[0])
                                if mouvement(piece,case,self._couleur,"",nbcoup)[0] : #si le mouvement est possible, pas mat
                                    position=archive_pos[:] #annule le mouvement
                                    self.ligne=ligne
                                    self.colonne=colonne
                                    if a==1:
                                        position[case[0]][case[1]]=mangee #on annule le mouvement
                                        prises_Blanc=archive_prisesB[:]
                                        prises_Noir=archive_prisesN[:]
                                        mangee.ligne=case[1]
                                        mangee.colonne=case[0]
                                        #position[case[0]][case[1]].ligne=coordL
                                        #position[case[0]][case[1]].colonne=coordC
                                    return False
                                position=archive_pos[:] #annule le mouvement
                                self.ligne=ligne
                                self.colonne=colonne
                                if a==1:
                                    position[case[0]][case[1]]=mangee
                                    mangee.ligne=case[1]
                                    mangee.colonne=case[0]
                                    prises_Blanc=archive_prisesB[:]
                                    prises_Noir=archive_prisesN[:]

                    elif type(piece)==Pion:
                        if piece._couleur=="Blanc":
                            L=[[colonne,ligne + 1],[colonne - 1,ligne + 1],[colonne + 1,ligne + 1]]
                            for case in L:
                                a=0
                                if case[0]<=7 and case[0]>=0 and case[1]<=7 and case[1]>=0:
                                    if position[case[0]][case[1]]!=0:
                                        a=1
                                        mangee=position[case[0]][case[1]]
                                        #coordL=position[case[0]][case[1]].ligne
                                        #coordC=position[case[0]][case[1]].colonne
                                    if mouvement(piece,case,self._couleur,"",nbcoup)[0] : #si mouvement possible, pas mat
                                        position=archive_pos[:]
                                        prises_Blanc=archive_prisesB[:]
                                        prises_Noir=archive_prisesN[:]
                                        self.ligne=ligne
                                        self.colonne=colonne
                                        if a==1:
                                            position[case[0]][case[1]]=mangee
                                            mangee.ligne=case[1]
                                            mangee.colonne=case[0]
                                        return False
                                    position=archive_pos[:]
                                    prises_Blanc=archive_prisesB[:]
                                    prises_Noir=archive_prisesN[:]
                                    self.ligne=ligne
                                    self.colonne=colonne
                                    if a==1:
                                        position[case[0]][case[1]]=mangee
                                        mangee.ligne=case[1]
                                        mangee.colonne=case[0]
                        if piece._couleur=="Noir":
                            L=[[colonne,ligne - 1],[colonne - 1,ligne - 1],[colonne + 1,ligne - 1]]                    
                            for case in L:
                                a=0
                                if case[0]<=7 and case[0]>=0 and case[1]<=7 and case[1]>=0:
                                    if position[case[0]][case[1]]!=0:
                                        a=1
                                        mangee=position[case[0]][case[1]]
                                    if mouvement(piece,case,self._couleur,"",nbcoup)[0] : #si mouvement possible, pas mat
                                        position=archive_pos[:] #on 
                                        prises_Blanc=archive_prisesB[:]
                                        prises_Noir=archive_prisesN[:]
                                        self.ligne=ligne
                                        self.colonne=colonne
                                        if a==1:
                                            position[case[0]][case[1]]=mangee
                                            mangee.ligne=case[1]
                                            mangee.colonne=case[0]
                                        return False
                                    position=archive_pos[:]
                                    prises_Blanc=archive_prisesB[:]
                                    prises_Noir=archive_prisesN[:]
                                    self.ligne=ligne
                                    self.colonne=colonne
                                    if a==1:
                                        position[case[0]][case[1]]=mangee
                                        mangee.ligne=case[1]
                                        mangee.colonne=case[0]

                    elif type(piece)==Cavalier:
                        L=[[colonne - 2,ligne + 1],[colonne - 2,ligne - 1],[colonne - 1,ligne + 2],[colonne - 1,ligne - 2],[colonne + 1,ligne + 2],[colonne + 1,ligne - 2],[colonne + 2,ligne + 1],[colonne + 2,ligne + 1],[colonne + 2,ligne - 1]]
                        for case in L:
                            a=0
                            if case[0]<=7 and case[0]>=0 and case[1]<=7 and case[1]>=0:
                                if position[case[0]][case[1]]!=0:
                                    a=1
                                    mangee=position[case[0]][case[1]]
                                if mouvement(piece,case,self._couleur,"",nbcoup)[0] : #si mouvement possible, pas mat
                                    position=archive_pos[:]
                                    prises_Blanc=archive_prisesB[:]
                                    prises_Noir=archive_prisesN[:]
                                    self.ligne=ligne
                                    self.colonne=colonne
                                    if a==1:
                                        position[case[0]][case[1]]=mangee
                                        mangee.ligne=case[1]
                                        mangee.colonne=case[0]
                                    return False
                                position=archive_pos[:]
                                prises_Blanc=archive_prisesB[:]
                                prises_Noir=archive_prisesN[:]
                                self.ligne=ligne
                                self.colonne=colonne
                                if a==1:
                                    position[case[0]][case[1]]=mangee
                                    mangee.ligne=case[1]
                                    mangee.colonne=case[0]

                    if type(piece)==Fou or type(piece)==Dame:
                        A=1
                        for i in range(1,max(colonne,7-colonne)+1):
                            L=[[colonne+i,ligne+i],[colonne-i,ligne-i],[colonne+i,ligne-i],[colonne-i,ligne+i]]
                            for case in L:
                                a=0
                                if case[0]<=7 and case[0]>=0 and case[1]<=7 and case[1]>=0:
                                    if position[case[0]][case[1]]!=0:
                                        a=1
                                        mangee=position[case[0]][case[1]]
                                    if mouvement(piece,case,self._couleur,"",nbcoup)[0] : #si mouvement possible, pas mat
                                        position=archive_pos[:]
                                        prises_Blanc=archive_prisesB[:]
                                        prises_Noir=archive_prisesN[:]
                                        self.ligne=ligne
                                        self.colonne=colonne
                                        if a==1:
                                            position[case[0]][case[1]]=mangee
                                            mangee.ligne=case[1]
                                            mangee.colonne=case[0]
                                        return False
                                    position=archive_pos[:]
                                    prises_Blanc=archive_prisesB[:]
                                    prises_Noir=archive_prisesN[:]
                                    self.ligne=ligne
                                    self.colonne=colonne
                                    if a==1:
                                        position[case[0]][case[1]]=mangee
                                        mangee.ligne=case[1]
                                        mangee.colonne=case[0]
                    
                    if type(piece)==Tour or type(piece)==Dame:
                        for i in range(1,max(colonne,7-colonne)+1): #colonnes
                            L=[[colonne+i,ligne],[colonne-i,ligne]]
                            for case in L:
                                a=0
                                if case[0]<=7 and case[0]>=0 and case[1]<=7 and case[1]>=0:
                                    if position[case[0]][case[1]]!=0:
                                        a=1
                                        mangee=position[case[0]][case[1]]
                                    if mouvement(piece,case,self._couleur,"",nbcoup)[0] : #and not(self.Echec2())
                                        position=archive_pos[:]
                                        prises_Blanc=archive_prisesB[:]
                                        prises_Noir=archive_prisesN[:]
                                        self.ligne=ligne
                                        self.colonne=colonne
                                        if a==1:
                                            position[case[0]][case[1]]=mangee
                                            mangee.ligne=case[1]
                                            mangee.colonne=case[0]
                                        return False
                                    position=archive_pos[:]
                                    prises_Blanc=archive_prisesB[:]
                                    prises_Noir=archive_prisesN[:]
                                    self.ligne=ligne
                                    self.colonne=colonne
                                    if a==1:
                                        position[case[0]][case[1]]=mangee
                                        mangee.ligne=case[1]
                                        mangee.colonne=case[0]
                        for i in range(1,max(ligne,7-ligne)+1): #lignes
                            L=[[colonne,ligne+i],[colonne,ligne-i]]
                            for case in L:
                                a=0
                                if case[0]<=7 and case[0]>=0 and case[1]<=7 and case[1]>=0:
                                    if position[case[0]][case[1]]!=0:
                                        a=1
                                        mangee=position[case[0]][case[1]]
                                    if mouvement(piece,case,self._couleur,"",nbcoup)[0] : #si mouvement possible, pas mat
                                        position=archive_pos[:]
                                        prises_Blanc=archive_prisesB[:]
                                        prises_Noir=archive_prisesN[:]
                                        self.ligne=ligne
                                        self.colonne=colonne
                                        if a==1:
                                            position[case[0]][case[1]]=mangee
                                            mangee.ligne=case[1]
                                            mangee.colonne=case[0]
                                        return False
                                    position=archive_pos[:]
                                    prises_Blanc=archive_prisesB[:]
                                    prises_Noir=archive_prisesN[:]
                                    self.ligne=ligne
                                    self.colonne=colonne
                                    if a==1:
                                        position[case[0]][case[1]]=mangee
                                        mangee.ligne=case[1]
                                        mangee.colonne=case[0]
        return True

        
        
def promoDameB(piece):
    from board import position
    cpt=0
    for colonne in position:
        for p in colonne:
            if type(p)==Dame and p._couleur=="Blanc":
                cpt+=1

    position[piece.colonne][piece.ligne]=Dame("Blanc",piece.colonne,piece.ligne,cpt+1)
    piece.colonne=-3
    piece.ligne=-3


def promoTourB(piece):
    from board import position
    cpt=0
    for colonne in position:
        for p in colonne:
            if type(p)==Tour and p._couleur=="Blanc":
                cpt+=1

    position[piece.colonne][piece.ligne]=Tour("Blanc",piece.colonne,piece.ligne,cpt+1,True)
    piece.colonne=-3
    piece.ligne=-3
    
def promoFouB(piece):
    from board import position
    cpt=0
    for colonne in position:
        for p in colonne:
            if type(p)==Fou and p._couleur=="Blanc":
                cpt+=1

    position[piece.colonne][piece.ligne]=Fou("Blanc",piece.colonne,piece.ligne,cpt+1)
    piece.colonne=-3
    piece.ligne=-3

def promoCavalierB(piece):
    from board import position
    cpt=0
    for colonne in position:
        for p in colonne:
            if type(p)==Cavalier and p._couleur=="Blanc":
                cpt+=1

    position[piece.colonne][piece.ligne]=Cavalier("Blanc",piece.colonne,piece.ligne,cpt+1)
    piece.colonne=-3
    piece.ligne=-3


def promoDameN(piece):
    from board import position
    cpt=0
    for colonne in position:
        for p in colonne:
            if type(p)==Dame and p._couleur=="Noir":
                cpt+=1

    position[piece.colonne][piece.ligne]=Dame("Noir",piece.colonne,piece.ligne,cpt+1)
    piece.colonne=-3
    piece.ligne=-3

def promoTourN(piece):
    from board import position
    cpt=0
    for colonne in position:
        for p in colonne:
            if type(p)==Tour and p._couleur=="Noir":
                cpt+=1

    position[piece.colonne][piece.ligne]=Tour("Noir",piece.colonne,piece.ligne,cpt+1,True)
    piece.colonne=-3
    piece.ligne=-3
    
def promoFouN(piece):
    from board import position
    cpt=0
    for colonne in position:
        for p in colonne:
            if type(p)==Fou and p._couleur=="Noir":
                cpt+=1

    position[piece.colonne][piece.ligne]=Fou("Noir",piece.colonne,piece.ligne,cpt+1)
    piece.colonne=-3
    piece.ligne=-3

def promoCavalierN(piece):
    from board import position
    cpt=0
    for colonne in position:
        for p in colonne:
            if type(p)==Cavalier and p._couleur=="Noir":
                cpt+=1

  
    position[piece.colonne][piece.ligne]=Cavalier("Noir",piece.colonne,piece.ligne,cpt+1)
    piece.colonne=-3
    piece.ligne=-3





# pour chaque pièce :
# def mouvementpossible (self,case) :
# if dans les règles (pas de sortie de l'échiqiuer, bonne forme de déplacement, pas d'autre pièce sur le chemin):
# return True
# elif piece ne bouge pas:
# return True
# else:
# return False
