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