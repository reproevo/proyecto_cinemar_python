from tkinter import *
import tkinter as tk
from tkinter import *
from gui.winusuario import *

class WinUsuario(tk.Toplevel):
    def __init__(self, master=None,id_usuario=None):
        super().__init__(master)
        self.master = master
        self.id_usuario = id_usuario
        self.title("Menu Usuario")    
        #Tamaño de ventana
        self.resizable(width=False,height=False)
        self.config(padx=10,pady=10)
        #Cuerpo de la ventana        
        button1 = Button(self, text = "RESERVAR ENTRADA",command=self.crearWinReservas)
        button1.grid(row = 0, column = 0,sticky="ew", padx=10, pady=2,ipadx=3, ipady=3)
        button2 = Button(self, text = "MIS RESERVAS",command=self.crearWinMisReservas)
        button2.grid(row = 1, column = 0,sticky="ew", padx=10,pady=2,ipadx=3, ipady=3)
        button3 = Button(self, text = "HISTORIAL",command=self.crearWinHistorial)
        button3.grid(row = 2, column = 0,sticky="ew", padx=10,pady=2,ipadx=3, ipady=3)
        label1 = Label(self,width=40,height=2)
        label1.grid(row=3,column=0)
        button5 = Button(self, text = "SALIR",command = self.destroy)
        button5.grid(row = 4, column = 0, sticky="ew", padx=10, pady=2 , ipadx=3, ipady=3)

    def crearWinReservas(self):
        WinReservas(self.master,self.id_usuario)

    def crearWinMisReservas(self):
        WinMisReservas(self.master,self.id_usuario)

    def crearWinHistorial(self):
        WinHistorialReservas(self.master,self.id_usuario)