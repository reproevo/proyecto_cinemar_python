import tkinter as tk
from tkinter import *
from app import registro,disponibilidad
import tkinter.messagebox as tkMsgBox

class WinRegistro(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.title("Registro")   
        #Tamaño de ventana
        self.resizable(width=False, height=False)
        self.config(padx=10,pady=10)

        #Cuerpo de la ventana
        label1 = Label(self, text = "Usuario :")
        label1.grid(row = 0 ,column = 0,sticky="w",padx=2, pady=2, ipadx=2, ipady=2)
        
        entry1 = Entry(self,width=40,name="txtUsuario")
        entry1.grid(row = 0 ,column = 1,padx=2, pady=2, ipadx=2, ipady=2)

        label2 = Label(self, text="Password :")
        label2.grid(row = 1, column = 0,sticky="w",padx=2, pady=2, ipadx=2, ipady=2)

        entry2 = Entry(self, show="*",width=40,name="txtPassword")
        entry2.grid(row = 1 ,column = 1,padx=2, pady=2, ipadx=2, ipady=2)

        label3 = Label(self, text="Re-Password :")
        label3.grid(row = 2, column = 0,sticky="w",padx=2, pady=2, ipadx=2, ipady=2)

        entry3 = Entry(self, show="*",width=40,name="txtRePassword")
        entry3.grid(row = 2 ,column = 1,padx=2, pady=2, ipadx=2, ipady=2,)

        label4 = Label(self,text="Email :")
        label4.grid(row = 3, column = 0,sticky="w",padx=2, pady=2, ipadx=2, ipady=2)

        entry4 = Entry(self,width=40,name="txtEmail")
        entry4.grid(row = 3 ,column = 1,padx=2, pady=2, ipadx=2, ipady=2)

        label5 = Label(self,text="Nombre :")
        label5.grid(row = 4, column = 0,sticky="w",padx=2, pady=2, ipadx=2, ipady=2)
        
        entry5 = Entry(self,width=40,name="txtNombre")
        entry5.grid(row = 4 ,column = 1,padx=2, pady=2, ipadx=2, ipady=2)

        label6 = Label(self,text="Apellido :")
        label6.grid(row = 5, column = 0,sticky="w",padx=2, pady=2, ipadx=2, ipady=2)

        entry6 = Entry(self,width=40,name="txtApellido")
        entry6.grid(row = 5 ,column = 1,padx=2, pady=2, ipadx=2, ipady=2)

        button1 = Button(self, text = "Enviar",command=self.iniciar_registro)
        button1.grid(row = 6, column = 1,sticky="w", pady=2,ipadx=3, ipady=3)

        button2 = Button(self, text = "Cancelar",command = self.destroy)
        button2.grid(row = 6, column = 1,sticky="e", pady=2,ipadx=3, ipady=3)

    def iniciar_registro(self):
        try:
            txtUsuario = self.nametowidget("txtUsuario")
            usuario = txtUsuario.get()            

            txtPassword = self.nametowidget("txtPassword")
            password = txtPassword.get()

            txtRePassword = self.nametowidget("txtRePassword")
            repassword = txtRePassword.get()

            txtEmail = self.nametowidget("txtEmail")
            email = txtEmail.get()

            txtNombre = self.nametowidget("txtNombre")
            nombre = txtNombre.get()

            txtApellido = self.nametowidget("txtApellido")
            apellido = txtApellido.get()

            if usuario != "" and password != "" and repassword !="" and email !="" and nombre != "" and apellido !="":
                if password == repassword:
                    if disponibilidad(usuario):
                        if registro(usuario,password,email,nombre,apellido):
                            tkMsgBox.showwarning(self.master.title(), "Se produjo un error al intentar registrarse")
                        else:
                            tkMsgBox.showinfo(self.master.title(), "Registro agregado!!!!!!")
                            self.destroy()
                    else:
                            tkMsgBox.showwarning(self.master.title(), "El nombre de Usuario ya existe")
                else:
                    tkMsgBox.showwarning(self.master.title(), "Las contraseñas no coinciden")
            else:
                tkMsgBox.showwarning(self.master.title(), "Existen campos sin completar")
        except Exception as ex:
            tkMsgBox.showerror(self.master.title(), str(ex))