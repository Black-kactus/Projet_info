#Ancien fichier : gestion de l'interface (version de sauvegarde)

# ajout de pop up
# ajout de label avec erreur actualisé 
# implémentation du retournement de plateau dans le jeu!
# :))

from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from time import *

# # #pour récupérer la liste des positions
# from board import position
# from piece import*
# from new_interface import Entry_pieceabouger
# def fonction_lecture(position):
#     LPOSITION=[]
#     for l in range(len(position)):
#         LPOSITION.append([])
#         for j in range(8):
#             if position[l][j]==0:
#                 LPOSITION[l].append(0)
#             else:
#                 LPOSITION[l].append(str(position[l][j]))
#     return(LPOSITION)


root = Tk()
root.title("Jeu d'échec - Lila ~ Lou ~ Raphaël")
root.iconbitmap(r'icone.ico')

content = ttk.Frame(root, padding=(0,0,0,0))
frame = ttk.Frame(content, borderwidth=0, relief="ridge", width=100, height=100)
content.grid(column=0, row=0, sticky=(N, S, E, W))

# Variables de Tkinter
piece_a_bouger = StringVar()
piece_a_bouger.set("Position piece à bouger")

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
python_imageVIDE= ImageTk.PhotoImage(ImgVide)

dicopiece = {0 : python_imageVIDE}
dicopieceB = {"TB1": python_imageTB,"CB1": python_imageCB,"FB1": python_imageFB,"QB1":python_imageDB,"KB1":python_imageRB,"FB2":python_imageFB,"CB2":python_imageCB,"TB2":python_imageTB}
dicopieceN= {"TN1":python_imageTN,"CN1":python_imageCN,"FN1":python_imageFN,"QN1":python_imageDN,"KN1":python_imageRN,"FN2":python_imageFN,"CN2":python_imageCN,"TN2":python_imageTN}
dicopiecepionB = {"PB1": python_imagePB, "PB2":python_imagePB,"PB3":python_imagePB,"PB4":python_imagePB,"PB5":python_imagePB,"PB6":python_imagePB,"PB7":python_imagePB,"PB8":python_imagePB}
dicopiecepionN = {"PN1":python_imagePN,"PN2":python_imagePN,"PN3":python_imagePN,"PN4":python_imagePN,"PN5":python_imagePN,"PN6":python_imagePN,"PN7":python_imagePN,"PN8":python_imagePN}

dicopiece.update(dicopieceB)
dicopiece.update(dicopieceN)
dicopiece.update(dicopiecepionB)
dicopiece.update(dicopiecepionN)

#Creation des indices horizontaux de l'échiquier
# for i in range(0,18,2):
#     # L = ["","A",'B',"C","D","E","F",'G','H']
#     L = ["","H","G",'F',"E","D","C","B",'A']
#     namelbl = ttk.Label(content, text= str(int(9-i/2)),relief="solid",anchor=CENTER)
#     namelbl.grid(column=0, row=i, columnspan=2, rowspan=2,sticky=(N,S,E,W),pady=1, padx=1)
#     namelbl = ttk.Label(content, text= L[int(i/2)],relief="solid",anchor=CENTER)
#     namelbl.grid(column=i, row=0, columnspan=2, rowspan=2,sticky=(N,S,E,W),pady=1, padx=1)



#Liste des positions renvoyées par Raph
LPOSITION= [["TB1","PB1",0,0,0,0,"PN1","TN1"],["CB1","PB2",0,0,0,0,"PN2","CN1"],["FB1","PB3",0,0,0,0,"PN3","FN1"],["QB1","PB4",0,0,0,0,"PN4","QN1"],["KB1","PB5",0,0,0,0,"PN5","KN1"],["FB2","PB6",0,0,0,0,"PN6","FN2"],["CB2","PB7",0,0,0,0,"PN7","CN2"],["TB2","PB8",0,0,0,0,"PN8","TN2"]]



