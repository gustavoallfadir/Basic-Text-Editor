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
colorcursor="black"

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
        global colorcursor

        fondoVar="white"
        fuenteVar="black"
        colormenu="#0B0B3B"
        fuentemenu="white"
        colorcursor="blue"


        root.destroy()
        iniciar()

    def Dskin():
        global fuenteVar
        global fondoVar
        global fuentemenu
        global colormenu
        global colorcursor

        fondoVar="black"
        fuenteVar="white"
        colormenu="black"
        fuentemenu="#2AEF0A"
        colorcursor="white"
        
        root.destroy()
        iniciar()


    def Mskin():
        global fuenteVar
        global fondoVar
        global fuentemenu
        global colormenu
        global colorcursor

        fondoVar="black"
        fuenteVar="#2AEF0A"
        colormenu="black"
        fuentemenu="white"
        colorcursor="white"
        
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
    menuSkin.add_command(label="Colores Matrix",command=lambda:Mskin())

    menuayuda=Menu(barramenu,tearoff=0, fg=fuentemenu, bg=colormenu)
    menuayuda.add_command(label="Acerca de...     ", command=acerca_de)

    barramenu.add_cascade(label="Archivo   ", menu=menuarchivo)
    barramenu.add_cascade(label="Color del editor ",menu=menuSkin)
    barramenu.add_cascade(label="Ayuda   ",menu=menuayuda)

    #---------Menu click derecho-----------------------


    def make_menu(w):
        global the_menu
        the_menu = Menu(w, tearoff=0)
        the_menu.add_command(label="Cortar  ")
        the_menu.add_command(label="Copiar  ")
        the_menu.add_command(label="Pegar  ")
    
    make_menu(root)

    def show_menu(e):
        w = e.widget
        the_menu.entryconfigure("Cortar  ",
        command=lambda: w.event_generate("<<Cut>>"))
        the_menu.entryconfigure("Copiar  ",
        command=lambda: w.event_generate("<<Copy>>"))
        the_menu.entryconfigure("Pegar  ",
        command=lambda: w.event_generate("<<Paste>>"))
        the_menu.tk.call("tk_popup", the_menu, e.x_root, e.y_root)


    #-------------Caja de texto-----------------------------

    textBox=Text(frame,width=30,height=10,wrap="none",font="14",insertbackground=colorcursor, fg=fuenteVar,bg=fondoVar)
    textBox.configure(font=("Courier 10 Pitch", 14))
    textBox.pack(side="top",fill="both",expand="true")

    scrollx=Scrollbar(frame, command=textBox.xview,width=15,orient="horizontal") 
    scrollx.pack(side="bottom",fill="x")

    yframe=Frame(root)
    yframe.pack(side="right",fill="y")

    scrolly=Scrollbar(yframe, command=textBox.yview, width=15)
    scrolly.pack(side="left",fill="y")

    textBox.config(xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
    textBox.bind("<Button-3><ButtonRelease-3>", show_menu)


iniciar()






root.mainloop()


