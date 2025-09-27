import numpy as np


# ReLU - funkcja aktywacji

# jest narażona na martwe neurony
def relu(x):
    return np.maximum(0, x)


# pochodna relu
def relu_derivative(x):
    return np.where(x > 0, 1, 0)


# XOR
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])  # etykiety

np.random.seed(42)

W_hidden = np.random.rand(2, 2) * 2 - 1
W_output = np.random.rand(2, 1) * 2 - 1

learning_rate = 0.01
epochs = 50000

# trenowanie sieci
for epoch in range(epochs):
    hidden_input = np.dot(X, W_hidden)
    hidden_output = relu(hidden_input)

    final_input = np.dot(hidden_output, W_output)
    final_output = relu(final_input)

    # obliczanie błędu
    error = y - final_output

    # backpropagation
    d_output = error * relu_derivative(final_output)  # pochodna relu
    error_hidden = d_output.dot(W_output.T)
    d_hidden = error_hidden * relu_derivative(hidden_output)

    # aktualizacja wag
    W_output += hidden_output.T.dot(d_output) * learning_rate
    W_hidden += X.T.dot(d_hidden) * learning_rate

# testowanie
for i in range(4):
    hidden_layer_inpput = np.dot(X[i], W_hidden)
    hidden_layer_output = relu(hidden_layer_inpput)

    final_input = np.dot(hidden_layer_output, W_output)
    final_output = relu(final_input)

    print(f'Wejśie: {X[i]} -> Przewidywane wyjścia: {final_output[0]:.4f}')
    # print(f'Wejśie: {X[i]} -> Przewidywane wyjścia: {int(output[0] > 0.5):.4f}')
