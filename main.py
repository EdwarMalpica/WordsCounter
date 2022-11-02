import time
import threading as th
import tkinter as tk
from datetime import datetime


ventana = tk.Tk()
ventana.geometry('600x200')
ventana.title('Aplicacion')

labelTitle=tk.Label(ventana)
varText = tk.StringVar(value='Ingrese el texto aqui')
textArea =tk.Text(ventana)
labelHour = tk.Label(ventana)
labelTitle.pack(side='right')
labelHour.pack(side='left')
textArea.pack()


def countCharacter():
    while True:
        text = len(textArea.get(1.0, tk.END))-1
        labelTitle.config(text='Total caracteres: '+str(text))
        time.sleep(0.1)


def setCurrentHour():
    while True:
        currentHour = datetime.now()
        labelHour.config(text='Hora Actual: '+ currentHour.strftime("%H:%M:%S"))
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
hiloCurrentHour = th.Thread(target=setCurrentHour)
hiloCurrentHour.start()
ventana.mainloop()