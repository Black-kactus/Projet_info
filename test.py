from tkinter import *
from tkinter import ttk

from PIL import ImageTk, Image


root = Tk()
root.title("Jeu d'échec")

content = ttk.Frame(root, padding=(0,0,0,0))
frame = ttk.Frame(content, borderwidth=0, relief="ridge", width=100, height=100)


# myimg = ImageTk.PhotoImage(Image.open('fou_noir.png'))




# namelbl = ttk.Label(content, text="Name")
# name = ttk.Entry(content)

# onevar = BooleanVar()
# twovar = BooleanVar()
# threevar = BooleanVar()

# onevar.set(True)
# twovar.set(False)
# threevar.set(True)

# one = ttk.Checkbutton(content, text="One", variable=onevar, onvalue=True)
# two = ttk.Checkbutton(content, text="Two", variable=twovar, onvalue=True)
# three = ttk.Checkbutton(content, text="Three", variable=threevar, onvalue=True)
# ok = ttk.Button(content, text="Valider")
# cancel = ttk.Button(content, text="Abandonner")

content.grid(column=0, row=0, sticky=(N, S, E, W))

# for i in range(0,18,2):
#     for j in range(0,18,2):
#         print(i,j)
#         namelbl = ttk.Label(content, text= str(i)+","+str(j),relief="solid")
#         namelbl.grid(column=i, row=j, columnspan=2, rowspan=2,sticky=(N,S,E,W),pady=1, padx=1)

for i in range(0,18,2):
    L = ["","A",'B',"C","D","E","F",'G','H']
    namelbl = ttk.Label(content, text= str(int(9-i/2)),relief="solid",anchor=CENTER)
    namelbl.grid(column=0, row=i, columnspan=2, rowspan=2,sticky=(N,S,E,W),pady=1, padx=1)
    namelbl = ttk.Label(content, text= L[int(i/2)],relief="solid",anchor=CENTER)
    namelbl.grid(column=i, row=0, columnspan=2, rowspan=2,sticky=(N,S,E,W),pady=1, padx=1)

Listepiece = [] 
L= []

img = PhotoImage(file = 'fou_noir.png')
img = img.subsample(15, 15)
# img = img.zoom(10,10)
  
for i in range(2,18,2):
    sousListe = []
    for j in range(2,18,2):
        if (i/2+j/2)%2 == 0:
            couleur = "white"
            # print((i/2+j/2)%2 )
        else :
            couleur = "black"
        sousListe.append(ttk.Label(content, text= str(i)+","+str(j),relief="solid",image = img,anchor=CENTER, background= couleur))
        L.append((i,j))
    Listepiece.append(sousListe)
        #creation de la liste contenant les 64 pièces d'éches numérotés de 0 à 63

#T,C,F,Q,K,P = tour, cavalier, fou, reine(queen), roi(king), pion #N,B = noir, blanc position=[[TB1,CB1,FB1,QB1,KB1,FB2,CB2,TB2],[PB1,PB2,PB3,PB4,PB5,PB6,PB7,PB8],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[PN1,PN2,PN3,PN4,PN5,PN6,PN7,PN8],[TN1,CN1,FN1,QN1,KN1,FN2,CN2,TN2]]

# for i in range(len(Listepiece)):
#    Listepiece[i].grid(column=L[i][0], row=L[i][1], columnspan=2, rowspan=2,sticky=(N,S,E,W),pady=1, padx=1)

dicopiece = {"FB1": 'fou_blanc.png',"FB2": 'fou_blanc.png',"FN1": 'fou_noir.png',"FN2": 'fou_noir.png',"FN1": 'fou_noir.png', "TB1" : "tour_blanche.png", "TB2" : "tour_blanche.png", "TN1" : "tour_noire.png", "TN2" : "tour_noire.png"}

img2 = PhotoImage(file = dicopiece["FB1"])
img2 = img2.subsample(15, 15)
Listepiece[2][0] = ttk.Label(content, text= str(i)+","+str(j),relief="solid",image = img2,anchor=CENTER, background= "red")

for i in range(8):
    for j in range(8):
        Listepiece[j][i].grid(column=2+2*j, row=2+2*i, columnspan=2, rowspan=2,sticky=(N,S,E,W),pady=1, padx=1)
        # print(Listepiece[i][j])

# setting image with the help of label
# La = Label(root, image = img)
# La.grid(column = 10, row = 10, columnspan = 2, rowspan = 2)


