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
            k = abs(colonne-self.colonne)

            if k != abs(ligne-self.ligne):
                return False #pas le bon motif de déplacement
            
            elif (colonne == self.colonne + k and ligne == self.ligne + k):  # si le fou bouge sur la diagonale de bas gauche à haut droit (/)
                for i in range(1, k):
                        if position[self.colonne + i][self.ligne + i] != 0:  # s'il y a une autre piece en travers du chemin
                            return False

            elif (colonne == self.colonne - k and ligne == self.ligne - k):  # si le fou bouge sur la diagonale de haut droite à bas gauche (/)
                for i in range(1, k):
                    if position[self.colonne - i][self.ligne - i] != 0:  # s'il y a une autre piece en travers du chemin
                        return False

            elif (colonne == self.colonne - k and ligne == self.ligne + k):  # si le fou bouge sur la diagonale de bas droit à haut gauche (\)
                for i in range(1, k):
                    if position[self.colonne - i][self.ligne + i] != 0:  # s'il y a une autre piece en travers du chemin
                        return False

            else:  # si le fou bouge sur la diagonale de haut gauche à bas droit (\)
                for i in range(1, k):
                    if position[self.colonne + i][self.ligne - i] != 0:  # s'il y a une autre piece en travers du chemin
                        return False   
        
        return True




class Tour(Piece):

    def __init__(self, couleur, colonne, ligne, numero,Move1=False):
        super().__init__(couleur, colonne, ligne, numero)
        self._valeur = 5
        self.Move1 = Move1  # indique si la tour a déjà bougé (utile pour le roque)


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
            if Fou(self._couleur, self.colonne, self.ligne, self._numero).mouvement_possible(colonne,ligne) or Tour(self._couleur, self.colonne, self.ligne, self._numero).mouvement_possible(colonne,ligne): #peut bouger comme le fou et la tour
                return True
            else :
                return False




class Cavalier(Piece):

    def __init__(self, couleur, colonne, ligne, numero):
        super().__init__(couleur, colonne, ligne, numero)
        self._valeur = 3

    def mouvement_possible(self, colonne, ligne):  # indique si le cavalier peut bouger jusqu'à la case indiquée
        # liste des cases d'arrivée possibles (y compris la case de départ) :
        L = [[self.colonne - 2,self.ligne + 1], [self.colonne - 2, self.ligne - 1],[self.colonne - 1, self.ligne + 2], [self.colonne - 1, self.ligne - 2], [self.colonne + 1, self.ligne + 2], [self.colonne + 1, self.ligne - 2], [self.colonne + 2, self.ligne + 1], [self.colonne + 2, self.ligne - 1], [self.colonne, self.ligne]]
        if [colonne, ligne] in L and (ligne <= 7 and ligne >= 0 and colonne <= 7 and colonne >= 0):  # bon déplacement et reste dans l'échiquier
            return True
        else:
            return False




class Pion(Piece):

    def __init__(self, couleur, colonne, ligne, numero):
        super().__init__(couleur, colonne, ligne, numero)
        self._valeur = 1
        self._condition2 = 5  # sert à la prise en passant (vérifie que le pion a bougé de 2 cases au bon endroit)

    def mouvement_possible(self, colonne, ligne):  # indique si le pion peut bouger jusqu'à la case indiquée
        from board import position

        if ligne > 7 or colonne > 7 or ligne < 0 or colonne < 0:  # pas le bon "motif" de déplacement ou sortie de l'échiquier
            return (False, 0)

        elif colonne == self.colonne and ligne == self.ligne:  # si le pion ne bouge pas
            return (True, "statique")

        elif colonne != self.colonne and ligne == self.ligne: # mouvement horizontal
            return (False, 0)

        else:

            if colonne == self.colonne:  # mouvement vertical

                if ligne == (self.ligne + 1) and self._couleur == "Blanc":
                    if position[colonne][ligne] == 0:  # s'il n'y a pas de piece sur la case d'arrivée
                        return (True, "tout_droit")
                    else:
                        return (False, 0)

                elif self.ligne == 1 and ligne == 3 and self._couleur == "Blanc":  # premier mouvement du pion
                    if position[colonne][ligne - 1] == 0 and position[colonne][ligne] == 0:  # s'il n'y a pas de piece sur la case d'arrivée
                        return (True, "tout_droit_2")
                    else:
                        return (False, 0)

                elif ligne == (self.ligne - 1) and self._couleur == "Noir":
                    if position[colonne][ligne] == 0:  # s'il n'y a pas de piece sur la case d'arrivée
                        return (True, "tout_droit")
                    else:
                        return (False, 0)

                elif ligne == 4 and self.ligne == 6 and self._couleur == "Noir":  # premier mouvement du pion
                    if position[colonne][ligne + 1] == 0 and position[colonne][ligne] == 0:  # s'il n'y a pas de piece sur la case d'arrivée
                        return (True, "tout_droit_2")
                    else:
                        return (False, 0)

                else:
                    return (False, 0)

            elif colonne == (self.colonne + 1) or colonne == (self.colonne - 1):  # mouvement diagonal
                if (ligne == (self.ligne + 1) and self._couleur == "Blanc") or (ligne == (self.ligne - 1) and self._couleur == "Noir"):
                    return (True, "diagonale")
                else:
                    return (False, 0)

            else:
                return (False, 0)






