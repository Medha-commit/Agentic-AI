import time
import pyautogui
import keyboard

First = 0
Second = 0

VarX = 0
VarY = 0
LnT = 0

Top = 0
Left = 0
STop = 0
SLeft = 0
WnH = 0

while True:
    if keyboard.is_pressed('o'):
        while True:
            if keyboard.is_pressed('f'):
                First = pyautogui.position()
                Left = First[0]
                Top = First[1]
            if keyboard.is_pressed('t'):
                Second = pyautogui.position()
                SLeft = Second[0]
                STop = Second[1]
            if keyboard.is_pressed('u'):
                break
        VarX = SLeft - Left
        VarY = STop - Top
        WnH = VarX, VarY
        LnT = Left, Top
        print(f'Left, Top: {LnT}')
        print(f'Width, Height: {WnH}')
        break
    if keyboard.is_pressed('x'):
        for i in range(10):
            time.sleep(0.5)
            print(pyautogui.position())
    if keyboard.is_pressed('l'):
        break
