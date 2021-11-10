import tkinter as tk
from typing import Text

class AppliCanevas(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.size = 10000
        self.height = 600
        self.width  = 1000
        self.milieu = 00
        self.couleur = "Blanc"

        self.tester = 0
        self.text1 ="hello"
        self._text = tk.StringVar(self)
        

        self.bind("Escape",self.quit)
        self.creer_widgets()


    def creer_widgets(self):

        # création canevas
        self.canv = tk.Canvas(self, bg="white", height=self.height,width=self.width)
        self.canv.pack(side=tk.LEFT)

        self.canv.xview(tk.SCROLL, int(self.width*1.5), tk.UNITS)
        self.canv.yview(tk.SCROLL, int(self.height*1.5), tk.UNITS)

        for ligne in range(5):
            for colonne in range(5):
                 Button(fenetre, text='L%s-C%s' % (ligne, colonne), borderwidth=1).grid(row=ligne, column=colonne)

        #variables de Tkinter
        self._deplacement = tk.StringVar(self)
        self._deplacement.set("E3")

        self._coup =tk.StringVar(self)
        self._coup.set("fouN2")

        self._couleur =tk.StringVar(self)
        self._couleur.set("blanc")

        #Boutons
        self._bouton_commencer = tk.Button(self, text="Commencer", command=self.commencer)
        self._bouton_abandonner = tk.Button(self, text="Abandon",command=self.save)
        self._bouton_valider = tk.Button(self, text="Valider",command=self.valider)

        #les labels
        self._label_couleurquijoue= tk.Label(self, text="Couleur qui joue")
        self._label_pieceabouger = tk.Label(self, text="Piece à bouger")
        self._label_coupsuivant = tk.Label(self, text="Coup suivant")


        #Entry (entrees)
        self._entree_deplacement = tk.Entry(self, textvariable=self._deplacement)
        self._entree_deplacement.get()

        self._entree_coup = tk.Entry(self, textvariable=self._coup)
        self._entree_coup.get()

        #labels actualisés
        self._label_couleuractualise = tk.Label(self, textvariable=self._couleur)
        self._label_coupactualise = tk.Label(self, textvariable= self._deplacement)

        #affichage de tous les elements du canvas

        self._bouton_commencer.pack(side=tk.TOP) #commencer
        self._label_couleurquijoue.pack(side=tk.TOP) #couleur qui joue
        self._label_couleuractualise.pack(side=tk.TOP) #couleur actualisé

        self._label_pieceabouger.pack(side=tk.TOP) #Piece a bouger
        self._entree_coup.pack(side =tk.TOP) #coup à jouer 
        
        self._label_coupactualise.pack(side =tk.TOP) #coup à jouer
        

        self._label_coupsuivant.pack(side=tk.TOP) #coup suivant
        self._entree_deplacement.pack(side = tk.TOP) #entrée de ttes les pièces 
        self._bouton_valider.pack(side=tk.TOP)#valider

        self._bouton_abandonner.pack(side=tk.BOTTOM)       #abandonner

    
    def test(self):
        if self._text.get() == "hello":
            self._text.set("quoi")
        else :
            self._text.set("hello")

    def valider(self):
        if self._couleur.get() == "blanc":
            self._couleur.set("noir")
        else:
            self._couleur.set("blanc")


    def save(self):
        print("Save")

    def commencer (self):
            pass

if __name__ == "__main__":
    Interface = AppliCanevas()
    Interface.title("Jeu echec")

    Interface.mainloop()
    print(Interface.tester)


# import tkinter as tk

# class Application(tk.Frame):
#     def __init__(self, racine=None):
#         tk.Frame.__init__(self, racine)
#         self.racine = racine
#         self.create_widgets()

#     def create_widgets(self):
#         self.label = tk.Label(self.racine, text="J'adore Python !")
#         self.bouton = tk.Button(self.racine, text="Quitter",fg="green", command=self.quit)
#         self.label.pack()
#         self.bouton.pack()


# if __name__ == "__main__":
#     racine = tk.Tk()
#     racine.title("Ma Première App :-)")
#     app = Application(racine)
#     racine.mainloop()