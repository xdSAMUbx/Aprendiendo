import tkinter as tk
from tkinter import ttk

def button_function():
    print("El boton fue presionado")

# Creando la ventana
window = tk.Tk()
window.title('Prueba 2')
window.geometry('800x700')

#tk text
text = tk.Text(master=window) #crea un cuadro de texto en la ventana, el pack es como el div, en el medio arriba
text.pack()

#ttk label
label = ttk.Label(master=window, text='Este es un test')
label.pack()

#ttk entry
entry = ttk.Entry(master=window)
entry.pack()

#ttk button
button = ttk.Button(master=window, text='Prueba', command=button_function)
button.pack()

#Corriendo el programa
window.mainloop()