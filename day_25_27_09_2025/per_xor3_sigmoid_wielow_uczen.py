# perceptron wielowarstwowy
import numpy as np


# warstwa wejściowej
# warstwy ukrytej
# warstwa wyjscia

# funkcja aktywacji sigmoid
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])  # etykiety

np.random.seed(42)

W_hidden = np.random.rand(2, 2)
W_output = np.random.rand(2, 1)

learning_rate = 0.5
epochs = 5000

for epoch in range(epochs):
    # warstwa ukryta
    hidden_input = np.dot(X, W_hidden)
    hidden_output = sigmoid(hidden_input)

    # warstwa wyjściowa
    output_input = np.dot(hidden_output, W_output)
    output = sigmoid(output_input)

    # bład
    error = y - output

    # aktualizacja wag, backpropagation
    d_output = error * (output * (1 - output))
    error_hidden = d_output.dot(W_output.T)
    d_hidden = error_hidden * (hidden_output * (1 - hidden_output))

    # aktualizacja wag
    W_output += hidden_output.T.dot(d_output) * learning_rate
    W_hidden += X.T.dot(d_hidden) * learning_rate
