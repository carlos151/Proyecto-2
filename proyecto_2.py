import os
import os.path
from tkinter import *
import tkinter as tk
import stat
from tkinter import messagebox
import datetime

def has_hidden_attribute(filepath):
    return bool(os.stat(filepath).st_file_attributes & stat.FILE_ATTRIBUTE_HIDDEN)

def noHiddenDir(): #función para eliminar directorios ocultos
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
        return "Acceso denegado"

def CurSelet(event): #funcion para la selección actual en las listboxes
    try:
        widget = event.widget
        value = str((widget.get(widget.curselection())))
        return value
    except:
        pass

def show_error(self, *args): #muestra una ventana para las excepciones de tkinter
    messagebox.showerror('Error',"No ha seleccionado una carpeta")

def convert_bytes(num): #hace una conversion de bytes hasta su máxima expresión
    for x in ['B', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0

def ejecutarArchivo(archivo):
    if os.path.isfile(archivo):
        os.startfile(archivo)
    else:
        messagebox.showinfo("Error","No ha seleccionado un archivo")

def get_size(file_path):
    if os.path.isfile(file_path):
        file_info = os.stat(file_path)
        return convert_bytes(file_info.st_size)
    else:
        return " "

def obtenerTamaños(directorios):
    resultado = []
    for elemento in directorios:
        path = os.path.join(os.getcwd(),elemento)
        size = get_size(path)
        resultado.append(size)
    return resultado

def separarArchivosCarpetas(directorios):
    resultado = directorios.copy()
    for elemento in directorios:
        if not os.path.isdir(os.path.join(os.getcwd(),elemento)):
            resultado.remove(elemento)
            resultado.append(elemento)
    return resultado

def get_extension(path):
    try:
        path = path[-4:]
        extention = path.split('.')[1]
    except:
        extention = ""
    return extention

def obtenerExtensiones(directorios):
    resultado = []
    for elemento in directorios:
        path = os.path.join(os.getcwd(),elemento)
        extension = get_extension(path)
        resultado.append(extension)
    return resultado

def get_fecha(path):
    fecha = str(datetime.datetime.fromtimestamp(os.path.getmtime(path)))
    año = fecha[:4]
    mes = fecha[5:7]
    dia = fecha[8:10]
    return dia + "/" + mes + "/" + año

def obtenerFechas(directorio):
    resultado = []
    for elemento in directorio:
        file_path = os.path.join(os.getcwd(),elemento)
        fecha = get_fecha(file_path)
        resultado.append(str(fecha)[:10])
    return resultado

def directorioAnterior(path):
    slash = 0
    for i in range(len(path)):
        if path[i] == "\\":
            slash = i
    newPath = path[:slash]
    return newPath

def MouseWheel(event,arg): #Función para añadir la función de scroll
    for lista in arg:
        lista.yview("scroll",-(event.delta),"units")
    return "break"

def entrarEnDirectorio(directorio,ord="n"):
    for child in cRight.winfo_children():#Borrar directorios anteriores de la ventana
        child.destroy()
    try:
        os.chdir(directorio)
    except:
        messagebox.showinfo("Error","No ha seleccionado una carpeta")

    directorios = noHiddenDir()
    if type(directorios) == list:
        if ord == "n":#ordenar directorios alfabeticamente
            directorios.sort(key = lambda k : k.lower())

        directorios = separarArchivosCarpetas(directorios)

    if type(directorios) == list: #listas con todos los tamaños,extensiones y fechas
        tamaños = obtenerTamaños(directorios)
        extensiones = obtenerExtensiones(directorios)
        fechas = obtenerFechas(directorios)

    #listboxes de directorios,tamaños,etc
    lista = Listbox(cRight,height=34,fg="black",bg="#ada6a6",bd=0,width=47,font=("Arial","12"))
    listaTamaño = Listbox(cRight,height=34,fg="black",bg="#ada6a6",bd=0,width=8,font=("Arial","12"))
    listaExtension = Listbox(cRight,height=34,fg="black",bg="#ada6a6",bd=0,width=10,font=("Arial","12"))
    listaFechas = Listbox(cRight,height=34,fg="black",bg="#ada6a6",bd=0,width=10,font=("Arial","12"))

    #textos
    cwd = Label(cRight, text=os.getcwd(), bg="#ada6a6", font=("Arial", "12")).place(x=210, y=10)
    acciones = Label(cLeft, text="Acciones", bg="#ada6a6", font=("Arial", "12")).place(x=6, y=70)
    ordenar = Label(cLeft, text="Ordenar por", bg="#ada6a6", font=("Arial", "12")).place(x=6, y=345)

    #Botones de acciones y ordenamientos
    ejecutar = Button(cLeft,text="Ejecutar archivo",bg="#ada6a6",command = lambda: ejecutarArchivo(os.path.join(os.getcwd()
    ,lista.get("active"))),font=("Arial", "12"))
    ejecutar.place(x=8, y=128,width=185)
    abrir = Button(cLeft,text="Abrir carpeta",bg="#ada6a6",command = lambda: entrarEnDirectorio(os.path.join(os.getcwd()
    ,lista.get("active"))), font=("Arial", "12"))
    crearDir = Button(cLeft,text="Crear directorio",bg="#ada6a6",font=("Arial", "12"))
    crearDir.place(x=8,y=163,width=185)
    consultarInfo = Button(cLeft,text="Consultar información",bg="#ada6a6",font=("Arial", "12"))
    consultarInfo.place(x=8,y=198,width=185)
    eliminar = Button(cLeft,text="Eliminar",bg="#ada6a6",font=("Arial", "12"))
    eliminar.place(x=8,y=234,width=185)
    copiar = Button(cLeft,text="Copiar",bg="#ada6a6",font=("Arial", "12"))
    copiar.place(x=8,y=270,width=185)
    atras = Button(cLeft, text="Atrás", bg="#ada6a6",command=lambda: entrarEnDirectorio(directorioAnterior(os.getcwd())), font=("Arial", "12"))
    atras.place(x=8, y=305, width=185)
    nombre = Button(cLeft,text="Nombre",bg="#ada6a6",font=("Arial", "12"))
    nombre.place(x=8,y=370,width=73)
    tamaño = Button(cLeft, text="Tamaño", bg="#ada6a6", font=("Arial", "12"))
    tamaño.place(x=8, y=405,width=73)
    tipo = Button(cLeft, text="Tipo", bg="#ada6a6", font=("Arial", "12"))
    tipo.place(x=8, y=440,width=73)

    #llenar listboxes
    if type(directorios) == list:
        for i in range(len(directorios)):
            lista.insert(i,directorios[i])
            abrir.place(x=8, y=95,width=185)
        for i in range(len(tamaños)):
            listaTamaño.insert(i," " + tamaños[i])
        for i in range(len(extensiones)):
            if os.path.isdir(os.path.join(os.getcwd(),extensiones[i])):
                listaExtension.insert(i," " + "Carpeta")
            else:
                listaExtension.insert(i," " + "Archivo " + extensiones[i])
        for i in range(len(fechas)):
            listaFechas.insert(i," " + fechas[i])
    else:
        lista.insert(1,directorios)
        abrir.destroy()
    
    listas = [lista,listaTamaño,listaExtension,listaFechas]
    lista.bind('<<ListboxSelect>>',CurSelet)
    lista.bind('<MouseWheel>',lambda event, arg = listas: MouseWheel(event,arg))
    listaTamaño.bind('<MouseWheel>',lambda event, arg = listas: MouseWheel(event,arg))
    listaExtension.bind('<MouseWheel>',lambda event, arg = listas: MouseWheel(event,arg))
    listaFechas.bind('<MouseWheel>',lambda event, arg = listas: MouseWheel(event,arg))
    lista.place(x=210,y=40)
    listaTamaño.place(x=631,y=40)
    listaExtension.place(x=704,y=40)
    listaFechas.place(x=795,y=40)
    tk.Tk.report_callback_exception = show_error #Atrapa las excepciones de tkinter

#GUI principal
root = tk.Tk()
root.minsize(height=700,width=900)
root.resizable(width=False,height=False)
root.title("File Explorer")

cRight = Canvas(root,bg="#ada6a6",width=700)
cRight.place(width=900,height=700)
cLeft = Canvas(root,bg="#ada6a6",width=200).place(width=200,height=700)
unidadesLogicas = Label(cLeft,text="Unidades lógicas",bg="#ada6a6",font=("Arial","12")).place(x=5,y=10)
homeBoton= Button(cLeft,text="C:\\",bg="#ada6a6",command= lambda: entrarEnDirectorio("C:\\"),font=("Arial","12")).place(x=8,y=35,height=30)
if os.listdir("D:\\"):
    botonD = Button(cLeft,text="D:\\",bg="#ada6a6",command= lambda: entrarEnDirectorio("D:\\"),font=("Arial","12")).place(x=48,y=35,height=30)
propiedades = Button(cLeft,text="Propiedades",bg="#ada6a6",font=("Arial", "12")).place(x=88,y=35,height=30)


root.mainloop()
