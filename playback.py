import sys
import time
import pynput as pnp
from pynput.keyboard import Key
from writeread_actionsfromfile import readActionsfromFile

def pressMouse(locX, locY, state, key, mouse):
    key = key.strip()
    if key == 'Button.left':
        key = pnp.mouse.Button.left
    else:
        key = pnp.mouse.Button.right
    mouse.position = (locX, locY)
    if state == 'p':
        mouse.press(key)
    else:
        mouse.release(key)

def pressKey(locX, locY, state, key, keyboard, mouse):
    key = key.strip()
    mouse.position = (locX, locY)
    if key[0] == 'K':
        key = Key[key[4:]]
    if state == 'p':
        keyboard.press(key)
    else:
        keyboard.release(key)

    pass
    
def runCommands(deltas, keystrokes, keyboard, mouse):
    for index in range(len(keystrokes)):
        if keystrokes[index][3][0] == 'B':
            pressMouse(*keystrokes[index], mouse)
        else:
            pressKey(*keystrokes[index], keyboard, mouse)
        
        time.sleep(deltas[index])


if __name__ == '__main__':
    keyboard = pnp.keyboard.Controller()
    mouse = pnp.mouse.Controller()

    keystrokes, deltas = readActionsfromFile(sys.argv[1])
    print(deltas, keystrokes)
    runCommands(deltas, keystrokes, keyboard, mouse)




