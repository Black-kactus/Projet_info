#La véritable fenêtre d'interface 

from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from time import *

#probleme de prototypage

# from panique import Bouton_Regles

# # #pour récupérer la liste des positions
# from board import position
# from piece import*
# from new_interface import Entry_pieceabouger

#Fonction : permet d'importer le tableau qui contient la position des pièces 
def fonction_lecture(position):
    #from board import position
    from piece import Piece
    LPOSITION=[]
    for l in range(len(position)):
        LPOSITION.append([])
        for j in range(8):
            if position[l][j]==0:
                LPOSITION[l].append(0)
            else:
                LPOSITION[l].append(str(position[l][j]))
    return(LPOSITION)

#Fonction : permet de renvoyer un tableau de pièces prises par les blancs ou par les noirs 
def fonction_lecture_prises(prises):
    from piece import Piece
    PRISES = []
    for p in prises:
        PRISES.append(str(p))
    return PRISES

#Fonction : permet d'interpréter des scripts 
def interpreteur_script(script):
    import time
    script = script.split(' ')
    for i in range(len(script)):
        coup_script=script[i].split("-")
        if len(coup_script)==1:
            coup_special.set(coup_script[0])
            print(coup_special.get())
        elif len(coup_script)==2:
            piece_a_bouger.set(coup_script[0])
            coup.set(coup_script[1])
        if coup_special.get()=="abandon":
            cmd_bouton_abandonner()
        else:
            cmd_bouton_valider()
            #time.sleep(5)

# Mise en place de la fenêtre d'interface principale
root = Tk()
root.title("Jeu d'échec - Lila ~ Lou ~ Raphaël")
root.iconbitmap(r'icone.ico')

content = ttk.Frame(root, padding=(0,0,0,0))
frame = ttk.Frame(content, borderwidth=0, relief="ridge", width=200, height=200)
content.grid(column=0, row=0, sticky=(N, S, E, W))

#Permet de gérer le style des boutons
s = ttk.Style()
# s.configure(root, font=('Raleway', 10))
# s.configure(root, font=('', 10))

# Variables de Tkinter
piece_a_bouger = StringVar()
piece_a_bouger.set("Position pièce à bouger")

coup = StringVar()
coup.set("Position où aller")

couleurA = StringVar()
couleurA.set("Blanc")

nbcoup= StringVar()
nbcoup.set("0")

coup_special= StringVar()
coup_special.set("")

temps= StringVar()
temps.set(str(localtime()))

message_erreur =StringVar()
message_erreur.set("")

script = StringVar()
script.set("")
 
message_echec= StringVar()
message_echec.set("")

prenom_blanc = StringVar()
prenom_blanc.set('Blanc')

prenom_noir = StringVar()
prenom_noir.set('Noir')

prenom = StringVar()
prenom.set("")

duree_de_la_partie=0

## Images de la pop up perdu

ImageperduB = Image.open('defaite _des_blancs.png')
ImageperduB = ImageperduB.resize((300,300), Image.ANTIALIAS)
python_imageperduB = ImageTk.PhotoImage(ImageperduB)

ImageperduN = Image.open('defaite_des_noirs.png')
ImageperduN = ImageperduN.resize((300,300), Image.ANTIALIAS)
python_imageperduN = ImageTk.PhotoImage(ImageperduN)

## Images des règles 

ImageTableau = Image.open('tableau.jpg')
ImageTableau = ImageTableau.resize((400,300), Image.ANTIALIAS)
python_imageTableau = ImageTk.PhotoImage(ImageTableau)

ImagePEP = Image.open('PEP.png')
ImagePEP = ImagePEP.resize((200,200), Image.ANTIALIAS)
python_imagePEP = ImageTk.PhotoImage(ImagePEP)

ImageEchecMate = Image.open('checkmate.jpg')
ImageEchecMate = ImageEchecMate.resize((300,200), Image.ANTIALIAS)
python_imageEchecMate = ImageTk.PhotoImage(ImageEchecMate)


## Images des pieces de l'échiquier

ImgFouNoir = Image.open('fou_noir.png')
ImgFouBlanc = Image.open('fou_blanc.png')
ImgCavalierBlanc = Image.open('cavalier_blanc.png')
ImgCavalierNoir= Image.open('cavalier_noir.png')
ImgRoiBlanc = Image.open('roi_blanc.png')
ImgRoiNoir = Image.open('roi_noir.png')
ImgDameBlanche = Image.open('reine_blanche.png')
ImgDameNoire = Image.open('reine_noire.png')
ImgPionBlanc = Image.open('pion_blanc.png')
ImgPionNoir = Image.open('pion_noir.png')
ImgTourBlanche = Image.open('tour_blanche.png')
ImgTourNoire = Image.open('tour_noire.png')
ImgVide = Image.open('vide.png')

resizeX = 60
resizeY = 60
ImgFouNoir = ImgFouNoir.resize((resizeX,resizeY), Image.ANTIALIAS)
ImgFouBlanc = ImgFouBlanc.resize((resizeX,resizeY), Image.ANTIALIAS)
ImgCavalierBlanc = ImgCavalierBlanc.resize((resizeX,resizeY), Image.ANTIALIAS)
ImgCavalierNoir = ImgCavalierNoir.resize((resizeX,resizeY), Image.ANTIALIAS)
ImgRoiBlanc = ImgRoiBlanc.resize((resizeX,resizeY), Image.ANTIALIAS)
ImgRoiNoir = ImgRoiNoir.resize((resizeX,resizeY), Image.ANTIALIAS)
ImgDameBlanche = ImgDameBlanche.resize((resizeX,resizeY), Image.ANTIALIAS)
ImgDameNoire = ImgDameNoire.resize((resizeX,resizeY), Image.ANTIALIAS)
ImgPionBlanc = ImgPionBlanc.resize((resizeX,resizeY), Image.ANTIALIAS)
ImgPionNoir = ImgPionNoir.resize((resizeX,resizeY), Image.ANTIALIAS)
ImgTourBlanche = ImgTourBlanche.resize((resizeX,resizeY), Image.ANTIALIAS)
ImgTourNoire = ImgTourNoire.resize((resizeX,resizeY), Image.ANTIALIAS)
ImgVide = ImgVide.resize((resizeX,resizeY), Image.ANTIALIAS)


python_imageFN = ImageTk.PhotoImage(ImgFouNoir)
python_imageFB = ImageTk.PhotoImage(ImgFouBlanc)
python_imageCB = ImageTk.PhotoImage(ImgCavalierBlanc)
python_imageCN = ImageTk.PhotoImage(ImgCavalierNoir)
python_imageRB = ImageTk.PhotoImage(ImgRoiBlanc)
python_imageRN = ImageTk.PhotoImage(ImgRoiNoir)
python_imageDB = ImageTk.PhotoImage(ImgDameBlanche)
python_imageDN = ImageTk.PhotoImage(ImgDameNoire)
python_imagePB = ImageTk.PhotoImage(ImgPionBlanc)
python_imagePN = ImageTk.PhotoImage(ImgPionNoir)
python_imageTB = ImageTk.PhotoImage(ImgTourBlanche)
python_imageTN = ImageTk.PhotoImage(ImgTourNoire)
python_imageVIDE = ImageTk.PhotoImage(ImgVide)

## Images des icones des pieces prise

resizeX = 30
resizeY = 30
ImgFouNoir2 = ImgFouNoir.resize((resizeX,resizeY), Image.ANTIALIAS)
ImgFouBlanc2 = ImgFouBlanc.resize((resizeX,resizeY), Image.ANTIALIAS)
ImgCavalierBlanc2 = ImgCavalierBlanc.resize((resizeX,resizeY), Image.ANTIALIAS)
ImgCavalierNoir2 = ImgCavalierNoir.resize((resizeX,resizeY), Image.ANTIALIAS)
ImgRoiBlanc2 = ImgRoiBlanc.resize((resizeX,resizeY), Image.ANTIALIAS)
ImgRoiNoir2 = ImgRoiNoir.resize((resizeX,resizeY), Image.ANTIALIAS)
ImgDameBlanche2 = ImgDameBlanche.resize((resizeX,resizeY), Image.ANTIALIAS)
ImgDameNoire2 = ImgDameNoire.resize((resizeX,resizeY), Image.ANTIALIAS)
ImgPionBlanc2 = ImgPionBlanc.resize((resizeX,resizeY), Image.ANTIALIAS)
ImgPionNoir2 = ImgPionNoir.resize((resizeX,resizeY), Image.ANTIALIAS)
ImgTourBlanche2 = ImgTourBlanche.resize((resizeX,resizeY), Image.ANTIALIAS)
ImgTourNoire2 = ImgTourNoire.resize((resizeX,resizeY), Image.ANTIALIAS)
ImgVide2 = ImgVide.resize((resizeX,resizeY), Image.ANTIALIAS)

python_imageFN2= ImageTk.PhotoImage(ImgFouNoir2)
python_imageFB2= ImageTk.PhotoImage(ImgFouBlanc2)
python_imageCB2 = ImageTk.PhotoImage(ImgCavalierBlanc2)
python_imageCN2 = ImageTk.PhotoImage(ImgCavalierNoir2)
python_imageRB2 = ImageTk.PhotoImage(ImgRoiBlanc2)
python_imageRN2 = ImageTk.PhotoImage(ImgRoiNoir2)
python_imageDB2 = ImageTk.PhotoImage(ImgDameBlanche2)
python_imageDN2 = ImageTk.PhotoImage(ImgDameNoire2)
python_imagePB2 = ImageTk.PhotoImage(ImgPionBlanc2)
python_imagePN2 = ImageTk.PhotoImage(ImgPionNoir2)
python_imageTB2 = ImageTk.PhotoImage(ImgTourBlanche2)
python_imageTN2 = ImageTk.PhotoImage(ImgTourNoire2)
python_imageVIDE2 = ImageTk.PhotoImage(ImgVide2)

