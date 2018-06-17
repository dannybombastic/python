from tkinter import*

root = Tk()
root.config(padx=10,pady=10)
#frame = Frame(root,width=100,height=100)
#frame.pack()
#frame_2 = Frame(root,width=100,height=100)
#frame_2.pack()
label = Label(root,text="campos de entrada")
label.grid(row=0,column=0)
entry = Entry(root)
entry.grid(row=0,column=1)
entry.config(justify='center',state='disable')


label_2 = Label(root,text="apellidos")
label_2.grid(row=1,column=0,sticky='w')

entry_2 = Entry(root)
entry_2.grid(row=1,column=1)
entry_2.config(show='-')

root.mainloop()