from tkinter import *
import tkinter
import time
import pyautogui as pg


inicio = None

    
def iniciar(pos, click = 1):
    
    pg.moveTo(pos)
    pg.click(button='right')    

def process(cancel=False):
    global inicio
    if not cancel:
        pos = 1218,270
        pos2 = 1249,618
        
        iniciar(pos)
        time.sleep(5)
        iniciar(pos2)
        time.sleep(5)
        inicio = raiz.after(5000, process)
    else: 
        raiz.after_cancel(inicio)

def start():
    print("inicio")
    boton_inicio.config(text="FIN", command=stop)
    pg.hotkey('winleft','d')
    process()

def stop():
    print("fin")
    boton_inicio.config(text="INICIAR", command=start)
    process(True)
    
    
    
if __name__=='__main__':

    raiz = Tk()
    raiz.title("BOTSITO")
    raiz.config(bg="black")

    label_1 = Label(raiz,text="HOLA SOY BOTSITO",fg="white",bg="black",font=("Helvetica",25))
    # label_1.grid(row=0, column=2, padx=10, pady=10)
    label_1.pack(anchor="center")
    
    mi_frame = Frame()
    mi_frame.pack()
    ancho = 640
    alto = 320
    mi_frame.config(width=ancho, height=alto)
    mi_frame.config(bg="black")
    boton_inicio = tkinter.Button(mi_frame, text="INICIAR",padx=60,pady=20, command=start)
    boton_inicio.place(x=(ancho/2), y = (alto/1.25), anchor="center")


    raiz.mainloop()


 
    

  