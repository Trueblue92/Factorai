import pygetwindow as pgw
import pyautogui as pag
from PIL import Image
import numpy

def takeFactorioScreenshot(path, window, camera):

	image = camera.grab(region=(window["left"], window["top"], window["right"], window["bottom"]))
	try:
		image = Image.fromarray(image)
		image.save(path + '.jpeg')
	except Exception:
		pass

#'Factorio 2.0.23'