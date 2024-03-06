#Entrenamiento Tkinter

import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk #Usamos bootstrap para darle detalles a la GUI

def convert():
    mile_input = entry_int.get()
    km_output = mile_input * 1.161
    output_string.set(km_output)

#Ventana
ventana = ttk.Window(themename='darkly')
ventana.title("Prueba 1") # pone un titulo a la ventana
ventana.geometry("300x150") # Geometria de la ventana

#Titulo
tittle_label = ttk.Label(master = ventana, text = 'Millas a Kilometros', font='Calibri 24 bold')
tittle_label.pack() # div mas sencillo de la gui

#Campo de escritura
input_frame= ttk.Frame(master = ventana)
entry_int = tk.IntVar(master=input_frame)
entry = ttk.Entry(master = input_frame, textvariable = entry_int)
button = ttk.Button(master = input_frame, text = "Conversión", command= convert)
entry.pack(side = 'left', padx = 10)
button.pack(side = 'left')
#.PACK() nos mete la entrada y el boton en al cuadro de escritura, que posteriormente ingresa a la ventana
input_frame.pack(pady = 10)

#Salida o impresion
output_string = tk.StringVar()
output_label = ttk.Label(
    master=ventana,
    text='Salida',
    font='Times  24',
    textvariable= output_string) # esta nos permite mostrar los resultados
output_label.pack(pady = 5)

#corriendo la ventana
ventana.mainloop()