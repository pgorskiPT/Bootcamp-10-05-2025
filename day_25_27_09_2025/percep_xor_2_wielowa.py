# perceptron wielowarstwowy
import numpy as np


# warstwa wejściowej
# warstwy ukrytej
# warstwa wyjscia

# funkcja aktywacji sigmoid
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 1, 1, 0])  # etykiety

# warstwa ukryta 2 neurony
W1 = np.array([[1, 1], [1, 1]])
b1 = np.array([-1.0, 0.5])

# warstwa wyjściowa 1 neuron
W2 = np.array([1, -1])
b2 = -0.5

for x in X:
    print(x)

    # warstwa ukryta
    hidden_input = np.dot(x, W1) + b1
    hidden_output = sigmoid(hidden_input)

    output_input = np.dot(hidden_output, W2) + b2
    output = sigmoid(output_input)

    print(f'Wejście: {x}, Wyjście: {output}')
    print(f'Wejście: {x}, Wyjście: {int(output > 0.5)}')
# https://playground.tensorflow.org/ - trenowanie sieci neuronowych