## Image des déplacements 

ImgDFou= Image.open('dep_fou.png')
ImgDTour= Image.open('dep_tour.png')
ImgDDame= Image.open('dep_dame.png')
ImgDRoi= Image.open('dep_roi.png')
ImgDCavalier= Image.open('dep_cavalier.png')

resizeX= 350
resizeY= 350
ImgDFou = ImgDFou.resize((resizeX,resizeY), Image.ANTIALIAS)
ImgDTour = ImgDTour.resize((resizeX,resizeY), Image.ANTIALIAS)
ImgDDame = ImgDDame.resize((resizeX,resizeY), Image.ANTIALIAS)
ImgDRoi = ImgDRoi.resize((resizeX,resizeY), Image.ANTIALIAS)
ImgDCavalier = ImgDCavalier.resize((resizeX,resizeY), Image.ANTIALIAS)


python_imageDF = ImageTk.PhotoImage(ImgDFou)
python_imageDT = ImageTk.PhotoImage(ImgDTour)
python_imageDD = ImageTk.PhotoImage(ImgDDame)
python_imageDR = ImageTk.PhotoImage(ImgDRoi)
python_imageDC = ImageTk.PhotoImage(ImgDCavalier)



#Dictionnaire dicopiece pour les pièces sur l'échiquier: 
# fait le lien entre des objets tkinter et les notations du code   
dicopiece = {0 : python_imageVIDE}
dicopieceB = {"TB1": python_imageTB,"CB1": python_imageCB,"FB1": python_imageFB,"QB1":python_imageDB,"KB1":python_imageRB,"FB2":python_imageFB,"CB2":python_imageCB,"TB2":python_imageTB}
dicopieceN= {"TN1":python_imageTN,"CN1":python_imageCN,"FN1":python_imageFN,"QN1":python_imageDN,"KN1":python_imageRN,"FN2":python_imageFN,"CN2":python_imageCN,"TN2":python_imageTN}
dicopiecepionB = {"PB1": python_imagePB, "PB2":python_imagePB,"PB3":python_imagePB,"PB4":python_imagePB,"PB5":python_imagePB,"PB6":python_imagePB,"PB7":python_imagePB,"PB8":python_imagePB}
dicopiecepionN = {"PN1":python_imagePN,"PN2":python_imagePN,"PN3":python_imagePN,"PN4":python_imagePN,"PN5":python_imagePN,"PN6":python_imagePN,"PN7":python_imagePN,"PN8":python_imagePN}

dicopiecePromoDameB ={"QB2":python_imageDB,"QB3":python_imageDB,"QB4":python_imageDB,"QB5":python_imageDB,"QB6":python_imageDB,"QB7":python_imageDB,"QB8":python_imageDB,"QB9":python_imageDB}
dicopiecePromoFouB ={"FB3":python_imageFB,"FB4":python_imageFB,"FB5":python_imageFB,"FB6":python_imageFB,"FB7":python_imageFB,"FB8":python_imageFB,"FB9":python_imageFB,"FB10":python_imageFB}
dicopiecePromoTourB = {"TB3":python_imageTB,"TB4":python_imageTB,"TB5":python_imageTB,"TB6":python_imageTB,"TB7":python_imageTB,"TB8":python_imageTB,"TB9":python_imageTB,"TB10":python_imageTB}
dicopiecePromoCavalierB ={"CB3":python_imageCB,"CB4":python_imageCB,"CB5":python_imageCB,"CB6":python_imageCB,"CB7":python_imageCB,"CB8":python_imageCB,"CB9":python_imageCB,"CB10":python_imageCB}

dicopiecePromoDameN ={"QN2":python_imageDN,"QN3":python_imageDN,"QN4":python_imageDN,"QN5":python_imageDN,"QN6":python_imageDN,"QN7":python_imageDN,"QN8":python_imageDN,"QN9":python_imageDN}
dicopiecePromoFouN ={"FN3":python_imageFN,"FN4":python_imageFN,"FN5":python_imageFN,"FN6":python_imageFN,"FN7":python_imageFN,"FN8":python_imageFN,"FN9":python_imageFN,"FN10":python_imageFN}
dicopiecePromoTourN = {"TN3":python_imageTN,"TN4":python_imageTN,"TN5":python_imageTN,"TN6":python_imageTN,"TN7":python_imageTN,"TN8":python_imageTN,"TN9":python_imageTN,"TN10":python_imageTN}
dicopiecePromoCavalierN ={"CN3":python_imageCN,"CN4":python_imageCN,"CN5":python_imageCN,"CN6":python_imageCN,"CN7":python_imageCN,"CN8":python_imageCN,"CN9":python_imageCN,"CN10":python_imageCN}

dicopiece.update(dicopieceB)
dicopiece.update(dicopieceN)
dicopiece.update(dicopiecepionB)
dicopiece.update(dicopiecepionN)

dicopiece.update(dicopiecePromoDameB)
dicopiece.update(dicopiecePromoFouB)
dicopiece.update(dicopiecePromoTourB)
dicopiece.update(dicopiecePromoCavalierB)

dicopiece.update(dicopiecePromoDameN)
dicopiece.update(dicopiecePromoFouN)
dicopiece.update(dicopiecePromoTourN)
dicopiece.update(dicopiecePromoCavalierN)


#Dictionnaire dicopiece2 pour la promotion 

dicopiece2 = {0 : python_imageVIDE2}
dicopieceB2 = {"TB1": python_imageTB2,"CB1": python_imageCB2,"FB1": python_imageFB2,"QB1":python_imageDB2,"KB1":python_imageRB2,"FB2":python_imageFB2,"CB2":python_imageCB2,"TB2":python_imageTB2}
dicopieceN2= {"TN1":python_imageTN2,"CN1":python_imageCN2,"FN1":python_imageFN2,"QN1":python_imageDN2,"KN1":python_imageRN2,"FN2":python_imageFN2,"CN2":python_imageCN2,"TN2":python_imageTN2}
dicopiecepionB2 = {"PB1": python_imagePB2, "PB2":python_imagePB2,"PB3":python_imagePB2,"PB4":python_imagePB2,"PB5":python_imagePB2,"PB6":python_imagePB2,"PB7":python_imagePB2,"PB8":python_imagePB2}
dicopiecepionN2 = {"PN1":python_imagePN2,"PN2":python_imagePN2,"PN3":python_imagePN2,"PN4":python_imagePN2,"PN5":python_imagePN2,"PN6":python_imagePN2,"PN7":python_imagePN2,"PN8":python_imagePN2}

dicopiecePromoDameB2 ={"QB2":python_imageDB2,"QB3":python_imageDB2,"QB4":python_imageDB2,"QB5":python_imageDB2,"QB6":python_imageDB2,"QB7":python_imageDB2,"QB8":python_imageDB2,"QB9":python_imageDB2}
dicopiecePromoFouB2={"FB3":python_imageFB2,"FB4":python_imageFB2,"FB5":python_imageFB2,"FB6":python_imageFB2,"FB7":python_imageFB2,"FB8":python_imageFB2,"FB9":python_imageFB2,"FB10":python_imageFB2}
dicopiecePromoTourB2 = {"TB3":python_imageTB2,"TB4":python_imageTB2,"TB5":python_imageTB2,"TB6":python_imageTB2,"TB7":python_imageTB2,"TB8":python_imageTB2,"TB9":python_imageTB2,"TB10":python_imageTB2}
dicopiecePromoCavalierB2 ={"CB3":python_imageCB2,"CB4":python_imageCB2,"CB5":python_imageCB2,"CB6":python_imageCB2,"CB7":python_imageCB2,"CB8":python_imageCB2,"CB9":python_imageCB2,"CB10":python_imageCB2}

dicopiecePromoDameN2 ={"QN2":python_imageDN2,"QN3":python_imageDN2,"QN4":python_imageDN2,"QN5":python_imageDN2,"QN6":python_imageDN2,"QN7":python_imageDN2,"QN8":python_imageDN2,"QN9":python_imageDN2}
dicopiecePromoFouN2 ={"FN3":python_imageFN2,"FN4":python_imageFN2,"FN5":python_imageFN2,"FN6":python_imageFN2,"FN7":python_imageFN2,"FN8":python_imageFN2,"FN9":python_imageFN2,"FN10":python_imageFN2}
dicopiecePromoTourN2 = {"TN3":python_imageTN2,"TN4":python_imageTN2,"TN5":python_imageTN2,"TN6":python_imageTN2,"TN7":python_imageTN2,"TN8":python_imageTN2,"TN9":python_imageTN2,"TN10":python_imageTN2}
dicopiecePromoCavalierN2 ={"CN3":python_imageCN2,"CN4":python_imageCN2,"CN5":python_imageCN2,"CN6":python_imageCN2,"CN7":python_imageCN2,"CN8":python_imageCN2,"CN9":python_imageCN2,"CN10":python_imageCN2}

dicopiece2.update(dicopieceB2)
dicopiece2.update(dicopieceN2)
dicopiece2.update(dicopiecepionB2)
dicopiece2.update(dicopiecepionN2)

dicopiece2.update(dicopiecePromoDameB2)
dicopiece2.update(dicopiecePromoFouB2)
dicopiece2.update(dicopiecePromoTourB2)
dicopiece2.update(dicopiecePromoCavalierB2)

dicopiece2.update(dicopiecePromoDameN2)
dicopiece2.update(dicopiecePromoFouN2)
dicopiece2.update(dicopiecePromoTourN2)
dicopiece2.update(dicopiecePromoCavalierN2)

#Creation des indices horizontaux de l'échiquier
# for i in range(0,18,2):
#     L = ["","A",'B',"C","D","E","F",'G','H']
#     ttk.Label(content, text= str(int(9-i/2)),relief="solid",anchor=CENTER).grid(column=0, row=i, columnspan=2, rowspan=2,sticky=(N,S,E,W),pady=1, padx=1)
#     ttk.Label(content, text= L[int(i/2)],relief="solid",anchor=CENTER).grid(column=i, row=0, columnspan=2, rowspan=2,sticky=(N,S,E,W),pady=1, padx=1)



