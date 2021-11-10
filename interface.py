import tkinter as tk

class AppliCanevas(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.size = 10000
        self.height = 600
        self.width  = 1000
        self.milieu = 00


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
        self.bouton_cercles = tk.Button(self, text="Commencer!", command=self.dessine_cercles)
        self.bouton_cercles.pack(side=tk.TOP)

      
        #Button Quitter
        self.bouton_quitter = tk.Button(self, text="Quitter",command=self.quit)
        self.bouton_quitter.pack(side=tk.BOTTOM)

        #Button Save
        self.bouton_save = tk.Button(self, text="Save",command=self.save)
        self.bouton_save.pack(side=tk.BOTTOM)

        #Button Pause
        self.CheckPause = tk.IntVar()
        self.CheckPause.set(0)
        self.Pause= tk.Checkbutton (self, text = "Pause/Play", variable = self.CheckPause, onvalue = 1, offvalue = 0)
        self.Pause.pack(side = tk.BOTTOM)

        #Checkbutton Show All
        self.CheckCercle5 = tk.IntVar()
        self.CheckCercle5.set(0)
        self.cercle5 = tk.Checkbutton (self, text = "Show all", variable = self.CheckCercle5, onvalue = 1, offvalue = 0)
        self.cercle5.pack(side = tk.TOP)

        #Checkbutton 1
        self.CheckCercle1 = tk.IntVar()
        self.CheckCercle1.set(1)
        self.cercle1 = tk.Checkbutton (self, text = "Show circle 1", variable = self.CheckCercle1, onvalue = 1, offvalue = 0)
        self.cercle1.pack(side = tk.TOP)

        #Checkbutton 2
        self.CheckCercle2 = tk.IntVar()
        self.CheckCercle2.set(1)
        self.cercle2 = tk.Checkbutton (self, text = "Show circle 2", variable = self.CheckCercle2, onvalue = 1, offvalue = 0)
        self.cercle2.pack(side = tk.TOP)

        #Checkbutton 3
        self.CheckCercle3 = tk.IntVar()
        self.CheckCercle3.set(1)
        self.cercle3 = tk.Checkbutton (self, text = "Show circle 3", variable = self.CheckCercle3, onvalue = 1, offvalue = 0)
        self.cercle3.pack(side = tk.TOP)

        #Checkbutton Do not Show
        self.CheckCercle4 = tk.IntVar()
        self.CheckCercle4.set(0)
        self.cercle4 = tk.Checkbutton (self, text = "No Circle", variable = self.CheckCercle4, onvalue = 1, offvalue = 0)
        self.cercle4.pack(side = tk.TOP)

        #Checkbutton Show Tracé 1
        self.CheckCercle5 = tk.IntVar()
        self.CheckCercle5.set(0)
        self.cercle5 = tk.Checkbutton (self, text = "Show Tracé 1", variable = self.CheckCercle5, onvalue = 1, offvalue = 0)
        self.cercle5.pack(side = tk.TOP)

        #Checkbutton Show Tracé 2
        self.CheckCercle6 = tk.IntVar()
        self.CheckCercle6.set(0)
        self.cercle6 = tk.Checkbutton (self, text = "Show Tracé 2", variable = self.CheckCercle6, onvalue = 1, offvalue = 0)
        self.cercle6.pack(side = tk.TOP)

        #Checkbutton Show Tracé 3
        self.CheckCercle7 = tk.IntVar()
        self.CheckCercle7.set(0)
        self.cercle7 = tk.Checkbutton (self, text = "Show Tracé 3", variable = self.CheckCercle7, onvalue = 1, offvalue = 0)
        self.cercle7.pack(side = tk.TOP)

        #Button Clearscreen
        self.bouton_clearscreen = tk.Button(self, text="Clear Screen !",command=self.clear_screen)
        self.bouton_clearscreen.pack(side=tk.TOP)


        #Entry Speed
        L1 = tk.Label(self, text="Speed :")
        L1.pack(side=tk.TOP)

        self.speed =tk.StringVar(self)
        self.speed.set(30)
        self.button_speed = tk.Entry (self, textvariable=self.speed)
        self.button_speed.pack(side = tk.TOP)
        self.button_speed.get()

        #Entry K1
        L2 = tk.Label(self, text="Rayon cercle 1")
        L2.pack(side=tk.TOP)

        self.k =tk.IntVar(self)
        self.k.set(100)
        self.button_k = tk.Entry (self, textvariable=self.k)
        self.button_k.pack(side = tk.TOP)
        self.button_k.get()

        #Entry K2
        L3 = tk.Label(self, text="Coup suivant")
        L3.pack(side=tk.TOP)

        self.k2 =tk.IntVar(self)
        self.k2.set("E3")
        self.button_k2 = tk.Entry (self, textvariable=self.k2)
        self.button_k2.pack(side = tk.TOP)
        self.button_k2.get()




    def save(self):
        print("Save")

    def clear_screen(self):
        # self.canv.delete("all")
        for id in self.representationCyclo:
            self.canv.delete(id)

    def rd_col(self):
        return rd.choice(("black", "red", "green", "blue", "yellow", "magenta",
                          "cyan", "white", "purple"))

    def dessine_cercles(self):
            pass


    def quit(self):
        self.destroy()


if __name__ == "__main__":
    app = AppliCanevas()
    app.title("Jeu echec")
    app.mainloop()


