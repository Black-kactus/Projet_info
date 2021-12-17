from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import time 
import winsound

duree = 1

app =Tk()
app.title("Jeu d'échec")
app.iconbitmap(r'icone.ico')


# app.config(background="grey")

content = ttk.Frame(app, padding=(0,0,0,0))
frame = ttk.Frame(content, borderwidth=0, relief="ridge", width=100, height=100)

content.grid(column=0, row=0, sticky=(N, S, E, W))

# Image des pièces de l'échiquier
ImgFouNoir= Image.open('fou_noir.png')
ImgFouBlanc= Image.open('fou_blanc.png')

ImgFouNoir = ImgFouNoir.resize((60,60), Image.ANTIALIAS)
ImgFouBlanc = ImgFouBlanc.resize((60,60), Image.ANTIALIAS)

python_imageFN = ImageTk.PhotoImage(ImgFouNoir)
python_imageFB = ImageTk.PhotoImage(ImgFouBlanc)

## Image des déplacements 

ImgDFou= Image.open('dep_fou.png')

ImgDFou = ImgDFou.resize((300,300), Image.ANTIALIAS)

python_imageDF = ImageTk.PhotoImage(ImgDFou)


dico = {"FN1":python_imageFN, "FB1": python_imageFB, "FB2":python_imageFB, "FN2":python_imageFN}

L1 = ttk.Label(content, image=python_imageFN,background = "white",relief="solid",anchor=CENTER).grid(row = 0, column = 0, rowspan= 1, columnspan= 1,sticky=(N,S,E,W),pady=1, padx=1)
L2 = ttk.Label(content, image=python_imageFB,background = "black",relief="solid",anchor=CENTER).grid(row = 0, column = 1, rowspan= 1, columnspan= 1,sticky=(N,S,E,W),pady=1, padx=1)
L3 = ttk.Label(content, image=python_imageFB,background = "black",relief="solid",anchor=CENTER).grid(row = 1, column = 0, rowspan= 1, columnspan= 1,sticky=(N,S,E,W),pady=1, padx=1)
L4 = ttk.Label(content, image=python_imageFN,background = "white",relief="solid",anchor=CENTER).grid(row = 1, column = 1, rowspan= 1, columnspan= 1,sticky=(N,S,E,W),pady=1, padx=1)

Liste = [[python_imageFN,python_imageFB],[python_imageFB,python_imageFN]]

dico = {"FN1":python_imageFN, "FB1": python_imageFB, "FB2":python_imageFB, "FN2":python_imageFN}

def cmd_bouton_commencer():
    global LPOSITION
    LPOSITION = [["FN1","FB1"],["FB2","FN2"]]
    

def cmd_bouton_afficher():
    global LPOSITION
    for i in range(len(Liste)) : 
        for j in range(len(Liste)):
            if (i+j)%2 == 0: couleur = 'black'
            else : couleur = "white"
            ttk.Label(content, image=dico[LPOSITION[i][j]],background = couleur,relief="solid",anchor=CENTER).grid(row = i, column = j, rowspan= 1, columnspan= 1,sticky=(N,S,E,W),pady=1, padx=1)

def cmd_bouton_commencer2():
    global LPOSITION
    LPOSITION = [["FB1","FN1"],["FN2","FB2"]]

def cmd_bouton_bruitage():
    winsound.PlaySound('Whoush.wav', winsound.SND_FILENAME|winsound.SND_ASYNC)
    time.sleep(duree) 
    winsound.PlaySound(None, 0)

