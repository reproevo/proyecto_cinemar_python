import tkinter as tk
from tkinter import *
from gui.login import WinLogin
import tkinter.messagebox as tkMsgBox

class WinCinemar:
    def __init__(self, ventana):
        self.ventana = ventana
        #Titulo de ventana
        ventana.title("Cinemar")
        #Icono de la ventana
        ventana.iconbitmap(default="cinemark.ico")
        #Fondo de la ventana
        ventana.config(bg = "black")
        #Tamaño de ventana
        ventana.geometry("400x300")
        ventana.resizable(width=False, height=False)
        #Cuerpo de la ventana
        button1 = Button(ventana, text="Cinemar",command=self.abrir_login)
        button1.place(x=100,y=110,width=200,height= 80)
    
    def abrir_login(self):
        WinLogin(self.ventana)

ventana = tk.Tk()
app = WinCinemar(ventana)
ventana.mainloop()