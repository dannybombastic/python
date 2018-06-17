from tkinter import*

root = Tk()
"""
texto = StringVar()
texto.set("hola mundo desde el StringVar")

# frame = Frame(root,width=480,height=380)
# frame.pack()
label = Label(root,text="hola mundo")
label
label.pack(anchor='nw')
Label(root,text="hola mundo").pack(anchor='center')
Label(root,text="hola mundo").pack(anchor='se')
label.config(bg='green',fg='white', font=("Verdana",24))
label.config(textvariable=texto)
"""
imagen = PhotoImage(file='./imagen.gif')
Label(root,image=imagen, bd=0,bg='green').pack(fill='y',expand=1)
root.mainloop()