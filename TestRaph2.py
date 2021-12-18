
from piece import Cavalier, Dame, Fou, Pion, Roi, Tour

#à chaque coup, si Echec2 alors tester Echec_et_mat

def Echec_et_mat(self):
    from board import position,mouvement,prises_Blanc,prises_Noir
    from piece import Piece
    for piece in position:
        if piece!=0 and piece._couleur == self._couleur:
            archive_pos=position[:]
            archive_prisesB=prises_Blanc[:]
            archive_prisesN=prises_Noir[:]
            ligne=self.ligne
            colonne=self.colonne
            if type(piece)==Roi:
                L=[[self.colonne,self.ligne+1],[self.colonne,self.ligne-1],[self.colonne+1,self.ligne],[self.colonne-1,self.ligne-1],[self.colonne+1,self.ligne+1],[self.colonne-1,self.ligne+1],[self.colonne-1,self.ligne],[self.colonne+1,self.ligne-1]]
                a=0
                for case in L:
                    if case!=0:
                        a=1
                        coordL=case.ligne
                        coordC=case.colonne
                    if mouvement(piece,case,self._couleur,"")[0] and not(self.Echec2()):
                        return False
                    position=archive_pos[:]
                    prises_Blanc=archive_prisesB[:]
                    prises_Noir=archive_prisesN[:]
                    self.ligne=ligne
                    self.colonne=colonne
                    if a==1:
                        case.ligne=coordL
                        case.colonne=coordC

            elif type(piece)==Pion:
                if piece._couleur=="Blanc":
                    L=[[self.colonne,self.ligne + 1],[self.colonne - 1,self.ligne + 1],[self.colonne + 1,self.ligne + 1]]
                    a=0
                    for case in L:
                        if case!=0:
                            a=1
                            coordL=case.ligne
                            coordC=case.colonne
                        if mouvement(piece,case,self._couleur,"")[0] and not(self.Echec2()):
                            return False
                        position=archive_pos[:]
                        prises_Blanc=archive_prisesB[:]
                        prises_Noir=archive_prisesN[:]
                        self.ligne=ligne
                        self.colonne=colonne
                        if a==1:
                            case.ligne=coordL
                            case.colonne=coordC
                if piece._couleur=="Noir":
                    L=[[self.colonne,self.ligne - 1],[self.colonne - 1,self.ligne - 1],[self.colonne + 1,self.ligne - 1]]                    
                    a=0
                    for case in L:
                        if case!=0:
                            a=1
                            coordL=case.ligne
                            coordC=case.colonne
                        if mouvement(piece,case,self._couleur,"")[0] and not(self.Echec2()):
                            return False
                        position=archive_pos[:]
                        prises_Blanc=archive_prisesB[:]
                        prises_Noir=archive_prisesN[:]
                        self.ligne=ligne
                        self.colonne=colonne
                        if a==1:
                            case.ligne=coordL
                            case.colonne=coordC

            elif type(piece)==Cavalier:
                L=[[self.colonne - 2,self.ligne + 1],[self.colonne - 2,self.ligne - 1],[self.colonne - 1,self.ligne + 2],[self.colonne - 1,self.ligne - 2],[self.colonne + 1,self.ligne + 2],[self.colonne + 1,self.ligne - 2],[self.colonne + 2][self.ligne + 1],[self.colonne + 2][self.ligne + 1],[self.colonne + 2][self.ligne - 1]]
                a=0
                for case in L:
                    if case!=0:
                        a=1
                        coordL=case.ligne
                        coordC=case.colonne
                    if mouvement(piece,case,self._couleur,"")[0] and not(self.Echec2()):
                        return False
                    position=archive_pos[:]
                    prises_Blanc=archive_prisesB[:]
                    prises_Noir=archive_prisesN[:]
                    self.ligne=ligne
                    self.colonne=colonne
                    if a==1:
                        case.ligne=coordL
                        case.colonne=coordC

            if type(piece)==Fou or type(piece)==Dame:
                A=1
                for i in range(1,max(self.colonne,7-self.colonne)+1):
                    L=[[self.colonne+i,self.ligne+i],[self.colonne-i,self.ligne-i],[self.colonne+i,self.ligne-i],[self.colonne-i,self.ligne+i]]
                    a=0
                    for case in L:
                        if case!=0:
                            a=1
                            coordL=case.ligne
                            coordC=case.colonne
                        if mouvement(piece,case,self._couleur,"")[0] and not(self.Echec2()):
                            return False
                        position=archive_pos[:]
                        prises_Blanc=archive_prisesB[:]
                        prises_Noir=archive_prisesN[:]
                        self.ligne=ligne
                        self.colonne=colonne
                        if a==1:
                            case.ligne=coordL
                            case.colonne=coordC
            
            if type(piece)==Tour or type(piece)==Dame:
                for i in range(max(self.colonne,7-self.colonne), 8): #colonnes
                    L=[[self.colonne+i,self.ligne],[self.colonne-i,self.ligne]]
                    a=0
                    for case in L:
                        if case!=0:
                            a=1
                            coordL=case.ligne
                            coordC=case.colonne
                        if mouvement(piece,case,self._couleur,"")[0] and not(self.Echec2()):
                            return False
                        position=archive_pos[:]
                        prises_Blanc=archive_prisesB[:]
                        prises_Noir=archive_prisesN[:]
                        self.ligne=ligne
                        self.colonne=colonne
                        if a==1:
                            case.ligne=coordL
                            case.colonne=coordC
                for i in range(max(self.ligne,7-self.ligne), 8): #lignes
                    L=[[self.colonne,self.ligne+i],[self.colonne,self.ligne-i]]
                    a=0
                    for case in L:
                        if case!=0:
                            a=1
                            coordL=case.ligne
                            coordC=case.colonne
                        if mouvement(piece,case,self._couleur,"")[0] and not(self.Echec2()):
                            return False
                        position=archive_pos[:]
                        prises_Blanc=archive_prisesB[:]
                        prises_Noir=archive_prisesN[:]
                        self.ligne=ligne
                        self.colonne=colonne
                        if a==1:
                            case.ligne=coordL
                            case.colonne=coordC

    return True
