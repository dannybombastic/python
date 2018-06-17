from tkinter import*

root = Tk()
def pintar():
    texto = opcion.get()
    label.config(text=texto)
    
opcion = IntVar()
texto = StringVar()
texto.set(str(opcion.get()))
r1 = Radiobutton(root,text='Opcion 1', command=pintar ,variable=opcion,value=1).pack()
r2 = Radiobutton(root,text='Opcion 2', command=pintar ,variable=opcion,value=2).pack()
r3 = Radiobutton(root,text='Opcion 3', command=pintar ,variable=opcion,value=3).pack()
label = Label(root,text=texto.get())
label.pack()
root.mainloop()