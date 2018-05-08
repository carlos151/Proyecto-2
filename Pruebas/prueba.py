import os
import os.path
from tkinter import *
import tkinter as tk
from pathlib import Path


home = str(Path.home())
os.chdir(home)

def noHiddenDir():
    dir = os.listdir()
    hidden = []
    for elemento in dir:
        if elemento[0] == ".":
            hidden.append(elemento)
    for elemento in hidden:
        dir.remove(elemento)
    return dir

def botonHome():
    directorios = noHiddenDir()
    y = 143
    for elemento in directorios:
        if os.path.isdir(home + "/" + elemento):
            color = "#fff5a0"
        else:
            color = "#c0e7f9"
        boton=Button(c,text=elemento,bg=color).place(x=30,y=y)
        y += 30
#GUI
root = tk.Tk()
root.minsize(900,700)
root.title("File Explorer")

marco = Frame(root,width=200,height=700).place(anchor="e")
c = Canvas(marco,bg="#ada6a6").place(width=200,height=700)
dir = Label(c,text="Directorios",bg="#ada6a6").place(x=10,y=85)
homeBoton= Button(c,text=home,bg="#fff5a0",command= lambda: botonHome()).place(x=15,y=110,height=30)


root.mainloop()