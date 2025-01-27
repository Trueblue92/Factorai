from PIL import Image
from keras import utils
from keras.models import Model
from tensorflow.keras.layers import Concatenate, LayerNormalization, Attention, ConvLSTM2D, MaxPooling3D, Dense, Flatten, Dropout, Input
import numpy as np


imageData = []

testInput = Image.open("492.jpg")
testInput = testInput.resize((512,512), Image.BILINEAR)
imageData.append(utils.img_to_array(testInput))

testInput = Image.open("493.jpg")
testInput = testInput.resize((512,512), Image.BILINEAR)
imageData.append(utils.img_to_array(testInput))

testInput = Image.open("494.jpg")
testInput = testInput.resize((512,512), Image.BILINEAR)
imageData.append(utils.img_to_array(testInput))

testInput = Image.open("495.jpg")
testInput = testInput.resize((512,512), Image.BILINEAR)
imageData.append(utils.img_to_array(testInput))


print(*np.expand_dims(imageData, axis=0).shape[2:])

input = Input(shape=(4,512,512,3))
x = ConvLSTM2D(4, 5, activation="relu", return_sequences=True, padding="same", data_format="channels_last")(input)
x = MaxPooling3D(pool_size=(1,2,2), data_format="channels_last")(x)
x = LayerNormalization(epsilon=1e-6)(x)
x = ConvLSTM2D(16, 5, activation="relu", return_sequences=True, padding="same", data_format="channels_last")(x)
x = MaxPooling3D(pool_size=(1,2,2), data_format="channels_last")(x)
x = LayerNormalization(epsilon=1e-6)(x)
x = ConvLSTM2D(32, 5, activation="relu", return_sequences=True, padding="same", data_format="channels_last")(x)
x = MaxPooling3D(pool_size=(1,2,2), data_format="channels_last")(x)
x = LayerNormalization(epsilon=1e-6)(x)
x = ConvLSTM2D(64, 5, activation="relu", return_sequences=True, padding="same",data_format="channels_last")(x)
x = MaxPooling3D(pool_size=(1,2,2), data_format="channels_last")(x)
x = LayerNormalization(epsilon=1e-6)(x)
x = ConvLSTM2D(128, 5, activation="relu", return_sequences=True, padding="same",data_format="channels_last")(x)
x = MaxPooling3D(pool_size=(1,2,2), data_format="channels_last")(x)

x = LayerNormalization(epsilon=1e-6)(x)
x1 = Attention()([x,x[0][3]])
x = Concatenate()([x,x1])
x = LayerNormalization(epsilon=1e-6)(x)
x = Flatten()(x)
x = Dropout(0.1)(x)
x = Dense(512, activation="softmax")(x)
x = Dropout(0.1)(x)
x = Dense(16, activation="softmax")(x)
x = Dropout(0.1)(x)
x = Dense(7, activation="softmax")(x)

model = Model(input,x)

print(model.summary())


model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
print(model(np.expand_dims(imageData, axis=0)))
