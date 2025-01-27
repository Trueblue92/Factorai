from pynput.keyboard import Listener as  KeyboardListener
from pynput.mouse import Listener as MouseListener
from screenshot import takeFactorioScreenshot as tFS
from datetime import datetime
import sys
from random import random

def getDateTime():
    datetimeStr = datetime.utcnow().strftime('%Y-%m-%d_%H-%M-%S-%f')[:-3]
    return datetimeStr

def on_move(x, y):
    # with open(path + 'inputs\\keys.txt', 'a') as file:
    #             timeStr = getDateTime()
    #             file.write('movement\\' + timeStr + ':' +'{0} {1}\n'.format(x-window["left"],y-window["top"]))
    global mouseX, mouseY
    mouseX = x
    mouseY = y

def get_tick():
    with open(tick_path, 'r') as file:
        data = file.readlines()
    if data is None or data == []:
        return get_tick()
    else:
        return data[0]   
        
def on_click(x, y, button, pressed, path):
    # if x > window["left"] and y > window["top"] and x < window["right"] and y < window["bottom"]:
    if pressed:
        with open(path + 'inputs\\keys.txt', 'a') as file:
            timeStr = get_tick()
            file.write('action\\' + timeStr + ':' +'{0} {1} p {2}\n'.format(x,y, button))
            # tFS(path + 'action\\' + timeStr, window, camera)
    else:
        with open(path + 'inputs\\keys.txt', 'a') as file:
            timeStr = get_tick()
            file.write('action\\' + timeStr + ':' +'{0} {1} r {2}\n'.format(x,y, button))
                # tFS(path + 'action\\' + timeStr, window, camera)

#def on_scroll(x, y, dx, dy):
#    global top
#    global left
#    global window
#    global path
#    with open('inputs/keys.txt', 'a') as file:
#        timeStr = getDateTime()
#        file.write(timeStr + ':' +'({0}, {1})({2}, {3})\n'.format(x-left,y-top, dx, dy))
#        tFS(path + timeStr, window)
       
def on_press(keys, path, mouseX, mouseY):

    with open(path + 'inputs\\keys.txt', 'a') as file:
        timeStr = get_tick()
        key = str(keys).replace("'", "")
        if key == 'Key.esc':
            file.write('End\n')
            sys.exit('delete key pressed')
        file.write('action\\' + timeStr + ':' + '{0} {1} p {2}'.format(mouseX, mouseY, key) + '\n')
        # tFS(path + 'action\\' + timeStr, window, camera)

def on_release(keys, path, mouseX, mouseY):

    with open(path + 'inputs\\keys.txt', 'a') as file:
        timeStr = get_tick()
        key = str(keys).replace("'", "")
        if key == 'Key.esc':
            file.write('End\n')
            sys.exit('delete key pressed')
        file.write('action\\' + timeStr + ':' + '{0} {1} r {2}'.format(mouseX, mouseY, key) + '\n')
        # tFS(path + 'action\\' + timeStr, window, camera)


def keyLogger(path, top, left):

    # window = window
    # camera = camera
    path = path

    with open(path + 'inputs\\keys.txt', 'a') as file:
        file.write('Start ' + str(left) + ' ' + str(top) + '\n')
        # 

    with MouseListener(
        on_move = lambda x, y: on_move(x=x, y=y), 
        on_click= lambda x, y, button, pressed: on_click(x, y, button, pressed, path=path)
    ) as listener:
        with KeyboardListener(
            on_press=lambda event: on_press(event, path=path, mouseX=mouseX, mouseY=mouseY), 
            on_release=lambda event: on_release(event, path=path, mouseX=mouseX, mouseY=mouseY)
        ) as listener:
            listener.join()

if __name__ == '__main__':
    import os
    # import dxcam
    import pygetwindow as pgw

    path = os.path.dirname(os.path.abspath(__file__)) + "\\run1\\"
    tick_path = "C:\\Users\\mitch\\AppData\\Roaming\\Factorio\\script-output\\tick.txt"

    print(path)

    window = pgw.getWindowsWithTitle('Factorio 2.0.28')[0]
    left, top = window.topleft

    # right, bottom = window.bottomright
    # top += 35
    # bottom -= 7
    # right -= 7
    # window = {
    #     "window" : window,
    #     "left"   : left,
    #     "top"    : top,
    #     "bottom" : bottom,
    #     "right"  : right
    # }
    # print(window)

    # camera = dxcam.create()

    global mouseX
    global mouseY
    mouseX = 0
    mouseY = 0

    last_tick = get_tick()
    tick = last_tick
    while tick == last_tick:
        tick = get_tick()

    keyLogger(path, top, left)