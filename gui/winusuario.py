from tkinter import *
import tkinter.ttk as ttk
import tkinter as tk
import tkinter.messagebox as tkMsgBox
from app import ver_reservas,ver_salas,consultar_sala,consultarDescuentoVip,calcularPrecio,consultar_usuario,crear_reserva,precios
from app import disponibilidadSala,mis_reservas,eliminar_reserva,mi_historial

class WinReservas(Toplevel):
    def __init__(self, master=None,id=None):
        super().__init__(master)
        self.master = master
        self.id_usuario = id
        self.title("Menu Usuario")
        #self.geometry("900x350")
        self.resizable(width=False, height=True)
        
        #Menu
        label1= Label(self,text="Ver Salas",font="20")
        label1.pack()
        
        tv = ttk.Treeview(self, columns=("num_sala", "pelicula", "tipo_sala", "hora", "fecha"), name="tvSalas")
        tv.column("#0", width=50)
        tv.column("num_sala", width=50, anchor=CENTER)
        tv.column("pelicula", width=250, anchor=CENTER)
        tv.column("tipo_sala", width=80, anchor=CENTER)
        tv.column("hora", width=100, anchor=CENTER)
        tv.column("fecha", width=100, anchor=CENTER)

        tv.heading("#0", text="Indice", anchor=CENTER)
        tv.heading("num_sala", text="N° Sala", anchor=CENTER)
        tv.heading("pelicula", text="Pelicula", anchor=CENTER)
        tv.heading("tipo_sala", text="Formato", anchor=CENTER)
        tv.heading("hora", text="Hora", anchor=CENTER)
        tv.heading("fecha", text="Fecha", anchor=CENTER)
        tv.bind("<<TreeviewSelect>>", self.obtener_fila)
        tv.pack(padx=5,pady=5,side=LEFT,fill=Y)

        frame1= Frame(self)
        frame1.pack(side=RIGHT)
        button1=Button(frame1,text="RESERVAR",command=self.abrir_crearReserva)
        button1.pack(padx=5,pady=5,ipadx=5,ipady=5,fill=X)
        button4=Button(frame1,text="ACTUALIZAR",command=self.refrescar)
        button4.pack(padx=5,pady=5,ipadx=5,ipady=5,fill=X)
        
        self.refrescar()
    def abrir_crearReserva(self):
        WinCrearReserva(self.master,self.id_usuario,self.select_id)
    def obtener_fila(self, event):
        tvSalas = self.nametowidget("tvSalas")
        current_item = tvSalas.focus()
        if current_item:
            data = tvSalas.item(current_item)
            self.select_id = int(data["text"])
        else:
            self.select_id = -1

    def refrescar(self):        
        tvSalas = self.nametowidget("tvSalas")
        for record in tvSalas.get_children():
            tvSalas.delete(record)
        salas = ver_salas()
        for i in salas:
            tvSalas.insert("", END, text=i[0], values=(i[1], i[2], i[3], i[4], i[5]))