def cmd_bouton_popup():
    Popup = Toplevel()
    Popup.title('Règles de jeu')

    Popup.geometry("400x400")
    Popup.grid_columnconfigure(0, weight=1)
    Popup.grid_rowconfigure(0, weight=1)


    n = ttk.Notebook(Popup)   # Création du système d'onglets
    n.columnconfigure(0, weight=1)
    n.rowconfigure(0, weight=1)
    n.grid(column=0, row=0,sticky= NSEW)

    Onglet1_Regles = ttk.Frame(n,padding=(0,0,0,0))       # Ajout de l'onglet 1
    Onglet2_Pion = ttk.Frame(n,padding=(0,0,0,0))      # Ajout de l'onglet 2
    Onglet3_Fou = ttk.Frame(n,padding=(0,0,0,0))
    Onglet4_Tour = ttk.Frame(n,padding=(0,0,0,0))
    Onglet5_Cavalier = ttk.Frame(n,padding=(0,0,0,0))
    Onglet6_Dame = ttk.Frame(n,padding=(0,0,0,0))
    Onglet7_Roi = ttk.Frame(n,padding=(0,0,0,0))


    Onglet1_Regles.grid(column=0, row=0, sticky=(N, S, E, W))
    Onglet2_Pion.grid(column=0, row=0, sticky=(N, S, E, W))
    Onglet3_Fou.grid(column=0, row=0, sticky=(N, S, E, W))
    Onglet4_Tour.grid(column=0, row=0, sticky=(N, S, E, W))
    Onglet5_Cavalier.grid(column=0, row=0, sticky=(N, S, E, W))
    Onglet6_Dame.grid(column=0, row=0, sticky=(N, S, E, W))
    Onglet7_Roi.grid(column=0, row=0, sticky=(N, S, E, W))


    n.add(Onglet1_Regles, text='Règles générales')      # Nom de l'onglet 1
    n.add(Onglet2_Pion, text='Pion')      # Nom de l'onglet 2
    n.add(Onglet3_Fou, text='Fou')
    n.add(Onglet4_Tour, text='Tour')
    n.add(Onglet5_Cavalier, text='Cavalier')
    n.add(Onglet6_Dame, text='Dame')
    n.add(Onglet7_Roi, text='Roi')

    # Onglet 1 : Regles
    Button(Onglet1_Regles, text='Quitter', command=Popup.destroy).grid(column=18, row=18, columnspan=2, rowspan=2,sticky=(N,S,E,W),pady=1, padx=1)
    
    #Onglet 2: Pion


    #Onglet 3 : Fou
    ttk.Label(Onglet3_Fou, image= python_imageDF,background = 'white',relief="solid",anchor=CENTER).grid(row = 0, column = 0, rowspan= 20, columnspan= 20,sticky=(N,S,E,W),pady=1, padx=1)


    #Onglet 4 : Tour

    for i in range(20):
        print(i)
        Button(Onglet4_Tour, text = f'Button {i}').grid(column= 0, row = 20+i, padx= 10, pady =10, sticky = NSEW, columnspan= 1, rowspan= 1)

    #Onglet 5 : Cavalier

    #Onglet 6: Dame

    #Onglet 7 : Roi
    
    Button(Onglet2_Pion, text='En attente', command=None).grid(column=18, row=2, columnspan=1, rowspan=2,sticky=(N,S,E,W),pady=1, padx=1)
    
    ch1 = "Le principe du jeu d'échec"
    ch2 = "Déplacement du pion: "
    ch3 = "Déplacement de la "
    
    ttk.Label(Onglet1_Regles, text= "ch1",relief="solid",anchor=CENTER).grid(column=0, row=0, columnspan=18, rowspan=20,sticky=(N,S,E,W),pady=1, padx=1)
    
    #cd

    for i in range(20):
        Onglet1_Regles.columnconfigure(i,weight=1)
        Onglet2_Pion.columnconfigure(i,weight=1)
        Onglet3_Fou.columnconfigure(i,weight=1)
        Onglet4_Tour.columnconfigure(i,weight=1)
        Onglet5_Cavalier.columnconfigure(i,weight=1)
        Onglet6_Dame.columnconfigure(i,weight=1)
        Onglet7_Roi.columnconfigure(i,weight=1)

    for j in range(20):
        Onglet1_Regles.rowconfigure(j,weight=1)
        Onglet2_Pion.rowconfigure(j,weight=1)
        Onglet3_Fou.rowconfigure(j,weight=1)
        Onglet4_Tour.rowconfigure(j,weight=1)
        Onglet5_Cavalier.columnconfigure(j,weight=1)
        Onglet6_Dame.columnconfigure(j,weight=1)
        Onglet7_Roi.columnconfigure(j,weight=1)


        

Bouton_commencer = Button(content, text= "Valider coup 1",command= cmd_bouton_commencer,relief="solid",highlightbackground="red", activebackground="grey",highlightcolor="red",background="white")
Bouton_commencer.grid(column=1, row=2, columnspan=1, rowspan=2,sticky=(N,S,E,W),pady=1, padx=1)

Bouton_commencer2 = Button(content, text= "Valider coup 2",command= cmd_bouton_commencer2,relief="solid",highlightbackground="red", activebackground="grey",highlightcolor="red",background="white")
Bouton_commencer2.grid(column=2, row=2, columnspan=1, rowspan=2,sticky=(N,S,E,W),pady=1, padx=1)

Bouton_Affichage = Button(content, text= "Affichage",command= cmd_bouton_afficher,relief="solid",highlightbackground="red", activebackground="grey",highlightcolor="red",background="white")
Bouton_Affichage.grid(column=2, row=0, columnspan=1, rowspan=2,sticky=(N,S,E,W),pady=1, padx=1)

Bouton_Popup = Button(content, text= "Popup",command= cmd_bouton_popup,relief="solid",highlightbackground="red", activebackground="grey",highlightcolor="red",background="white")
Bouton_Popup.grid(column=0, row=2, columnspan=1, rowspan=2,sticky=(N,S,E,W),pady=1, padx=1)

Bouton_Son = Button(content, text= "Bruitage",command= cmd_bouton_bruitage,relief="solid",highlightbackground="red", activebackground="grey",highlightcolor="red",background="white")
Bouton_Son.grid(column=3, row=3, columnspan=1, rowspan=2,sticky=(N,S,E,W),pady=1, padx=1)


app.columnconfigure(0, weight=1)
app.rowconfigure(0, weight=1)

for i in range(2):
    content.columnconfigure(i,weight=1)

for j in range(2):
    content.rowconfigure(j,weight=1)

if __name__ == '__main__':
    app.mainloop()

# https://s15847115.domainepardefaut.fr/python/tkinter/menus.html