from pynput.keyboard import Listener as  KeyboardListener
from pynput.mouse import Listener as MouseListener
from screenshot import takeFactorioScreenshot as tFS
from datetime import datetime
import sys


def getDateTime():
    datetimeStr = datetime.utcnow().strftime('%Y-%m-%d_%H-%M-%S-%f')[:-3]
    return datetimeStr

def on_move(x, y):
    global mouseX, mouseY
    mouseX = x
    mouseY = y

        
def on_click(x, y, button, pressed, path, window, camera):
    if x > window["left"] and y > window["top"] and x < window["right"] and y < window["bottom"]:
        if pressed:
            with open(path + 'inputs\\keys.txt', 'a') as file:
                timeStr = getDateTime()
                file.write('action\\' + timeStr + ':' +'{0} {1} p {2}\n'.format(x-window["left"],y-window["top"], button))
                tFS(path + 'action\\' + timeStr, window, camera)
        else:
            with open(path + 'inputs\\keys.txt', 'a') as file:
                timeStr = getDateTime()
                file.write('action\\' + timeStr + ':' +'{0} {1} r {2}\n'.format(x-window["left"],y-window["top"], button))
                tFS(path + 'action\\' + timeStr, window, camera)

#def on_scroll(x, y, dx, dy):
#    global top
#    global left
#    global window
#    global path
#    with open('inputs/keys.txt', 'a') as file:
#        timeStr = getDateTime()
#        file.write(timeStr + ':' +'({0}, {1})({2}, {3})\n'.format(x-left,y-top, dx, dy))
#        tFS(path + timeStr, window)
       
def on_press(keys, path, window, camera, mouseX, mouseY):

    with open(path + 'inputs\\keys.txt', 'a') as file:
        timeStr = getDateTime()
        key = str(keys).replace("'", "")
        if key == 'Key.delete':
            file.write('End\n')
            sys.exit('delete key pressed')
        file.write('action\\' + timeStr + ':' + '{0} {1} p {2}'.format(mouseX-window["left"], mouseY-window["top"], key) + '\n')
        tFS(path + 'action\\' + timeStr, window, camera)

def on_release(keys, path, window, camera, mouseX, mouseY):

    with open(path + 'inputs\\keys.txt', 'a') as file:
        timeStr = getDateTime()
        key = str(keys).replace("'", "")
        if key == 'Key.delete':
            file.write('End\n')
            sys.exit('delete key pressed')
        file.write('action\\' + timeStr + ':' + '{0} {1} r {2}'.format(mouseX-window["left"], mouseY-window["top"], key) + '\n')
        tFS(path + 'action\\' + timeStr, window, camera)


def keyLogger(path, window, camera):
    global mouseX, mouseY

    window = window
    camera = camera
    path = path

    with open(path + 'inputs\\keys.txt', 'a') as file:
        file.write('Start ' + str(window['left']) + ' ' + str(window['top']) + '\n')

    with MouseListener(
        on_move = lambda x, y: on_move(x=x, y=y), 
        on_click= lambda x, y, button, pressed: on_click(x, y, button, pressed, path=path, window=window, camera=camera)
    ) as listener:
        with KeyboardListener(
            on_press=lambda event: on_press(event, path=path, window=window, camera=camera, mouseX=mouseX, mouseY=mouseY), 
            on_release=lambda event: on_release(event, path=path, window=window, camera=camera, mouseX=mouseX, mouseY=mouseY)
        ) as listener:
            listener.join()

if __name__ == '__main__':
    import os
    import dxcam
    import pygetwindow as pgw

    path = os.path.dirname(os.path.abspath(__file__)) + "\\run1\\"
    print(path)

    window = pgw.getWindowsWithTitle('Factorio 2.0.23')[0]
    left, top = window.topleft

    right, bottom = window.bottomright
    top += 35
    bottom -= 7
    right -= 7
    window = {
        "window" : window,
        "left"   : left,
        "top"    : top,
        "bottom" : bottom,
        "right"  : right
    }
    print(window)

    camera = dxcam.create()

    mouseX=0
    mouseY=0

    keyLogger(path=path, window=window, camera=camera)