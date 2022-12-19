from tkinter import *
import tkinter.ttk as ttk
from gui.crudSalas import *
from app import ver_descuentos,consultar_descuentos,modificar_descuentos,consultar_diadescuentos

class WinDescuentos(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)        
        self.master = master
        self.title("Menu de Descuentos")
        #self.geometry("900x350")
        self.resizable(width=False, height=False)
        
        #Menu
        label1= Label(self,text="Menu de Descuentos",font="20")
        label1.pack()
        
        tv = ttk.Treeview(self, columns=("dia", "porcent_descuento"), name="tvDescuentos")
        tv.column("#0", width=50)
        tv.column("dia", width=250, anchor=CENTER)
        tv.column("porcent_descuento", width=50, anchor=CENTER)
        
        tv.heading("#0", text="Id", anchor=CENTER)
        tv.heading("dia", text="Día", anchor=CENTER)
        tv.heading("porcent_descuento", text="%", anchor=CENTER)
        
        tv.bind("<<TreeviewSelect>>", self.obtener_fila)
        tv.pack(padx=5,pady=5,side=LEFT)

        frame1= Frame(self)
        frame1.pack(side=RIGHT)
        button2=Button(frame1,text="EDITAR",command=self.abrir_editarDescuento)
        button2.pack(padx=5,pady=5,ipadx=5,ipady=5,fill=X)
        
        button4=Button(frame1,text="ACTUALIZAR",command=self.refrescar)
        button4.pack(padx=5,pady=5,ipadx=5,ipady=5,fill=X)
        
        self.refrescar()

    def abrir_editarDescuento(self):
        WinEditarDescuento(self.master,self.select_id)

    def obtener_fila(self, event):
        tvDescuentos = self.nametowidget("tvDescuentos")
        current_item = tvDescuentos.focus()
        if current_item:
            data = tvDescuentos.item(current_item)
            self.select_id = int(data["text"])
        else:
            self.select_id = -1

    def refrescar(self):        
        tvDescuentos = self.nametowidget("tvDescuentos")
        for record in tvDescuentos.get_children():
            tvDescuentos.delete(record)
        descuentos = ver_descuentos()
        for i in descuentos:
            tvDescuentos.insert("", END, text=i[0], values=(i[1], i[2]))
    
class WinEditarDescuento(tk.Toplevel):
    def __init__(self, master=None,id=None):
        super().__init__(master)
        self.master = master
        self.id_descuento = id
        self.title("Editar Descuento")   
        #Tamaño de ventana
        self.resizable(width=False, height=False)
        self.config(padx=10,pady=10)
        #self.geometry("220x300")
        datosDescuentos = consultar_descuentos(self.id_descuento)
        datosDia = consultar_diadescuentos(self.id_descuento)
        for i in datosDescuentos:
            textlabel1=f"{i[0]}"
        for i in datosDia:
            textlabel2=f"{i[0]}"
        #Cuerpo de la ventana

        label1 = Label(self, text = "Dia : ")
        label1.grid(row = 0 ,column = 0,sticky="ew",padx=2, pady=2, ipadx=2, ipady=2)

        entry0 = Entry(self,width=40)
        entry0.grid(row = 0 ,column = 1,sticky="ew",padx=2, pady=2, ipadx=2, ipady=2)

        entry0.insert(0, textlabel2)
        entry0.config(state="readonly")
        
        label2 = Label(self, text = "Descuento : ")
        label2.grid(row = 1, column = 0,sticky="ew",padx=2, pady=2, ipadx=2, ipady=2)

        entry1 = Entry(self,width=40,name="txtDescuento")
        entry1.grid(row = 1 ,column = 1,padx=2, pady=2, ipadx=2, ipady=2)

        entry1.insert(0,textlabel1)

        button1 = Button(self, text = "Aceptar",command=self.modificar_descuentos)
        button1.grid(row = 2, column = 1,sticky="w", pady=2,ipadx=3, ipady=3)

        button2 = Button(self, text = "Cancelar",command = self.destroy)
        button2.grid(row = 2, column = 1,sticky="e", pady=2,ipadx=3, ipady=3)

    def modificar_descuentos(self):
        try:
            id_Descuento= self.id_descuento

            txtDescuento = self.nametowidget("txtDescuento")
            descuento = txtDescuento.get()            

            if descuento != "":
                if modificar_descuentos(id_Descuento,descuento):
                    tkMsgBox.showwarning(self.master.title(), "Se produjo un error al modificar el descuento")
                else:
                    tkMsgBox.showinfo(self.master.title(), "Descuento Modificado Exitosamente!!!!!!")
                    self.destroy()
            else:
                tkMsgBox.showwarning(self.master.title(), "Existen campos sin completar")
        except Exception as ex:
            tkMsgBox.showerror(self.master.title(), str(ex))