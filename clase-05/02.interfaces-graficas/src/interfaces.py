import tkinter as tk

class mi_aplicacion:
    def __init__(self, ventana):
        """ Configurar la interfaz """
        self.ventana = ventana
        self.ventana.title("Mi primera aplicación")
        self.ventana.geometry("800x600")

    def iniciar(self):
        """ Mostrar la ventana """
        self.ventana.mainloop()

# Crear ventana principal
ventana = tk.Tk()

# Creamos la aplicación
app = mi_aplicacion(ventana)

# Mostrar
app.iniciar()
