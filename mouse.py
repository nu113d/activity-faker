import pyautogui as mouse
from wakepy import keep
import time, random

def moveMouse():
    x = random.randrange(-5, 5)
    y = random.randrange(-5, 5)
    mouse.moveRel(x, y, 0.5)

with keep.presenting():
    while True:
        pos = mouse.position()
        time.sleep(60)
        if(pos == mouse.position()):
            moveMouse()
        #time.sleep(15)
