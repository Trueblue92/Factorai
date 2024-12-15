from pynput.keyboard import Listener as  KeyboardListener
from pynput.mouse import Listener as MouseListener
from screenshot import takeFactorioScreenshot as tFS
from keylogger import keyLogger as kL
from gamecapture import captureGame as cG
from datetime import datetime
import pygetwindow as pgw
import sys
import dxcam
import os
import multiprocessing
from subprocess import Popen


path = os.path.dirname(os.path.abspath(__file__)) + "\\run1\\"
print(path)
window = pgw.getWindowsWithTitle('Factorio 2.0.23')[0]
left, top = window.topleft

right, bottom = window.bottomright
top += 35
bottom -= 7
right -= 7
left += 7
window = {
    "window" : window,
    "left"   : left,
    "top"    : top,
    "bottom" : bottom,
    "right"  : right
}
print(window)
camera = dxcam.create()

Popen('python .\keylogger.py')
#kl(path=path, window=window, camera=camera)
cG(path=path + "capture\\", window=window, camera=camera)
