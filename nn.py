from PIL import Image
from keras import utils
from keras.models import Model
from keras.layers import AdditiveAttention, TimeDistributed, Concatenate, LayerNormalization, Attention, ConvLSTM2D, MaxPooling3D, Dense, Flatten, Dropout, Input
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


def initialize_model():


    input = Input(shape=(1,1278,664,3))
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
    x1 = Attention()([x,x[0][0]])
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
    return model


def test_model():
    # Define input shape (sequence of 4 frames of size 512x512x3)
    input = Input(shape=(4, 664, 1278, 3))  # (time_steps, height, width, channels)

    # ConvLSTM2D layers to process the temporal sequence of frames
    x = ConvLSTM2D(32, kernel_size=(3, 3), activation="relu", return_sequences=True, padding="same", data_format="channels_last")(input)
    x = MaxPooling3D(pool_size=(1, 4, 4), data_format="channels_last")(x)
    x = LayerNormalization(epsilon=1e-6)(x)

    x = ConvLSTM2D(64, kernel_size=(3, 3), activation="relu", return_sequences=True, padding="same", data_format="channels_last")(x)
    x = MaxPooling3D(pool_size=(1, 4, 4), data_format="channels_last")(x)
    x = LayerNormalization(epsilon=1e-6)(x)

    # x = ConvLSTM2D(128, kernel_size=(3, 3), activation="relu", return_sequences=True, padding="same", data_format="channels_last")(x)
    # x = MaxPooling3D(pool_size=(1, 4, 4), data_format="channels_last")(x)
    # x = LayerNormalization(epsilon=1e-6)(x)

    # x = ConvLSTM2D(256, kernel_size=(3, 3), activation="relu", return_sequences=True, padding="same", data_format="channels_last")(x)
    # x = MaxPooling3D(pool_size=(1, 2, 2), data_format="channels_last")(x)
    # x = LayerNormalization(epsilon=1e-6)(x)

    # Optional: Apply self-attention to focus on important time steps
    x_attention = AdditiveAttention()([x, x])  # Self-attention over the sequence of frames
    x = Concatenate()([x, x_attention])
    x = LayerNormalization(epsilon=1e-6)(x)
    x = TimeDistributed(Flatten())(x)
    x = TimeDistributed(Dropout(0.3))(x)  # Another Dropout layer
    x = TimeDistributed(Dense(32, activation="relu"))(x)
    # Use TimeDistributed to apply Dense layer to each time step (frame)
    x = TimeDistributed(Dense(6, activation="sigmoid"))(x)

    # Define the model
    model = Model(input, x)
    print(model.summary())
    return model




# model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
# print(model(np.expand_dims([imageData[0]], axis=0)))