class WinCrearReserva(tk.Toplevel):
    def __init__(self, master=None,id=None,sala=None):
        super().__init__(master)
        self.master = master
        self.id_usuario = id
        #self.usuario = consultar_usuario(id)[0][1]
        self.id_sala = sala
        self.title("Solicitar Reserva")   
        #Tamaño de ventana
        self.resizable(width=False, height=False)
        self.config(padx=10,pady=10)
        #self.geometry("220x300")
        #Cuerpo de la ventana
        labelPreg = Label(self,text="Reserva" ,font=20)
        labelPreg.grid(row = 0 ,column = 0,sticky="ew",padx=2, pady=2, ipadx=2, ipady=2)

        label1 = Label(self, text = "N° de Sala : ")
        label1.grid(row = 1 ,column = 0,sticky="ew",padx=2, pady=2, ipadx=2, ipady=2)

        entry1 = Entry(self,width=40,name="txtSala")
        entry1.grid(row = 1 ,column = 1,padx=2, pady=2, ipadx=2, ipady=2)
        
        label2 = Label(self, text="Pelicula : ")
        label2.grid(row = 2, column = 0,sticky="ew",padx=2, pady=2, ipadx=2, ipady=2)

        entry2 = Entry(self,width=40,name="txtPelicula")
        entry2.grid(row = 2 ,column = 1,padx=2, pady=2, ipadx=2, ipady=2)

        label3 = Label(self, text="Formato : ")  
        label3.grid(row = 3, column = 0,sticky="ew",padx=2, pady=2, ipadx=2, ipady=2)

        entry3 = Entry(self,width=40,name="txtFormato")
        entry3.grid(row = 3 ,column = 1,padx=2, pady=2, ipadx=2, ipady=2)

        label4 = Label(self,text="Hora : ")
        label4.grid(row = 4, column = 0,sticky="ew",padx=2, pady=2, ipadx=2, ipady=2)

        entry4 = Entry(self,width=40,name="txtHora")
        entry4.grid(row = 4 ,column = 1,padx=2, pady=2, ipadx=2, ipady=2)

        label5 = Label(self,text="Fecha : ")
        label5.grid(row = 5, column = 0,sticky="ew",padx=2, pady=2, ipadx=2, ipady=2)

        entry5 = Entry(self,width=40,name="txtFecha")
        entry5.grid(row = 5 ,column = 1,padx=2, pady=2, ipadx=2, ipady=2)

        label6 = Label(self,text="Entradas")
        label6.grid(row = 6, column = 0,sticky="ew",padx=2, pady=2, ipadx=2, ipady=2)

        entry6 = Entry(self,width=40,name="txtEntradas")
        entry6.grid(row = 6 ,column = 1,padx=2, pady=2, ipadx=2, ipady=2)

        label7 = Label(self,text="Descuento")
        label7.grid(row = 7, column = 0,sticky="ew",padx=2, pady=2, ipadx=2, ipady=2)

        entry7 = Entry(self,width=40,name="txtDescuento")
        entry7.grid(row = 7 ,column = 1,padx=2, pady=2, ipadx=2, ipady=2)

        label8 = Label(self,text="Precio : ")
        label8.grid(row = 8, column = 0,sticky="ew",padx=2, pady=2, ipadx=2, ipady=2)

        entry8 = Entry(self,width=40,name="txtPrecio")
        entry8.grid(row = 8 ,column = 1,padx=2, pady=2, ipadx=2, ipady=2)

        labelEspacio = Label(self,text="")
        labelEspacio.grid(row = 9, column = 0,sticky="ew",padx=2, pady=4, ipadx=2, ipady=2)

        label9 = Label(self,text="Total a Pagar")
        label9.grid(row = 10, column = 0,sticky="ew",padx=2, pady=2, ipadx=2, ipady=2)

        entry9 = Entry(self,width=40,name="txtTotal")
        entry9.grid(row = 10 ,column = 1,padx=2, pady=2, ipadx=2, ipady=2)

        button1 = Button(self, text = "Aceptar",command=self.crear_reserva)
        button1.grid(row = 11, column = 1,sticky="w", pady=2,ipadx=3, ipady=3)

        button2 = Button(self, text = "Cancelar",command = self.destroy)
        button2.grid(row = 11, column = 1,sticky="e", pady=2,ipadx=3, ipady=3)

        datosSala = consultar_sala(self.id_sala)
        datosDescuento = (consultarDescuentoVip(self.id_usuario))
        pagar = calcularPrecio(datosSala[0][3],datosDescuento)
        precioEntrada = precios(datosSala[0][3])
        for i in datosSala:          
            entry1.insert(0, i[1])
            entry2.insert(0, i[2])
            entry3.insert(0, i[3])
            entry4.insert(0, i[4])
            entry5.insert(0, i[5])
            entry6.insert(0, "1")
            entry1.config(state="readonly")
            entry2.config(state="readonly")
            entry3.config(state="readonly")
            entry4.config(state="readonly")
            entry5.config(state="readonly")
            entry6.config(state="readonly")
            entry7.insert(0, f"{str(datosDescuento)} %")            
            entry7.config(state="readonly")
            entry8.insert(0, f"{str(precioEntrada[0][2])}")            
            entry8.config(state="readonly")
            entry9.insert(0, str(pagar))
            entry9.config(state="readonly")

    def crear_reserva(self):
        try:
            usuario = consultar_usuario(self.id_usuario)[0][1]

            txtSala = self.nametowidget("txtSala")
            sala = int(txtSala.get())

            txtPelicula = self.nametowidget("txtPelicula")
            pelicula = txtPelicula.get()

            txtFormato = self.nametowidget("txtFormato")
            formato = txtFormato.get()

            txtHora = self.nametowidget("txtHora")
            hora = txtHora.get()

            txtFecha = self.nametowidget("txtFecha")
            fecha = txtFecha.get()

            idSala = self.id_sala
            if usuario != "" and sala != "" and pelicula != "" and formato !="" and hora !="" and fecha != "" and idSala !="":
                if disponibilidadSala(idSala)  == True:
                    if crear_reserva(usuario,sala,pelicula,formato,hora,fecha,idSala):
                        tkMsgBox.showwarning(self.master.title(), "Se produjo un error al realizar la reserva")
                    else:
                        tkMsgBox.showinfo(self.master.title(), "Reserva Exitosa!!!!!!")
                        self.destroy()
                else:
                    tkMsgBox.showinfo(self.master.title(), "¡No hay entradas disponibles!")
            else:
                tkMsgBox.showwarning(self.master.title(), "Existen campos sin completar")
        except Exception as ex:
            tkMsgBox.showerror(self.master.title(), str(ex))
