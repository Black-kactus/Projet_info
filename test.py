from tkinter import *
from tkinter import ttk

root = Tk()

content = ttk.Frame(root, padding=(0,0,0,0))
frame = ttk.Frame(content, borderwidth=0, relief="ridge", width=100, height=100)
namelbl = ttk.Label(content, text="Name")
name = ttk.Entry(content)

onevar = BooleanVar()
twovar = BooleanVar()
threevar = BooleanVar()

onevar.set(True)
twovar.set(False)
threevar.set(True)

one = ttk.Checkbutton(content, text="One", variable=onevar, onvalue=True)
two = ttk.Checkbutton(content, text="Two", variable=twovar, onvalue=True)
three = ttk.Checkbutton(content, text="Three", variable=threevar, onvalue=True)
ok = ttk.Button(content, text="Valider")
cancel = ttk.Button(content, text="Abandonner")

content.grid(column=0, row=0, sticky=(N, S, E, W))

for i in range(0,18,2):
    for j in range(0,18,2):
        print(i,j)
        namelbl = ttk.Label(content, text= str(i)+","+str(j),relief="solid")
        namelbl.grid(column=i, row=j, columnspan=2, rowspan=2,sticky=(N,S,E,W),pady=1, padx=1)
        


root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
    
for i in range(0,20):
    content.columnconfigure(i,weight=1)
    content.rowconfigure(i,weight=1)

Lvide = ttk.Label(content, text= "vide",relief="solid")
Lvide.grid(column=18, row=0, columnspan=2, rowspan=18,sticky=(N,S,E,W),pady=1, padx=1)

Lcommencer = ttk.Label(content, text= "Commencer",relief="solid")
Lcommencer.grid(column=20, row=0, columnspan=4, rowspan=2,sticky=(N,S,E,W),pady=1, padx=1)

Lcouleurquijoue = ttk.Label(content, text= "Couleur qui joue",relief="solid")
Lcouleurquijoue.grid(column=20, row=2, columnspan=4, rowspan=1,sticky=(N,S,E,W),pady=1, padx=1)

Lcouleuractualise= ttk.Label(content, text= "blanc",relief="solid")
Lcouleuractualise.grid(column=20,row=3, columnspan=4, rowspan=1,sticky=(N,S,E,W),pady=1, padx=1)





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

root.mainloop()