#Liste des positions renvoyées par Raph
LPOSITION= [["TB1","PB1",0,0,0,0,"PN1","TN1"],["CB1","PB2",0,0,0,0,"PN2","CN1"],["FB1","PB3",0,0,0,0,"PN3","FN1"],["QB1","PB4",0,0,0,0,"PN4","QN1"],["KB1","PB5",0,0,0,0,"PN5","KN1"],["FB2","PB6",0,0,0,0,"PN6","FN2"],["CB2","PB7",0,0,0,0,"PN7","CN2"],["TB2","PB8",0,0,0,0,"PN8","TN2"]]
# LPIECESPRISES = [[1,1,0,1,0,1,1,0],[1,0,1,0,1,0,1,1],[1,0,1,1,1,0,1,1],[1,0,1,1,0,1,1,1]]
LPIECESPRISES = [[1,1,0,1,0,1,1,0],[1,0,1,0,1,0,1,1],[1,0,1,1,1,0,1,1],[1,0,1,1,0,1,1,1]]
LIMAGESPICESPRISES = [[python_imageTB2, python_imageCB2, python_imageFB2, python_imageDB2, python_imageRB2, python_imageFB2, python_imageCB2, python_imageTB2], [python_imageTN2, python_imageCN2, python_imageFN2, python_imageDN2, python_imageRN2, python_imageFN2, python_imageCN2, python_imageTN2] ]

# def afficherPiece():
#     global LPOSITION
#     for i in range(len(LPOSITION)) : 
#         for j in range(len(LPOSITION)):
#             if (i+j)%2 == 0: couleur = 'black'
#             else : couleur = "white"
#             if couleurA.get() == "Noir":
#                 ttk.Label(content, image=dicopiece[LPOSITION[7-j][i]],background = couleur,relief="solid",anchor=CENTER).grid(row = 2*i+2, column = 2*j+2, rowspan= 2, columnspan= 2,sticky=(N,S,E,W),pady=1, padx=1)
#             else : 
#                 ttk.Label(content, image=dicopiece[LPOSITION[j][7-i]],background = couleur,relief="solid",anchor=CENTER).grid(row = 2*i+2, column = 2*j+2, rowspan= 2, columnspan= 2,sticky=(N,S,E,W),pady=1, padx=1)
#     if couleurA.get() == "Noir":
#         for k in range(0,18,2):
#             # L = ["","A",'B',"C","D","E","F",'G','H']
#             L = ["","H","G",'F',"E","D","C","B",'A']
#             ttk.Label(content, text= str(int(k/2)),relief="solid",anchor=CENTER).grid(column=0, row=k, columnspan=2, rowspan=2,sticky=(N,S,E,W),pady=1, padx=1)
#             ttk.Label(content, text= L[int((k)/2)],relief="solid",anchor=CENTER).grid(column=k, row=0, columnspan=2, rowspan=2,sticky=(N,S,E,W),pady=1, padx=1)
#     else: 
#         for k in range(0,18,2):
#             L = ["","A",'B',"C","D","E","F",'G','H']
#             # L = ["","H","G",'F',"E","D","C","B",'A']
#             ttk.Label(content, text= str(int(9-k/2)),relief="solid",anchor=CENTER).grid(column=0, row=k, columnspan=2, rowspan=2,sticky=(N,S,E,W),pady=1, padx=1)
#             ttk.Label(content, text= L[int(k/2)],relief="solid",anchor=CENTER).grid(column=k, row=0, columnspan=2, rowspan=2,sticky=(N,S,E,W),pady=1, padx=1)

#Fonction : gère l'évènement clic gauche sur les pièces de l'échiquer
def BoutonGestClicgauche(evt, i, j):
    # print('CGauche',i, j )
    piece_a_bouger.set(chr(j+97)+str(8-i))

#Fonction : gère l'évènement clic droit sur les pièces de l'échiquer
def BoutonGestClicdroit(evt, i, j ):
    # print('CDroit', i, j)
    coup.set(chr(j+97)+str(8-i))

#Fonction : gère l'affichage des pièces sur l'échiquier 
BoutonListe = [[0 for i in range(8)]for j in range(8)]
def afficherPiece():
    global LPOSITION
    for i in range(len(LPOSITION)) : 
        for j in range(len(LPOSITION)):
            if (i+j)%2 == 0: couleur = 'black'
            else : couleur = "white"
            if couleurA.get() == "Noir":
                Bouton_piece = ttk.Label(content, image=dicopiece[LPOSITION[7-j][i]],background = couleur,relief="solid",anchor=CENTER)
                BoutonListe[i].insert(j,Bouton_piece)
                Bouton_piece.grid(row = 2*i+2, column = 2*j+2, rowspan= 2, columnspan= 2,sticky=(N,S,E,W),pady=1, padx=1)
                
                #Gestion des clics gauche et droits sur les images des pièces 
                def gestCG(evt, i=i,j=j):   
                    return BoutonGestClicgauche(evt, 7-i,7-j)
                def gestCD(evt, i=i, j= j):   
                    return BoutonGestClicdroit(evt, 7-i,7-j)
            else : 
                Bouton_piece = ttk.Label(content, image=dicopiece[LPOSITION[j][7-i]],background = couleur,relief="solid",anchor=CENTER)
                BoutonListe[i].insert(j,Bouton_piece)
                Bouton_piece.grid(row = 2*i+2, column = 2*j+2, rowspan= 2, columnspan= 2,sticky=(N,S,E,W),pady=1, padx=1)

                #Gestion des clics gauche et droit sur les images des pièces 
                def gestCG(evt, i=i,j=j):   
                     return BoutonGestClicgauche(evt, i,j)
                def gestCD(evt, i=i, j= j):   
                    return BoutonGestClicdroit(evt, i,j)
           
            Bouton_piece.bind('<Button-1>', gestCG)
            Bouton_piece.bind('<Button-3>', gestCD)

    if couleurA.get() == "Noir":
        for k in range(0,18,2):
            # L = ["","A",'B',"C","D","E","F",'G','H']
            L = ["","H","G",'F',"E","D","C","B",'A']
            ttk.Label(content, text= str(int(k/2)),relief="solid",anchor=CENTER).grid(column=0, row=k, columnspan=2, rowspan=2,sticky=(N,S,E,W),pady=1, padx=1)
            ttk.Label(content, text= L[int((k)/2)],relief="solid",anchor=CENTER).grid(column=k, row=0, columnspan=2, rowspan=2,sticky=(N,S,E,W),pady=1, padx=1)
    else: 
        for k in range(0,18,2):
            L = ["","A",'B',"C","D","E","F",'G','H']
            # L = ["","H","G",'F',"E","D","C","B",'A']
            ttk.Label(content, text= str(int(9-k/2)),relief="solid",anchor=CENTER).grid(column=0, row=k, columnspan=2, rowspan=2,sticky=(N,S,E,W),pady=1, padx=1)
            ttk.Label(content, text= L[int(k/2)],relief="solid",anchor=CENTER).grid(column=k, row=0, columnspan=2, rowspan=2,sticky=(N,S,E,W),pady=1, padx=1)

#Fonction : gère l'affichage des pièces prises 
def afficherPiecesPrises():
    global LPIECESPRISES
    global LIMAGESPICESPRISES
    couleurBg = 'white'
    couleurBg2 = 'black'

    from board import prises_Noir, prises_Blanc
    LPIECESPRISESNOIRES = fonction_lecture_prises(prises_Noir)
    LPIECESPRISESBLANC = fonction_lecture_prises(prises_Blanc)
    print(LPIECESPRISESBLANC)
    # for i in range(8):
        # if LPIECESPRISES[0][i] == 0: ttk.Label(content, anchor= CENTER, relief="solid", background= couleurBg2, image = LIMAGESPICESPRISES[1][i]).grid(column=20+i,row=12, columnspan=1, rowspan = 1 ,sticky=(N,S,E,W))
        # else : ttk.Label(content, anchor= CENTER, relief="solid",image = python_imageVIDE2, background = couleurBg2).grid(column=20+i,row=12, columnspan=1, rowspan = 1 ,sticky=(N,S,E,W))
        
        # if LPIECESPRISES[1][i] == 0:  ttk.Label(content, anchor= CENTER, relief="solid", background=couleurBg2, image = python_imagePN2).grid(column=20+i,row=13, columnspan=1, rowspan = 1 ,sticky=(N,S,E,W))
        # else :  ttk.Label(content, anchor= CENTER, relief="solid",image = python_imageVIDE2,background = couleurBg2).grid(column=20+i,row=13, columnspan=1, rowspan = 1 ,sticky=(N,S,E,W))

        # if LPIECESPRISES[2][i] == 0 : ttk.Label(content, textvariable= "", anchor= CENTER, relief="solid",background= couleurBg, image = python_imagePB2).grid(column=20+i,row=14, columnspan=1, rowspan = 1 ,sticky=(N,S,E,W))
        # else: ttk.Label(content, textvariable= "", anchor= CENTER, relief="solid", image = python_imageVIDE2, background =couleurBg).grid(column=20+i,row=14, columnspan=1, rowspan = 1 ,sticky=(N,S,E,W))

        # if LPIECESPRISES[3][i] == 0 :  ttk.Label(content, textvariable= "", anchor= CENTER, relief="solid",background=couleurBg,image = LIMAGESPICESPRISES[0][i]).grid(column=20+i,row=15, columnspan=1, rowspan = 1 ,sticky=(N,S,E,W))
        # else:  ttk.Label(content, textvariable= "", anchor= CENTER, relief="solid", image= python_imageVIDE2, background = couleurBg).grid(column=20+i,row=15, columnspan=1, rowspan = 1 ,sticky=(N,S,E,W))

    NbpiecesmangesN = len(LPIECESPRISESNOIRES)
    for i in range (NbpiecesmangesN):
        if i <8:
                ttk.Label(content, anchor= CENTER, relief="solid", background= couleurBg2, image =dicopiece2[LPIECESPRISESNOIRES[i]]).grid(column=20+i,row=12, columnspan=1, rowspan = 1 ,sticky=(N,S,E,W))
        else: 
                ttk.Label(content, anchor= CENTER, relief="solid", background=couleurBg2, image = dicopiece2[LPIECESPRISESNOIRES[i]]).grid(column=20+i-8,row=13, columnspan=1, rowspan = 1 ,sticky=(N,S,E,W))
    
    for k in range (NbpiecesmangesN,16):
        if k <8:
                ttk.Label(content, anchor= CENTER, relief="solid",image = python_imageVIDE2, background = couleurBg2).grid(column=20+k,row=12, columnspan=1, rowspan = 1 ,sticky=(N,S,E,W))
        else: 
                ttk.Label(content, anchor= CENTER, relief="solid",image = python_imageVIDE2,background = couleurBg2).grid(column=20+k-8,row=13, columnspan=1, rowspan = 1 ,sticky=(N,S,E,W))

    NbpiecesmangesB = len(LPIECESPRISESBLANC)
    for j in range (NbpiecesmangesB):
        if j <8:
                ttk.Label(content, anchor= CENTER, relief="solid", background= couleurBg, image =dicopiece2[LPIECESPRISESBLANC[j]]).grid(column=20+j,row=14, columnspan=1, rowspan = 1 ,sticky=(N,S,E,W))
        else: 
                ttk.Label(content, anchor= CENTER, relief="solid", background=couleurBg, image = dicopiece2[LPIECESPRISESBLANC[j]]).grid(column=20+j-8,row=15, columnspan=1, rowspan = 1 ,sticky=(N,S,E,W))
    
    for l in range (NbpiecesmangesB,16):
        if l <8:
                ttk.Label(content, anchor= CENTER, relief="solid",image = python_imageVIDE2, background = couleurBg).grid(column=20+l,row=14, columnspan=1, rowspan = 1 ,sticky=(N,S,E,W))
        else: 
                ttk.Label(content, anchor= CENTER, relief="solid",image = python_imageVIDE2,background = couleurBg).grid(column=20+l-8,row=15, columnspan=1, rowspan = 1 ,sticky=(N,S,E,W))
     
     

