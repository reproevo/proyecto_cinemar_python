from tkinter import *
import tkinter.ttk as ttk

class WinSalas(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)        
        self.master = master
        self.title("Menu Salas")
        self.resizable(width=False, height=False)
        
        #Menu
        label1= Label(self,text="Menu de Salas",font="20")
        label1.grid(row=0,column=0)

        frame1= Frame(self)
        frame1.grid(row=1,column=1)

        frame2= Frame(self,width=900,height=400)
        frame2.grid(row=1,column=0)
        #widget frame 1
        button1=Button(frame1,text="AGREGAR")
        button1.pack(padx=5,pady=5,ipadx=5,ipady=5,fill=X)
        button2=Button(frame1,text="EDITAR")
        button2.pack(padx=5,pady=5,ipadx=5,ipady=5,fill=X)
        button3=Button(frame1,text="ELIMINAR")
        button3.pack(padx=5,pady=5,ipadx=5,ipady=5,fill=X)
        #widget frame2
        tv = ttk.Treeview(frame2, columns=("num_sala", "pelicula", "tipo_sala", "hora", "fecha", "cant_butacas"), name="tvSalas")
        tv.column("#0", width=50)
        tv.column("num_sala", width=50, anchor=CENTER)
        tv.column("pelicula", width=250, anchor=CENTER)
        tv.column("tipo_sala", width=50, anchor=CENTER)
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
        tv.place(x=10,y=40,width=870,height=300)

    def obtener_fila(self, event):
        tvSalas = self.nametowidget("tvSalas")
        current_item = tvSalas.focus()
        if current_item:
            data = tvSalas.item(current_item)
            self.select_id = int(data["text"])
        else:
            self.select_id = -1

    # def refrescar(self):        
    #     tvUsuarios = self.nametowidget("tvUsuarios")
    #     for record in tvUsuarios.get_children():
    #         tvUsuarios.delete(record)
    #     usuarios = user.listar()
    #     for usuario in usuarios:
    #         tvUsuarios.insert("", END, text=usuario[0], values=(usuario[6], usuario[1], usuario[2], usuario[5], usuario[8]))