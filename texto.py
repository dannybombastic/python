from tkinter import*

root = Tk()
texti = StringVar()

def hola():
   texti.set("ya cambie")
   crear_label(texti)

def crear_label(tex):
    Label(root,textvariable=texti).pack()


texto = Text(root)
texto.pack()
texto.config(width=25,height=5,font=("Consolas",18),padx=10, selectbackground='red')
cadena = texti.get()
button = Button(root,text="agrega etiqueta",command=hola)
button.pack()


root.mainloop()