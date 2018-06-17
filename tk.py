from tkinter import *

root = Tk()
root.title("Hola mundo")
root.iconbitmap("./hola.ico")
# or frame = Frame(root,width=300, height=300)
frame = Frame(root)
frame.pack(side='bottom',anchor='w')
frame.config(bg='black')
# frame.pack(fill='y or x or both',expand=1)

frame.config(width=300, height=300)
frame.config(cursor="pirate")
label = Label(frame,text='!Hola mundo¡')
label.place(x=100,y=100)
root.mainloop()  # siempre al final