class Roi(Fou,Tour):


    def __init__(self, couleur, colonne, ligne, numero, echec=False):
        super().__init__(couleur, colonne, ligne, numero)
        self._valeur = 0
        self.echec = echec
        self.Move1 = False  # sert à savoir si le roi a déjà bougé (utile pour roque)


    def mouvement_possible(self,colonne,ligne):
            if (Fou(self._couleur, self.colonne, self.ligne, self._numero).mouvement_possible(colonne,ligne) or Tour(self._couleur, self.colonne, self.ligne, self._numero).mouvement_possible(colonne,ligne)) and (abs(ligne-self.ligne<=1) and abs(colonne-self.colonne<=1)):
                return True
            else:
                return False


    # Fonctions pour l'échec et l'échec et mat

    def Echec1(self):  # complexité très élevée
        from board import position
        for c in position:
            for piece in c:
                if piece !=0 and piece._couleur == self._couleur and piece.mouvement_possible(self.colonne,self.ligne):
                    return True
        return False
    

    def Echec2(self):  # meilleure complexité
        from board import position

        # Pièce qui bouge en diagonale : Dame ou Fou

        A=1
        a, b, c, d = True, True, True, True

        for i in range(1, min(max(self.colonne, 7-self.colonne), max(self.ligne, 7-self.ligne))+1):

            if not(self.colonne+i > 7) and not(self.ligne+i > 7) and position[self.colonne+i][self.ligne+i] != 0 and a:
                A = position[self.colonne+i][self.ligne+i]
                if (type(A) == Fou or type(A) == Dame) and A._couleur != self._couleur:
                    self.echec = True
                    return True
                else:
                    a = False

            if not(self.ligne-i < 0) and not(self.colonne-i < 0) and position[self.colonne-i][self.ligne-i] != 0 and b:
                A = position[self.colonne-i][self.ligne-i]
                if (type(A)==Fou or type(A) == Dame) and A._couleur != self._couleur:
                    self.echec = True
                    return True
                else:
                    b = False

            if self.colonne+i <= 7 and self.ligne-i >= 0 and position[self.colonne+i][self.ligne-i] != 0 and c:
                A = position[self.colonne+i][self.ligne-i]
                if (type(A) == Fou or type(A) == Dame) and A._couleur != self._couleur:
                    self.echec = True
                    return True
                else:
                    c = False

            if not(self.colonne-i < 0) and not(self.ligne+i > 7) and position[self.colonne-i][self.ligne+i] != 0 and d:
                A = position[self.colonne-i][self.ligne+i]
                if (type(A) == Fou or type(A) == Dame) and A._couleur != self._couleur:
                    self.echec = True
                    return True
                else:
                    d = False


        # Pion

        if self._couleur == "Blanc" and self.ligne != 7:
            if (self.colonne != 7 and type(position[self.colonne+1][self.ligne+1]) == Pion and position[self.colonne+1][self.ligne+1]._couleur == "Noir") or (self.colonne != 0 and type(position[self.colonne-1][self.ligne+1]) == Pion and position[self.colonne-1][self.ligne+1]._couleur == "Noir"):
                return True

        elif self._couleur=="Noir" and self.ligne!=0:
            if (self.colonne != 7 and type(position[self.colonne+1][self.ligne-1]) == Pion and position[self.colonne+1][self.ligne-1]._couleur == "Blanc") or (self.colonne != 0 and type(position[self.colonne-1][self.ligne-1]) == Pion and position[self.colonne-1][self.ligne-1]._couleur == "Blanc"):
                return True


        # Cavalier

        L = [[self.colonne - 2,self.ligne + 1],[self.colonne - 2,self.ligne - 1],[self.colonne - 1,self.ligne + 2],[self.colonne - 1,self.ligne - 2],[self.colonne + 1,self.ligne + 2],[self.colonne + 1,self.ligne - 2],[self.colonne + 2,self.ligne + 1],[self.colonne + 2,self.ligne - 1]]
        for case in L:
            if case[0] >= 0 and case[0] <= 7 and case[1] >= 0 and case[1] <= 7 and type(position[case[0]][case[1]]) == Cavalier and position[case[0]][case[1]]._couleur != self._couleur:
                return True


        # Pièces qui bouge à l'horizontale ou à la verticale : Dame ou Tour

            # Mouvement horizontal :
        A = 1
        a, b = True, True

        for i in range(1, max(self.colonne, 7-self.colonne)+1):

            if self.colonne+i <= 7 and position[self.colonne+i][self.ligne] != 0 and a:
                A = position[self.colonne+i][self.ligne]
                if (type(A) == Tour or type(A) == Dame) and A._couleur != self._couleur:
                    return True
                else:
                    a = False

            if self.colonne-i >= 0 and position[self.colonne-i][self.ligne] != 0 and b:
                A = position[self.colonne-i][self.ligne]
                if (type(A) == Tour or type(A) == Dame) and A._couleur != self._couleur:
                    return True
                else:
                    b = False


            # Mouvement vertical :
        A = 1
        c, d = True, True
        for i in range(1, max(self.ligne, 7-self.ligne)+1):

            if self.ligne+i <= 7 and position[self.colonne][self.ligne+i] != 0 and c:
                A = position[self.colonne][self.ligne+i]
                if (type(A) == Tour or type(A) == Dame) and A._couleur != self._couleur:
                    return True
                else:
                    c = False

            if not(self.ligne-i < 0) and position[self.colonne][self.ligne-i] != 0 and d:
                A = position[self.colonne][self.ligne-i]
                if (type(A) == Tour or type(A)==Dame) and A._couleur!=self._couleur:
                    return True
                else:
                    d = False


        # Roi

        L = [[self.colonne,self.ligne+1],[self.colonne,self.ligne-1],[self.colonne+1,self.ligne],[self.colonne-1,self.ligne-1],[self.colonne+1,self.ligne+1],[self.colonne-1,self.ligne+1],[self.colonne-1,self.ligne],[self.colonne+1,self.ligne-1]]
        for case in L:
            if case[0] >= 0 and case[0] <= 7 and case[1] >= 0 and case[1] <= 7 and type(position[case[0]][case[1]]) == Roi and position[case[0]][case[1]]._couleur != self._couleur:
                return True

        return False
    



    def test_echec_mat_pas_bloque(self,piece,colonne,ligne,case,nbcoup):
        from board import position,mouvement,prises_Blanc,prises_Noir
        a = 0
        if case[0] <= 7 and case[0] >= 0 and case[1] <= 7 and case[1] >= 0:  # si on reste dans l'échiquier

            if position[case[0]][case[1]]!=0:  # s'il y a une piece sur la case d'arrivée
                a = 1
                mangee=position[case[0]][case[1]]  # on garde tout en mémoire pour annuler le mouvement
            
            if mouvement(piece, case, self._couleur, "", nbcoup)[0] :  # si le mouvement est possible, pas mat
                piece.ligne = ligne
                piece.colonne = colonne
                position[colonne][ligne] = piece
                position[case[0]][case[1]] = 0
                
                if a == 1:
                    mangee.ligne = case[1]
                    mangee.colonne = case[0]
                    position[case[0]][case[1]] = mangee
                    if self._couleur == "Blanc":
                        prises_Blanc.pop()
                    else:
                        prises_Noir.pop()

                return False
        return True



    def test_echec_mat_bloque(self,piece,colonne,ligne,case,nbcoup):
        from board import position,mouvement,prises_Blanc,prises_Noir
        a = 0
        if case[0] <= 7 and case[0] >= 0 and case[1] <= 7 and case[1] >= 0:
            
            if position[case[0]][case[1]]!=0:
                a = 1
                mangee = position[case[0]][case[1]]
            
            if mouvement(piece, case, self._couleur, "", nbcoup)[0] :  # si mouvement possible, pas mat
                self.ligne = ligne
                self.colonne = colonne
                position[colonne][ligne] = piece
                position[case[0]][case[1]] = 0

                if a == 1:
                    position[case[0]][case[1]] = mangee
                    mangee.ligne = case[1]
                    mangee.colonne = case[0]
                    if self._couleur == "Blanc":
                        prises_Blanc.pop()
                    else:
                        prises_Noir.pop()
                return False,False    

            if a==1: #si une piece sur le chemin, on arrête la boucle
                return(False,True)  

        return True,False



    def Echec_et_mat(self,nbcoup):
        from board import position, prises_Blanc, prises_Noir

        for c in position:  # on regarde chaque piece encore sur le plateau, pour cela on parcours la liste position
            for piece in c:
                if piece != 0 and piece._couleur == self._couleur:  # si on trouve une piece de notre couleur, alors on essaye de la bouger
                    ligne = piece.ligne
                    colonne = piece.colonne

                    if type(piece) == Roi:

                        L = [[colonne,ligne+1],[colonne,ligne-1],[colonne+1,ligne],[colonne-1,ligne-1],[colonne+1,ligne+1],[colonne-1,ligne+1],[colonne-1,ligne],[colonne+1,ligne-1]]
                        for case in L: #on teste tous les mouvements possibles du roi
                            
                            if not(self.test_echec_mat_pas_bloque(piece,colonne,ligne,case,nbcoup)):
                                return False

                    elif type(piece) == Pion:

                        if piece._couleur == "Blanc":

                            L = [[colonne,ligne + 1],[colonne - 1,ligne + 1],[colonne + 1,ligne + 1]]
                            for case in L:
                                if not(self.test_echec_mat_pas_bloque(piece,colonne,ligne,case,nbcoup)):
                                    return False
                                    

                        if piece._couleur=="Noir":

                            L = [[colonne,ligne - 1],[colonne - 1,ligne - 1],[colonne + 1,ligne - 1]]
                            for case in L:
                                if not(self.test_echec_mat_pas_bloque(piece,colonne,ligne,case,nbcoup)):
                                    return False
                                    

                    elif type(piece) == Cavalier:

                        L = [[colonne - 2,ligne + 1],[colonne - 2,ligne - 1],[colonne - 1,ligne + 2],[colonne - 1,ligne - 2],[colonne + 1,ligne + 2],[colonne + 1,ligne - 2],[colonne + 2,ligne + 1],[colonne + 2,ligne + 1],[colonne + 2,ligne - 1]]
                        for case in L:
                            if not(self.test_echec_mat_pas_bloque(piece,colonne,ligne,case,nbcoup)):
                                return False


                    if type(piece) == Fou or type(piece) == Dame:
                        for i in range(1, max(colonne, 7-colonne)+1):
                            if not(self.test_echec_mat_bloque(piece,colonne,ligne,[colonne+i,ligne+i],nbcoup)[0]):
                                return False
                            if self.test_echec_mat_bloque(piece,colonne,ligne,[colonne+i,ligne+i],nbcoup)[1]:
                                break

                        for i in range(1, max(colonne, 7-colonne)+1):
                            if not(self.test_echec_mat_bloque(piece,colonne,ligne,[colonne-i,ligne-i],nbcoup)):
                                return False
                            if self.test_echec_mat_bloque(piece,colonne,ligne,[colonne+i,ligne+i],nbcoup)[1]:
                                break
                        
                        for i in range(1, max(colonne, 7-colonne)+1):
                            if not(self.test_echec_mat_bloque(piece,colonne,ligne,[colonne+i,ligne-i],nbcoup)):
                                return False
                            if self.test_echec_mat_bloque(piece,colonne,ligne,[colonne+i,ligne+i],nbcoup)[1]:
                                break
                        
                        for i in range(1, max(colonne, 7-colonne)+1):
                            if not(self.test_echec_mat_bloque(piece,colonne,ligne,[colonne-i,ligne+i],nbcoup)):
                                return False
                            if self.test_echec_mat_bloque(piece,colonne,ligne,[colonne+i,ligne+i],nbcoup)[1]:
                                break
                        
                    
                    if type(piece) == Tour or type(piece) == Dame:
                        
                        # Mouvement horizontal
                        for i in range(1,max(colonne,7-colonne)+1):
                            if not(self.test_echec_mat_bloque(piece,colonne,ligne,[colonne+i,ligne],nbcoup)):
                                return False
                            if self.test_echec_mat_bloque(piece,colonne,ligne,[colonne+i,ligne+i],nbcoup)[1]:
                                break

                        for i in range(1,max(colonne,7-colonne)+1):
                            if not(self.test_echec_mat_bloque(piece,colonne,ligne,[colonne-i,ligne],nbcoup)):
                                return False
                            if self.test_echec_mat_bloque(piece,colonne,ligne,[colonne+i,ligne+i],nbcoup)[1]:
                                break
                            
                                    
                        # Mouvement vertical

                        for i in range(1, max(ligne, 7-ligne)+1):
                            if not(self.test_echec_mat_bloque(piece,colonne,ligne,[colonne,ligne+i],nbcoup)):
                                return False
                            if self.test_echec_mat_bloque(piece,colonne,ligne,[colonne+i,ligne+i],nbcoup)[1]:
                                break

                        for i in range(1, max(ligne, 7-ligne)+1):
                            if not(self.test_echec_mat_bloque(piece,colonne,ligne,[colonne,ligne-i],nbcoup)):
                                return False
                            if self.test_echec_mat_bloque(piece,colonne,ligne,[colonne+i,ligne+i],nbcoup)[1]:
                                break  
                                    
        return True







    def Echec_et_mat1(self, nbcoup):
        from board import position, mouvement, prises_Blanc, prises_Noir 

        for c in position:  # on regarde chaque piece encore sur le plateau, pour cela on parcours la liste position
            for piece in c:
                if piece != 0 and piece._couleur == self._couleur:  # si on trouve une piece de notre couleur, alors on essaye de la bouger
                    ligne = piece.ligne
                    colonne = piece.colonne

                    if type(piece) == Roi:

                        L = [[colonne,ligne+1],[colonne,ligne-1],[colonne+1,ligne],[colonne-1,ligne-1],[colonne+1,ligne+1],[colonne-1,ligne+1],[colonne-1,ligne],[colonne+1,ligne-1]]
                        for case in L: #on teste tous les mouvements possibles du roi
                            
                            a = 0
                            if case[0] <= 7 and case[0] >= 0 and case[1] <= 7 and case[1] >= 0:  # si on reste dans l'échiquier

                                if position[case[0]][case[1]]!=0:  # s'il y a une piece sur la case d'arrivée
                                    a = 1
                                    mangee=position[case[0]][case[1]]  # on garde tout en mémoire pour annuler le mouvement
                                
                                if mouvement(piece, case, self._couleur, "", nbcoup)[0] :  # si le mouvement est possible, pas mat
                                    piece.ligne = ligne
                                    piece.colonne = colonne
                                    position[colonne][ligne] = piece
                                    position[case[0]][case[1]] = 0
                                    
                                    if a == 1:
                                        mangee.ligne = case[1]
                                        mangee.colonne = case[0]
                                        position[case[0]][case[1]] = mangee
                                        if self._couleur == "Blanc":
                                            prises_Blanc.pop()
                                        else:
                                            prises_Noir.pop()

                                    return False
                                

                    elif type(piece) == Pion:

                        if piece._couleur == "Blanc":

                            L = [[colonne,ligne + 1],[colonne - 1,ligne + 1],[colonne + 1,ligne + 1]]
                            for case in L:
                                a = 0

                                if case[0] <= 7 and case[0] >= 0 and case[1] <= 7 and case[1] >= 0:
                                    if position[case[0]][case[1]] != 0:
                                        a = 1
                                        mangee = position[case[0]][case[1]]
                                        
                                    if mouvement(piece, case, self._couleur, "", nbcoup)[0] :  # si mouvement possible, pas mat
                                        piece.ligne = ligne
                                        piece.colonne = colonne
                                        position[colonne][ligne] = piece
                                        position[case[0]][case[1]] = 0
                                        
                                        if a == 1:
                                            position[case[0]][case[1]] = mangee
                                            mangee.ligne = case[1]
                                            mangee.colonne = case[0]
                                            prises_Blanc.pop()

                                        return False
                                    

                        if piece._couleur=="Noir":

                            L = [[colonne,ligne - 1],[colonne - 1,ligne - 1],[colonne + 1,ligne - 1]]
                            for case in L:
                                a = 0

                                if case[0] <= 7 and case[0] >= 0 and case[1] <= 7 and case[1] >= 0:
                                    if position[case[0]][case[1]] != 0:
                                        a = 1
                                        mangee = position[case[0]][case[1]]

                                    if mouvement(piece, case, self._couleur, "", nbcoup)[0] :  # si mouvement possible, pas mat
                                        piece.ligne = ligne
                                        piece.colonne = colonne
                                        position[colonne][ligne] = piece
                                        position[case[0]][case[1]] = 0


                                        if a == 1:
                                            position[case[0]][case[1]] = mangee
                                            mangee.ligne = case[1]
                                            mangee.colonne = case[0]
                                            prises_Noir.pop()
                                        return False
                                    

                    elif type(piece) == Cavalier:

                        L = [[colonne - 2,ligne + 1],[colonne - 2,ligne - 1],[colonne - 1,ligne + 2],[colonne - 1,ligne - 2],[colonne + 1,ligne + 2],[colonne + 1,ligne - 2],[colonne + 2,ligne + 1],[colonne + 2,ligne + 1],[colonne + 2,ligne - 1]]
                        for case in L:
                            
                            a = 0
                            if case[0] <= 7 and case[0] >= 0 and case[1] <= 7 and case[1] >= 0:

                                if position[case[0]][case[1]] != 0:
                                    a = 1
                                    mangee = position[case[0]][case[1]]

                                if mouvement(piece, case, self._couleur, "", nbcoup)[0] :  # si mouvement possible, pas mat
                                    piece.ligne = ligne
                                    piece.colonne = colonne
                                    position[colonne][ligne] = piece
                                    position[case[0]][case[1]] = 0
                                    
                                    if a == 1:
                                        position[case[0]][case[1]] = mangee
                                        mangee.ligne = case[1]
                                        mangee.colonne = case[0]
                                        if self._couleur == "Blanc":
                                            prises_Blanc.pop()
                                        else:
                                            prises_Noir.pop()
                                    return False


                    if type(piece) == Fou or type(piece) == Dame:
                        
                        for i in range(1, max(colonne, 7-colonne)+1):
                            L = [[colonne+i,ligne+i],[colonne-i,ligne-i],[colonne+i,ligne-i],[colonne-i,ligne+i]]
                            
                            for case in L:
                                a = 0
                                if case[0] <= 7 and case[0] >= 0 and case[1] <= 7 and case[1] >= 0:
                                    
                                    if position[case[0]][case[1]]!=0:
                                        a = 1
                                        mangee = position[case[0]][case[1]]
                                    
                                    if mouvement(piece, case, self._couleur, "", nbcoup)[0] :  # si mouvement possible, pas mat
                                        self.ligne = ligne
                                        self.colonne = colonne
                                        position[colonne][ligne] = piece
                                        position[case[0]][case[1]] = 0

                                        if a == 1:
                                            position[case[0]][case[1]] = mangee
                                            mangee.ligne = case[1]
                                            mangee.colonne = case[0]
                                            if self._couleur == "Blanc":
                                                prises_Blanc.pop()
                                            else:
                                                prises_Noir.pop()
                                        return False      
                    
                    
                    if type(piece) == Tour or type(piece) == Dame:
                        
                        # Mouvement horizontal

                        for i in range(1,max(colonne,7-colonne)+1):
                            L = [[colonne+i,ligne],[colonne-i,ligne]]
                            
                            for case in L:
                                a = 0
                                if case[0] <= 7 and case[0] >= 0 and case[1] <= 7 and case[1] >= 0:
                                    
                                    if position[case[0]][case[1]] != 0:
                                        a = 1
                                        mangee = position[case[0]][case[1]]
                                    
                                    if mouvement(piece, case, self._couleur, "", nbcoup)[0] :
                                        piece.ligne=ligne
                                        piece.colonne=colonne
                                        position[colonne][ligne]=piece
                                        position[case[0]][case[1]]=0

                                        if a == 1:
                                            position[case[0]][case[1]] = mangee
                                            mangee.ligne = case[1]
                                            mangee.colonne = case[0]
                                            if self._couleur == "Blanc":
                                                prises_Blanc.pop()
                                            else:
                                                prises_Noir.pop()
                                        return False
                                    
                        # Mouvement vertical

                        for i in range(1, max(ligne, 7-ligne)+1):
                            L = [[colonne,ligne+i],[colonne,ligne-i]]
                            
                            for case in L:
                                a = 0
                                if case[0] <= 7 and case[0] >= 0 and case[1] <= 7 and case[1] >= 0:
                                   
                                    if position[case[0]][case[1]] != 0:
                                        a = 1
                                        mangee = position[case[0]][case[1]]
                                    
                                    if mouvement(piece, case, self._couleur, "", nbcoup)[0] :  # si mouvement possible, pas mat
                                        piece.ligne = ligne
                                        piece.colonne = colonne
                                        position[colonne][ligne] = piece
                                        position[case[0]][case[1]] = 0

                                        if a == 1:
                                            position[case[0]][case[1]] = mangee
                                            mangee.ligne = case[1]
                                            mangee.colonne = case[0]
                                            if self._couleur == "Blanc":
                                                prises_Blanc.pop()
                                            else:
                                                prises_Noir.pop()

                                        return False
                                    
        return True

        
        


