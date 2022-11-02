import time
import pyautogui as pg

print ("thank you for call me")
time.sleep (1)
print ("initializing the task")


tiempo = [x for x in range (0,10)]

pos = 1218,270
pos2 = 1249,418
pg.hotkey("windows","d")

def iniciar(pos, click = 1):
    pg.moveTo(pos)
    pg.click(clicks=click)

for element in tiempo:
    iniciar(pos)
    time.sleep(5)
    iniciar(pos2)
    time.sleep(5)

print("finished")

    

