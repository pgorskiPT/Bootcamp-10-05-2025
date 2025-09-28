import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_derivative(x):
    return x * (1 - x)


# dane
# liczba końćzyn, sierść, pióra, waga, ogon
X = np.array([
    [4, 1, 0, 4, 1],  # kot
    [4, 1, 0, 20, 1],  # pies
    [2, 0, 1, 1.5, 0],  # kura
    [4, 1, 0, 5, 1],  # kot
    [4, 1, 0, 25, 1],  # pies
    [2, 0, 1, 2, 0],  # kura
])

y = np.array([
    [1, 0, 0],  # kot
    [0, 1, 0],  # pies
    [0, 0, 1],  # kura
    [1, 0, 0],  # kot
    [0, 1, 0],  # pies
    [0, 0, 1],  # kura
])

# stabilizacja danych
# w celu poprawy szybkości nauki
# min-max
X = X / np.max(X, axis=0)

# ustawienia modelu
input_neurons = X.shape[1]  # 5 neuronów
hidden_neurons = 4  # 4 neurony
output_neurons = y.shape[1]  # 3 wyjscia
learning_rate = 0.5
epochs = 10000

W_input_hidden = np.random.uniform(-1, 1, (input_neurons, hidden_neurons))
W_hidden_output = np.random.uniform(-1, 1, (hidden_neurons, output_neurons))