# Fonctions pour la promotion de pion

def promoDameB(piece):
    from board import position
    cpt = 0
    for colonne in position:
        for p in colonne:
            if type(p) == Dame and p._couleur == "Blanc":
                cpt += 1

    position[piece.colonne][piece.ligne]=Dame("Blanc",piece.colonne,piece.ligne,cpt+1)
    piece.colonne = -3
    piece.ligne = -3


def promoTourB(piece):
    from board import position
    cpt = 0
    for colonne in position:
        for p in colonne:
            if type(p) == Tour and p._couleur == "Blanc":
                cpt+=1

    position[piece.colonne][piece.ligne] = Tour("Blanc", piece.colonne, piece.ligne, cpt+1, True)
    piece.colonne = -3
    piece.ligne = -3
    

def promoFouB(piece):
    from board import position
    cpt = 0
    for colonne in position:
        for p in colonne:
            if type(p) == Fou and p._couleur == "Blanc":
                cpt += 1

    position[piece.colonne][piece.ligne]=Fou("Blanc",piece.colonne,piece.ligne,cpt+1)
    piece.colonne = -3
    piece.ligne = -3


def promoCavalierB(piece):
    from board import position
    cpt = 0
    for colonne in position:
        for p in colonne:
            if type(p) == Cavalier and p._couleur == "Blanc":
                cpt += 1

    position[piece.colonne][piece.ligne] = Cavalier("Blanc", piece.colonne, piece.ligne, cpt+1)
    piece.colonne = -3
    piece.ligne = -3