def afficherPiece():
    global LPOSITION
    for i in range(len(LPOSITION)) : 
        for j in range(len(LPOSITION)):
            if (i+j)%2 == 0: couleur = 'black'
            else : couleur = "white"
            if couleurA.get() == "Noir":
                ttk.Label(content, image=dicopiece[LPOSITION[7-j][i]],background = couleur,relief="solid",anchor=CENTER).grid(row = 2*i+2, column = 2*j+2, rowspan= 2, columnspan= 2,sticky=(N,S,E,W),pady=1, padx=1)
            else : 
                ttk.Label(content, image=dicopiece[LPOSITION[j][7-i]],background = couleur,relief="solid",anchor=CENTER).grid(row = 2*i+2, column = 2*j+2, rowspan= 2, columnspan= 2,sticky=(N,S,E,W),pady=1, padx=1)
    
    if couleurA.get() == "Blanc":
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

def cmd_bouton_valider():
    nbcoup.set(str(int(nbcoup.get())+1))
    if couleurA.get() == "Blanc": 
        couleurA.set("Noir")

    else:
        couleurA.set("Blanc")
    afficherPiece()

def cmd_bouton_commencer():
    nbcoup.set("0")
    couleurA.set("Blanc")
    global LPOSITION
    LPOSITION= [["TB1","PB1",0,0,0,0,"PN1","TN1"],["CB1","PB2",0,0,0,0,"PN2","CN1"],["FB1","PB3",0,0,0,0,"PN3","FN1"],["QB1","PB4",0,0,0,0,"PN4","QN1"],["KB1","PB5",0,0,0,0,"PN5","KN1"],["FB2","PB6",0,0,0,0,"PN6","FN2"],["CB2","PB7",0,0,0,0,"PN7","CN2"],["TB2","PB8",0,0,0,0,"PN8","TN2"]]
    afficherPiece()
    print("commencer")

def cmd_bouton_abandonner():
    print("abandonner")

def cmd_bouton_test():
    global LPOSITION
    LPOSITION= [["TB1","PB1",0,0,0,0,"PN1","TN1"],["CB1","PB2",0,0,0,0,"PN2","CN1"],["FB1","PB3",0,0,0,0,"PN3","FN1"],["QB1","PB4",0,0,0,0,"PN4","QN1"],["KB1","PB5",0,0,0,0,"PN5","KN1"],["FB2","PB6",0,0,0,0,"PN6","FN2"],["CB2",0,"PB7",0,0,0,"PN7","CN2"],["TB2","PB8",0,0,0,0,"PN8","TN2"]]
    print("test")

def cmd_bouton_pieces_perdues():
    pass

def cmd_bouton_regles():
    pass


root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
    
for i in range(0,24):
    content.columnconfigure(i,weight=1)

for j in range(0,18):
    content.rowconfigure(j,weight=1)

#on peut facilement retirer les bordures en retirant relief
largeur = 4

Lvide = ttk.Label(content, text= "",relief="solid",anchor=CENTER)
Lvide.grid(column=18, row=0, columnspan=2, rowspan=18,sticky=(N,S,E,W),pady=1, padx=1)

Bouton_commencer = Button(content, text= "Nouvelle Partie",command= cmd_bouton_commencer,relief="solid",highlightbackground="red", activebackground="grey",highlightcolor="red",background="white")
Bouton_commencer.grid(column=20, row=0, columnspan=largeur, rowspan=2,sticky=(N,S,E,W),pady=1, padx=1)

Label_couleurquijoue = ttk.Label(content, text= "Couleur qui joue",relief="solid",anchor=CENTER)
Label_couleurquijoue.grid(column=20, row=2, columnspan=int(largeur/4), rowspan=1,sticky=(N,S,E,W),pady=1, padx=1)

Label_couleuractualise= ttk.Label(content, textvariable= couleurA, anchor= CENTER, relief="solid")
Label_couleuractualise.grid(column=22,row=2, columnspan=largeur, rowspan=1,sticky=(N,S,E,W),pady=1, padx=1)

