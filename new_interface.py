#La véritable fenêtre d'interface 


from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from time import *

# # #pour récupérer la liste des positions
# from board import position
# from piece import*
# from new_interface import Entry_pieceabouger
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


def interpreteur_script(script):
    import time
    #from new_interface import coup_special,coup,piece_a_bouger
    #from new_interface import LPOSITION, fonction_lecture, couleurA,nbcoup,message_erreur,afficherPiece
    #from new_interface import cmd_bouton_valider
    script = script.split(' ')
    #L=[]
    #for i in range(0,len(script),2):
        #L.append([script[i].split("-"),script[i+1].split("-")])
    for i in range(len(script)):
        #time.sleep(10)
        coup_script=script[i].split("-")
        print(coup_script, type(coup_script))
        #L.append(script[i].split("-"))
        if len(coup_script)==1:
            coup_special.set(coup_script[0])
            print(coup_special.get())
        elif len(coup_script)==2:
            piece_a_bouger.set(coup_script[0])
            coup.set(coup_script[1])
        cmd_bouton_valider()




root = Tk()
root.title("Jeu d'échec - Lila ~ Lou ~ Raphaël")
root.iconbitmap(r'icone.ico')

content = ttk.Frame(root, padding=(0,0,0,0))
frame = ttk.Frame(content, borderwidth=0, relief="ridge", width=100, height=100)

content.grid(column=0, row=0, sticky=(N, S, E, W))

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
#     L = ["","A",'B',"C","D","E","F",'G','H']
#     ttk.Label(content, text= str(int(9-i/2)),relief="solid",anchor=CENTER).grid(column=0, row=i, columnspan=2, rowspan=2,sticky=(N,S,E,W),pady=1, padx=1)
#     ttk.Label(content, text= L[int(i/2)],relief="solid",anchor=CENTER).grid(column=i, row=0, columnspan=2, rowspan=2,sticky=(N,S,E,W),pady=1, padx=1)



#Liste des positions renvoyées par Raph
LPOSITION= [["TB1","PB1",0,0,0,0,"PN1","TN1"],["CB1","PB2",0,0,0,0,"PN2","CN1"],["FB1","PB3",0,0,0,0,"PN3","FN1"],["QB1","PB4",0,0,0,0,"PN4","QN1"],["KB1","PB5",0,0,0,0,"PN5","KN1"],["FB2","PB6",0,0,0,0,"PN6","FN2"],["CB2","PB7",0,0,0,0,"PN7","CN2"],["TB2","PB8",0,0,0,0,"PN8","TN2"]]
# LPIECESPRISES = [[1,1,0,1,0,1,1,0],[1,0,1,0,1,0,1,1],[1,0,1,1,1,0,1,1],[1,0,1,1,0,1,1,1]]
LPIECESPRISES = [[1,1,0,1,0,1,1,0],[1,0,1,0,1,0,1,1],[1,0,1,1,1,0,1,1],[1,0,1,1,0,1,1,1]]
LIMAGESPICESPRISES = [[python_imageTB2, python_imageCB2, python_imageFB2, python_imageDB2, python_imageRB2, python_imageFB2, python_imageCB2, python_imageTB2], [python_imageTN2, python_imageCN2, python_imageFN2, python_imageDN2, python_imageRN2, python_imageFN2, python_imageCN2, python_imageTN2] ]

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

def afficherPiecesPrises():
    global LPIECESPRISES
    global LIMAGESPICESPRISES
    couleurBg = 'white'
    couleurBg2 = 'black'
    for i in range(8):
        if LPIECESPRISES[0][i] == 0: ttk.Label(content, anchor= CENTER, relief="solid", background= couleurBg2, image = LIMAGESPICESPRISES[1][i]).grid(column=20+i,row=12, columnspan=1, rowspan = 1 ,sticky=(N,S,E,W))
        else : ttk.Label(content, anchor= CENTER, relief="solid",image = python_imageVIDE2, background = couleurBg2).grid(column=20+i,row=12, columnspan=1, rowspan = 1 ,sticky=(N,S,E,W))
        
        if LPIECESPRISES[1][i] == 0:  ttk.Label(content, anchor= CENTER, relief="solid", background=couleurBg2, image = python_imagePN2).grid(column=20+i,row=13, columnspan=1, rowspan = 1 ,sticky=(N,S,E,W))
        else :  ttk.Label(content, anchor= CENTER, relief="solid",image = python_imageVIDE2,background = couleurBg2).grid(column=20+i,row=13, columnspan=1, rowspan = 1 ,sticky=(N,S,E,W))

        if LPIECESPRISES[2][i] == 0 : ttk.Label(content, textvariable= "", anchor= CENTER, relief="solid",background= couleurBg, image = python_imagePB2).grid(column=20+i,row=14, columnspan=1, rowspan = 1 ,sticky=(N,S,E,W))
        else: ttk.Label(content, textvariable= "", anchor= CENTER, relief="solid", image = python_imageVIDE2, background =couleurBg).grid(column=20+i,row=14, columnspan=1, rowspan = 1 ,sticky=(N,S,E,W))

        if LPIECESPRISES[3][i] == 0 :  ttk.Label(content, textvariable= "", anchor= CENTER, relief="solid",background=couleurBg,image = LIMAGESPICESPRISES[0][i]).grid(column=20+i,row=15, columnspan=1, rowspan = 1 ,sticky=(N,S,E,W))
        else:  ttk.Label(content, textvariable= "", anchor= CENTER, relief="solid", image= python_imageVIDE2, background = couleurBg).grid(column=20+i,row=15, columnspan=1, rowspan = 1 ,sticky=(N,S,E,W))
       