def promoDameN(piece):
    from board import position
    cpt = 0
    for colonne in position:
        for p in colonne:
            if type(p) == Dame and p._couleur == "Noir":
                cpt += 1

    position[piece.colonne][piece.ligne]=Dame("Noir",piece.colonne,piece.ligne,cpt+1)
    piece.colonne = -3
    piece.ligne = -3


def promoTourN(piece):
    from board import position
    cpt = 0
    for colonne in position:
        for p in colonne:
            if type(p) == Tour and p._couleur == "Noir":
                cpt += 1

    position[piece.colonne][piece.ligne]=Tour("Noir",piece.colonne,piece.ligne,cpt+1,True)
    piece.colonne = -3
    piece.ligne = -3
    

def promoFouN(piece):
    from board import position
    cpt = 0
    for colonne in position:
        for p in colonne:
            if type(p) == Fou and p._couleur == "Noir":
                cpt += 1

    position[piece.colonne][piece.ligne] = Fou("Noir", piece.colonne, piece.ligne, cpt+1)
    piece.colonne = -3
    piece.ligne = -3


def promoCavalierN(piece):
    from board import position
    cpt = 0
    for colonne in position:
        for p in colonne:
            if type(p) == Cavalier and p._couleur == "Noir":
                cpt += 1
  
    position[piece.colonne][piece.ligne] = Cavalier("Noir", piece.colonne, piece.ligne, cpt+1)
    piece.colonne = -3
    piece.ligne = -3




# pour chaque pièce :
# def mouvementpossible (self,case) :
# if dans les règles (pas de sortie de l'échiqiuer, bonne forme de déplacement, pas d'autre pièce sur le chemin):
# return True
# elif piece ne bouge pas:
# return True
# else:
# return False