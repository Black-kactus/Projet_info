#La véritable fenêtre d'interface 


from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from time import *

#pour récupérer la liste des positions
from board import position
from piece import*
LPOSITION=[]
for l in position:
    if l==0:
        LPOSITION.append(0)
    else:
        LPOSITION.append(str(l))



root = Tk()
root.title("Jeu d'échec")

content = ttk.Frame(root, padding=(0,0,0,0))
frame = ttk.Frame(content, borderwidth=0, relief="ridge", width=100, height=100)


# Variables de Tkinter
deplacement = StringVar()
deplacement.set("Position piece à bouger")

coup = StringVar()
coup.set("Position où aller")

couleurA = StringVar()
couleurA.set("Blanc")

nbcoup= StringVar()
nbcoup.set("0")

temps= StringVar()
temps.set(str(localtime()))

content.grid(column=0, row=0, sticky=(N, S, E, W))

# Dictionaires des images 
dicopiece = {0:"vide.png","":"vide.png","0":"vide.png"}

dicopieceB = {"TB1":"tour_blanche.png","CB1":"cavalier_blanc.png","FB1":"fou_blanc.png","QB1":"reine_blanche.png","KB1":"roi_blanc.png","FB2":"fou_blanc.png","CB2":"cavalier_blanc.png","TB2":"tour_blanche.png"}
dicopieceN= {"TN1":"tour_noire.png","CN1":"cavalier_noir.png","FN1":"fou_noir.png","QN1":"reine_noire.png","KN1":"roi_noir.png","FN2":"fou_noir.png","CN2":"cavalier_noir.png","TN2":"tour_noire.png"}
dicopiecepionB = {"PB1":"pion_blanc.png","PB2":"pion_blanc.png","PB3":"pion_blanc.png","PB4":"pion_blanc.png","PB5":"pion_blanc.png","PB6":"pion_blanc.png","PB7":"pion_blanc.png","PB8":"pion_blanc.png"}
dicopiecepionN = {"PN1":"pion_noir.png","PN2":"pion_noir.png","PN3":"pion_noir.png","PN4":"pion_noir.png","PN5":"pion_noir.png","PN6":"pion_noir.png","PN7":"pion_noir.png","PN8":"pion_noir.png"}

dicopiece.update(dicopieceN)
dicopiece.update(dicopieceB)
dicopiece.update(dicopiecepionB)
dicopiece.update(dicopiecepionN)

#Creation des indices horizontaux de l'échiquier
for i in range(0,18,2):
    L = ["","A",'B',"C","D","E","F",'G','H']
    namelbl = ttk.Label(content, text= str(int(9-i/2)),relief="solid",anchor=CENTER)
    namelbl.grid(column=0, row=i, columnspan=2, rowspan=2,sticky=(N,S,E,W),pady=1, padx=1)
    namelbl = ttk.Label(content, text= L[int(i/2)],relief="solid",anchor=CENTER)
    namelbl.grid(column=i, row=0, columnspan=2, rowspan=2,sticky=(N,S,E,W),pady=1, padx=1)

Listepiece = [] 
L= []


Limg = [["0" for i in range(8)] for j in range(8)]

#Liste des positions renvoyées par Raph
LPOSITION= [["TB1","PB1",0,0,0,0,"PN1","TN1"],["CB1","PB2",0,0,0,0,"PN2","CN1"],["FB1","PB3",0,0,0,0,"PN3","FN1"],["QB1","PB4",0,0,0,0,"PN4","QN1"],["KB1","PB5",0,0,0,0,"PN5","KN1"],["FB2","PB6",0,0,0,0,"PN6","FN2"],["CB2","PB7",0,0,0,0,"PN7","CN2"],["TB2","PB8",0,0,0,0,"PN8","TN2"]]

#variable Tkinter correspondant à LPOSITION
LPOS = StringVar()
LPOS.set(str(LPOSITION))
LPOS.get()

def afficherPiece():

    global dicopiece

    Limg = [["0" for i in range(8)] for j in range(8)]
    Listepiece = [] 
    

    # Creation de la liste #Listepiece# contenant tous les labels (avec images) de toutes les pieces de l'echiquier
    for i in range(8):
        for j in range(8):
            if (i+j)%2 == 0:
                couleur = "white"
            else :
                couleur = "black"
            label = ttk.Label(content, text= str(i)+","+str(j),relief="solid",image = Limg[int(i)][int(j)],anchor=CENTER, background= couleur)
            #label.grid(column=2, row=2, columnspan=2, rowspan=2,sticky=(N,S,E,W),pady=1, padx=1)


def cmd_bouton_valider():
    print("valider")
    afficherPiece()
    nbcoup.set(str(int(nbcoup.get())+1))
    if couleurA.get() == "Blanc": 
        couleurA.set("Noir")
        print("Noir")
    else:
        couleurA.set("Blanc")
        print("Blanc")

