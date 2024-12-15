import threading
from screenshot import takeFactorioScreenshot as tFS
from datetime import datetime
import time

def captureGame(path, window, camera):
  timeStr = datetime.utcnow().strftime('%Y-%m-%d_%H-%M-%S-%f')[:-3]
  tFS(path + timeStr, window, camera)
  time.sleep(0.05)
  captureGame(path, window, camera)

