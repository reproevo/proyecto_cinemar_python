from tkinter import *
import tkinter.ttk as ttk
import tkinter as tk
from app import listar_usuarios
from app import registroAdm
from app import disponibilidad
from app import consultar_usuario
from app import encriptar_contraseña
from app import editarUsuarioAdm
import tkinter.messagebox as tkMsgBox

class WinUsuarios(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)        
        self.master = master
        self.title("Menu de Administracion de Usuarios")
        self.resizable(width=False, height=True)
        
        #Menu
        label1= Label(self,text="Menu de Administracion de Usuarios",font="20")
        label1.pack()
        label2= Label(self,text="Estados: 0-Usuario   1-Administrador   2-Supervisor   3-Bloqueado   4-Vip")
        label2.pack()

        tv = ttk.Treeview(self, columns=("usuario", "password","email","nombre","apellido","estado"), name="tvUsuarios")
        tv.column("#0", width=50)
        tv.column("usuario", width=100, anchor=CENTER)
        tv.column("password", width=100, anchor=CENTER)
        tv.column("email", width=250, anchor=CENTER)
        tv.column("nombre", width=100, anchor=CENTER)
        tv.column("apellido", width=100, anchor=CENTER)
        tv.column("estado", width=50, anchor=CENTER)
        
        tv.heading("#0", text="Id", anchor=CENTER)
        tv.heading("usuario", text="Usuario", anchor=CENTER)
        tv.heading("password", text="Password", anchor=CENTER)
        tv.heading("email", text="Email", anchor=CENTER)
        tv.heading("nombre", text="Nombre", anchor=CENTER)
        tv.heading("apellido", text="Apellido", anchor=CENTER)
        tv.heading("estado", text="Estado", anchor=CENTER)
        
        tv.bind("<<TreeviewSelect>>", self.obtener_fila)
        tv.pack(padx=5,pady=5,side=LEFT,fill=Y)

        frame1= Frame(self)
        frame1.pack(side=RIGHT)
        button1=Button(frame1,text="AGREGAR",command=self.abrir_crearUsuarioAdm)
        button1.pack(padx=5,pady=5,ipadx=5,ipady=5,fill=X)
        button2=Button(frame1,text="EDITAR",command=self.abrir_editarUsuarioAdm)
        button2.pack(padx=5,pady=5,ipadx=5,ipady=5,fill=X)
        button3=Button(frame1,text="ELIMINAR")
        button3.pack(padx=5,pady=5,ipadx=5,ipady=5,fill=X)
        button4=Button(frame1,text="ACTUALIZAR",command=self.refrescar)
        button4.pack(padx=5,pady=5,ipadx=5,ipady=5,fill=X)
        
        self.refrescar()

    def abrir_crearUsuarioAdm(self):
        WinCrearUsuarioAdm(self.master)

    def abrir_editarUsuarioAdm(self):
        WinEditarUsuarioAdm(self.master,self.select_id)

    def obtener_fila(self, event):
        tvUsuarios = self.nametowidget("tvUsuarios")
        current_item = tvUsuarios.focus()
        if current_item:
            data = tvUsuarios.item(current_item)
            self.select_id = int(data["text"])
        else:
            self.select_id = -1

    def refrescar(self):        
        tvUsuarios = self.nametowidget("tvUsuarios")
        for record in tvUsuarios.get_children():
            tvUsuarios.delete(record)
        usuarios = listar_usuarios()
        for i in usuarios:
            tvUsuarios.insert("", END, text=i[0], values=(i[1], i[2], i[3], i[4], i[5], i[6]))
