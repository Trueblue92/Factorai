from decodeActions import *
from datetime import datetime
import random
import time

def createRandomAction(delay):
    datetimeStr = datetime.utcnow().strftime('%Y-%m-%d_%H-%M-%S-%f')[:-3]
    actiontype = random.choice(list(peripheral_decoding))
    x = random.randint(0, windowCoords_decoding['x2'])
    y = random.randint(0, windowCoords_decoding['y2'])
    if actiontype == 0:
        button = random.choice(list(MBKeyCode_decoding))
        button = MBKeyCode_decoding[button]
    else:
        button = random.choice(list(KeyboardKeyCode_decoding))
        button = KeyboardKeyCode_decoding[button]
    pressrelease = random.choice(list(pressRelease_decoding))
    time.sleep(delay)
    return "captures\\" + datetimeStr + ':' + str(x) + ' ' + str(y) + ' ' + pressRelease_decoding[pressrelease] + ' ' + button


def generateMultipleRandomActions(number):
    actions = []
    for i in range(number):
        delay = random.random() * 3
        actions.append(createRandomAction(delay))
    return actions

actions = generateMultipleRandomActions(20)
