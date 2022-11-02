import time
import threading as th
import tkinter as tk

ventana = tk.Tk()
ventana.geometry('600x200')
ventana.title('Aplicacion')

labelTitle=tk.Label(ventana)
varText = tk.StringVar(value='Ingrese el texto aqui')
textArea =tk.Text(ventana)

labelTitle.pack()
textArea.pack()


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

hiloContarPalabras = th.Thread(target=countCharacter)
hiloContarPalabras.start()
hiloGuardarArchivo = th.Thread(target=saveFile)
hiloGuardarArchivo.start()
ventana.mainloop()