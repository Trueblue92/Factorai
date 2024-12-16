from gamecapture import captureGame as cG
import pygetwindow as pgw
import dxcam
import os
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