#------------------------------------------------------------------------------
class WinMisReservas(tk.Toplevel):
    def __init__(self, master=None,id=None):
        super().__init__(master)
        self.master = master
        self.id_usuario = id
        self.usuario = consultar_usuario(id)[0][1]
        self.title("Mis Reservas")
        #self.geometry("900x350")
        self.resizable(width=False, height=True)
        
        #Menu
        label1= Label(self,text="MIS RESERVAS",font="20")
        label1.pack()
        
        tv = ttk.Treeview(self, columns=("usuario","num_sala", "pelicula", "tipo_sala", "hora", "fecha","id_sala"), name="tvMisReservas")
        tv.column("#0", width=50)
        tv.column("usuario", width=50, anchor=CENTER)
        tv.column("num_sala", width=50, anchor=CENTER)
        tv.column("pelicula", width=250, anchor=CENTER)
        tv.column("tipo_sala", width=80, anchor=CENTER)
        tv.column("hora", width=100, anchor=CENTER)
        tv.column("fecha", width=100, anchor=CENTER)
        tv.column("id_sala", width=100, anchor=CENTER)

        tv.heading("#0", text="ID Reserva", anchor=CENTER)
        tv.heading("usuario", text="Usuario", anchor=CENTER)
        tv.heading("num_sala", text="N° Sala", anchor=CENTER)
        tv.heading("pelicula", text="Pelicula", anchor=CENTER)
        tv.heading("tipo_sala", text="Formato", anchor=CENTER)
        tv.heading("hora", text="Hora", anchor=CENTER)
        tv.heading("fecha", text="Fecha", anchor=CENTER)
        tv.heading("id_sala", text="ID Sala", anchor=CENTER)
        tv.bind("<<TreeviewSelect>>", self.obtener_fila)
        tv.pack(padx=5,pady=5,side=LEFT,fill=Y)

        frame1= Frame(self)
        frame1.pack(side=RIGHT)
        button1=Button(frame1,text="CANCELAR RESERVA",command=self.abrir_cancelarReserva)
        button1.pack(padx=5,pady=5,ipadx=5,ipady=5,fill=X)
        button4=Button(frame1,text="ACTUALIZAR",command=self.refrescar)
        button4.pack(padx=5,pady=5,ipadx=5,ipady=5,fill=X)
        
        self.refrescar()
    def abrir_cancelarReserva(self):
        WinCancelarReserva(self.master,self.id_usuario,self.select_id)

    def obtener_fila(self, event):
        tvMisReservas = self.nametowidget("tvMisReservas")
        current_item = tvMisReservas.focus()
        if current_item:
            data = tvMisReservas.item(current_item)
            self.select_id = int(data["text"])
        else:
            self.select_id = -1

    def refrescar(self):        
        tvMisReservas = self.nametowidget("tvMisReservas")
        for record in tvMisReservas.get_children():
            tvMisReservas.delete(record)
        datosreservas = mis_reservas(self.usuario)
        print(self.usuario)
        print(datosreservas)
        for i in datosreservas:
            tvMisReservas.insert("", END, text=i[0], values=(i[1],i[2], i[3], i[4], i[5], i[6],i[7]))
