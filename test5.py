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
    creerWidgets()

ccListe = []
def creerWidgets():
    print("creer")
    for i in range(10):
        cc = Button(content, text= "Valider coup 1",command= cmd_bouton_commencer,relief="solid",highlightbackground="red", activebackground="grey",highlightcolor="red",background="white")
        ccListe.append(cc)
        cc.grid(row=10, column=i)
        def gest(evt, i=i):   
            return ccGest(evt, i)
        def gest2(evt, i=i):   
            return ccGest2(evt, i)
        cc.bind('<Button-1>', gest)
        cc.bind('<Button-3>', gest2)
    #...
def ccGest(evt, ccNb):
    print('Gauche', ccNb)
    coup.set(str(ccNb))

def ccGest2(evt, ccNb):
    print('Droit', ccNb)
    deplacement.set(str(ccNb))

def BoutonGestClicgauche(evt, i, j):
    print('CGauche',i, j )
    coup.set(chr(j+97)+str(i+1))

def BoutonGestClicdroit(evt, i, j ):
    print('CDroit', i, j)
    deplacement.set(chr(j+97)+str(i+1))

BoutonListe = [[0 for i in range(2)]for j in range(2)]
def cmd_bouton_afficher():
    global LPOSITION
    for i in range(len(Liste)) : 
        for j in range(len(Liste)):
            if (i+j)%2 == 0: couleur = 'black'
            else : couleur = "white"
            # ttk.Label(content, image=dico[LPOSITION[i][j]],background = couleur,relief="solid",anchor=CENTER).grid(row = i, column = j, rowspan= 1, columnspan= 1,sticky=(N,S,E,W),pady=1, padx=1)
            # Bouton_piece =Label(content, image=dico[LPOSITION[i][j]],background = couleur,relief="solid",anchor=CENTER, highlightcolor='red')
            Bouton_piece =Button(content, image=dico[LPOSITION[i][j]],background = couleur,relief="solid",anchor=CENTER, highlightcolor='red', activebackground='red')
            BoutonListe[i].insert(j,Bouton_piece)
            Bouton_piece.grid(row = i, column = j, rowspan= 1, columnspan= 1,sticky=(N,S,E,W),pady=1, padx=1)
            def gestCG(evt, i=i,j=j):   
                 return BoutonGestClicgauche(evt, i,j)
            def gestCD(evt, i=i, j= j):   
                return BoutonGestClicdroit(evt, i,j)
            Bouton_piece.bind('<Button-1>', gestCG)
            Bouton_piece.bind('<Button-3>', gestCD)

