from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os
import sys


#---------------------  Skin--------------------------

fondoVar="white"
fuenteVar="black"
colormenu="#0B0B3B"
fuentemenu="white"

#----------------------Root-------------------------
def iniciar():
    global root
    root=Tk()
    root.geometry("500x500+350+50")
    root.title("GuzPad")
    root.minsize(300,300)


    #----------------------Frame------------------------

    frame=Frame(root)
    frame.pack(padx=1,pady=1,side="left", fill="both",expand="true")




    #----------------------Comandos---------------------
    def nuevo():
        textBox.delete(1.0,END)

    
    def abrir():

        archivo=filedialog.askopenfilename(filetypes =[('Archivo de texto', '*.txt')])
        
        temp=open(archivo,"r")

        text=temp.read()

        textBox.delete(1.0,END)
        textBox.insert(1.0, text)

        temp.close()


    def guardar():
        temp=textBox.get(1.0,END)
        
        file=filedialog.asksaveasfilename(filetypes =[('Archivo de texto', '*.txt')])

        target=open(file, "w")
        
        target.write(temp)

        target.close()

    def Lskin():
        global fuenteVar
        global fondoVar
        global fuentemenu
        global colormenu

        fondoVar="white"
        fuenteVar="black"
        colormenu="#0B0B3B"
        fuentemenu="white"

        root.destroy()
        iniciar()

    def Dskin():
        global fuenteVar
        global fondoVar
        global fuentemenu
        global colormenu

        fondoVar="black"
        fuenteVar="white"
        colormenu="black"
        fuentemenu="#2AEF0A"
        
        root.destroy()
        iniciar()

    def salir():
        root.destroy()

    def acerca_de():
        messagebox.showinfo("Editor de texto","Creado por Gustavo Allfadir\nTodos los derechos reservados.\n©2020")

    #-----------------------Menus------------------------

    #Setup

    barramenu=Menu(root, fg=fuentemenu, bg=colormenu)
    root.config(menu=barramenu)

    #Comandos menu

    menuarchivo=Menu(barramenu, tearoff=0, fg=fuentemenu, bg=colormenu)
    menuarchivo.add_command(label="Nuevo      ", command=lambda:nuevo())
    menuarchivo.add_command(label="Abrir      ", command=lambda:abrir())
    menuarchivo.add_command(label="Guardar      ", command=lambda:guardar())
    menuarchivo.add_command(label="Salir", command=lambda:salir())

    menuSkin=Menu(barramenu,tearoff=0,fg=fuentemenu,bg=colormenu)
    menuSkin.add_command(label="Colores claros", command=lambda:Lskin())
    menuSkin.add_command(label="Colores oscuros", command=lambda:Dskin())

    menuayuda=Menu(barramenu,tearoff=0, fg=fuentemenu, bg=colormenu)
    menuayuda.add_command(label="Acerca de...     ", command=acerca_de)

    barramenu.add_cascade(label="Archivo   ", menu=menuarchivo)
    barramenu.add_cascade(label="Color del editor ",menu=menuSkin)
    barramenu.add_cascade(label="Ayuda   ",menu=menuayuda)


    #-------------Caja de texto-----------------------------

    textBox=Text(frame,width=30,height=10,wrap="none",font=10, fg=fuenteVar,bg=fondoVar)
    textBox.pack(side="top",fill="both",expand="true")

    scrollx=Scrollbar(frame, command=textBox.xview,width=15,orient="horizontal") 
    scrollx.pack(side="bottom",fill="x")

    yframe=Frame(root)
    yframe.pack(side="right",fill="y")

    scrolly=Scrollbar(yframe, command=textBox.yview, width=15)
    scrolly.pack(side="left",fill="y")

    textBox.config(xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)

iniciar()






root.mainloop()


