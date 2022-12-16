from tkinter import *

import tkinter as tk
from tkinter import *

class WinUsuario(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.title("Menu Usuario")    
        #Tamaño de ventana
        self.resizable(width=False,height=False)
        self.config(padx=10,pady=10)
        #Cuerpo de la ventana        
        button1 = Button(self, text = "RESERVAR ENTRADA")
        button1.grid(row = 0, column = 0,sticky="ew", padx=10, pady=2,ipadx=3, ipady=3)
        button2 = Button(self, text = "MODIFICAR RESERVA")
        button2.grid(row = 1, column = 0,sticky="ew", padx=10,pady=2,ipadx=3, ipady=3)
        button3 = Button(self, text = "MIS RESERVAS")
        button3.grid(row = 2, column = 0,sticky="ew", padx=10,pady=2,ipadx=3, ipady=3)
        button4 = Button(self, text = "HISTORIAL")
        button4.grid(row = 3, column = 0,sticky="ew", padx=10,pady=2,ipadx=3, ipady=3)
        label1 = Label(self,width=40,height=2)
        label1.grid(row=4,column=0)
        button5 = Button(self, text = "SALIR",command = self.destroy)
        button5.grid(row = 5, column = 0, sticky="ew", padx=10, pady=2 , ipadx=3, ipady=3)