def cmd_bouton_commencer():
    coup.set("0")
    LPOSITION= [["TB1","PB1",0,0,0,0,"PN1","TN1"],["CB1","PB2",0,0,0,0,"PN2","CN1"],["FB1","PB3",0,0,0,0,"PN3","FN1"],["QB1","PB4",0,0,0,0,"PN4","QN1"],["KB1","PB5",0,0,0,0,"PN5","KN1"],["FB2","PB6",0,0,0,0,"PN6","FN2"],["CB2","PB7",0,0,0,0,"PN7","CN2"],["TB2","PB8",0,0,0,0,"PN8","TN2"]]
    LPOS.set(str(LPOSITION))
    afficherPiece()
    print("commencer")

def cmd_bouton_abandonner():
    print("abandonner")


def cmd_bouton_test():
    LPOSITION= [["TB1","PB1",0,0,0,0,"PN1","TN1"],["CB1","PB2",0,0,0,0,"PN2","CN1"],["FB1","PB3",0,0,0,0,"PN3","FN1"],["QB1","PB4",0,0,0,0,"PN4","QN1"],["KB1",0,0,"PB5",0,0,"PN5","KN1"],["FB2","PB6",0,0,0,0,"PN6","FN2"],["CB2","PB7",0,0,0,0,"PN7","CN2"],["TB2","PB8",0,0,0,0,"PN8","TN2"]]
    LPOS.set(str(LPOSITION))
    #print(LPOS.get())
    print("test")


root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
    
for i in range(0,24):
    content.columnconfigure(i,weight=1)

for j in range(0,18):
    content.rowconfigure(j,weight=1)

largeur = 4

Lvide = ttk.Label(content, text= "",relief="solid",anchor=CENTER)
Lvide.grid(column=18, row=0, columnspan=2, rowspan=18,sticky=(N,S,E,W),pady=1, padx=1)

Bouton_commencer = Button(content, text= "Nouvelle Partie",command= cmd_bouton_commencer,relief="solid",highlightbackground="red", activebackground="grey",highlightcolor="red",background="white")
Bouton_commencer.grid(column=20, row=0, columnspan=largeur, rowspan=2,sticky=(N,S,E,W),pady=1, padx=1)

Label_couleurquijoue = ttk.Label(content, text= "Couleur qui joue",relief="solid",anchor=CENTER)
Label_couleurquijoue.grid(column=20, row=2, columnspan=largeur, rowspan=1,sticky=(N,S,E,W),pady=1, padx=1)

Entry_couleuractualise= ttk.Entry(content, textvariable= couleurA)
Entry_couleuractualise.grid(column=20,row=3, columnspan=largeur, rowspan=1,sticky=(N,S,E,W),pady=1, padx=1)

Lpieceabouger = ttk.Label(content, text= "Piece à bouger",relief="solid",anchor=CENTER)
Lpieceabouger.grid(column=20, row=4, columnspan=largeur, rowspan=1,sticky=(N,S,E,W),pady=1, padx=1)

Entry_deplacement= ttk.Entry(content, textvariable= deplacement)
Entry_deplacement.grid(column=20,row=5, columnspan=largeur, rowspan=1,sticky=(N,S,E,W),pady=1, padx=1)

Label_coupajouer = ttk.Label(content, text= "Coup à jouer",relief="solid",anchor=CENTER)
Label_coupajouer.grid(column=20, row=6, columnspan=largeur, rowspan=1,sticky=(N,S,E,W),pady=1, padx=1)

Entry_coup= ttk.Entry(content, textvariable= coup)
Entry_coup.grid(column=20,row=7, columnspan=largeur, rowspan=1,sticky=(N,S,E,W),pady=1, padx=1)

Bouton_valider= ttk.Button(content, text= "Valider",command= cmd_bouton_valider)
Bouton_valider.grid(column=20,row=8, columnspan=largeur, rowspan=2,sticky=(N,S,E,W),pady=1, padx=1)

Bouton_test= ttk.Button(content, text= "Bouton TEST",command= cmd_bouton_test)
Bouton_test.grid(column=20,row=10, columnspan=largeur, rowspan=2,sticky=(N,S,E,W),pady=1, padx=1)

Label_Nbcoup = ttk.Label(content, text= "n° coup",relief="solid",anchor=CENTER)
Label_Nbcoup.grid(column=20, row=12, columnspan=2, rowspan=1 ,sticky=(N,S,E,W),pady=1, padx=1)

Entry_coup= ttk.Entry(content, textvariable= nbcoup)
Entry_coup.grid(column=22,row=12, columnspan=int(largeur/2), rowspan=1,sticky=(N,S,E,W),pady=1, padx=1)

root.mainloop()