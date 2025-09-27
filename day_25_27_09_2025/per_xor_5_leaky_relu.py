import numpy as np


# Leaky ReLU - funkcja aktywacji - p pomaga ominąć problem martwych neuronów

def leaky_relu(x, alpha=0.01):
    return np.where(x > 0, x, alpha * x)


# pochodna leaky_relu
def leaky_relu_derivative(x, alpha=0.01):
    return np.where(x > 0, 1, alpha)


# # XOR
# X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
# y = np.array([[0], [1], [1], [0]])  # etykiety

# AND
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [0], [0], [1]])

np.random.seed(42)

# W_hidden = np.random.rand(2, 2) * 2 - 1
# W_output = np.random.rand(2, 1) * 2 - 1

# inicjalizacja wg Xavier/Glorot
W_hidden = np.random.randn(2, 2) * np.sqrt(2 / 2)
W_output = np.random.randn(2, 1) * np.sqrt(2 / 2)

# learning_rate = 0.01
# epochs = 4000
learning_rate = 0.1
epochs = 1000

# trenowanie sieci
for epoch in range(epochs):
    hidden_input = np.dot(X, W_hidden)
    hidden_output = leaky_relu(hidden_input)

    final_input = np.dot(hidden_output, W_output)
    final_output = leaky_relu(final_input)

    # obliczanie błędu
    error = y - final_output

    # backpropagation
    d_output = error * leaky_relu_derivative(final_output)  # pochodna relu
    error_hidden = d_output.dot(W_output.T)
    d_hidden = error_hidden * leaky_relu_derivative(hidden_output)

    # aktualizacja wag
    W_output += hidden_output.T.dot(d_output) * learning_rate
    W_hidden += X.T.dot(d_hidden) * learning_rate

# testowanie
for i in range(4):
    hidden_layer_inpput = np.dot(X[i], W_hidden)
    hidden_layer_output = leaky_relu(hidden_layer_inpput)

    final_input = np.dot(hidden_layer_output, W_output)
    final_output = leaky_relu(final_input)

    print(f'Wejśie: {X[i]} -> Przewidywane wyjścia: {final_output[0]:.4f}')
    # print(f'Wejśie: {X[i]} -> Przewidywane wyjścia: {int(output[0] > 0.5):.4f}')
