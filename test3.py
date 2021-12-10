from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


app =Tk()
app.title("Jeu d'échec")
app.iconbitmap(r'icone.ico')

content = ttk.Frame(app, padding=(0,0,0,0))
frame = ttk.Frame(content, borderwidth=0, relief="ridge", width=100, height=100)

content.grid(column=0, row=0, sticky=(N, S, E, W))

ImgFouNoir= Image.open('fou_noir.png')
ImgFouBlanc= Image.open('fou_blanc.png')

ImgFouNoir = ImgFouNoir.resize((60,60), Image.ANTIALIAS)
ImgFouBlanc = ImgFouBlanc.resize((60,60), Image.ANTIALIAS)

python_imageFN = ImageTk.PhotoImage(ImgFouNoir)
python_imageFB = ImageTk.PhotoImage(ImgFouBlanc)

dico = {"FN1":python_imageFN, "FB1": python_imageFB, "FB2":python_imageFB, "FN2":python_imageFN}

L1 = ttk.Label(content, image=python_imageFN,background = "white",relief="solid").grid(row = 0, column = 0, rowspan= 1, columnspan= 1,sticky=(N,S,E,W),pady=1, padx=1)
L2 = ttk.Label(content, image=python_imageFB,background = "black",relief="solid").grid(row = 0, column = 1, rowspan= 1, columnspan= 1,sticky=(N,S,E,W),pady=1, padx=1)
L3 = ttk.Label(content, image=python_imageFB,background = "black",relief="solid").grid(row = 1, column = 0, rowspan= 1, columnspan= 1,sticky=(N,S,E,W),pady=1, padx=1)
L4 = ttk.Label(content, image=python_imageFN,background = "white",relief="solid").grid(row = 1, column = 1, rowspan= 1, columnspan= 1,sticky=(N,S,E,W),pady=1, padx=1)

Liste = [[python_imageFN,python_imageFB],[python_imageFB,python_imageFN]]

dico = {"FN1":python_imageFN, "FB1": python_imageFB, "FB2":python_imageFB, "FN2":python_imageFN}
LPOSITION = [["FN1","FB1"],["FB2","FN2"]]

def cmd_bouton_commencer():
    global LPOSITION
    LPOSITION = [["FN1","FB1"],["FB2","FN2"]]
    

def cmd_bouton_afficher():
    global LPOSITION
    for i in range(len(Liste)) : 
        for j in range(len(Liste)):
            if (i+j)%2 == 0: couleur = 'black'
            else : couleur = "white"
            ttk.Label(content, image=dico[LPOSITION[i][j]],background = couleur,relief="solid").grid(row = i, column = j, rowspan= 1, columnspan= 1,sticky=(N,S,E,W),pady=1, padx=1)
            # ttk.Label(content, image=Liste[i][j],background = couleur,relief="solid").grid(row = i, column = j, rowspan= 1, columnspan= 1,sticky=(N,S,E,W),pady=1, padx=1)

def cmd_bouton_commencer2():
    global LPOSITION
    LPOSITION = [["FB1","FN1"],["FN2","FB2"]]

Bouton_commencer = Button(content, text= "Valider coup 1",command= cmd_bouton_commencer,relief="solid",highlightbackground="red", activebackground="grey",highlightcolor="red",background="white")
Bouton_commencer.grid(column=1, row=2, columnspan=1, rowspan=2,sticky=(N,S,E,W),pady=1, padx=1)

Bouton_commencer2 = Button(content, text= "Valider coup 2",command= cmd_bouton_commencer2,relief="solid",highlightbackground="red", activebackground="grey",highlightcolor="red",background="white")
Bouton_commencer2.grid(column=2, row=2, columnspan=1, rowspan=2,sticky=(N,S,E,W),pady=1, padx=1)

Bouton_Affichage = Button(content, text= "Affichage",command= cmd_bouton_afficher,relief="solid",highlightbackground="red", activebackground="grey",highlightcolor="red",background="white")
Bouton_Affichage.grid(column=2, row=0, columnspan=1, rowspan=2,sticky=(N,S,E,W),pady=1, padx=1)


for i in range(2):
    app.columnconfigure(i,weight=1)

for j in range(2):
    app.rowconfigure(j,weight=1)

if __name__ == '__main__':
    app.mainloop()