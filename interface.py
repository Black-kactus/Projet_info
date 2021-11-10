import tkinter as tk

class AppliCanevas(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.size = 10000
        self.height = 600
        self.width  = 1000
        self.milieu = 00
        self.couleur = "Blanc"


        self.bind("Escape",self.quit)
        self.creer_widgets()

    def creer_widgets(self):

        self.representationCyclo = []

        # création canevas
        self.canv = tk.Canvas(self, bg="white", height=self.height,
                              width=self.width)
        self.canv.pack(side=tk.LEFT)

        self.canv.xview(tk.SCROLL, int(self.width*1.5), tk.UNITS)
        self.canv.yview(tk.SCROLL, int(self.height*1.5), tk.UNITS)

        #Button Commencer
        self.bouton_commencer = tk.Button(self, text="Commencer", command=self.commencer)
       
        #Button Quitter
        self.bouton_quitter = tk.Button(self, text="Quitter",command=self.quit)

        #Button Save
        self.bouton_abandonner = tk.Button(self, text="Abandon",command=self.save)

        #les labels
        Lcouleurquijoue= tk.Label(self, text="Couleur qui joue")
        LabelPieceabouger = tk.Label(self, text="Piece à bouger")



        self.deplacement =tk.StringVar(self)
        self.deplacement.set("E3")
        self.button_deplacement = tk.Entry (self, textvariable=self.deplacement)
        
        self.button_deplacement.get()

        self.coup =tk.StringVar(self)
        self.coup.set("fouN2")
        self.button_coup = tk.Entry (self, textvariable=self.coup)
        
        self.button_coup.get()


        #Entry K2
        Lcoupsuivant = tk.Label(self, text="Coup suivant")
        
        

        self.couleur =tk.IntVar(self)
        self.couleur.set("blanc")
        self.button_couleur = tk.Entry (self, textvariable=self.couleur)
        # self.button_couleur.pack(side = tk.TOP)
        self.button_couleur.get()

        self.bouton_valider = tk.Button(self, text="Valider",command=self.valider)
        

        Lcouleuractualise = tk.Label(self, textvariable=self.couleur)


        #affichage de tous 


        self.bouton_commencer.pack(side=tk.TOP) #commencer
        Lcouleurquijoue.pack(side=tk.TOP) #couleur qui joue
        Lcouleuractualise.pack(side=tk.TOP) #couleur actualisé

        LabelPieceabouger.pack(side=tk.TOP) #Piece a bouger
        self.button_coup.pack(side =tk.TOP) #coup à jouer actualisé

        Lcoupsuivant.pack(side=tk.TOP) #coup suivant
        self.button_deplacement.pack(side = tk.TOP) #entrée de ttes les pièces 
        self.bouton_valider.pack(side=tk.TOP)#valider

        # self.bouton_quitter.pack(side=tk.BOTTOM)    
        self.bouton_abandonner.pack(side=tk.BOTTOM)       #abandonner
        
        
    
       
       

    def valider(self):
        if self.button_couleur.get() == "blanc":
            # self.couleur.("Noir")
            self.couleur.set("noir")
            # print("valider")
        else:
            # self.couleur.set("Blanc")
            self.couleur.set("blanc")
            # print("valider2", type(self.button_couleur.get()))

    def save(self):
        print("Save")

    # def clear_screen(self):
    #     # self.canv.delete("all")
    #     for id in self.representationCyclo:
    #         self.canv.delete(id)

    def rd_col(self):
        return rd.choice(("black", "red", "green", "blue", "yellow", "magenta",
                          "cyan", "white", "purple"))

    def commencer (self):
            pass

    def quit(self):
        self.destroy()


if __name__ == "__main__":
    app = AppliCanevas()
    app.title("Jeu echec")
    app.mainloop()


