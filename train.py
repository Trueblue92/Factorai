from nn import test_model
import os
import numpy as np
from PIL import Image
import json
from tqdm import tqdm

def create_windows(dir):
    images = os.listdir(dir)
    images.sort(key=lambda x: int(x.split('.')[0]))
    windows = []
    for i in range(len(images) - 3):
        windows.append([images[i], images[i+1], images[i+2], images[i+3]])
    return windows
    

def create_target_windows(dir):
    targets = loadEncodedActions(dir)
    targetWindows = []
    for i in range(len(targets) - 3):
        targetWindows.append([targets[i], targets[i+1], targets[i+2], targets[i+3]])
    print(len(targetWindows))
    return targetWindows


def loadEncodedActions(dir):
    targets = []
    with open(dir, 'r') as file:
        for line in file:
            target = line.split('[')
            if len(target) > 1:
                target = '[' + target[1]
                target = json.loads(target)
                targets.append(target)
    return targets


def loadImages_lazy(dir, imagesSlice):
    windows = []
    for i in tqdm(range(len(imagesSlice))):
        window = []
        for j in range(len(imagesSlice[i])):
            with Image.open(os.path.join(dir, imagesSlice[i][j])) as img:
                img = np.array(img)
                window.append(img)
        windows.append(window)
    print(len(windows))
    return windows


model = test_model()
for j in range(1,9):
        
    imagePaths = create_windows("./run"+str(j)+"/capture")
    ys = np.array(create_target_windows("./run"+str(j)+".txt"))

    for i in range(0,len(ys), 32):
        X = np.array(loadImages_lazy("./run"+str(j)+"/capture",imagePaths[i:min(i+64, len(ys)-1)]))
        y =ys[i:min(i+64, len(ys)-1)]
        assert(len(X) == len(y))


        model.compile(loss="MSE", optimizer="adam", metrics=["mean_squared_error"])
        model.fit(x=X, y=y, batch_size=4, epochs=1)
        model.save('model.keras')