#-----------------------------------------------------------------
class WinCancelarReserva(tk.Toplevel):
    def __init__(self, master=None,id=None,sala=None):
        super().__init__(master)
        self.master = master
        self.id_usuario = id
        #self.usuario = consultar_usuario(id)[0][1]
        self.id_sala = sala
        self.title("Cancelar Reserva")   
        #Tamaño de ventana
        self.resizable(width=False, height=False)
        self.config(padx=10,pady=10)
        #self.geometry("220x300")
        #Cuerpo de la ventana
        labelPreg = Label(self,text="¿Desea Cancelar la Reserva?" ,font=10)
        labelPreg.grid(row = 0 ,column = 0,sticky="ew",padx=2, pady=2, ipadx=2, ipady=2)

        label1 = Label(self, text = "ID de Reserva")
        label1.grid(row = 1 ,column = 0,sticky="ew",padx=2, pady=2, ipadx=2, ipady=2)

        entry1 = Entry(self,width=40,name="txtID")
        entry1.grid(row = 2 ,column = 0,padx=2, pady=2, ipadx=2, ipady=2)
        
        button1 = Button(self, text = "Aceptar",command=self.cancelar_reserva)
        button1.grid(row = 3, column = 0,sticky="w", pady=2,ipadx=3, ipady=3)

        button2 = Button(self, text = "Cancelar",command = self.destroy)
        button2.grid(row = 3, column = 0,sticky="e", pady=2,ipadx=3, ipady=3)
         
        entry1.insert(0, self.id_sala)
        entry1.config(state="readonly")

        # print(consultar_usuario(self.id_usuario)[0][1])
        # print(self.id_sala)

    def cancelar_reserva(self):
        try:
            usuario = consultar_usuario(self.id_usuario)[0][1]
            id = self.id_sala

            if usuario != "" and id != "":
                if eliminar_reserva(usuario,id):
                    tkMsgBox.showwarning(self.master.title(), "Se produjo un error al realizar la reserva")
                else:
                    tkMsgBox.showinfo(self.master.title(), "Reserva Cancelada!!!!!!")
                    self.destroy()
            else:
                tkMsgBox.showwarning(self.master.title(), "Existen campos sin completar")
        except Exception as ex:
            tkMsgBox.showerror(self.master.title(), str(ex))
#-----------------------------------------------------------
class WinHistorialReservas(tk.Toplevel):
    def __init__(self, master=None,id=None):
        super().__init__(master)
        self.master = master
        self.id_usuario = id
        self.usuario = consultar_usuario(id)[0][1]

        self.title("Historial")
        self.resizable(width=False, height=True)
        
        #Menu
        label1= Label(self,text="Historial",font="20")
        label1.pack()
        
        tv = ttk.Treeview(self, columns=("usuario","num_sala", "pelicula", "tipo_sala", "hora", "fecha","id_sala"), name="tvHistorial")
        tv.column("#0", width=50)
        tv.column("usuario", width=50, anchor=CENTER)
        tv.column("num_sala", width=50, anchor=CENTER)
        tv.column("pelicula", width=250, anchor=CENTER)
        tv.column("tipo_sala", width=80, anchor=CENTER)
        tv.column("hora", width=100, anchor=CENTER)
        tv.column("fecha", width=100, anchor=CENTER)
        tv.column("id_sala", width=100, anchor=CENTER)

        tv.heading("#0", text="ID Reserva", anchor=CENTER)
        tv.heading("usuario", text="Usuario", anchor=CENTER)
        tv.heading("num_sala", text="N° Sala", anchor=CENTER)
        tv.heading("pelicula", text="Pelicula", anchor=CENTER)
        tv.heading("tipo_sala", text="Formato", anchor=CENTER)
        tv.heading("hora", text="Hora", anchor=CENTER)
        tv.heading("fecha", text="Fecha", anchor=CENTER)
        tv.heading("id_sala", text="ID Sala", anchor=CENTER)
        tv.bind("<<TreeviewSelect>>", self.obtener_fila)
        tv.pack(padx=5,pady=5,side=LEFT,fill=Y)

        frame1= Frame(self)
        frame1.pack(side=RIGHT)
        button4=Button(frame1,text="ACTUALIZAR",command=self.refrescar)
        button4.pack(padx=5,pady=5,ipadx=5,ipady=5,fill=X)
        
        self.refrescar()

    def obtener_fila(self, event):
        tvHistorial = self.nametowidget("tvHistorial")
        current_item = tvHistorial.focus()
        if current_item:
            data = tvHistorial.item(current_item)
            self.select_id = int(data["text"])
        else:
            self.select_id = -1

    def refrescar(self):        
        tvHistorial = self.nametowidget("tvHistorial")
        for record in tvHistorial.get_children():
            tvHistorial.delete(record)
        datosreservas = mi_historial(self.usuario)

        for i in datosreservas:
            tvHistorial.insert("", END, text=i[0], values=(i[1],i[2], i[3], i[4], i[5], i[6],i[7]))