#Ancienne Fonction : gère l'actualisation des pièces prises 
def actualiserPiecesPrises():
    global LPOSITION
    global LPIECESPRISES

    Lconcordance = [["TN1","CN1","FN1","QN1","KN1","FN2","CN2","TN2"],["PN1","PN2","PN3","PN4","PN5","PN6","PN7","PN8"],["PB1","PB2","PB3","PB4","PB5","PB6","PB7","PB8"],["TB1","CB1","FB1","QB1","KB1","FB2","CB2","TB2"]]
    for i in range(4):
        for j in range(8):
            dedans = False 
            for k in range(8):
                if Lconcordance[i][j] in LPOSITION[k]: 
                    dedans = True
            if dedans :
                LPIECESPRISES[i][j] = 1
                #si la piece n'est pas mangée on marque 1 (ie si elle est toujours dans LPOSITION)
            else : 
                LPIECESPRISES[i][j] = 0
                #si la piece est mangée on marque 0

#LILA modifie le code : je pense que ça marche pas a cause de la gestion des pop ups, donc je te propose qqch d'autre, et si ça te convient pasn au mieux ça te donne des idées, sinon tu peux supprimer sans souci
# SAUVEGARDE DU CODE DE RAPHAEL, NE PS SUPPRIMER 

choix_de_promotion = StringVar()
choix_de_promotion.set("Indiquez la pièce.")

# def cmd_bouton_dameB(piece):
#     from piece import promoDameB
#     choix_de_promotion.set("Dame")
#     print("Dame")
#     promoDameB(piece)
#     PopUp_promo.destroy()

# def cmd_bouton_tourB(piece):
#     from piece import promoTourB
#     choix_de_promotion.set("Tour")
#     print("Tour")
#     promoTourB(piece)
#     PopUp_promo.destroy()

# def cmd_bouton_fouB(piece):
#     from piece import promoFouB
#     choix_de_promotion.set("Fou")
#     print("Fou")
#     promoFouB(piece)
#     PopUp_promo.destroy()


# def cmd_bouton_cavalierB(piece):
#     from piece import promoCavalierB
#     choix_de_promotion.set("Cavalier")
#     print("Cavalier")
#     promoCavalierB(piece)
#     PopUp_promo.destroy()

# def cmd_bouton_pionB(piece):
#     choix_de_promotion.set("Pion")
#     print("Pion")
#     PopUp_promo.destroy()

# def cmd_bouton_dameN(piece):
#     from piece import promoDameN
#     choix_de_promotion.set("Dame")
#     print("Dame")
#     promoDameN(piece)
#     PopUp_promo.destroy()

# def cmd_bouton_tourN(piece):
#     from piece import promoTourN
#     choix_de_promotion.set("Tour")
#     print("Tour")
#     promoTourN(piece)
#     PopUp_promo.destroy()

# def cmd_bouton_fouN(piece):
#     from piece import promoFouN
#     choix_de_promotion.set("Fou")
#     print("Fou")
#     promoFouN(piece)
#     PopUp_promo.destroy()

# def cmd_bouton_cavalierN(piece):
#     from piece import promoCavalierN
#     choix_de_promotion.set("Cavalier")
#     print("Cavalier")
#     promoCavalierN(piece)
#     PopUp_promo.destroy()
#     #là il va pas savoir ce que c'est piece

# def cmd_bouton_pionN(piece):
#     choix_de_promotion.set("Pion")
#     print("Pion")
#     PopUp_promo.destroy()

# def open_popup_promo(piece,couleur):
#     PopUp_promo= Toplevel()
#     PopUp_promo.geometry("750x350")
#     PopUp_promo.title("Promotion de pion")
#     PopUp_promo.iconbitmap(r'icone.ico')
#     PopUp_promo.lift()
#     Label(PopUp_promo, text= "En quoi voulez-vous changer votre pion ?", font=('Helvetica 12 bold')).pack(pady=10)
#     if couleur=="Blanc":
#         Bouton_dame= ttk.Button(PopUp_promo, text= "Dame",command= cmd_bouton_dameB(piece))
#         Bouton_dame.pack()
#         Bouton_tour= ttk.Button(PopUp_promo, text= "Tour",command= cmd_bouton_tourB(piece))
#         Bouton_tour.pack()
#         Bouton_fou= ttk.Button(PopUp_promo, text= "Fou",command= cmd_bouton_fouB(piece))
#         Bouton_fou.pack()
#         Bouton_cavalier= ttk.Button(PopUp_promo, text= "Cavalier",command= cmd_bouton_cavalierB(piece))
#         Bouton_cavalier.pack()
#         Bouton_pion= ttk.Button(PopUp_promo, text= "Garder un pion",command= cmd_bouton_pionB(piece))
#         Bouton_pion.pack()
#     else:
#         Bouton_dame= ttk.Button(PopUp_promo, text= "Dame",command= cmd_bouton_dameN(piece))
#         Bouton_dame.pack()
#         Bouton_tour= ttk.Button(PopUp_promo, text= "Tour",command= cmd_bouton_tourN(piece))
#         Bouton_tour.pack()
#         Bouton_fou= ttk.Button(PopUp_promo, text= "Fou",command= cmd_bouton_fouN(piece))
#         Bouton_fou.pack()
#         Bouton_cavalier= ttk.Button(PopUp_promo, text= "Cavalier",command= cmd_bouton_cavalierN(piece))
#         Bouton_cavalier.pack()
#         Bouton_pion= ttk.Button(PopUp_promo, text= "Garder un pion",command= cmd_bouton_pionN(piece))
#         Bouton_pion.pack()

#         #normalement dans les commande tu mets pas d'argument sinon ça va pas marcher
#         #parce que il sait pas a quoi correspond piece, ce qui explique peut etre pourquoi ça marche pas 

