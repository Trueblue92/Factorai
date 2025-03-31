from datetime import datetime

def writeActionstoFile(filepath, actions, xOffset, yOffset):
    with open(filepath, 'w') as file:
        file.write('Start ' + str(xOffset) + ' ' + str(yOffset) + '\n')
        for action in actions:
            file.write(action + '\n')
        file.write('End')


def readActionsfromFileDeltaKeypress(filename):
    pressedKeys = []
    keystrokes = []
    offsetX = 1273
    offsetY = 35
    with open(filename, 'r') as file:
        for line in file:
            if line[0] == 'S':
                _, x, y, _, _ = line.split(' ')
                offsetX = int(x)
                offsetY = int(y)
                continue
            
            if line[0] == 'E':
                continue
            
            if line[0] == 'a':
                keypress = line.split('\\')[1]
                tick, keypress = keypress.split(':')
                locX, locY, state, key = keypress.split(' ')
                locX = int(locX)
                locY = int(locY)
                tick = int(tick)
                key = key.strip()

                if state == 'p':
                    duplicate = False
                    for pressedKey in pressedKeys:
                        if key in pressedKey:
                            duplicate = True
                    
                    if duplicate:
                        continue
                    
                    pressedKeys.append([key, len(keystrokes), tick])
                    keystrokes.append([tick, locX, locY, state, key])
                else:
                    for pressedKey in pressedKeys:
                        if key in pressedKey:
                            index = pressedKeys.index(pressedKey)
                            _, pressedIndex, pressedTick = pressedKeys.pop(index)
                            keystrokes[pressedIndex].append(tick-pressedTick)
        file.close()
        return keystrokes
    


def readActionsfromFile(filename):
    previous = -1
    offsetX = 1273
    offsetY = 35
    deltas = []
    keystrokes = []
    with open(filename, 'r') as file:
        # Read each line in the file
        for line in file:
            if line[0] == 'S':
                _, x, y, _, _ = line.split(' ')
                y = y.strip()
                offsetX = int(x)
                offsetY = int(y)
                continue

            if line[0] == 'E':
                continue
            # Print each line
            # if line[0] == 'm':
            #     keypress = line.split('\\')[1]
            #     timestamp, keypress = keypress.split(':')
            #     locX, locY = keypress.split(' ')
            #     locY = locY.strip()
            #     locX = int(locX) + offsetX
            #     locY = int(locY) + offsetY
            #     keystrokes.append([locX, locY, -1, [-1]])
            #     if previous != -1:
            #         now = datetime.strptime(timestamp, '%Y-%m-%d_%H-%M-%S-%f')
            #         timeDelta = now - previous
            #         if timeDelta.total_seconds() < 0:
            #             deltas.append(0)
            #         else:
            #             deltas.append(timeDelta.total_seconds())
            #     previous = datetime.strptime(timestamp, '%Y-%m-%d_%H-%M-%S-%f')


            if line[0] == 'a':
                keypress = line.split('\\')[1]
                timestamp, keypress = keypress.split(':')
                locX, locY, state, key = keypress.split(' ')
                locX = int(locX)
                locY = int(locY)
                key = key.strip()
                keystrokes.append([locX, locY, state, key])


                if previous != -1:
                    # now = datetime.strptime(timestamp, '%Y-%m-%d_%H-%M-%S-%f')
                    now = timestamp
                    # timeDelta = now - previous
                    timeDelta = int(now) - int(previous)
                    # if timeDelta.total_seconds() < 0:
                    if timeDelta < 0:
                        deltas.append(0)
                    else:
                        # deltas.append(timeDelta.total_seconds())
                        deltas.append(timeDelta)


                # previous = datetime.strptime(timestamp, '%Y-%m-%d_%H-%M-%S-%f')
                previous = timestamp

        file.close()
        deltas.append(0)
        return keystrokes, deltas