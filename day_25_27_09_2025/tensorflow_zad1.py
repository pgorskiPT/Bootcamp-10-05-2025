import os
import time
import numpy as np

# # pip install tensorflow
# # pip uninstall tensorflow
# # pip install tensorflow-cpu
#
# # pip install tensorflow-macos
# # pip install tensorflow-metal (gpu)

# os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

# 3.13.7
import tensorflow as tf
from tensorflow import keras
from keras import Input
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

print("Dostępne urządzenia:")
print(tf.config.list_physical_devices())
print("Czy GPU jest dostępne:", tf.config.list_physical_devices('GPU'))
print("Czy GPU jest dostępne:", tf.config.list_physical_devices())

# input()
# dane wejściowe
X = np.array(
    [[0, 0],
     [0, 1],
     [1, 0],
     [1, 1]]
)

# dane do nauki
y_xor = np.array([[0], [1], [1], [0]])
y_and = np.array([[0], [0], [0], [1]])
y_or = np.array([[0], [1], [1], [1]])


# trening
def train_model(y_train, logic_type):
    print(f"Uczenie modelu dla operacji: {logic_type}")

    # definiujemy model
    model = Sequential([
        Input(2, ),
        Dense(4, activation="relu"),  # warstwa ukryta, 4 neurony, funkcja relu
        Dense(1, activation="sigmoid")  # warstwa wyjściowa, sigmoid
    ])

    # kompilacja modelu
    model.compile(optimizer="adam", loss='binary_crossentropy', metric=['accuracy'])

    with tf.device("/GPU:0"):
        model.fit(X, y_train, epochs=500, verbose=1)

    # testowanie modelu
    predictions = model.predict(X)
    predictions = (predictions > 0.5).astype(int)

    print(f'Przewidywanie wyników dla operacji {logic_type}')
    for i in range(len(X)):
        print(f"{X[i]} {predictions[i][0]} oczekiwanie: {y_train[i][0]}")

    return model


start_time = time.time()

model_xor = train_model(y_xor, "XOR")

print(f'Estimated time:{time.time() - start_time}')
