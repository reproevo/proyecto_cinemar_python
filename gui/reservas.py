from tkinter import *
import tkinter.ttk as ttk
import tkinter as tk
import tkinter.messagebox as tkMsgBox
from app import ver_reservas,ver_reservasParticular

class WinReservas(Toplevel):
    def __init__(self, master=None,id=None):
        super().__init__(master)        
        self.master = master
        self.id = id
        self.title("Reservas")
        self.resizable(width=False, height=True)
        
        #Cuerpo de Ventana
        label1= Label(self,text=f"Lista de Reservas ",font="20")
        label1.pack()

        tv = ttk.Treeview(self, columns=("id_usuario", "num_sala","pelicula","formato","hora","fecha","butaca"), name="tvReservas")
        tv.column("#0", width=50)
        tv.column("id_usuario", width=100, anchor=CENTER)
        tv.column("num_sala", width=100, anchor=CENTER)
        tv.column("pelicula", width=250, anchor=CENTER)
        tv.column("formato", width=50, anchor=CENTER)
        tv.column("hora", width=100, anchor=CENTER)
        tv.column("fecha", width=100, anchor=CENTER)
        tv.column("butaca", width=50, anchor=CENTER)
        
        tv.heading("#0", text="Id", anchor=CENTER)
        tv.heading("id_usuario", text="Usuario", anchor=CENTER)
        tv.heading("num_sala", text="N° de Sala", anchor=CENTER)
        tv.heading("pelicula", text="Pelicula", anchor=CENTER)
        tv.heading("formato", text="Formato", anchor=CENTER)
        tv.heading("hora", text="Hora", anchor=CENTER)
        tv.heading("fecha", text="Fecha", anchor=CENTER)
        tv.heading("butaca", text="IdSala", anchor=CENTER)
        
        tv.bind("<<TreeviewSelect>>", self.obtener_fila)
        tv.pack(padx=5,pady=5,side=LEFT,fill=Y)

        frame1= Frame(self)
        frame1.pack(side=RIGHT)

        button4=Button(frame1,text="ACTUALIZAR",command=self.refrescar)
        button4.pack(padx=5,pady=5,ipadx=5,ipady=5,fill=X)
        
        self.refrescar()

    def obtener_fila(self, event):
        tvReservas = self.nametowidget("tvReservas")
        current_item = tvReservas.focus()
        if current_item:
            data = tvReservas.item(current_item)
            self.select_id = int(data["text"])
        else:
            self.select_id = -1

    def refrescar(self):        
        tvReservas = self.nametowidget("tvReservas")
        for record in tvReservas.get_children():
            tvReservas.delete(record)
        reservas = ver_reservas()
        for i in reservas:
            tvReservas.insert("", END, text=i[0], values=(i[1], i[2], i[3], i[4], i[5], i[6], i[7]))

class PreguntaID(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)        
        self.master = master
        self.resizable(width=False, height=True)
        self.config(padx=5,pady=5)
        label1= Label(self,text="Ingrese ID del Usuario",font="20")
        label1.grid(row = 0,column = 0,padx=2, pady=2, ipadx=2, ipady=2)

        entry6 = Entry(self,width=40,name="txtIdBuscar")
        entry6.grid(row = 1 ,column = 0,padx=2, pady=2, ipadx=2, ipady=2)

        button1 = Button(self, text = "BUSCAR",command= self.abrir_winReservasParticular)
        button1.grid(row = 3, column = 0,sticky="ew", padx=10,pady=2,ipadx=3, ipady=3)

    def abrir_winReservasParticular(self):
        txtIdBuscar = self.nametowidget("txtIdBuscar")
        idBuscar = txtIdBuscar.get() 
        WinReservasParticular(self.master,idBuscar)

class WinReservasParticular(Toplevel):
    def __init__(self, master=None,id=None):
        super().__init__(master)        
        self.master = master
        self.id = id
        self.title(f"Reservas de ID :{self.id}")
        self.resizable(width=False, height=True)
        
        #Menu
        label1= Label(self,text="Reservas Particulares",font="20")
        label1.pack()

        tv = ttk.Treeview(self, columns=("id_usuario", "num_sala","pelicula","formato","hora","fecha","butaca"), name="tvReservas")
        tv.column("#0", width=50)
        tv.column("id_usuario", width=100, anchor=CENTER)
        tv.column("num_sala", width=100, anchor=CENTER)
        tv.column("pelicula", width=250, anchor=CENTER)
        tv.column("formato", width=50, anchor=CENTER)
        tv.column("hora", width=100, anchor=CENTER)
        tv.column("fecha", width=100, anchor=CENTER)
        tv.column("butaca", width=50, anchor=CENTER)
        
        tv.heading("#0", text="Id", anchor=CENTER)
        tv.heading("id_usuario", text="Usuario", anchor=CENTER)
        tv.heading("num_sala", text="N° de Sala", anchor=CENTER)
        tv.heading("pelicula", text="Pelicula", anchor=CENTER)
        tv.heading("formato", text="Formato", anchor=CENTER)
        tv.heading("hora", text="Hora", anchor=CENTER)
        tv.heading("fecha", text="Fecha", anchor=CENTER)
        tv.heading("butaca", text="IdSala", anchor=CENTER)
        
        tv.bind("<<TreeviewSelect>>", self.obtener_fila)
        tv.pack(padx=5,pady=5,side=LEFT,fill=Y)

        frame1= Frame(self)
        frame1.pack(side=RIGHT)

        button4=Button(frame1,text="ACTUALIZAR",command=self.refrescar)
        button4.pack(padx=5,pady=5,ipadx=5,ipady=5,fill=X)
        
        self.refrescar()

    def obtener_fila(self, event):
        tvReservas = self.nametowidget("tvReservas")
        current_item = tvReservas.focus()
        if current_item:
            data = tvReservas.item(current_item)
            self.select_id = int(data["text"])
        else:
            self.select_id = -1

    def refrescar(self):        
        tvReservas = self.nametowidget("tvReservas")
        for record in tvReservas.get_children():
            tvReservas.delete(record)
        reservas = ver_reservasParticular(self.id)
        for i in reservas:
            tvReservas.insert("", END, text=i[0], values=(i[1], i[2], i[3], i[4], i[5], i[6], i[7]))