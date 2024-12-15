import sys
from datetime import datetime
import time
import pyautogui as pag
import pynput as pnp

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
    if state == 'p':
        keyboard.press(key)
    else:
        keyboard.release(key)

    pass

def extractCommands(filename):
    previous = -1
    offsetX = 1273
    offsetY = 35
    deltas = []
    keystrokes = []
    with open(filename, 'r') as file:
        # Read each line in the file
        for line in file:
            # Print each line
            if line[0] == 'c':
                keypress = line.split('\\')[1]
                timestamp, keypress = keypress.split(':')
                locX, locY, state, key = keypress.split(' ')
                locX = int(locX) + offsetX
                locY = int(locY) + offsetY
                key = key.strip()
                keystrokes.append([locX, locY, state, key])


                if previous != -1:
                    now = datetime.strptime(timestamp, '%Y-%m-%d_%H-%M-%S-%f')
                    timeDelta = now - previous
                    if timeDelta.total_seconds() < 0:
                        deltas.append(0)
                    else:
                        deltas.append(timeDelta.total_seconds())

                previous = datetime.strptime(timestamp, '%Y-%m-%d_%H-%M-%S-%f')

        file.close()
        deltas.append(0)
        return deltas, keystrokes
    
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

    deltas, keystrokes = extractCommands(sys.argv[1])
    print(deltas, keystrokes)
    runCommands(deltas, keystrokes, keyboard, mouse)




