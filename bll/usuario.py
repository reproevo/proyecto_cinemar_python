from tkinter import *

class WinUsuario:
    def __init__(self, ventana):
        #Titulo de ventana
        ventana.title("Cinemar")
        #Icono de la ventana
        ventana.iconbitmap(default="cinemark.ico")
        #Fondo de la ventana
        ventana.config(bg = "black")
        #Tamaño de ventana
        ventana.geometry("400x300")
        ventana.resizable(width=False, height=False)
        #Cuerpo de la ventana
        button1 = Button(ventana, text="Cinemar")
        button1.place(x=100,y=110,width=200,height= 80)

ventana = Tk()
app = WinUsuario(ventana)
ventana.mainloop()