def creerWidgets():
    print("creer")
    for i in range(10):
        cc = Button(content, text= "Valider coup 1",command= cmd_bouton_commencer,relief="solid",highlightbackground="red", activebackground="grey",highlightcolor="red",background="white")
        ccListe.append(cc)
        cc.grid(row=10, column=i)
        def gest(evt, i=i):   
            return ccGest(evt, i)
        def gest2(evt, i=i):   
            return ccGest2(evt, i)
        cc.bind('<Button-1>', gest)
        cc.bind('<Button-3>', gest2)
            

            

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

    Popup.geometry("500x500")
    Popup.grid_columnconfigure(0, weight=1)
    Popup.grid_rowconfigure(0, weight=1)

    n = ttk.Notebook(Popup)   # Création du système d'onglets
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
    ch1 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam. Maecenas ligula massa, varius a, semper congue, euismod non, mi. Proin porttitor, orci nec nonummy molestie, enim est eleifend mi, non fermentum diam nisl sit amet erat. Duis semper. Duis arcu massa, scelerisque vitae, consequat in, pretium a, enim. Pellentesque congue. Ut in risus volutpat libero pharetra tempor. Cras vestibulum bibendum augue. Praesent egestas leo in pede. Praesent blandit odio eu enim. Pellentesque sed dui ut augue blandit sodales. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Aliquam nibh. Mauris ac mauris sed pede pellentesque fermentum. Maecenas adipiscing ante non diam sodales hendrerit. "
    ttk.Label(Onglet1_Regles, text= ch1 ,relief="solid",anchor=CENTER, wraplength=500, justify='center').grid(column=0, row=0, columnspan=20, rowspan=20,sticky=(N,S,E,W),pady=1, padx=1)
    
    #Onglet 2: Pion
    ttk.Label(Onglet2_Pion, image= python_imageDF,background = 'white',relief="solid",anchor=CENTER).grid(row = 0, column = 0, rowspan= 16, columnspan= 20,sticky=(N,S,E,W),pady=1, padx=1)
    ttk.Label(Onglet2_Pion, text= 'Les déplacements du pion se font verticalement, coup spécial : prise en passant \n mange en diagonale et promotion de pion',background = 'white',relief="solid",anchor=CENTER).grid(row = 16, column = 0, rowspan= 4, columnspan= 20,sticky=(N,S,E,W),pady=1, padx=1)

    #Onglet 3 : Fou
    ttk.Label(Onglet3_Fou, image= python_imageDF,background = 'white',relief="solid",anchor=CENTER).grid(row = 0, column = 0, rowspan= 18, columnspan= 20,sticky=(N,S,E,W),pady=1, padx=1)
    ttk.Label(Onglet3_Fou, text= 'Les déplacements du fou se font diagonalement',background = 'white',relief="solid",anchor=CENTER).grid(row = 18, column = 0, rowspan= 2, columnspan= 20,sticky=(N,S,E,W),pady=1, padx=1)

    #Onglet 4 : Tour
    ttk.Label(Onglet4_Tour, image= python_imageDT,background = 'white',relief="solid",anchor=CENTER).grid(row = 0, column = 0, rowspan= 18, columnspan= 20,sticky=(N,S,E,W),pady=1, padx=1)
    ttk.Label(Onglet4_Tour, text= 'Les déplacements de la tour se font horizontalement et verticalement',background = 'white',relief="solid",anchor=CENTER).grid(row = 18, column = 0, rowspan= 2, columnspan= 20,sticky=(N,S,E,W),pady=1, padx=1)

    #Onglet 5 : Cavalier
    ttk.Label(Onglet5_Cavalier, image= python_imageDC,background = 'white',relief="solid",anchor=CENTER).grid(row = 0, column = 0, rowspan= 18, columnspan= 20,sticky=(N,S,E,W),pady=1, padx=1)
    ttk.Label(Onglet5_Cavalier, text= 'Les déplacements du cavalier se font en forme de L',background = 'white',relief="solid",anchor=CENTER).grid(row = 18, column = 0, rowspan= 2, columnspan= 20,sticky=(N,S,E,W),pady=1, padx=1)

    #Onglet 6: Dame
    ttk.Label(Onglet6_Dame, image= python_imageDD,background = 'white',relief="solid",anchor=CENTER).grid(row = 0, column = 0, rowspan= 18, columnspan= 20,sticky=(N,S,E,W),pady=1, padx=1)
    ttk.Label(Onglet6_Dame, text= "La Dame peut se déplacer dans toutes les directions de l'espace",background = 'white',relief="solid",anchor=CENTER).grid(row = 18, column = 0, rowspan= 2, columnspan= 20,sticky=(N,S,E,W),pady=1, padx=1)

    #Onglet 7 : Roi
    ttk.Label(Onglet7_Roi, image= python_imageDR,background = 'white',relief="solid",anchor=CENTER).grid(row = 0, column = 0, rowspan= 18, columnspan= 20,sticky=(N,S,E,W),pady=1, padx=1)
    ttk.Label(Onglet7_Roi, text= 'Le Roi peut se déplacer dans toutes les directions, mais seulement de 1',background = 'white',relief="solid",anchor=CENTER).grid(row = 18, column = 0, rowspan= 2, columnspan= 20,sticky=(N,S,E,W),pady=1, padx=1)

    #Onglet 8 : Action spéciale
    ttk.Label(Onglet8_ActionSpe, image= python_imageDR,background = 'white',relief="solid",anchor=CENTER).grid(row = 0, column = 0, rowspan= 18, columnspan= 20,sticky=(N,S,E,W),pady=1, padx=1)
    ttk.Label(Onglet8_ActionSpe, text= "Expliquer le pat et la promotion",background = 'white',relief="solid",anchor=CENTER).grid(row = 18, column = 0, rowspan= 2, columnspan= 20,sticky=(N,S,E,W),pady=1, padx=1)

    #Onglet 9 : Fin de partie 
    ch2= "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam. Maecenas ligula massa, varius a, semper congue, euismod non, mi. Proin porttitor, orci nec nonummy molestie, enim est eleifend mi, non fermentum diam nisl sit amet erat. Duis semper. Duis arcu massa, scelerisque vitae, consequat in, pretium a, enim. Pellentesque congue. Ut in risus volutpat libero pharetra tempor. Cras vestibulum bibendum augue. Praesent egestas leo in pede. Praesent blandit odio eu enim. Pellentesque sed dui ut augue blandit sodales. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Aliquam nibh. Mauris ac mauris sed pede pellentesque fermentum. Maecenas adipiscing ante non diam sodales hendrerit. "
    ttk.Label(Onglet9_Fin, text= ch2 ,relief="solid",anchor=CENTER, wraplength=500, justify='center').grid(column=0, row=0, columnspan=20, rowspan=20,sticky=(N,S,E,W),pady=1, padx=1)

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

coup= StringVar()
coup.set("coup")

deplacement= StringVar()
deplacement.set("deplacement")
        
        

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

Coup_Entry = ttk.Entry(content, textvariable= coup,background="white")
Coup_Entry.grid(column=0, row=5, columnspan=1, rowspan=2,sticky=(N,S,E,W),pady=1, padx=1)

Deplacement_Entry = ttk.Entry(content, textvariable= deplacement,background="white")
Deplacement_Entry.grid(column=1, row=5, columnspan=1, rowspan=2,sticky=(N,S,E,W),pady=1, padx=1)


app.columnconfigure(0, weight=1)
app.rowconfigure(0, weight=1)

for i in range(20):
    content.columnconfigure(i,weight=1)

for j in range(20):
    content.rowconfigure(j,weight=1)

if __name__ == '__main__':
    app.mainloop()

# https://s15847115.domainepardefaut.fr/python/tkinter/menus.html