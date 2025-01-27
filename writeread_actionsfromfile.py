from datetime import datetime

def writeActionstoFile(filepath, actions, xOffset, yOffset):
    with open(filepath, 'w') as file:
        file.write('Start ' + str(xOffset) + ' ' + str(yOffset) + '\n')
        for action in actions:
            file.write(action + '\n')
        file.write('End')


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
                _, x, y = line.split(' ')
                y = y.strip()
                offsetX = int(x)
                offsetY = int(y)

            if line[0] == 'E':
                previous = -1
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
                locX = int(locX) + offsetX
                locY = int(locY) + offsetY
                key = key.strip()
                keystrokes.append([locX, locY, state, key])


                if previous != -1:
                    now = datetime.strptime(timestamp, '%Y-%m-%d_%H-%M-%S-%f')
                    timeDelta = now - previous
                    if timeDelta.total_seconds() < 0:
                        deltas.append(0)
                    else:
                        deltas.append(timeDelta.total_seconds())

                previous = datetime.strptime(timestamp, '%Y-%m-%d_%H-%M-%S-%f')

        file.close()
        deltas.append(0)
        return keystrokes, deltas