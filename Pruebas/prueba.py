import os
import os.path
from tkinter import *
import tkinter as tk
import stat
from tkinter import messagebox
import traceback

home = "C:\\"

def has_hidden_attribute(filepath):
    return bool(os.stat(filepath).st_file_attributes & stat.FILE_ATTRIBUTE_HIDDEN)

def noHiddenDir():
    try:
        dir = os.listdir()
        hidden = []
        for elemento in dir:
            if has_hidden_attribute(os.path.abspath(elemento)):
                hidden.append(elemento)
        for elemento in hidden:
            dir.remove(elemento)
        return dir
    except:
        return "No tiene permisos para acceder a esta carpeta"

def CurSelet(event):
    widget = event.widget
    value = str((widget.get(widget.curselection())))
    return value

def show_error(self, *args):
    messagebox.showerror('Exception',"No ha seleccionado nada")

def entrarEnDirectorio(directorio):
    for child in cRight.winfo_children():
        child.destroy()
    try:
        os.chdir(directorio)
    except:
        messagebox.showinfo("Error","No ha seleccionado una carpeta")
    directorios = noHiddenDir()
    lista = Listbox(cRight,height=34,fg="black",bg="#ada6a6",selectmode=SINGLE,
    bd=0,width=73,font=("Arial","12"))
    scroll = Scrollbar(cRight, orient=VERTICAL,command=lista.yview)
    scroll.pack(side=RIGHT, fill=Y)
    lista.config(yscrollcommand=scroll.set)
    cwd = Label(cRight, text=os.getcwd(), bg="#ada6a6", font=("Arial", "12")).place(x=210, y=10)
    abrir = Button(cLeft,text="Abrir carpeta",bg="#ada6a6",command = lambda: entrarEnDirectorio(os.path.join(os.getcwd()
    ,lista.get("active"))), font=("Arial", "12"))
    tk.Tk.report_callback_exception = show_error
    if type(directorios) == list:
        for i in range(len(directorios)):
            lista.insert(i,directorios[i])
            abrir.place(x=55, y=35, height=30)
    else:
        lista.insert(1,directorios)
        abrir.destroy()
    lista.bind('<<ListboxSelect>>',CurSelet)
    lista.place(x=210,y=40)

#GUI
root = tk.Tk()
root.minsize(height=700,width=900)
root.resizable(width=False,height=False)
root.title("File Explorer")


cRight = Canvas(root,bg="#ada6a6",width=700)
cRight.place(width=900,height=700)
cLeft = Canvas(root,bg="#ada6a6",width=200).place(width=200,height=700)
dir = Label(cLeft,text="Unidades lógicas",bg="#ada6a6",font=("Arial","12")).place(x=10,y=10)
homeBoton= Button(cLeft,text=home,bg="#ada6a6",command= lambda: entrarEnDirectorio(home),font=("Arial","12")).place(x=15,y=35,height=30)
if os.listdir("D:\\"):
    botonD = Button(cLeft,text="D:\\",bg="#ada6a6",command= lambda: entrarEnDirectorio("D:\\"),font=("Arial","12")).place(x=15,y=70,height=30)



root.mainloop()