#Pop up: gère le cas de la promotion de pion
def open_popup_promo(piece,couleur):

    def cmd_bouton_dameB():
        from piece import promoDameB
        global choix_de_promotion
        choix_de_promotion.set("Dame")
        print("Dame")
        promoDameB(piece)
        PopUp_promo.destroy()

    def cmd_bouton_tourB():
        from piece import promoTourB
        global choix_de_promotion
        choix_de_promotion.set("Tour")
        print("Tour")
        promoTourB(piece)
        PopUp_promo.destroy()

    def cmd_bouton_fouB():
        from piece import promoFouB
        global choix_de_promotion
        choix_de_promotion.set("Fou")
        print("Fou")
        promoFouB(piece)
        PopUp_promo.destroy()


    def cmd_bouton_cavalierB():
        from piece import promoCavalierB
        global choix_de_promotion
        choix_de_promotion.set("Cavalier")
        print("Cavalier")
        promoCavalierB(piece)
        PopUp_promo.destroy()

    def cmd_bouton_pionB():
        global choix_de_promotion
        choix_de_promotion.set("Pion")
        print("Pion")
        PopUp_promo.destroy()

    def cmd_bouton_dameN():
        from piece import promoDameN
        global choix_de_promotion
        choix_de_promotion.set("Dame")
        print("Dame")
        promoDameN(piece)
        PopUp_promo.destroy()
        #ce que fait la fonction, c'est donner une nouvelle valeur à choix de promotion, sans l'utiliser après, c'est normal? 

    def cmd_bouton_tourN():
        from piece import promoTourN
        global choix_de_promotion
        choix_de_promotion.set("Tour")
        print("Tour")
        promoTourN(piece)
        PopUp_promo.destroy()

    def cmd_bouton_fouN():
        from piece import promoFouN
        global choix_de_promotion
        choix_de_promotion.set("Fou")
        print("Fou")
        promoFouN(piece)
        PopUp_promo.destroy()

    def cmd_bouton_cavalierN():
        from piece import promoCavalierN
        global choix_de_promotion
        choix_de_promotion.set("Cavalier")
        print("Cavalier")
        promoCavalierN(piece)
        PopUp_promo.destroy()

    def cmd_bouton_pionN():
        global choix_de_promotion
        choix_de_promotion.set("Pion")
        print("Pion")
        PopUp_promo.destroy()

    PopUp_promo= Toplevel()
    PopUp_promo.title("Promotion de pion")
    PopUp_promo.iconbitmap(r'icone.ico')
    PopUp_promo.geometry("750x350")
    PopUp_promo.lift()

    ttk.Label(PopUp_promo, text= "En quoi voulez-vous changer votre pion ?").pack(pady=10)
    if couleur=="Blanc":
        Bouton_dame= ttk.Button(PopUp_promo, text= "Dame",command= cmd_bouton_dameB())
        Bouton_dame.pack()
        Bouton_tour= ttk.Button(PopUp_promo, text= "Tour",command= cmd_bouton_tourB())
        Bouton_tour.pack()
        Bouton_fou= ttk.Button(PopUp_promo, text= "Fou",command= cmd_bouton_fouB())
        Bouton_fou.pack()
        Bouton_cavalier= ttk.Button(PopUp_promo, text= "Cavalier",command= cmd_bouton_cavalierB())
        Bouton_cavalier.pack()
        Bouton_pion= ttk.Button(PopUp_promo, text= "Garder un pion",command= cmd_bouton_pionB())
        Bouton_pion.pack()
    else:
        Bouton_dame= ttk.Button(PopUp_promo, text= "Dame",command= cmd_bouton_dameN())
        Bouton_dame.pack()
        Bouton_tour= ttk.Button(PopUp_promo, text= "Tour",command= cmd_bouton_tourN())
        Bouton_tour.pack()
        Bouton_fou= ttk.Button(PopUp_promo, text= "Fou",command= cmd_bouton_fouN())
        Bouton_fou.pack()
        Bouton_cavalier= ttk.Button(PopUp_promo, text= "Cavalier",command= cmd_bouton_cavalierN())
        Bouton_cavalier.pack()
        Bouton_pion= ttk.Button(PopUp_promo, text= "Garder un pion",command= cmd_bouton_pionN())
        Bouton_pion.pack()


#Pop up : gère le cas où la partie est nulle (cas du pat)
def open_popup_pat(couleur):
    import time
    global duree_de_la_partie
    duree_de_la_partie=time.time()-duree_de_la_partie
    PopUp_pat= Toplevel()
    PopUp_pat.geometry("750x300")
    PopUp_pat.title("Pat")
    PopUp_pat.iconbitmap(r'icone.ico')
    PopUp_pat.lift()
    Label(PopUp_pat, text= "Partie nulle", font=('Helvetica 35 bold')).pack(pady=10)
    if couleur=="Noir":
        Label(PopUp_pat, text= "Les Noirs sont pat", font=('Helvetica 15')).pack()
    else:
        Label(PopUp_pat, text= "Les Blancs sont pat", font=('Helvetica 15')).pack()
    Label(PopUp_pat, text= "Durée de la partie : "+str(duree_de_la_partie)+" s", font=('Helvetica 10')).pack()

#Pop up : si la partie est finie
def open_popup_perdu(couleur):
    import time
    global duree_de_la_partie
    duree_de_la_partie=time.time()-duree_de_la_partie
    top= Toplevel()
    top.geometry("750x450")
    top.title("Perduuuu")
    top.iconbitmap(r'icone.ico')
    top.lift()
    # Label(top, text= "T'as perdu LOL, looser !", font=('Helvetica 35 bold')).pack(pady=10)
    if couleur=="Noir":
        ch = str(prenom_noir.get()) + " a perdu. Bravo à " + str(prenom_blanc.get())
        # ch = str(prenom_noir.get()) + " a perdu LOL, looser!. Bravo à " + str(prenom_blanc.get())

        Label(top, text= ch , font=('Helvetica 25 bold')).pack(pady=10)
        Label(top, text= "Les Blancs ont gagné", font=('Helvetica 15')).pack()

        # img = ImageTk.PhotoImage(file="defaite_des_noirs.png")
        Label(top, image = python_imageperduN).pack(side = "bottom", fill = "both", expand = "yes")

        #j'ai essayé de rajouter une image, n'hésitez pas à corriger car l'image s'ouvre en trop grand
        #je l'ai corrigé (Lila)
        #NB: n'ouvre jamais des images dans le programme, c'est ce qui faisait buger l'nterface, faut les déclarer tous en haut, pour qu'on charge les images seulement une fois

    else:
        ch = str(prenom_blanc.get()) + " a perdu. Bravo à " + str(prenom_noir.get())

        Label(top, text= ch , font=('Helvetica 35 bold')).pack(pady=10)
        Label(top, text= "Les Noirs ont gagné", font=('Helvetica 15')).pack()

        # img = ImageTk.PhotoImage(file="defaite_des_blancs.png")

        Label(top, image = python_imageperduB).pack(side = "bottom", fill = "both", expand = "yes")
        #j'ai essayé de rajouter une image, n'hésitez pas à corriger car l'image s'ouvre en trop grand

    Label(top, text= "Durée de la partie : "+str(round(duree_de_la_partie))+" s", font=('Helvetica 10')).pack()
    top.mainloop() #j'ai mis ça pour afficher l'image mais ça fait bugger le temps je crois ??
    #personnaliser le message avec les prenoms

#Pop up du bouton commencer permettant de choisir qui joue les blancs/les noirs 
def pop_up_commencer():
    def cmd_lancer_bouton_prenom():
        import time
        global duree_de_la_partie
        global prenom_noir
        global prenom_blanc
        if entry_prenom_blanc.get() == "":
            prenom_blanc.set("Blanc")
        else: 
            prenom_blanc.set(entry_prenom_blanc.get())
        if entry_prenom_noir.get() == "":
            prenom_noir.set('Noir')
        else: 
            prenom_noir.set(entry_prenom_noir.get())
        duree_de_la_partie=time.time()
        Popup3.destroy()

    #Mise en place de la fenêtre pop up 
    Popup3 = Toplevel()
    Popup3.title('Faites un choix')
    Popup3.iconbitmap(r'icone.ico')

    Popup3.geometry("200x100")
    Popup3.grid_columnconfigure(0, weight=1)
    Popup3.grid_rowconfigure(0, weight=1)

    content3 = ttk.Frame(Popup3, padding=(0,0,0,0))
    content3.grid(column=0, row=0, sticky=(N, S, E, W))

    #Mise en place des widgets 

    entry_prenom_blanc = StringVar()
    entry_prenom_blanc.set("")

    entry_prenom_noir = StringVar()
    entry_prenom_noir.set("")

    Label_Choixcouleur = ttk.Label(content3, text= "Choix des couleurs",relief="solid",anchor=CENTER)
    Label_Choixcouleur.grid(column=0, row=0, columnspan=2, rowspan=2 ,sticky=(N,S,E,W),pady=1, padx=1)

    Label_Joueur1= ttk.Label(content3, text= "Blancs",relief="solid",anchor=CENTER)
    Label_Joueur1.grid(column=0, row=2, columnspan=1, rowspan=2 ,sticky=(N,S,E,W),pady=1, padx=1)

    Entry_Joueur1= ttk.Entry(content3, textvariable= entry_prenom_blanc)
    Entry_Joueur1.grid(column=1,row=2, columnspan=1, rowspan=2,sticky=(N,S,E,W),pady=1, padx=1)

    Label_Joueur2= ttk.Label(content3, text= "Noirs",relief="solid",anchor=CENTER)
    Label_Joueur2.grid(column=0, row=4, columnspan=1, rowspan=2 ,sticky=(N,S,E,W),pady=1, padx=1)

    Entry_Joueur2= ttk.Entry(content3, textvariable= entry_prenom_noir)
    Entry_Joueur2.grid(column=1,row=4, columnspan=1, rowspan=2,sticky=(N,S,E,W),pady=1, padx=1)

    Bouton_CompilerScript= ttk.Button(content3, text= "Lancer la partie",command= cmd_lancer_bouton_prenom)
    Bouton_CompilerScript.grid(column=0,row=6, columnspan=2, rowspan=2,sticky=(N,S,E,W),pady=1, padx=1)
    
    #Poids des colonnes et des lignes 
    for i in range(0,2):
        content3.columnconfigure(i,weight=1)

    for j in range(0,8):
        content3.rowconfigure(j,weight=1)

    Popup3.lift()                   #met la fenetre en premier plan
    Popup3.transient(root)          #on ne peut pas réduire cette pop up
    Popup3.grab_set()               #empeche ttes actions avec la fenetre principale
    root.wait_window(Popup3)        #Arrete le script principal tant que la fenetre n'est pas fermée

#Fonction de boutons abandonnés : 
def cmd_bouton_visuel():
    pass

def cmd_bouton_son():
    pass

