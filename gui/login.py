import tkinter as tk
from tkinter import *
import tkinter.messagebox as tkMsgBox
from gui.registro import WinRegistro
from gui.usuario import WinUsuario
from gui.administrador import WinAdmin
from app import inicio_sesion

class WinLogin(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.title("Login")    
        #Tamaño de ventana
        self.resizable(width=False,height=False)
        self.config(padx=10,pady=10)
        #Cuerpo de la ventana
        label1 = Label(self, text = "Usuario :")
        label1.grid(row = 0 ,column = 0, sticky="w", padx=2, pady=2, ipadx=2, ipady=2)
        
        entry1 = Entry(self,name= "txtUsuario",width=40)
        entry1.grid(row = 0 ,column = 1, padx=2, pady=2, ipadx=2, ipady=2)

        label2 = Label(self, text="Password :")
        label2.grid(row = 1, column = 0, sticky="w", padx=2, pady=2, ipadx=2, ipady=2)

        entry2 = Entry(self, show="*",name="txtPassword",width=40)
        entry2.grid(row = 1 ,column = 1, padx=2, pady=2, ipadx=2, ipady=2)

        button1 = Button(self, text = "Ingresar",command=self.iniciar_sesion)
        button1.grid(row = 3, column = 1, pady=2, ipadx=2, ipady=2,sticky="w")

        button1 = Button(self, text = "Registrarse",command=self.abrir_registro)
        button1.grid(row = 3, column = 1, pady=2, ipadx=2, ipady=2,sticky="e")
    
    def iniciar_sesion(self):
        try:
            txtUsuario = self.nametowidget("txtUsuario")
            usuario = txtUsuario.get()            

            txtPassword = self.nametowidget("txtPassword")
            password = txtPassword.get()

            if usuario != "" and password != "":
                if inicio_sesion(usuario, password):
                    consulta = inicio_sesion(usuario,password)[1][0][6]
                    idConsulta = inicio_sesion(usuario,password)[1][0][0]
                    if consulta == 0:
                        WinUsuario(self.master,idConsulta)
                    elif consulta == 1:
                        print("Ventana de Admin")
                        WinAdmin(self.master)
                    elif consulta == 2:
                        print("Ventana de Supervisor")
                        WinAdmin(self.master)
                    elif consulta == 3:
                        tkMsgBox.showerror(self.master.title(), "Usuario Bloqueado")
                    elif consulta == 4:
                        WinUsuario(self.master,idConsulta)
                    else:
                        tkMsgBox.showerror(self.master.title(), "Se produjo un error al obtener los datos del usuario, reintente nuevamente")
                else:
                    tkMsgBox.showwarning(self.master.title(), "Usuario/Contraseña incorrecta")
            else:
                tkMsgBox.showwarning(self.master.title(), "Usuario o Password vacio")
        except Exception as ex:
            tkMsgBox.showerror(self.master.title(), str(ex))

    def abrir_registro(self):
        WinRegistro(self.master)