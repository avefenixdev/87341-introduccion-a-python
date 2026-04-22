import tkinter as tk

ventana = tk.Tk()

ventana.title("Mi primera App")
ventana.geometry("400x300")

entrada = tk.Entry(ventana)
entrada.pack()

def obtener_texto():
    texto = entrada.get() # obtengo lo ingresado en el input
    print(f"Escribiste: {texto}")

boton = tk.Button(ventana, text="Enviar", command=obtener_texto)
boton.pack()

ventana.mainloop()