# Fonction du bouton valider: gère la validation du coup
def cmd_bouton_valider():
    lettres = "a,b,c,d,e,f,g,h"
    chiffres = "1,2,3,4,5,6,7,8"
    special=["roque","ROQUE","abandon","","PEP"]
    position_ou_aller=coup.get()
    piece_bougee=piece_a_bouger.get()
    if (coup_special.get() in ["","PEP"]) and (len(position_ou_aller)!=2 or (position_ou_aller[0] not in lettres) or (position_ou_aller[1] not in chiffres)):
        message_erreur.set("Syntaxe incorrecte. Retentez.")
    if (coup_special.get() in ["","PEP"]) and (len(piece_bougee)!=2 or (piece_bougee[0] not in lettres) or (piece_bougee[1] not in chiffres)):
        message_erreur.set("Syntaxe incorrecte. Retentez.")
    if not(coup_special.get() in special):
        message_erreur.set("Syntaxe incorrecte. Retentez.")

    if message_erreur.get()=="":
        from board import position,KB1,KN1
        print("valider")
        from main import interpreteur
        global LPOSITION

        result=interpreteur(coup,piece_a_bouger,couleurA.get(),coup_special.get(),nbcoup)
        print(result)
        if result[0]:
            #global LPOSITION
            LPOSITION=fonction_lecture(position)
            if not (coup_special.get() in ["ROQUE","roque","PEP"]):
                ligne=coup.get()[1]
            nbcoup.set(str(int(nbcoup.get())+1))
            
            message_erreur.set("")

            if couleurA.get() == "Blanc":
                if KN1.Echec2():
                    message_echec.set("Les noirs sont en échec.")
                    print("Echec noir")
                    if KN1.Echec_et_mat(nbcoup):
                        print("Echec et mat.")
                        open_popup_perdu("Noir")
                if not (coup_special.get() in ["ROQUE","roque","PEP"]) and ligne=="8": #promotion de pion
                    open_popup_promo(result[2],"Blanc")
                    #from piece import promoDameB,promoTourB,promoFouB,promoCavalierB
                    #if choix_de_promotion=="Dame":
                        #promoDameB(result[2])
                    #elif choix_de_promotion=="Tour":
                        #promoTourB(result[2])
                    #elif choix_de_promotion=="Fou":
                        #promoFouB(result[2])
                    #elif choix_de_promotion=="Cavalier":
                        #promoCavalierB(result[2])
                couleurA.set("Noir")
                prenom.set(prenom_noir.get())
            else: #noirs
                if KB1.Echec2():
                    message_echec.set("Les blancs sont en échec.")
                    print("Echec blanc")
                    if KB1.Echec_et_mat(nbcoup):
                        print("Echec et mat.") ### afficher quelque part
                        open_popup_perdu("Blanc")
                if not (coup_special.get() in ["ROQUE","roque","PEP"]) and ligne=="1": #promotion de pion
                    open_popup_promo(result[2],"Noir")
                    #from piece import promoDameN,promoTourN,promoFouN,promoCavalierN
                    #if choix_de_promotion=="Dame":
                        #promoDameN(result[2])
                    #elif choix_de_promotion=="Tour":
                        #promoTourN(result[2])
                    #elif choix_de_promotion=="Fou":
                        #promoFouN(result[2])
                    #elif choix_de_promotion=="Cavalier":
                        #promoCavalierN(result[2])
                couleurA.set("Blanc")
                prenom.set(prenom_blanc.get())
            LPOSITION=fonction_lecture(position)
            coup.set("")
            piece_a_bouger.set("")
            coup_special.set("")
            afficherPiece()
            actualiserPiecesPrises()
            afficherPiecesPrises()
        elif result[0]==False:
            message_erreur.set(result[1])
            #print(message_erreur.get())

# Fonction du bouton commencer, gère la mise en place de la partie
def cmd_bouton_commencer():
    #appel pop up permettant de choisir les couleurs
    pop_up_commencer()

    #initialisation des variables tkinter 
    nbcoup.set("0")
    couleurA.set("Blanc")
    prenom.set(prenom_blanc.get())
    coup.set("")
    piece_a_bouger.set("")
    coup_special.set("")
    message_echec.set("")
    script.set("")
    message_echec.set("")

    if prenom_blanc.get()== "":
        # print("oui")
        prenom_blanc.set("Blanc")
    if prenom_noir.get() =="":
        prenom_noir.set("Noir")
    
    #Initialisation du tableau de position et des pièces prises 
    global LPOSITION
    global LPIECESPRISES

    LPOSITION= [["TB1","PB1",0,0,0,0,"PN1","TN1"],["CB1","PB2",0,0,0,0,"PN2","CN1"],["FB1","PB3",0,0,0,0,"PN3","FN1"],["QB1","PB4",0,0,0,0,"PN4","QN1"],["KB1","PB5",0,0,0,0,"PN5","KN1"],["FB2","PB6",0,0,0,0,"PN6","FN2"],["CB2","PB7",0,0,0,0,"PN7","CN2"],["TB2","PB8",0,0,0,0,"PN8","TN2"]]
    LPIECESPRISES = [[1 for i in range(8)] for j in range(4)]

    #On affiche les pièces, on actualise les pièces prises, puis on les affiche 
    afficherPiece()
    actualiserPiecesPrises()
    afficherPiecesPrises()
    # print("commencer")

#Fonction du bouton abandonner : ouvre la pop up 'perdu' si on perd
def cmd_bouton_abandonner():
    print("abandonner")
    if couleurA.get()=="Blanc":
        open_popup_perdu("Blanc")
    else:
        open_popup_perdu("Noir")

#Ancien bouton test utilisé pour voir si l'implémentation visuelle marche
def cmd_bouton_test():
    global LPOSITION
    LPOSITION= [["TB1","PB1",0,0,0,0,"PN1","TN1"],["CB1","PB2",0,0,0,0,"PN2","CN1"],["FB1","PB3",0,0,0,0,"PN3","FN1"],["QB1","PB4",0,0,0,0,"PN4","QN1"],["KB1",0,0,"PB5",0,0,"PN5","KN1"],["FB2","PB6",0,0,0,0,"PN6","FN2"],["CB2","PB7",0,0,0,0,"PN7","CN2"],["TB2","PB8",0,0,0,0,"PN8","TN2"]]
    print("test")
    message_erreur.set("bye bitch")

# def cmd_bouton_pieces_perdues():
#     pass

#Fonction du bouton complier script : permet de compiler un script 
def cmd_bouton_Compiler_script():
    script_compile=script.get() #
    script.set("") #
    interpreteur_script(script_compile)

