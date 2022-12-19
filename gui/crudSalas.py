import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from app import crear_sala
from app import consultar_sala
from app import modificar_sala
from app import eliminar_sala
import tkinter.messagebox as tkMsgBox
#from gui.salas import WinSalas

class WinCrearSalas(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.title("Crear Sala")   
        #Tamaño de ventana
        self.resizable(width=False, height=False)
        self.config(padx=10,pady=10)

        #Cuerpo de la ventana
        label1 = Label(self, text = "N° de Sala :")
        label1.grid(row = 0 ,column = 0,sticky="w",padx=2, pady=2, ipadx=2, ipady=2)
        
        entry1 = Entry(self,width=40,name="txtSala")
        entry1.grid(row = 0 ,column = 1,padx=2, pady=2, ipadx=2, ipady=2)

        label2 = Label(self, text="Pelicula :")
        label2.grid(row = 1, column = 0,sticky="w",padx=2, pady=2, ipadx=2, ipady=2)

        entry2 = Entry(self,width=40,name="txtPelicula")
        entry2.grid(row = 1 ,column = 1,padx=2, pady=2, ipadx=2, ipady=2)

        label3 = Label(self, text="Formato :")  
        label3.grid(row = 2, column = 0,sticky="w",padx=2, pady=2, ipadx=2, ipady=2)
        
        formato = ttk.Combobox(self, state="readonly", values=("2D","3D"), name="txtFormato")
        formato.grid(row = 2 ,column = 1,padx=2, pady=2, ipadx=2, ipady=2,sticky="ew")

        label4 = Label(self,text="Hora :")
        label4.grid(row = 3, column = 0,sticky="w",padx=2, pady=2, ipadx=2, ipady=2)

        entry4 = Entry(self,width=40,name="txtHora")
        entry4.grid(row = 3 ,column = 1,padx=2, pady=2, ipadx=2, ipady=2)

        label5 = Label(self,text="Fecha :")
        label5.grid(row = 4, column = 0,sticky="w",padx=2, pady=2, ipadx=2, ipady=2)
        
        entry5 = Entry(self,width=40,name="txtFecha")
        entry5.grid(row = 4 ,column = 1,padx=2, pady=2, ipadx=2, ipady=2)

        label6 = Label(self,text="N° de Butacas :")
        label6.grid(row = 5, column = 0,sticky="w",padx=2, pady=2, ipadx=2, ipady=2)

        entry6 = Entry(self,width=40,name="txtButacas")
        entry6.grid(row = 5 ,column = 1,padx=2, pady=2, ipadx=2, ipady=2)

        button1 = Button(self, text = "Enviar",command=self.crear_sala)
        button1.grid(row = 6, column = 1,sticky="w", pady=2,ipadx=3, ipady=3)

        button2 = Button(self, text = "Cancelar",command = self.destroy)
        button2.grid(row = 6, column = 1,sticky="e", pady=2,ipadx=3, ipady=3)

    def crear_sala(self):
        try:
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

            txtButacas = self.nametowidget("txtButacas")
            butacas = int(txtButacas.get())

            if sala != "" and pelicula != "" and formato !="" and hora !="" and fecha != "" and butacas !="":
                if crear_sala(sala,pelicula,formato,hora,fecha,butacas):
                    tkMsgBox.showwarning(self.master.title(), "Se produjo un error al crear la sala")
                else:
                    tkMsgBox.showinfo(self.master.title(), "Sala Creada!!!!!!")
                    self.destroy()
            else:
                tkMsgBox.showwarning(self.master.title(), "Existen campos sin completar")
        except Exception as ex:
            tkMsgBox.showerror(self.master.title(), str(ex))

class WinEditarSalas(tk.Toplevel):
    def __init__(self, master=None,id=None):
        super().__init__(master)
        self.master = master
        self.id_sala = id
        self.title("Editar Sala")   
        #Tamaño de ventana
        self.resizable(width=False, height=False)
        self.config(padx=10,pady=10)

        #Cuerpo de la ventana
        label1 = Label(self, text = "N° de Sala :")
        label1.grid(row = 0 ,column = 0,sticky="w",padx=2, pady=2, ipadx=2, ipady=2)
        
        entry1 = Entry(self,width=40,name="txtSala")
        entry1.grid(row = 0 ,column = 1,padx=2, pady=2, ipadx=2, ipady=2)

        label2 = Label(self, text="Pelicula :")
        label2.grid(row = 1, column = 0,sticky="w",padx=2, pady=2, ipadx=2, ipady=2)

        entry2 = Entry(self,width=40,name="txtPelicula")
        entry2.grid(row = 1 ,column = 1,padx=2, pady=2, ipadx=2, ipady=2)

        label3 = Label(self, text="Formato :")  
        label3.grid(row = 2, column = 0,sticky="w",padx=2, pady=2, ipadx=2, ipady=2)
        
        formato = ttk.Combobox(self, state="readonly", values=("2D","3D"), name="txtFormato")
        formato.grid(row = 2 ,column = 1,padx=2, pady=2, ipadx=2, ipady=2,sticky="ew")

        label4 = Label(self,text="Hora :")
        label4.grid(row = 3, column = 0,sticky="w",padx=2, pady=2, ipadx=2, ipady=2)

        entry4 = Entry(self,width=40,name="txtHora")
        entry4.grid(row = 3 ,column = 1,padx=2, pady=2, ipadx=2, ipady=2)

        label5 = Label(self,text="Fecha :")
        label5.grid(row = 4, column = 0,sticky="w",padx=2, pady=2, ipadx=2, ipady=2)
        
        entry5 = Entry(self,width=40,name="txtFecha")
        entry5.grid(row = 4 ,column = 1,padx=2, pady=2, ipadx=2, ipady=2)

        label6 = Label(self,text="N° de Butacas :")
        label6.grid(row = 5, column = 0,sticky="w",padx=2, pady=2, ipadx=2, ipady=2)

        entry6 = Entry(self,width=40,name="txtButacas")
        entry6.grid(row = 5 ,column = 1,padx=2, pady=2, ipadx=2, ipady=2)

        button1 = Button(self, text = "Enviar",command=self.editar_sala)
        button1.grid(row = 6, column = 1,sticky="w", pady=2,ipadx=3, ipady=3)

        button2 = Button(self, text = "Cancelar",command = self.destroy)
        button2.grid(row = 6, column = 1,sticky="e", pady=2,ipadx=3, ipady=3)

        datosSala = consultar_sala(self.id_sala)
        for i in datosSala:            
            entry1.insert(0, i[1])
            entry2.insert(0, i[2])
            formato.set(i[3])
            entry4.insert(0, i[4])
            entry5.insert(0, i[5])
            entry6.insert(0, i[6])

    def editar_sala(self):
        try:
            id_sala= self.id_sala

            txtSala = self.nametowidget("txtSala")
            sala = txtSala.get()            

            txtPelicula = self.nametowidget("txtPelicula")
            pelicula = txtPelicula.get()

            txtFormato = self.nametowidget("txtFormato")
            formato = txtFormato.get()

            txtHora = self.nametowidget("txtHora")
            hora = txtHora.get()

            txtFecha = self.nametowidget("txtFecha")
            fecha = txtFecha.get()

            txtButacas = self.nametowidget("txtButacas")
            butacas = txtButacas.get()

            if sala != "" and pelicula != "" and formato !="" and hora !="" and fecha != "" and butacas !="":
                if modificar_sala(id_sala,sala,pelicula,formato,hora,fecha,butacas):
                    tkMsgBox.showwarning(self.master.title(), "Se produjo un error al modificar la sala")
                else:
                    tkMsgBox.showinfo(self.master.title(), "Sala Modificada Exitosamente!!!!!!")
                    self.destroy()
            else:
                tkMsgBox.showwarning(self.master.title(), "Existen campos sin completar")
        except Exception as ex:
            tkMsgBox.showerror(self.master.title(), str(ex))

class WinEliminarSalas(tk.Toplevel):
    def __init__(self, master=None,id=None):
        super().__init__(master)
        self.master = master
        self.id_sala = id
        self.title("Eliminar Salas")   
        #Tamaño de ventana
        self.resizable(width=False, height=False)
        self.config(padx=10,pady=10)
        #self.geometry("220x300")

        datosSala = consultar_sala(self.id_sala)
        # print(self.id_sala)
        # print(datosSala)
        for i in datosSala:
            textlabel0=f"N° de ID : {i[0]}"            
            textlabel1=f"N° de Sala : {i[1]}"
            textlabel2=f"Pelicula : {i[2]}"
            textlabel3=f"Formato : {i[3]}"
            textlabel4=f"Hora : {i[4]}"
            textlabel5=f"Fecha : {i[5]}"
            textlabel6=f"N° de Butacas : {i[6]}"

        #Cuerpo de la ventana
        labelPreg = Label(self,text="¿Desea Eliminar la Sala?" ,font=20)
        labelPreg.grid(row = 0 ,column = 0,sticky="ew",padx=2, pady=2, ipadx=2, ipady=2)

        label0 = Label(self,text=textlabel0)
        label0.grid(row = 1 ,column = 0,sticky="ew",padx=2, pady=2, ipadx=2, ipady=2)

        label1 = Label(self, text = textlabel1)
        label1.grid(row = 2 ,column = 0,sticky="ew",padx=2, pady=2, ipadx=2, ipady=2)
        
        label2 = Label(self, text=textlabel2)
        label2.grid(row = 3, column = 0,sticky="ew",padx=2, pady=2, ipadx=2, ipady=2)

        label3 = Label(self, text=textlabel3)  
        label3.grid(row = 4, column = 0,sticky="ew",padx=2, pady=2, ipadx=2, ipady=2)

        label4 = Label(self,text=textlabel4)
        label4.grid(row = 5, column = 0,sticky="ew",padx=2, pady=2, ipadx=2, ipady=2)

        label5 = Label(self,text=textlabel5)
        label5.grid(row = 6, column = 0,sticky="ew",padx=2, pady=2, ipadx=2, ipady=2)

        label6 = Label(self,text=textlabel6)
        label6.grid(row = 7, column = 0,sticky="ew",padx=2, pady=2, ipadx=2, ipady=2)

        label7 = Label(self,text="")
        label7.grid(row = 8, column = 0,sticky="ew",padx=2, pady=2, ipadx=2, ipady=2)

        button1 = Button(self, text = "Aceptar",command=self.eliminar_sala)
        button1.grid(row = 9, column = 0,sticky="w", pady=2,ipadx=3, ipady=3)

        button2 = Button(self, text = "Cancelar",command = self.destroy)
        button2.grid(row = 9, column = 0,sticky="e", pady=2,ipadx=3, ipady=3)

    def eliminar_sala(self):
        eliminar_sala(self.id_sala)
