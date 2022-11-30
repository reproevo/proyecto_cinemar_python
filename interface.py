import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("Proyecto Cinemar")
        #setting window size
        width=800
        height=600
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_842=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_842["font"] = ft
        GLabel_842["fg"] = "#333333"
        GLabel_842["justify"] = "center"
        GLabel_842["text"] = "Usuario : "
        GLabel_842.place(x=120,y=60,width=80,height=30)

        GLabel_291=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_291["font"] = ft
        GLabel_291["fg"] = "#333333"
        GLabel_291["justify"] = "center"
        GLabel_291["text"] = "Correo : "
        GLabel_291.place(x=120,y=140,width=80,height=30)

        GLabel_901=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_901["font"] = ft
        GLabel_901["fg"] = "#333333"
        GLabel_901["justify"] = "center"
        GLabel_901["text"] = "Nombres : "
        GLabel_901.place(x=120,y=180,width=80,height=30)

        GLabel_282=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_282["font"] = ft
        GLabel_282["fg"] = "#333333"
        GLabel_282["justify"] = "center"
        GLabel_282["text"] = "Apellidos : "
        GLabel_282.place(x=120,y=220,width=80,height=30)

        GLineEdit_527=tk.Entry(root)
        GLineEdit_527["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_527["font"] = ft
        GLineEdit_527["fg"] = "#333333"
        GLineEdit_527["justify"] = "center"
        GLineEdit_527["text"] = ""
        GLineEdit_527.place(x=200,y=60,width=200,height=30)

        GLineEdit_692=tk.Entry(root)
        GLineEdit_692["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_692["font"] = ft
        GLineEdit_692["fg"] = "#333333"
        GLineEdit_692["justify"] = "center"
        GLineEdit_692["text"] = ""
        GLineEdit_692.place(x=200,y=100,width=200,height=30)

        GLineEdit_951=tk.Entry(root)
        GLineEdit_951["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_951["font"] = ft
        GLineEdit_951["fg"] = "#333333"
        GLineEdit_951["justify"] = "center"
        GLineEdit_951["text"] = ""
        GLineEdit_951.place(x=200,y=140,width=200,height=30)

        GLabel_492=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_492["font"] = ft
        GLabel_492["fg"] = "#333333"
        GLabel_492["justify"] = "center"
        GLabel_492["text"] = "Contraseña : "
        GLabel_492.place(x=120,y=100,width=80,height=30)

        GLineEdit_349=tk.Entry(root)
        GLineEdit_349["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_349["font"] = ft
        GLineEdit_349["fg"] = "#333333"
        GLineEdit_349["justify"] = "center"
        GLineEdit_349["text"] = ""
        GLineEdit_349.place(x=200,y=180,width=200,height=30)

        GLineEdit_645=tk.Entry(root)
        GLineEdit_645["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_645["font"] = ft
        GLineEdit_645["fg"] = "#333333"
        GLineEdit_645["justify"] = "center"
        GLineEdit_645["text"] = ""
        GLineEdit_645.place(x=200,y=220,width=200,height=30)

        GLabel_2=tk.Label(root)
        ft = tkFont.Font(family='Times',size=28)
        GLabel_2["font"] = ft
        GLabel_2["fg"] = "#333333"
        GLabel_2["justify"] = "center"
        GLabel_2["text"] = "REGISTRO"
        GLabel_2["relief"] = "flat"
        GLabel_2.place(x=200,y=10,width=200,height=30)

        GButton_107=tk.Button(root)
        GButton_107["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_107["font"] = ft
        GButton_107["fg"] = "#000000"
        GButton_107["justify"] = "center"
        GButton_107["text"] = "ENVIAR"
        GButton_107.place(x=260,y=260,width=80,height=30)
        GButton_107["command"] = self.GButton_107_command

    def GButton_107_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