Label_Nbcoup = ttk.Label(content, text= "coup n°",relief="solid",anchor=CENTER)
Label_Nbcoup.grid(column=22, row=3, columnspan=2, rowspan=1 ,sticky=(N,S,E,W),pady=1, padx=1)

Label_coup_actualise= ttk.Label(content, textvariable= nbcoup, anchor = CENTER, relief = "solid")
Label_coup_actualise.grid(column=24,row=3, columnspan=int(largeur/2), rowspan=1,sticky=(N,S,E,W),pady=1, padx=1)

Lpieceabouger = ttk.Label(content, text= "Piece à bouger",relief="solid",anchor=CENTER)
Lpieceabouger.grid(column=20, row=4, columnspan=largeur, rowspan=1,sticky=(N,S,E,W),pady=1, padx=1)

Entry_pieceabouger= ttk.Entry(content, textvariable= piece_a_bouger)
Entry_pieceabouger.grid(column=20,row=5, columnspan=largeur, rowspan=1,sticky=(N,S,E,W),pady=1, padx=1)

Label_coupajouer = ttk.Label(content, text= "Coup à jouer",relief="solid",anchor=CENTER)
Label_coupajouer.grid(column=20, row=6, columnspan=largeur, rowspan=1,sticky=(N,S,E,W),pady=1, padx=1)

Entry_coup= ttk.Entry(content, textvariable= coup)
Entry_coup.grid(column=20,row=7, columnspan=largeur, rowspan=1,sticky=(N,S,E,W),pady=1, padx=1)

Bouton_valider= ttk.Button(content, text= "Valider",command= cmd_bouton_valider)
Bouton_valider.grid(column=20,row=9, columnspan=largeur, rowspan=1,sticky=(N,S,E,W),pady=1, padx=1)

Bouton_test= ttk.Button(content, text= "Bouton TEST",command= cmd_bouton_test)
Bouton_test.grid(column=20,row=15, columnspan=largeur, rowspan=1,sticky=(N,S,E,W),pady=1, padx=1)

Label_CoupSpecial= ttk.Label(content, text= "coup spécial:",relief="solid",anchor=CENTER)
Label_CoupSpecial.grid(column=20, row=8, columnspan=2, rowspan=1 ,sticky=(N,S,E,W),pady=1, padx=1)

Entry_CoupSpecial= ttk.Entry(content, textvariable= coup_special)
Entry_CoupSpecial.grid(column=22,row=8, columnspan=int(largeur/2), rowspan=1,sticky=(N,S,E,W),pady=1, padx=1)

Bouton_Piecesperdues= ttk.Button(content, text= "Bilan des pièces perdues",command= cmd_bouton_pieces_perdues)
Bouton_Piecesperdues.grid(column=20,row=11, columnspan=largeur, rowspan=1,sticky=(N,S,E,W),pady=1, padx=1)

Bouton_Regles= ttk.Button(content, text= "Consulter les règles",command= cmd_bouton_regles)
Bouton_Regles.grid(column=20,row=16, columnspan=largeur, rowspan=1,sticky=(N,S,E,W),pady=1, padx=1)

Bouton_Abandonner= ttk.Button(content, text= "Reconnaître sa cuisante défaite",command= cmd_bouton_abandonner)
Bouton_Abandonner.grid(column=20,row=17, columnspan=largeur, rowspan=1,sticky=(N,S,E,W),pady=1, padx=1)

root.mainloop()

# dicopieceB = {"TB1":"","CB1":"","FB1":"","QB1":"","KB1":"","FB2":"","CB2":"","TB2":""}
# dicopieceN= {"TN1":"","CN1":"","FN1":"","QN1":"","KN1":"","FN2":"","CN2":"","TN2":""}
# dicopiecepionB = {"PB1":"","PB2":"","PB3":"","PB4":"","PB5":"","PB6":"","PB7":"","PB8":""}
# dicopiecepionN = {"PN1":"","PN2":"","PN3":"","PN4":"","PN5":"","PN6":"","PN7":"","PN8":""}
