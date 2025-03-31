windowCoords_encoding = {
    'offsetX': 1273,
    'offsetY': 0,
    'width': 1294,
    'height': 703
}


pressRelease_encoding = {
    'p': 0.5,
    'r': 1
}

MBKeyCode_encoding = {
    'Button.left': 0.5,
    'Button.right': 1
}

KeyboardKeyCode_encoding  = {
    'w' :1,
    's' :2,
    'a' :3,
    'd' :4,
    'e' :5,
    'q' :6,
    'r' :7,
    'h' :8,
    'v' :9,
    'f' :10,
    'z' :11,
    'c' :12,
    '`' :13,
    'x' :14,
    '1' :15,
    '2' :16,
    '3' :17,
    '4' :18,
    '5' :19,
    '6' :20,
    '7' :21,
    '8' :22,
    '9' :23,
    '0' :24,
    'Key.f1' :25,
    'Key.f2' :26,
    'Key.f3' :27,
    't' :28,
    'p' :29,
    'l' :30,
    'b' :31,
    'o' :32,
    'j' :33,
    'k' :34,
    'Key.f10' :35,
    'Key.f4' :36,
    'Key.f5' :37,
    'Key.f9' :38,
    'Key.shift' :39,
    'Key.ctrl_l' :40,
    'Key.ctrl_r' :41,
    'Key.alt' :42,
    'Key.space' :43,
    'Key.enter' :44,
    'up' :45,
    'down' :46,
    'Key.shift_l' :47,
    'Key.shift_r' :48,
    'Key.alt_l' :49,
    'Key.alt_r' :50,
    'y' :51,
    'g' :52,
    'u' :53,
    'Key.esc' :54,
    'Key.tab' :55,
    'left' :56,
    'right' :57,
    'Key.pause' :58,
    'Key.backspace' :59,
}

peripheral_encoding = {
    'MBKeyCode_encoding' : 0.5,
    'KeyboardKeyCode_encoding' : 1
}

actionPerformed_encoding = {
    'True' : 1,
    'False' : 0
}

# [1,600,400,0,1,1,10] = press w at 600 400 and wait 10 ms
# [actionperformed, locX, locY, actionstate, actionperipheral, key, delay]
# [0,0,0,0,0,0,0] for no action
# 7 outputs



def encodeActions(actions, deltas):
    deltas.append(0)
    encodedActions = []
    for i in range(len(actions)):
        encodedActions.append(encodeAction(actions[i],deltas[i]))
    return encodedActions

#[locX, locY, state, key]
def encodeAction(action, delta):
    encodedAction = []
    encodedAction.append(actionPerformed_encoding['True'])
    encodedAction.extend([int(action[0])-int(windowCoords_encoding['offsetX']), int(action[1])-int(windowCoords_encoding['offsetY'])]) #locX locY
    encodedAction.append(pressRelease_encoding[action[2]]) #press/release
    if action[3][0] == "B":
        encodedAction.append(peripheral_encoding['MBKeyCode_encoding'])
        encodedAction.append(MBKeyCode_encoding[action[3]])
    else:
        encodedAction.append(peripheral_encoding['KeyboardKeyCode_encoding'])
        encodedAction.append(KeyboardKeyCode_encoding[action[3]])
    encodedAction.append(int(delta))
    return encodedAction





#new encoding = [action?, locX, locY, peripheral, key, total action time from press to release];
# 6 outputs

def encodeActionsNewEncoding(actions, maxTick):
    actionIndex = 0
    encodedActions = []
    ticks = []
    for i in range(int(maxTick)+1):
        if i == 0:
            continue
        ticks.append(i)
        if actionIndex < len(actions) and i >= actions[actionIndex][0]:
            encodedActions.append(encodeActionProperDelta(actions[actionIndex]))
            actionIndex += 1
        else:
            encodedActions.append(encodedNoActionNewEncoding())
    return ticks, encodedActions


def encodeActionProperDelta(action):
    encodedAction = []
    encodedAction.extend(
        [actionPerformed_encoding['True'], 
         (action[1] - windowCoords_encoding['offsetX']) / windowCoords_encoding['width'], 
         (action[2] - windowCoords_encoding['offsetY']) / windowCoords_encoding['height']
        ]
    )

    if action[4][0] == "B":
        encodedAction.append(peripheral_encoding['MBKeyCode_encoding'])
        encodedAction.append(MBKeyCode_encoding[action[4]])
    else:
        encodedAction.append(peripheral_encoding['KeyboardKeyCode_encoding'])
        encodedAction.append(KeyboardKeyCode_encoding[action[4]] / 59)
    encodedAction.append(action[0] / 1800) # 30 sec limit to actions.
    return encodedAction

def encodedNoActionNewEncoding():
    return [0,0,0,0,0,0]







def encodeNoAction():
    return [0,0,0,0,0,0,0]


def readEncodedActionFile(filename):
    actions = []
    with open(filename, 'r') as file:
        start = file.readline()
        _, offsetX, offsetY = start.split(' ')
        offsetY = offsetY.strip()
        for line in file:
            if line[0] != 'E':
                line = line.strip('[] \n')
                action = line.split(',')
                action = [int(string) for string in action]
                actions.append(action)
    return actions, offsetX, offsetY


if __name__ == '__main__':
    # from writeread_actionsfromfile import readActionsfromFile
    # import sys
    # actions,deltas = readActionsfromFile(sys.argv[1])
    # encodedActions = encodeActions(actions,deltas)
    # with open('encodedActions.txt','w') as file:
    #     file.write('Start ' + windowCoords_encoding['x1'] + ' ' + windowCoords_encoding['y1'] + '\n')
    #     for encodedAction in encodedActions:
    #         file.write(str(encodedAction) + '\n')
    #     file.write('End')
    # file.close()
    from writeread_actionsfromfile import readActionsfromFileDeltaKeypress
    import sys

    actions = readActionsfromFileDeltaKeypress(sys.argv[1])
    ticks, encodedActions = encodeActionsNewEncoding(actions, sys.argv[2])
    with open(sys.argv[3], 'w') as file:
        file.write('Start ' + str(windowCoords_encoding['offsetX']) + ' ' + str(windowCoords_encoding['offsetY']) + '\n')
        for i in range(len(ticks)):
            file.write(str(ticks[i]) + " " + str(encodedActions[i]) + '\n')
        file.write('End')



