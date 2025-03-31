import numpy as np
import keras
from keras import ops
from keras import utils
from PIL import Image

model = keras.models.load_model('./model.keras')

        # window = []
        # for j in range(len(imagesSlice[i])):
        #     with Image.open(os.path.join(dir, imagesSlice[i][j])) as img:
        #         img = np.array(img)
        #         window.append(img)

imageData = []
testInput = np.array(Image.open("492.jpg"))
imageData.append(testInput)

testInput = np.array(Image.open("493.jpg"))
imageData.append(testInput)

testInput = np.array(Image.open("494.jpg"))
imageData.append(testInput)

testInput = np.array(Image.open("495.jpg"))
imageData.append(testInput)
imageData = np.expand_dims(np.array(imageData), axis=0)

print(model.predict(imageData))