from datetime import datetime, timedelta

windowCoords_decoding = {
    'x1': 1273,
    'y1': 35,
    'x2': 1280,
    'y2': 661
}

pressRelease_decoding = {
    0: 'p',
    1: 'r'
}

MBKeyCode_decoding = {
    0: 'Button.left',
    1: 'Button.right'
}

KeyboardKeyCode_decoding  = {
    0:'w',
    1:'s',
    2:'a',
    3:'d',
    4:'e',
    5:'q',
    6:'r',
    7:'h',
    8:'v',
    9:'f',
    10:'z',
    11:'c',
    12:'`',
    13:'x',
    14:'1',
    15:'2',
    16:'3',
    17:'4',
    18:'5',
    19:'6',
    20:'7',
    21:'8',
    22:'9',
    23:'0',
    24:'Key.f1',
    25:'Key.f2',
    26:'Key.f3',
    27:'t',
    28:'p',
    29:'l',
    30:'b',
    31:'o',
    32:'j',
    33:'k',
    34:'Key.f10',
    35:'Key.f4',
    36:'Key.f5',
    37:'Key.f9',
    38:'Key.shift',
    40:'Key.ctrl',
    41:'Key.alt',
    42:'Key.space',
    43:'Key.enter',
    44:'up',
    45:'down',
    46:'Key.shift_l',
    47:'Key.shift_r',
    48:'Key.alt_l',
    49:'Key.alt_r',
    50:'y',
    51:'g',
    52:'u',
    53:'Key.esc',
    54:'Key.tab',
    55:'left',
    56:'right',
    57:'Key.pause',
    58:'Key.backspace',
}

peripheral_decoding = {
    0: MBKeyCode_decoding,
    1: KeyboardKeyCode_decoding
}

actionPerformed_decoding = {
    1: True,
    0: False
}

def decodeActions(actions):
    decodedActions = []
    time = datetime.utcnow().strftime('%Y-%m-%d_%H-%M-%S-%f')[:-3]
    for action in actions:
        decodedActions.append(decodeAction(action, time))
        delta = timedelta(milliseconds=action[6])
        time = datetime.strptime(time, '%Y-%m-%d_%H-%M-%S-%f')
        time += delta
        time = time.strftime('%Y-%m-%d_%H-%M-%S-%f')
    return decodedActions

#[locX, locY, state, key]
## [actionperformed, locX, locY, actionstate, actionperipheral, key, delay]
#r Button.left
def decodeAction(encodedAction, timestamp):
    decodedAction = 'action\\'
    print(encodedAction)
    decodedAction += timestamp + ':'
    decodedAction += str(encodedAction[1]) + ' ' + str(encodedAction[2]) + ' ' #loX locY
    decodedAction += pressRelease_decoding[encodedAction[3]] + ' '
    decodedAction += peripheral_decoding[encodedAction[4]][encodedAction[5]]
    return decodedAction

def decodeNoAction(timeStr):
    return 'noaction\\' + timeStr


if __name__ == '__main__':
    from encodeActions import readEncodedActionFile
    import sys

    actions, offsetX, offsetY = readEncodedActionFile(sys.argv[1])
    print(actions)
    decodedActions = decodeActions(actions)
    with open('decodedActions.txt','w') as file:
        file.write('Start ' + offsetX + ' ' + offsetY + '\n')
        for decodedAction in decodedActions:
            file.write(str(decodedAction) + '\n')
        file.write('End')
    file.close()