#-------------------------------CRUD USUARIOS---------------------------
class WinCrearUsuarioAdm(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.title("Crear Usuario")   
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

        label7 = Label(self,text="Estado :")
        label7.grid(row = 6, column = 0,sticky="w",padx=2, pady=2, ipadx=2, ipady=2)

        formato = ttk.Combobox(self, state="readonly", values=("Usuario","Administrador","Supervisor","Vip"), name="txtEstado")
        formato.grid(row = 6 ,column = 1,padx=2, pady=2, ipadx=2, ipady=2,sticky="ew")

        button1 = Button(self, text = "Enviar",command=self.crear_usuarioAdm)
        button1.grid(row = 7, column = 1,sticky="w", pady=2,ipadx=3, ipady=3)

        button2 = Button(self, text = "Cancelar",command = self.destroy)
        button2.grid(row = 7, column = 1,sticky="e", pady=2,ipadx=3, ipady=3)

    def crear_usuarioAdm(self):
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

            txtEstado = self.nametowidget("txtEstado")
            estado = txtEstado.get()
            
            if estado == "Usuario":
                val_estado = 0
            elif estado == "Administrador":
                val_estado = 1
            elif estado == "Supervisor":
                val_estado = 2
            elif estado == "Vip":
                val_estado = 4
            else:
                tkMsgBox.showwarning(self.master.title(), "Existen campos sin completar")

            if usuario != "" and password != "" and repassword !="" and email !="" and nombre != "" and apellido !="" and val_estado !="":
                if password == repassword:
                    if disponibilidad(usuario):
                        if registroAdm(usuario,password,email,nombre,apellido,val_estado):
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

class WinEditarUsuarioAdm(tk.Toplevel):
    def __init__(self, master=None,id=None):
        super().__init__(master)
        self.master = master
        self.id_usuario = id
        self.title("Editar Usuario")   
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

        label7 = Label(self,text="Estado :")
        label7.grid(row = 6, column = 0,sticky="w",padx=2, pady=2, ipadx=2, ipady=2)

        formato = ttk.Combobox(self, state="readonly", values=("Usuario","Administrador","Supervisor","Bloqueado","Vip"), name="txtEstado")
        formato.grid(row = 6 ,column = 1,padx=2, pady=2, ipadx=2, ipady=2,sticky="ew")

        button1 = Button(self, text = "Enviar",command=self.editar_usuarioAdm)
        button1.grid(row = 7, column = 1,sticky="w", pady=2,ipadx=3, ipady=3)

        button2 = Button(self, text = "Cancelar",command = self.destroy)
        button2.grid(row = 7, column = 1,sticky="e", pady=2,ipadx=3, ipady=3)
        
        datosUsuario = consultar_usuario(self.id_usuario)        
        for i in datosUsuario:         
            entry1.insert(0, i[1])
            entry2.insert(0, i[2])
            entry4.insert(0, i[3])
            entry5.insert(0, i[4])
            entry6.insert(0, i[5])
            if i[6] == 0:
                formato.set("Usuario")
            elif i[6] == 1:
                formato.set("Administrador")
            elif i[6] == 2:
                formato.set("Supervisor")
            elif i[6] == 3:
                formato.set("Bloqueado")
            elif i[6] == 4:
                formato.set("Vip")
            else:
                print("Usuario Sin Estado")
        entry1.config(state="readonly")
    
    def editar_usuarioAdm(self):
        try:
            txtUsuario = self.nametowidget("txtUsuario")
            usuario = txtUsuario.get()            

            txtPassword = self.nametowidget("txtPassword")
            password = txtPassword.get()

            txtEmail = self.nametowidget("txtEmail")
            email = txtEmail.get()

            txtNombre = self.nametowidget("txtNombre")
            nombre = txtNombre.get()

            txtApellido = self.nametowidget("txtApellido")
            apellido = txtApellido.get()

            txtEstado = self.nametowidget("txtEstado")
            estado = txtEstado.get()
            
            if estado == "Usuario":
                val_estado = 0
            elif estado == "Administrador":
                val_estado = 1
            elif estado == "Supervisor":
                val_estado = 2
            elif estado == "Bloqueado":
                val_estado = 3
            elif estado == "Vip":
                val_estado = 4

            if usuario != "" and password != "" and email !="" and nombre != "" and apellido !="":                
                if estado == "Usuario":
                    val_estado = 0
                elif estado == "Administrador":
                    val_estado = 1
                elif estado == "Supervisor":
                    val_estado = 2
                elif estado == "Bloqueado":
                    val_estado = 3
                elif estado == "Vip":
                    val_estado = 4
                datosPass = consultar_usuario(self.id_usuario)
                id = datosPass[0][0]
                if password != datosPass[0][2]:
                    password = encriptar_contraseña(password)
                if editarUsuarioAdm(id,usuario,password,email,nombre,apellido,val_estado):
                    tkMsgBox.showwarning(self.master.title(), "Se produjo un error al intentar registrarse")
                else:
                    tkMsgBox.showinfo(self.master.title(), "Registro Modificado!!!!!!")
                    self.destroy()
            else:
                tkMsgBox.showwarning(self.master.title(), "Existen campos sin completar")
        except Exception as ex:
            tkMsgBox.showerror(self.master.title(), str(ex))