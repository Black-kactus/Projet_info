#Ancien fichier : gestion de l'interface (à l'aide d'un code de référence)
# Import des noms du module

from tkinter import *
# Création d'un objet "fenêtre"
fenetre = Tk()
# Titre (Label)
titre = Label(fenetre, text = "L'informatique, c'est fantastique !")
# Affichage du titre
titre.pack()
# Ajout des autres widgets
# .........................
# Démarrage de la boucle Tkinter (à placer à la fin !!!)


resultat = StringVar()
resultat.set("10")
expression = StringVar()
expression.set("20")

print(type(resultat.get()),expression.get())

TOUT = StringVar()
# TOUT.set(str([resultat.get(),expression.get()]))
TOUT.set(str([resultat,expression]))

print(TOUT.get())

def calculer():
   resultat.set(eval(expression.get()))

fenetre.mainloop()