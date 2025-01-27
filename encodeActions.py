windowCoords_encoding = {
    'x1': '1273',
    'y1': '35',
    'x2': '1280',
    'y2': '661'
}

pressRelease_encoding = {
    'p': 0,
    'r': 1
}

MBKeyCode_encoding = {
    'Button.left': 0,
    'Button.right': 1
}

KeyboardKeyCode_encoding  = {
    'w' :0,
    's' :1,
    'a' :2,
    'd' :3,
    'e' :4,
    'q' :5,
    'r' :6,
    'h' :7,
    'v' :8,
    'f' :9,
    'z' :10,
    'c' :11,
    '`' :12,
    'x' :13,
    '1' :14,
    '2' :15,
    '3' :16,
    '4' :17,
    '5' :18,
    '6' :19,
    '7' :20,
    '8' :21,
    '9' :22,
    '0' :23,
    'Key.f1' :24,
    'Key.f2' :25,
    'Key.f3' :26,
    't' :27,
    'p' :28,
    'l' :29,
    'b' :30,
    'o' :31,
    'j' :32,
    'k' :33,
    'Key.f10' :34,
    'Key.f4' :35,
    'Key.f5' :36,
    'Key.f9' :37,
    'Key.shift' :38,
    'Key.ctrl' :40,
    'Key.alt' :41,
    'Key.space' :42,
    'Key.enter' :43,
    'up' :44,
    'down' :45,
    'Key.shift_l' :46,
    'Key.shift_r' :47,
    'Key.alt_l' :48,
    'Key.alt_r' :49,
    'y' :50,
    'g' :51,
    'u' :52,
    'Key.esc' :53,
    'Key.tab' :54,
    'left' :55,
    'right' :56,
    'Key.pause' :57,
    'Key.backspace' :58,
}

peripheral_encoding = {
    'MBKeyCode_encoding' : 0,
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
    encodedAction.extend([int(action[0])-int(windowCoords_encoding['x1']), int(action[1])-int(windowCoords_encoding['y1'])]) #locX locY
    encodedAction.append(pressRelease_encoding[action[2]]) #press/release
    if action[3][0] == "B":
        encodedAction.append(peripheral_encoding['MBKeyCode_encoding'])
        encodedAction.append(MBKeyCode_encoding[action[3]])
    else:
        encodedAction.append(peripheral_encoding['KeyboardKeyCode_encoding'])
        encodedAction.append(KeyboardKeyCode_encoding[action[3]])
    encodedAction.append(int(delta * 1000))
    return encodedAction

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
    from writeread_actionsfromfile import readActionsfromFile
    import sys
    actions,deltas = readActionsfromFile(sys.argv[1])
    encodedActions = encodeActions(actions,deltas)
    with open('encodedActions.txt','w') as file:
        file.write('Start ' + windowCoords_encoding['x1'] + ' ' + windowCoords_encoding['y1'] + '\n')
        for encodedAction in encodedActions:
            file.write(str(encodedAction) + '\n')
        file.write('End')
    file.close()