#Fonction du bouton règle : permet d'afficher une pop up explicative
def cmd_bouton_regles():
    
    #Mise en place de la fenêtre pop up
    Popup = Toplevel()
    Popup.title('Règles de jeu')
    Popup.iconbitmap(r'icone.ico')

    Popup.geometry("500x500")
    Popup.grid_columnconfigure(0, weight=1)
    Popup.grid_rowconfigure(0, weight=1)
    Popup.lift()

    # Création du système d'onglets
    n = ttk.Notebook(Popup)   
    n.columnconfigure(0, weight=1)
    n.rowconfigure(0, weight=1)
    n.grid(column=0, row=0,sticky= NSEW)

    Onglet1_Regles = ttk.Frame(n,padding=(0,0,0,0))      
    Onglet2_Pion = ttk.Frame(n,padding=(0,0,0,0))      
    Onglet3_Fou = ttk.Frame(n,padding=(0,0,0,0))
    Onglet4_Tour = ttk.Frame(n,padding=(0,0,0,0))
    Onglet5_Cavalier = ttk.Frame(n,padding=(0,0,0,0))
    Onglet6_Dame = ttk.Frame(n,padding=(0,0,0,0))
    Onglet7_Roi = ttk.Frame(n,padding=(0,0,0,0))
    Onglet8_ActionSpe = ttk.Frame(n,padding=(0,0,0,0))
    Onglet9_Fin = ttk.Frame(n,padding=(0,0,0,0))


    Onglet1_Regles.grid(column=0, row=0, sticky=(N, S, E, W))
    Onglet2_Pion.grid(column=0, row=0, sticky=(N, S, E, W))
    Onglet3_Fou.grid(column=0, row=0, sticky=(N, S, E, W))
    Onglet4_Tour.grid(column=0, row=0, sticky=(N, S, E, W))
    Onglet5_Cavalier.grid(column=0, row=0, sticky=(N, S, E, W))
    Onglet6_Dame.grid(column=0, row=0, sticky=(N, S, E, W))
    Onglet7_Roi.grid(column=0, row=0, sticky=(N, S, E, W))
    Onglet8_ActionSpe.grid(column=0, row=0, sticky=(N, S, E, W))
    Onglet9_Fin.grid(column=0, row=0, sticky=(N, S, E, W))


    n.add(Onglet1_Regles, text='Règles générales')     
    n.add(Onglet2_Pion, text='Pion')      
    n.add(Onglet3_Fou, text='Fou')
    n.add(Onglet4_Tour, text='Tour')
    n.add(Onglet5_Cavalier, text='Cavalier')
    n.add(Onglet6_Dame, text='Dame')
    n.add(Onglet7_Roi, text='Roi')
    n.add(Onglet8_ActionSpe, text='Action Speciale')
    n.add(Onglet9_Fin, text='Fin de partie')

    # Onglet 1 : Regles
    # ch1 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam. Maecenas ligula massa, varius a, semper congue, euismod non, mi. Proin porttitor, orci nec nonummy molestie, enim est eleifend mi, non fermentum diam nisl sit amet erat. Duis semper. Duis arcu massa, scelerisque vitae, consequat in, pretium a, enim. Pellentesque congue. Ut in risus volutpat libero pharetra tempor. Cras vestibulum bibendum augue. Praesent egestas leo in pede. Praesent blandit odio eu enim. Pellentesque sed dui ut augue blandit sodales. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Aliquam nibh. Mauris ac mauris sed pede pellentesque fermentum. Maecenas adipiscing ante non diam sodales hendrerit. "
    ch1 = "\t\tLa partie d’échecs de Sofonisba Anguissola (1555)\n\nLe jeu d’échec est un jeu opposant deux joueurs de part et d’autre d’un échiquier composé de soixante-quatre cases, 32 cases blanches et 32 cases noires. Les joueurs jouent à tour de rôle en déplaçant l'une de leurs seize pièces (ou deux pièces en cas de roque), blanches pour le camp des blancs, noires pour le camp des noirs. Chaque joueur possède au départ un roi, une dame, deux tours, deux fous, deux cavaliers et huit pions. Le but du jeu est d'infliger à son adversaire un échec et mat, une situation dans laquelle le roi d'un joueur est en prise sans qu'il soit possible d'y remédier."
    ttk.Label(Onglet1_Regles, image = python_imageTableau, background = 'white',text= ch1 ,relief="solid",anchor= CENTER, compound='top',  wraplength=480).grid(column=0, row=0, columnspan=20, rowspan=20,sticky=(N,S,E,W),pady=1, padx=1)
    
    #Onglet 2: Pion
    ttk.Label(Onglet2_Pion, image= python_imageDF, text = "Les déplacements du pion se font verticalement, le pion est la seule pièce qui ne peut pas reculer. C’est aussi la seule pièce qui ne prend pas comme elle avance. Les pions avancent en effet d’une case sur la même colonne, si la case située devant eux est libre. Ils prennent sur l’une ou l’autre des deux cases situées devant eux en diagonale", compound = 'top', wraplength = "480", background = 'white',relief="solid",anchor=CENTER).grid(row = 0, column = 0, rowspan= 20, columnspan= 20,sticky=(N,S,E,W),pady=1, padx=1)

    #Onglet 3 : Fou
    ttk.Label(Onglet3_Fou, image= python_imageDF, text = "Les déplacements du fou se font diagonalement, il peut se déplacer d'autant de cases qu'il veut. Chaque joueur dispose au départ d’un Fou sur une case noire et d’un Fou sur une case blanche. Ces Fous ne pourront jamais changer de couleur durant toute la partie." , compound= 'top', wraplength = '480', background = 'white',relief="solid",anchor=CENTER).grid(row = 0, column = 0, rowspan= 20, columnspan= 20,sticky=(N,S,E,W),pady=1, padx=1)
    
    #Onglet 4 : Tour
    ttk.Label(Onglet4_Tour, wraplength="480",image= python_imageDT, text ="Les déplacements de la tour se font horizontalement et verticalement, elle se déplace d'autant de pièces qu'elle veut", compound ='top', background = 'white',relief="solid",anchor=CENTER).grid(row = 0, column = 0, rowspan= 20, columnspan= 20,sticky=(N,S,E,W),pady=1, padx=1)
    
    #Onglet 5 : Cavalier
    ttk.Label(Onglet5_Cavalier, image= python_imageDC, text = "Les déplacements du cavalier se font en forme de 'L'. Le cavalier ne peut être intercepté par aucune des pièces autour de lui, il saute jusqu'à sa case d'arrivée.", compound = 'top', background = 'white',relief="solid",anchor=CENTER, wraplength='480').grid(row = 0, column = 0, rowspan= 20, columnspan= 20,sticky=(N,S,E,W),pady=1, padx=1)
    
    #Onglet 6: Dame
    ttk.Label(Onglet6_Dame, wraplength = '480', text = "La Dame peut se déplacer comme la Tour et le Fou: elle peut donc se déplacer verticalement, horizontalement et en diagonale, d’autant de cases qu’elle veut.", compound= 'top', image= python_imageDD,background = 'white',relief="solid",anchor=CENTER).grid(row = 0, column = 0, rowspan= 20, columnspan= 20,sticky=(N,S,E,W),pady=1, padx=1)
    
    #Onglet 7 : Roi
    ttk.Label(Onglet7_Roi, image= python_imageDR, text = "Le Roi peut se déplacer dans toutes les directions, mais seulement de une case. Lorsqu’un Roi est attaqué par une pièce adverse, on dit qu’il est en échec. Un joueur n’a pas le droit de laisser son Roi en échec. Il n’a pas non plus le droit de déplacer son Roi sur une case où celui-ci sera attaqué (donc en échec).", compound ='top', wraplength = '480', background = 'white',relief="solid",anchor=CENTER).grid(row = 0, column = 0, rowspan= 20, columnspan= 20,sticky=(N,S,E,W),pady=1, padx=1)

    #Onglet 8 : Action spéciale
    ch2= "\t\t\t\tPrise en passant\nCoup spéciaux du pion :\n- Prise en passant : Lorsqu’un pion situé sur sa rangée de départ avance de deux cases et se retrouve à côté d’un pion adverse, alors l’adversaire peut, au coup suivant (et uniquement ce coup-là), prendre le pion qui vient d’avancer avec son pion comme si le pion adverse n’avait avancé que d’une case.\n- Promotion de pion: Lorsqu’un joueur avance un pion sur la dernière rangée, ou s’il prend avec un pion une pièce qui se trouve sur la dernière rangée, il doit le remplacer par une pièce de son choix (Dame, Tour, Fou ou Cavalier), de la même couleur, quelles que soient les pièces restantes sur l’échiquier. \nLe Roque: \nLorsque le Roi et cette Tour sont encore sur leurs cases initiales et qu’il n’y a plus de pièces entre eux, le joueur peut déplacer de deux cases le Roi vers la Tour, puis placer cette Tour sur la case juste à côté du Roi, de l’autre côté. Le roque peut être effectué sur l’aile roi (on parle alors de petit roque) ou sur l’aile dame (on parle alors de grand roque). Attention, si le roi est Roi est en échec, si une case qu’il doit traverser est attaquée ou si sa case d’arrivée est attaquée, alors le roque est interdit."
    ttk.Label(Onglet8_ActionSpe, image= python_imagePEP, text = ch2, compound = 'top', wraplength = '480', background = 'white',relief="solid",anchor=CENTER).grid(row = 0, column = 0, rowspan= 20, columnspan= 20,sticky=(N,S,E,W),pady=1, padx=1)

    #Onglet 9 : Fin de partie 
    ch3 = "\n\nUne partie d’échec peut avoir trois résultats: le gain des Blancs, le gain des Noirs ou un match nul. \nLe gain survient lors d'un échec et mat, ie lorsque l'échec ne peut être paré ou bien lorsqu'un des joueurs abandonne. \nUne partie est nulle dans les cas suivants:\n- Par accord mutuel entre les deux joueurs\n- En cas de PAT: si l’un des joueurs n’a aucun coup légal mais que son Roi n’est pas en échec\n- En cas de matériel insuffisant pour permettre le mat\n- Si la même position survient trois fois sur l’échiquier\n- Si les deux joueurs ont joué chacun 50 coups consécutifs sans poussée de pion ni prise de pièce"
    ttk.Label(Onglet9_Fin, text= ch3, image = python_imageEchecMate, compound = 'top',relief="solid",background = 'white',anchor=CENTER, wraplength=480).grid(column=0, row=0, columnspan=20, rowspan=20,sticky=(N,S,E,W),pady=1, padx=1)

    #On gère le poids des colonnes et des lignes dans les onglets 
    for i in range(20):
        Onglet1_Regles.columnconfigure(i,weight=1)
        Onglet2_Pion.columnconfigure(i,weight=1)
        Onglet3_Fou.columnconfigure(i,weight=1)
        Onglet4_Tour.columnconfigure(i,weight=1)
        Onglet5_Cavalier.columnconfigure(i,weight=1)
        Onglet6_Dame.columnconfigure(i,weight=1)
        Onglet7_Roi.columnconfigure(i,weight=1)
        Onglet8_ActionSpe.columnconfigure(i,weight=1)
        Onglet9_Fin.columnconfigure(i,weight=1)

    for j in range(20):
        Onglet1_Regles.rowconfigure(j,weight=1)
        Onglet2_Pion.rowconfigure(j,weight=1)
        Onglet3_Fou.rowconfigure(j,weight=1)
        Onglet4_Tour.rowconfigure(j,weight=1)
        Onglet5_Cavalier.rowconfigure(j,weight=1)
        Onglet6_Dame.rowconfigure(j,weight=1)
        Onglet7_Roi.rowconfigure(j,weight=1)
        Onglet8_ActionSpe.rowconfigure(j,weight=1)
        Onglet9_Fin.rowconfigure(j,weight=1)

#Fonction du bouton comment jouer : joue le role d'un README
def cmd_bouton_cmtjouer():
    Popup4 = Toplevel()
    Popup4.title('Comment jouer ?')
    Popup4.iconbitmap(r'icone.ico')
    Popup4.resizable(width=False, height=False)

    Popup4.geometry("500x340")
    Popup4.grid_columnconfigure(0, weight=1)
    Popup4.grid_rowconfigure(0, weight=1)

    content4 = ttk.Frame(Popup4, padding=(0,0,0,0))
    content4.grid(column=0, row=0, sticky=(N, S, E, W))

    Label_Explication = ttk.Label(content4, text= "Utilisation du logiciel : ",relief="solid",anchor=CENTER)
    Label_Explication.grid(column=0, row=0, columnspan=10, rowspan=1,sticky=(N,S,E,W),pady=1, padx=1)
    
    ch2= "1- Commencer la partie :\nAppuyez sur le bouton 'Nouvelle Partie' et choisissez ensuite qui joue les blancs ou les noirs. \n\n2- Entrer les coups:\nPour entrer les coups rien de plus simple! Il suffit d'indiquer les coordonnées de la pièces que vous vouler jouer, sous la forme 'a5' (colonne puis ligne) dans la 1e zone de saisie, puis d'entrer dans la deuxième zone de saisie l'endroit où vous voulez vous diriger. Si le coup est incorrect, le jeu l'indiquera.\n\n3- Coup spéciaux: Dans la zone de saisie 'Coup spécial', vous pouvez jouer :\n- Une prise en passant : 'PEP'\n- Un petit roque : 'roque'\n- Un grand roque : 'ROQUE'\n\n4- Fin de partie : \nLe jeu indiquera les échecs et l'échec et mat, dans ce cas la partie sera terminé. De plus, vous pouvez reconnaitre votre défaite, lorsque c'est votre tour, en appuyant sur le bouton 'Reconnaître sa cuisante défaite'."
    ttk.Label(content4, text = ch2, wraplength = "480", background = 'white',relief="solid",anchor=CENTER).grid(row = 1, column = 0, rowspan= 8, columnspan= 10,sticky=(N,S,E,W),pady=1, padx=1)

    for i in range(0,8):
        content4.columnconfigure(i,weight=1)

    for j in range(0,4):
        content4.rowconfigure(j,weight=1)

