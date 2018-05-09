import os
import os.path
from tkinter import *
import tkinter as tk
import stat

home = "C:\\"

def has_hidden_attribute(filepath):
    return bool(os.stat(filepath).st_file_attributes & stat.FILE_ATTRIBUTE_HIDDEN)

def noHiddenDir():
    dir = os.listdir()
    hidden = []
    for elemento in dir:
        if has_hidden_attribute(os.path.abspath(elemento)):
            hidden.append(elemento)
    for elemento in hidden:
        dir.remove(elemento)
    return dir

def entrarEnDirectorio(directorio):
    for child in cRight.winfo_children():
        child.destroy()
    scroll = Scrollbar(cRight, orient="vertical", jump=True)
    scroll.pack(side=RIGHT, fill=Y)
    os.chdir(directorio)
    directorios = noHiddenDir()
    lista = Listbox(cRight,height=len(directorios),fg="black",bg="#ada6a6",selectmode=SINGLE,
    yscrollcommand=scroll.set,bd=0,width=30)
    for i in range(len(directorios)):
        lista.insert(i+1," "+directorios[i])
    lista.place(x=210,y=40)
    scroll.config(command=lista.yview)
    cwd = Label(cRight, text=os.getcwd(), bg="#ada6a6").place(x=210, y=10)

#GUI
root = tk.Tk()
root.minsize(height=700,width=900)
root.resizable(width=False,height=False)
root.title("File Explorer")

cRight = Canvas(root,bg="#ada6a6",width=700)
cRight.place(width=900,height=700)
cLeft = Canvas(root,bg="#ada6a6",width=200).place(width=200,height=700)
scroll = Scrollbar(cRight,orient="vertical",jump=True)
scroll.pack(side=RIGHT,fill= Y)
dir = Label(cLeft,text="Unidades lógicas",bg="#ada6a6").place(x=10,y=10)
homeBoton= Button(cLeft,text=home,bg="#ada6a6",command= lambda: entrarEnDirectorio(home)).place(x=15,y=30,height=30)
if os.listdir("D:\\"):
    botonD = Button(cLeft,text="D:\\",bg="#ada6a6",command= lambda: entrarEnDirectorio("D:\\")).place(x=15,y=65,height=30)


root.mainloop()
