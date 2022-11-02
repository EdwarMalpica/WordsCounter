import time
import threading as th
import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry('600x500')
ventana.title('Aplicacion')

labelTitle=tk.Label(ventana)
varText = tk.StringVar(value='Ingrese el texto aqui')
textArea =tk.Text(ventana)

ventana.rowconfigure(0, weight=1)
ventana.rowconfigure(1, weight=1)

ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=1)

ventana.rowconfigure(2, weight=1)
ventana.rowconfigure(3, weight=1)

ventana.columnconfigure(2, weight=1)
ventana.columnconfigure(3, weight=1)

labelTitle.grid(row=0, column=0)
textArea.grid(row=1, column=0, columnspan=2, rowspan=1)


def countCharacter():
    while True:
        text = len(textArea.get(1.0, tk.END))-1
        labelTitle.config(text='Total caracteres: '+str(text))
        time.sleep(0.1)


def saveFile():
    while True:
        with open('../textoPrueba.txt', 'w') as f:
            f.write(textArea.get(1.0, tk.END))
            f.close()
            time.sleep(0.1)

def deleteText():
    textArea.delete(1.0, tk.END)


buttonDelete = ttk.Button(ventana, text='Borrar Texto', command=deleteText)
buttonDelete.grid(row=2, column=0)

hiloContarPalabras = th.Thread(target=countCharacter)
hiloContarPalabras.start()
hiloGuardarArchivo = th.Thread(target=saveFile)
hiloGuardarArchivo.start()
ventana.mainloop()