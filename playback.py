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

# def moveMouse(locX, locY, state, key, mouse):
#     mouse.position = (locX, locY)
    
def runCommands(deltas, keystrokes, keyboard, mouse):
    for index in range(len(keystrokes)):
        if keystrokes[index][3][0] == 'B':
            pressMouse(*keystrokes[index], mouse)
            print('mouse')
        # elif keystrokes[index][3][0] == -1:
        #     moveMouse(*keystrokes[index], mouse)
        else:
            pressKey(*keystrokes[index], keyboard, mouse)
            print('key')
        
        time.sleep(deltas[index])


if __name__ == '__main__':
    keyboard = pnp.keyboard.Controller()
    mouse = pnp.mouse.Controller()

    keystrokes, deltas = readActionsfromFile(sys.argv[1])
    # print(deltas)
    runCommands(deltas, keystrokes, keyboard, mouse)




