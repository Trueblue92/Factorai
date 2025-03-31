import sys
import time
import pynput as pnp
from pynput.keyboard import Key
from writeread_actionsfromfile import readActionsfromFile
import pygetwindow as pgw

def get_tick():
    with open(tick_path, 'r') as file:
        data = file.readlines()
    if data is None or data == []:
        return get_tick()
    else:
        return data[0]   

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
    window = pgw.getWindowsWithTitle('Factorio 2.0.43')[0]
    window.activate()
    previous_tick = get_tick()
    print(deltas)
    for index in range(len(keystrokes)):

        if keystrokes[index][3][0] == 'B':
            pressMouse(*keystrokes[index], mouse)
            print('mouse ', keystrokes[index][3])
        # elif keystrokes[index][3][0] == -1:
        #     moveMouse(*keystrokes[index], mouse)
        else:
            pressKey(*keystrokes[index], keyboard, mouse)
            print('key ', keystrokes[index][3])
        
        if deltas[index] == 0:
            continue
        
        current_tick = get_tick()
        while int(current_tick)-int(previous_tick) < deltas[index]:
            current_tick = get_tick()
        previous_tick = get_tick()
        # time.sleep(deltas[index])


if __name__ == '__main__':
    

    keyboard = pnp.keyboard.Controller()
    mouse = pnp.mouse.Controller()

    tick_path = "C:\\Users\\mitch\\AppData\\Roaming\\Factorio\\script-output\\tick.txt"
    keystrokes, deltas = readActionsfromFile(sys.argv[1])
    # print(deltas)

    last_tick = get_tick()
    tick = last_tick
    while tick == last_tick:
        tick = get_tick()

    runCommands(deltas, keystrokes, keyboard, mouse)
    