#Fonction du bouton options: permet d'accéder aux règles, au README adapté, à la compilation de script
def cmd_bouton_options():
    Popup2 = Toplevel()
    Popup2.title('Options')
    Popup2.resizable(width=False, height=False)
    Popup2.iconbitmap(r'icone.ico')

    Popup2.geometry("300x200")
    Popup2.grid_columnconfigure(0, weight=1)
    Popup2.grid_rowconfigure(0, weight=1)

    content2 = ttk.Frame(Popup2, padding=(0,0,0,0))
    content2.grid(column=0, row=0, sticky=(N, S, E, W))

    Label_Option = ttk.Label(content2, text= "Options : ",relief="solid",anchor=CENTER)
    Label_Option.grid(column=0, row=0, columnspan=2, rowspan=2 ,sticky=(N,S,E,W),pady=1, padx=1)

    Label_Script= ttk.Label(content2, text= "Entrer un script",relief="solid",anchor=CENTER)
    Label_Script.grid(column=0, row=2, columnspan=1, rowspan=2 ,sticky=(N,S,E,W),pady=1, padx=1)

    Entry_Script= ttk.Entry(content2, textvariable= script)
    Entry_Script.grid(column=1,row=2, columnspan=1, rowspan=2,sticky=(N,S,E,W),pady=1, padx=1)

    Bouton_CompilerScript= ttk.Button(content2, text= "Compiler le script",command= cmd_bouton_Compiler_script)
    Bouton_CompilerScript.grid(column=0,row=4, columnspan=2, rowspan=2,sticky=(N,S,E,W),pady=1, padx=1)

    Bouton_Regles2= ttk.Button(content2, text= "Règles du jeu",command= cmd_bouton_regles)
    Bouton_Regles2.grid(column=0,row=6, columnspan=2, rowspan=2,sticky=(N,S,E,W),pady=1, padx=1)

    Bouton_CmtJouer= ttk.Button(content2, text= "Comment jouer ?",command= cmd_bouton_cmtjouer)
    Bouton_CmtJouer.grid(column=0,row=8, columnspan=2, rowspan=2,sticky=(N,S,E,W),pady=1, padx=1)

    # Bouton_Visuels= ttk.Button(content2, text= "Changer les pièces :)",command= cmd_bouton_visuel)
    # Bouton_Visuels.grid(column=0,row=8, columnspan=2, rowspan=2,sticky=(N,S,E,W),pady=1, padx=1)

    # Bouton_son= ttk.Button(content2, text= "Activer/Desactiver le son",command= cmd_bouton_son)
    # Bouton_son.grid(column=0,row=10, columnspan=2, rowspan=2,sticky=(N,S,E,W),pady=1, padx=1)

    for i in range(0,2):
        content2.columnconfigure(i,weight=1)

    for j in range(0,10):
        content2.rowconfigure(j,weight=1)

    

    
#permet l'expension des boutons 
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
    
for i in range(0,28):
    content.columnconfigure(i,weight=1)

for j in range(0,18):
    content.rowconfigure(j,weight=1)

#on peut facilement retirer les bordures en retirant relief
largeur = 8

#Tous les labels, entry et boutons

Lvide = ttk.Label(content, text= "",relief="solid",anchor=CENTER)
Lvide.grid(column=18, row=0, columnspan=2, rowspan=18,sticky=(N,S,E,W),pady=1, padx=1)

Bouton_commencer = Button(content, text= "Nouvelle Partie",command= cmd_bouton_commencer,relief="solid",highlightbackground="red", activebackground="grey",highlightcolor="red",background="white")
Bouton_commencer.grid(column=20, row=0, columnspan=largeur, rowspan=2,sticky=(N,S,E,W),pady=1, padx=1)

##
Label_couleurquijoue = ttk.Label(content, text= "Personne qui joue",relief="solid",anchor=CENTER)
Label_couleurquijoue.grid(column=20, row=2, columnspan=int(largeur/4), rowspan=1,sticky=(N,S,E,W),pady=1, padx=1)

Label_couleuractualise= ttk.Label(content, textvariable= couleurA, anchor= CENTER, relief="solid")
Label_couleuractualise2= ttk.Label(content, textvariable= prenom, anchor= CENTER, relief="solid")
Label_couleuractualise2.grid(column=20+int(largeur/4),row=2, columnspan=int(largeur/4), rowspan=1,sticky=(N,S,E,W),pady=1, padx=1)
##
 
##
Label_Nbcoup = ttk.Label(content, text= "Coup n°",relief="solid",anchor=CENTER)
Label_Nbcoup.grid(column=20 + int(largeur/2), row=2, columnspan=int(largeur/4), rowspan=1 ,sticky=(N,S,E,W),pady=1, padx=1)

Label_coup_actualise= ttk.Label(content, textvariable= nbcoup, anchor = CENTER, relief = "solid")
Label_coup_actualise.grid(column=20 +3*int(largeur/4),row=2, columnspan=int(largeur/4), rowspan=1,sticky=(N,S,E,W),pady=1, padx=1)
## 

Lpieceabouger = ttk.Label(content, text= "Pièce à bouger",relief="solid",anchor=CENTER)
Lpieceabouger.grid(column=20, row=4, columnspan=largeur, rowspan=1,sticky=(N,S,E,W),pady=1, padx=1)

Entry_pieceabouger= ttk.Entry(content, textvariable= piece_a_bouger)
Entry_pieceabouger.grid(column=20,row=5, columnspan=largeur, rowspan=1,sticky=(N,S,E,W),pady=1, padx=1)

Label_coupajouer = ttk.Label(content, text= "Coup à jouer",relief="solid",anchor=CENTER)
Label_coupajouer.grid(column=20, row=6, columnspan=largeur, rowspan=1,sticky=(N,S,E,W),pady=1, padx=1)

Entry_coup= ttk.Entry(content, textvariable= coup)
Entry_coup.grid(column=20,row=7, columnspan=largeur, rowspan=1,sticky=(N,S,E,W),pady=1, padx=1)

Bouton_valider= ttk.Button(content, text= "Valider",command= cmd_bouton_valider)
Bouton_valider.grid(column=20,row=9, columnspan=largeur, rowspan=2,sticky=(N,S,E,W),pady=1, padx=1)

# Bouton_test= ttk.Button(content, text= "Bouton TEST",command= cmd_bouton_test)
# Bouton_test.grid(column=20,row=15, columnspan=largeur, rowspan=1,sticky=(N,S,E,W),pady=1, padx=1)

Label_CoupSpecial= ttk.Label(content, text= "Coup spécial",relief="solid",anchor=CENTER)
Label_CoupSpecial.grid(column=20, row=8, columnspan=int(largeur/2), rowspan=1 ,sticky=(N,S,E,W),pady=1, padx=1)

Entry_CoupSpecial= ttk.Entry(content, textvariable= coup_special)
Entry_CoupSpecial.grid(column=20 + int(largeur/2),row=8, columnspan=int(largeur/2), rowspan=1,sticky=(N,S,E,W),pady=1, padx=1)

Bouton_Options= ttk.Button(content, text= "Options",command= cmd_bouton_options)
Bouton_Options.grid(column=20,row=16, columnspan=largeur, rowspan=1,sticky=(N,S,E,W),pady=1, padx=1)

# Label_Script= ttk.Label(content, text= "Script",relief="solid",anchor=CENTER)
# Label_Script.grid(column=20, row=15, columnspan=2, rowspan=1 ,sticky=(N,S,E,W),pady=1, padx=1)

# Entry_Script= ttk.Entry(content, textvariable= script)
# Entry_Script.grid(column=22,row=15, columnspan=int(largeur/2), rowspan=1,sticky=(N,S,E,W),pady=1, padx=1)

Bouton_Abandonner= ttk.Button(content, text= "Reconnaître sa cuisante défaite",command= cmd_bouton_abandonner)
Bouton_Abandonner.grid(column=20,row=17, columnspan=largeur, rowspan=1,sticky=(N,S,E,W),pady=1, padx=1)

Label_actualiseerreur= ttk.Label(content, textvariable= message_erreur, anchor= CENTER, relief="solid", foreground = 'orange', background='white')
Label_actualiseerreur.grid(column=20,row=11, columnspan=largeur, rowspan=1,sticky=(N,S,E,W),pady=1, padx=1)

Lechec = ttk.Label(content, textvariable= message_echec,relief="solid",anchor=CENTER, foreground='red')
Lechec.grid(column=20, row=3, columnspan=largeur, rowspan=1,sticky=(N,S,E,W),pady=1, padx=1)

# Label_piecesperdues= ttk.Label(content, text= "Pièces perdues",relief="solid",anchor=CENTER)
# Label_piecesperdues.grid(column=20, row=13, columnspan = largeur, rowspan=1 ,sticky=(N,S,E,W))

# permet de faire une boucle visuelle 
root.mainloop()

# dicopieceB = {"TB1":"","CB1":"","FB1":"","QB1":"","KB1":"","FB2":"","CB2":"","TB2":""}
# dicopieceN= {"TN1":"","CN1":"","FN1":"","QN1":"","KN1":"","FN2":"","CN2":"","TN2":""}
# dicopiecepionB = {"PB1":"","PB2":"","PB3":"","PB4":"","PB5":"","PB6":"","PB7":"","PB8":""}
# dicopiecepionN = {"PN1":"","PN2":"","PN3":"","PN4":"","PN5":"","PN6":"","PN7":"","PN8":""}





