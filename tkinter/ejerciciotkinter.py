import tkinter as tk
from tkinter import ttk

def saludo():
    print("Hola, como estas?")

window = tk.Tk()
window.title('Ejercicio Tkinter')
window.geometry('500x500')

cp_hllw = ttk.Label(master=window, text="Imprime Hola en la terminal")
cp_hllw.pack()

entry = ttk.Entry(master=window)
entry.pack()

btn_hllw = ttk.Button(master=window, text='Oprimeme', command=saludo)
btn_hllw.pack()


window.mainloop()