def actualiserPiecesPrises():
    global LPOSITION
    # LPOSITION= [[0,0,0,0,0,0,"PN1","TN1"],["CB1","PB2",0,0,0,0,"PN2","CN1"],["FB1","PB3",0,0,0,0,"PN3","FN1"],["QB1","PB4",0,0,0,0,"PN4","QN1"],["KB1","PB5",0,0,0,0,"PN5","KN1"],["FB2","PB6",0,0,0,0,"PN6","FN2"],["CB2","PB7",0,0,0,0,"PN7","CN2"],["TB2","PB8",0,0,0,0,"PN8","TN2"]]
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
    print("TN1" in LPOSITION)

    print(LPIECESPRISES)

def cmd_bouton_valider():
    #lettres = "a,b,c,d,e,f,g,h"
    #chiffres = "1,2,3,4,5,6,7,8"
    #position_ou_aller=coup.get()
    #piece_bougee=piece_a_bouger.get()
    #while len(position_ou_aller)!=2 or (position_ou_aller[0] not in lettres) or (position_ou_aller[1] not in chiffres):
        #message_erreur.set("Syntaxe incorrecte. Retentez.")
    #while len(piece_bougee)!=2 or (piece_bougee[0] not in lettres) or (piece_bougee[1] not in chiffres):
        #message_erreur.set("Syntaxe incorrecte. Retentez.")
    
    from board import position
    print("valider")
    from main import interpreteur

    if len(coup_special.get())>10: #
        script=coup_special.get() #
        coup_special.set("") #
        interpreteur_script(script) #


    elif not(interpreteur(coup,piece_a_bouger,couleurA,coup_special.get())[0]==False):
        global LPOSITION
        LPOSITION=fonction_lecture(position)
        
        nbcoup.set(str(int(nbcoup.get())+1))
        coup.set("")
        piece_a_bouger.set("")
        message_erreur.set("")
        coup_special.set("")

        if couleurA.get() == "Blanc": 
            couleurA.set("Noir")
        else:
            couleurA.set("Blanc")
        
        afficherPiece()
        actualiserPiecesPrises()
        afficherPiecesPrises()
    else:
        message_erreur.set(interpreteur(coup,piece_a_bouger,couleurA,coup_special.get())[1])
        #print(message_erreur.get())


def cmd_bouton_commencer():
    nbcoup.set("0")
    couleurA.set("Blanc")
    global LPOSITION
    global LPIECESPRISES

    LPOSITION= [["TB1","PB1",0,0,0,0,"PN1","TN1"],["CB1","PB2",0,0,0,0,"PN2","CN1"],["FB1","PB3",0,0,0,0,"PN3","FN1"],["QB1","PB4",0,0,0,0,"PN4","QN1"],["KB1","PB5",0,0,0,0,"PN5","KN1"],["FB2","PB6",0,0,0,0,"PN6","FN2"],["CB2","PB7",0,0,0,0,"PN7","CN2"],["TB2","PB8",0,0,0,0,"PN8","TN2"]]
    LPIECESPRISES = [[1 for i in range(8)] for j in range(4)]

    afficherPiece()
    actualiserPiecesPrises()
    afficherPiecesPrises()
    # print("commencer")

def cmd_bouton_abandonner():
    print("abandonner")

def cmd_bouton_test():
    global LPOSITION
    LPOSITION= [["TB1","PB1",0,0,0,0,"PN1","TN1"],["CB1","PB2",0,0,0,0,"PN2","CN1"],["FB1","PB3",0,0,0,0,"PN3","FN1"],["QB1","PB4",0,0,0,0,"PN4","QN1"],["KB1",0,0,"PB5",0,0,"PN5","KN1"],["FB2","PB6",0,0,0,0,"PN6","FN2"],["CB2","PB7",0,0,0,0,"PN7","CN2"],["TB2","PB8",0,0,0,0,"PN8","TN2"]]
    print("test")
    message_erreur.set("bye bitch")

def cmd_bouton_pieces_perdues():
    pass

def cmd_bouton_regles():
    pass

def cmd_bouton_options():
    pass
#permet l'expension des boutons 
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
    
for i in range(0,28):
    content.columnconfigure(i,weight=1)

for j in range(0,18):
    content.rowconfigure(j,weight=1)

