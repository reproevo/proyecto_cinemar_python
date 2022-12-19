from tkinter import *
import tkinter.ttk as ttk
from gui.crudSalas import *
from app import ver_salas

class WinSalas(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)        
        self.master = master
        self.title("Menu Salas")
        #Tamaño de ventana
        self.resizable(width=False, height=False)
        #Cuerpo de la ventana
        label1= Label(self,text="Menu de Salas",font="20")
        label1.pack()
        
        tv = ttk.Treeview(self, columns=("num_sala", "pelicula", "tipo_sala", "hora", "fecha", "cant_butacas"), name="tvSalas")
        tv.column("#0", width=50)
        tv.column("num_sala", width=50, anchor=CENTER)
        tv.column("pelicula", width=250, anchor=CENTER)
        tv.column("tipo_sala", width=80, anchor=CENTER)
        tv.column("hora", width=100, anchor=CENTER)
        tv.column("fecha", width=100, anchor=CENTER)
        tv.column("cant_butacas", width=80, anchor=CENTER)

        tv.heading("#0", text="Id", anchor=CENTER)
        tv.heading("num_sala", text="N° Sala", anchor=CENTER)
        tv.heading("pelicula", text="Pelicula", anchor=CENTER)
        tv.heading("tipo_sala", text="Formato", anchor=CENTER)
        tv.heading("hora", text="Hora", anchor=CENTER)
        tv.heading("fecha", text="Fecha", anchor=CENTER)
        tv.heading("cant_butacas", text="N° Butacas", anchor=CENTER)
        tv.bind("<<TreeviewSelect>>", self.obtener_fila)
        tv.pack(padx=5,pady=5,side=LEFT)

        frame1= Frame(self)
        frame1.pack(side=RIGHT)
        button1=Button(frame1,text="AGREGAR",command= self.abrir_crearSala)
        button1.pack(padx=5,pady=5,ipadx=5,ipady=5,fill=X)
        button2=Button(frame1,text="EDITAR",command=self.abrir_editarSala)
        button2.pack(padx=5,pady=5,ipadx=5,ipady=5,fill=X)
        button3=Button(frame1,text="ELIMINAR",command=self.abrir_eliminarSala)
        button3.pack(padx=5,pady=5,ipadx=5,ipady=5,fill=X)
        button4=Button(frame1,text="ACTUALIZAR",command=self.refrescar)
        button4.pack(padx=5,pady=5,ipadx=5,ipady=5,fill=X)
        
        self.refrescar()
    
    def abrir_crearSala(self):
        WinCrearSalas(self.master)
        

    def abrir_editarSala(self):
        WinEditarSalas(self.master,self.select_id)
        
    def abrir_eliminarSala(self):
        WinEliminarSalas(self.master,self.select_id)

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
            tvSalas.insert("", END, text=i[0], values=(i[1], i[2], i[3], i[4], i[5], i[6]))