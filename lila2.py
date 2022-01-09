#Ancien fichier : gestion de l'interface

import tkinter as tk
from PIL import Image, ImageTk
 
# Create the master object
master = tk.Tk()
 
# Create the label objects and pack them using grid
tk.Label(master, text="Label 1").grid(row=0, column=0)
tk.Label(master, text="Label 2").grid(row=1, column=0)
 
# Create the entry objects using master
e1 = tk.Entry(master)
e2 = tk.Entry(master)
 
# Pack them using grid
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
 
button1 = tk.Button(master, text="Button 1")
button1.grid(columnspan=2, row=2, column=0)
 
# Create the PIL image object
image = Image.open("pion_noir.png")
photo = ImageTk.PhotoImage(image)

# Create an image label
img_label = tk.Label(image=photo)
# Store a reference to a PhotoImage object, to avoid it
# being garbage collected! This is necesary to display the image!
img_label.image = photo
 
img_label.grid(row=0, column=2, rowspan= 2, columnspan= 2)
 
# Create another button
button2 = tk.Button(master, text="Button 2")
button2.grid(columnspan=2, row=2, column=2)

for i in range(0,3):
    master.columnconfigure(i,weight=1)

for j in range(0,3):
    master.rowconfigure(j,weight=1)
 
# The mainloop
tk.mainloop()