#on peut facilement retirer les bordures en retirant relief
largeur = 8

Lvide = ttk.Label(content, text= "",relief="solid",anchor=CENTER)
Lvide.grid(column=18, row=0, columnspan=2, rowspan=18,sticky=(N,S,E,W),pady=1, padx=1)

Bouton_commencer = Button(content, text= "Nouvelle Partie",command= cmd_bouton_commencer,relief="solid",highlightbackground="red", activebackground="grey",highlightcolor="red",background="white")
Bouton_commencer.grid(column=20, row=0, columnspan=largeur, rowspan=2,sticky=(N,S,E,W),pady=1, padx=1)

##
Label_couleurquijoue = ttk.Label(content, text= "Couleur qui joue",relief="solid",anchor=CENTER)
Label_couleurquijoue.grid(column=20, row=2, columnspan=int(largeur/2), rowspan=1,sticky=(N,S,E,W),pady=1, padx=1)

Label_couleuractualise= ttk.Label(content, textvariable= couleurA, anchor= CENTER, relief="solid")
Label_couleuractualise.grid(column=20+int(largeur/2),row=2, columnspan=int(largeur/2), rowspan=1,sticky=(N,S,E,W),pady=1, padx=1)
##
 
##
Label_Nbcoup = ttk.Label(content, text= "coup n°",relief="solid",anchor=CENTER)
Label_Nbcoup.grid(column=20, row=3, columnspan=int(largeur/2), rowspan=1 ,sticky=(N,S,E,W),pady=1, padx=1)

Label_coup_actualise= ttk.Label(content, textvariable= nbcoup, anchor = CENTER, relief = "solid")
Label_coup_actualise.grid(column=20 + int(largeur/2),row=3, columnspan=int(largeur/2), rowspan=1,sticky=(N,S,E,W),pady=1, padx=1)
## 

Lpieceabouger = ttk.Label(content, text= "Piece à bouger",relief="solid",anchor=CENTER)
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

Label_CoupSpecial= ttk.Label(content, text= "coup spécial:",relief="solid",anchor=CENTER)
Label_CoupSpecial.grid(column=20, row=8, columnspan=int(largeur/2), rowspan=1 ,sticky=(N,S,E,W),pady=1, padx=1)

Entry_CoupSpecial= ttk.Entry(content, textvariable= coup_special)
Entry_CoupSpecial.grid(column=20 + int(largeur/2),row=8, columnspan=int(largeur/2), rowspan=1,sticky=(N,S,E,W),pady=1, padx=1)

# Bouton_Piecesperdues= ttk.Button(content, text= "Bilan des pièces perdues",command= cmd_bouton_pieces_perdues)
# Bouton_Piecesperdues.grid(column=20,row=11, columnspan=largeur, rowspan=1,sticky=(N,S,E,W),pady=1, padx=1)

Bouton_Options= ttk.Button(content, text= "Options",command= cmd_bouton_options)
Bouton_Options.grid(column=20,row=16, columnspan=largeur, rowspan=1,sticky=(N,S,E,W),pady=1, padx=1)

# Label_Script= ttk.Label(content, text= "Script",relief="solid",anchor=CENTER)
# Label_Script.grid(column=20, row=15, columnspan=2, rowspan=1 ,sticky=(N,S,E,W),pady=1, padx=1)

# Entry_Script= ttk.Entry(content, textvariable= script)
# Entry_Script.grid(column=22,row=15, columnspan=int(largeur/2), rowspan=1,sticky=(N,S,E,W),pady=1, padx=1)

Bouton_Abandonner= ttk.Button(content, text= "Reconnaître sa cuisante défaite",command= cmd_bouton_abandonner)
Bouton_Abandonner.grid(column=20,row=17, columnspan=largeur, rowspan=1,sticky=(N,S,E,W),pady=1, padx=1)

Label_actualiseerreur= ttk.Label(content, textvariable= message_erreur, anchor= CENTER, relief="solid")
Label_actualiseerreur.grid(column=20,row=11, columnspan=largeur, rowspan=1,sticky=(N,S,E,W),pady=1, padx=1)

# Label_piecesperdues= ttk.Label(content, text= "Pièces perdues",relief="solid",anchor=CENTER)
# Label_piecesperdues.grid(column=20, row=13, columnspan = largeur, rowspan=1 ,sticky=(N,S,E,W))



root.mainloop()

# dicopieceB = {"TB1":"","CB1":"","FB1":"","QB1":"","KB1":"","FB2":"","CB2":"","TB2":""}
# dicopieceN= {"TN1":"","CN1":"","FN1":"","QN1":"","KN1":"","FN2":"","CN2":"","TN2":""}
# dicopiecepionB = {"PB1":"","PB2":"","PB3":"","PB4":"","PB5":"","PB6":"","PB7":"","PB8":""}
# dicopiecepionN = {"PN1":"","PN2":"","PN3":"","PN4":"","PN5":"","PN6":"","PN7":"","PN8":""}





