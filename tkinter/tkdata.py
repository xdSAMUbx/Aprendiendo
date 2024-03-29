import tkinter as tk
from tkinter import ttk


def funcion_boton():
    #get the content of the entry
    print(entry.get())
    #45:02

#Creando la ventana
window = tk.Tk()
window.title("Getting and setting widgets")
window.geometry("500x500")

#widgets
label = ttk.Label(master=window, text='Algo de texto')
label.pack()

entry = ttk.Entry(master=window)
entry.pack()

button = ttk.Button(master=window,text="Oprimeme", command=funcion_boton)
button.pack()


#run
window.mainloop()
