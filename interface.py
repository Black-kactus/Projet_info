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
        self.bouton_cercles = tk.Button(self, text="Commencer", command=self.commencer)
      
        #Button Quitter
        self.bouton_quitter = tk.Button(self, text="Quitter",command=self.quit)

        #Button Save
        self.bouton_save = tk.Button(self, text="Save",command=self.save)

        #Entry Speed
        L1 = tk.Label(self, text="Couleur qui joue")
        

        


        self.speed =tk.StringVar(self)
        self.speed.set("blanc")
        self.button_speed = tk.Entry (self, textvariable="test")
        self.button_speed.pack(side = tk.TOP)
        self.button_speed.get()

        #Entry K2
        L3 = tk.Label(self, text="Coup suivant")
        
        

        self.couleur =tk.IntVar(self)
        self.couleur.set("blanc")
        self.button_couleur = tk.Entry (self, textvariable=self.couleur)
        # self.button_couleur.pack(side = tk.TOP)
        self.button_couleur.get()

        self.bouton_valider = tk.Button(self, text="Valider",command=self.valider)
        

        L4 = tk.Label(self, textvariable=self.couleur)

        L1.pack(side=tk.TOP)
        L4.pack(side=tk.TOP)
        L3.pack(side=tk.TOP)
        self.bouton_valider.pack(side=tk.TOP)


        self.bouton_quitter.pack(side=tk.BOTTOM)
        self.bouton_cercles.pack(side=tk.TOP)
        self.bouton_save.pack(side=tk.BOTTOM)
        
    
       
       

    def valider(self):
        if self.button_couleur.get() == "blanc":
            # self.couleur.("Noir")
            self.couleur.set("noir")
            print("valider")
        else:
            # self.couleur.set("Blanc")
            self.couleur.set("blanc")
            print("valider2", type(self.button_couleur.get()))

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