root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
    
for i in range(0,24):
    content.columnconfigure(i,weight=1)

for j in range(0,18):
    content.rowconfigure(j,weight=1)

largeur = 4

Lvide = ttk.Label(content, text= "",relief="solid",anchor=CENTER)
Lvide.grid(column=18, row=0, columnspan=2, rowspan=18,sticky=(N,S,E,W),pady=1, padx=1)

Lcommencer = ttk.Label(content, text= "Commencer",relief="solid",anchor=CENTER)
Lcommencer.grid(column=20, row=0, columnspan=largeur, rowspan=2,sticky=(N,S,E,W),pady=1, padx=1)

Lcouleurquijoue = ttk.Label(content, text= "Couleur qui joue",relief="solid",anchor=CENTER)
Lcouleurquijoue.grid(column=20, row=2, columnspan=largeur, rowspan=1,sticky=(N,S,E,W),pady=1, padx=1)

Lcouleuractualise= ttk.Label(content, text= "blanc",relief="solid",anchor=CENTER)
Lcouleuractualise.grid(column=20,row=3, columnspan=largeur, rowspan=1,sticky=(N,S,E,W),pady=1, padx=1)

Lpieceabouger = ttk.Label(content, text= "Piece à bouger",relief="solid",anchor=CENTER)
Lpieceabouger.grid(column=20, row=4, columnspan=largeur, rowspan=1,sticky=(N,S,E,W),pady=1, padx=1)

Lpieceactualise= ttk.Label(content, text= "fou2N",relief="solid",anchor=CENTER)
Lpieceactualise.grid(column=20,row=5, columnspan=largeur, rowspan=1,sticky=(N,S,E,W),pady=1, padx=1)

Lcoupajouer = ttk.Label(content, text= "Coup à jouer",relief="solid",anchor=CENTER)
Lcoupajouer.grid(column=20, row=6, columnspan=largeur, rowspan=1,sticky=(N,S,E,W),pady=1, padx=1)

Lcoupactualise= ttk.Label(content, text= "E3",relief="solid",anchor=CENTER)
Lcoupactualise.grid(column=20,row=7, columnspan=largeur, rowspan=1,sticky=(N,S,E,W),pady=1, padx=1)

Lvalider= ttk.Label(content, text= "Valider",relief="solid",anchor=CENTER)
Lvalider.grid(column=20,row=8, columnspan=largeur, rowspan=2,sticky=(N,S,E,W),pady=1, padx=1)

Labandonner= ttk.Label(content, text= "Abandonner",relief="solid",anchor=CENTER)
Labandonner.grid(column=20,row=16, columnspan=largeur, rowspan=2,sticky=(N,S,E,W),pady=1, padx=1)


# L1= ttk.Label(content, text= "test1",relief="solid")
# L1.grid(column=20,row=10, columnspan=largeur, rowspan=1,sticky=(N,S,E,W),pady=1, padx=1)

# L2= ttk.Label(content, text= "test2",relief="solid")
# L2.grid(column=20,row=11, columnspan=largeur, rowspan=1,sticky=(N,S,E,W),pady=1, padx=1)


# test pour voir si on peut stocker tous les labels dans une liste 
# L = []
# L.append(ttk.Label(content, text= "test1",relief="solid"))
# L.append(ttk.Label(content, text= "test2",relief="solid"))

# for i in range(len(L)):
#     L[i].grid(column=20,row=10+i, columnspan=largeur, rowspan=1,sticky=(N,S,E,W),pady=1, padx=1)



# frame.grid(column=0, row=0, columnspan=3, rowspan=2, sticky=(N, S, E, W))
# namelbl.grid(column=3, row=0, columnspan=2, sticky=(N, W), padx=5)
# name.grid(column=3, row=1, columnspan=2, sticky=(N,E,W), pady=5, padx=5)
# one.grid(column=0, row=3)
# two.grid(column=1, row=3)
# three.grid(column=2, row=3)
# ok.grid(column=3, row=3)
# cancel.grid(column=4, row=3)



# content.columnconfigure(0, weight=3)
# content.columnconfigure(1, weight=3)
# content.columnconfigure(2, weight=3)
# content.columnconfigure(3, weight=1)
# content.columnconfigure(4, weight=1)
# content.rowconfigure(1, weight=1)

# adding image (remember image should be PNG and not JPG)



root.mainloop()