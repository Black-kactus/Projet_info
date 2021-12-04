class Piece():
    def __init__(self, couleur, numero):
        self._couleur = couleur
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
    def __init__(self, couleur, colonne, ligne, numero, valeur=3):
        self._couleur = couleur
        self._valeur = valeur
        self.ligne = ligne
        self.colonne = colonne
        self._numero = numero

    def mouvement_possible(self, colonne, ligne):  # indique si le fou peut bouger jusqu'à la case indiquée
        from board import position
        if ligne > 7 or colonne > 7 or ligne < 0 or colonne < 0:  # sortie de l'échiquier
            return False
        elif colonne == self.colonne and ligne == self.ligne:  # si le fou ne bouge pas
            return True
        else:
            K = 0
            cpt = 0
            for k in range(-8, 9):  # motif de déplacement du fou
                if (colonne == self.colonne + k and ligne == self.ligne + k) or (
                        colonne == self.colonne - k and ligne == self.ligne + k):
                    cpt += 1
                    K = k
            if cpt != 1:  # pas le bon "motif" de déplacement
                return False

            elif (
                    colonne == self.colonne + K and ligne == self.ligne + K):  # si le fou bouge sur la diagonale de bas gauche à haut droit (/)
                if K > 0:  # si le fou va vers le haut gauche
                    for k in range(1, K):
                        if position[self.colonne + k][
                            self.ligne + k] != 0:  # s'il y a une autre piece en travers du chemin
                            return False
                else:  # si le fou va vers le bas droit
                    for k in range(1, -(K - 1)):
                        if position[self.colonne - k][
                            self.ligne - k] != 0:  # s'il y a une autre piece en travers du chemin
                            return False

            elif (
                    colonne == self.colonne - K and ligne == self.ligne + K):  # si le fou bouge sur la diagonale de haut gauche à bas droit (\)
                if K > 0:  # si le fou va vers le haut droit
                    for k in range(1, K):
                        if position[self.colonne - k][
                            self.ligne + k] != 0:  # s'il y a une autre piece en travers du chemin
                            return False
                else:  # si la tour va vers le bas gauche
                    for k in range(1, -(K - 1)):
                        if position[self.colonne + k][
                            self.ligne - k] != 0:  # s'il y a une autre piece en travers du chemin
                            return False
        return True


class Roi(Piece):
    def __init__(self, couleur, colonne, ligne, numero, valeur=0,echec=False):
        self._couleur = couleur
        self._valeur = valeur
        self.ligne = ligne
        self.colonne = colonne
        self._numero = numero
        self.echec=echec


class Dame(Piece):
    def __init__(self, couleur, colonne, ligne, numero, valeur=9):
        self._couleur = couleur
        self._valeur = valeur
        self.ligne = ligne
        self.colonne = colonne
        self._numero = numero


class Cavalier(Piece):
    def __init__(self, couleur, colonne, ligne, numero, valeur=3):
        self._couleur = couleur
        self._valeur = valeur
        self.ligne = ligne
        self.colonne = colonne
        self._numero = numero

    def mouvement_possible(self, colonne, ligne):  # indique si le cavalier peut bouger jusqu'à la case indiquée
        from board import position
        if colonne == self.colonne and ligne == self.ligne:  # si le cavalier ne bouge pas
            return True
        elif ((colonne != self.colonne - 2 and ligne != self.ligne + 1) or (
                colonne != self.colonne - 2 and ligne != self.ligne - 1) or (
                      colonne != self.colonne - 1 and ligne != self.ligne + 2) or (
                      colonne != self.colonne - 1 and ligne != self.ligne - 2) or (
                      colonne != self.colonne + 1 and ligne != self.ligne + 2) or (
                      colonne != self.colonne + 1 and ligne != self.ligne - 2) or (
                      colonne != self.colonne + 2 and ligne != self.ligne + 1) or (
                      colonne != self.colonne + 2 and ligne != self.ligne - 1)) or ligne > 7 or colonne > 7 or ligne < 0 or colonne < 0:  # pas le bon "motif" de déplacement ou sortie de l'échiquier
            return False
        else:
            return True


class Pion(Piece):
    def __init__(self, couleur, colonne, ligne, numero, valeur=1):
        self._couleur = couleur
        self._valeur = valeur
        self.ligne = ligne
        self.colonne = colonne
        self._numero = numero
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
                        if position[colonne][ligne - 1] == 0 and position[colonne][
                            ligne] == 0:  # s'il n'y a pas de piece sur la case d'arrivée
                            return True
                if ligne == (self.ligne - 1) and self._couleur != "Blanc":
                    if position[colonne][ligne] == 0:  # s'il n'y a pas de piece sur la case d'arrivée
                        return True
                if ligne == (self.ligne - 2) and self._couleur != "Blanc":
                    if self.Move1:  # premier mouvement du pion ?
                        if position[colonne][ligne + 1] == 0 and position[colonne][
                            ligne] == 0:  # s'il n'y a pas de piece sur la case d'arrivée
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


class Tour(Piece):
    def __init__(self, couleur, colonne, ligne, numero, valeur=5):
        self._couleur = couleur
        self._valeur = valeur
        self.ligne = ligne
        self.colonne = colonne
        self._numero = numero

    def mouvement_possible(self, colonne, ligne):  # indique si la tour peut bouger jusqu'à la case indiquée
        from board import position
        if ((ligne != self.ligne) and (
                colonne != self.colonne)) or ligne > 7 or colonne > 7 or ligne < 0 or colonne < 0:  # pas le bon "motif" de déplacement ou sortie de l'échiquier
            return False
        elif colonne == self.colonne and ligne == self.ligne:  # si la tour ne bouge pas
            return True
        elif ligne == self.ligne:  # si la tour bouge en horizontal
            if colonne > self.colonne:  # si la tour va vers le haut
                for c in range(self.colonne, colonne):
                    if position[c][ligne] != 0:  # s'il y a une autre piece en travers du chemin
                        return False
            else:  # si la tour va vers le bas
                for c in range(colonne, self.colonne):
                    if position[c][ligne] != 0:  # s'il y a une autre piece en travers du chemin
                        return False
        elif colonne == self.colonne:  # si la tour bouge en vertical
            if ligne > self.ligne:  # si la tour va vers la droite
                for l in range(self.ligne, ligne):
                    if position[colonne][l] != 0:  # s'il y a une autre piece en travers du chemin
                        return False
            else:  # si la tour va vers la gauche
                for l in range(ligne, self.ligne):
                    if position[colonne][l] != 0:  # s'il y a une autre piece en travers du chemin
                        return False
        return True

# à faire pour chaque pièce :
# def mouvementpossible (self,case) :
# if dans les règles (pas de sortie de l'échiqiuer, bonne forme de déplacement, pas d'autre pièce sur le chemin):
# return True
# elif piece ne bouge pas:
# return True
# else:
# return False
