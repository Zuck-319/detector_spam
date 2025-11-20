import tkinter as tk
from tkinter import messagebox 

def mostrarmensaje():
    messagebox.showinfo("Aviso", "Boton presionado")

ventana = tk.Tk()
ventana.title("Página Principal")

label = tk.Label(ventana, text="Presiona el botón para ver el mensaje")
label.pack(pady=10)

boton = tk.Button(ventana, text="Da clic", command=mostrarmensaje)
boton.pack(pady=10)

ventana.mainloop()
