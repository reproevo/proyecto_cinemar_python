from tkinter import *

class WinLogin():
    def __init__(self, ventana):
        #Titulo de ventana
        ventana.title("Proyecto Cinemar")
        #Tamaño de ventana
        ventana.geometry("300x200")
        ventana.resizable(width=False, height=False)
        #Cuerpo de la ventana
        label1 = Label(ventana, text = "Usuario :")
        label1.grid(row = 0 ,column = 0)
        
        entry1 = Entry(ventana)
        entry1.grid(row = 0 ,column = 1)

        label2 = Label(ventana, text="Password :")
        label2.grid(row = 1, column = 0)

        entry2 = Entry(ventana, show="*")
        entry2.grid(row = 1 ,column = 1)

        button1 = Button(ventana, text = "Ingresar")
        button1.grid(row = 3, column = 1)
