# perceptron - matematyczne odzwierciedlenie neuronu
# przyjmuje zestaw danych
# na podstawie danych wejsciowych ustala wagi i dodakowe przesunięcie taka
# by jak najbardziej przewidziany wynik był własciwy
# suma ważona z = x*w + b
# # funkcja aktywacji - funkcja ktora daaje wynik działąnia perceptronu
# # np funkcja skokowa wartości 0 lub 1
# # perceptron binarny
import numpy as np


class Perceptron:
    def __init__(self, learning_rate=0.1, epochs=10):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.weights = None
        self.bias = None

    def activation_function(self, x):
        return 1 if x >= 0 else 0  # funkcja skokowa

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        for _ in range(self.epochs):
            for i in range(n_samples):
                linear_output = np.dot(X[i], self.weights) + self.bias  # z = x*w + b
                y_predicted = self.activation_function(linear_output)

                update = self.learning_rate * (y[i] - y_predicted)
                self.weights += update * X[i]
                self.bias += update

    def set_fit(self):
        self.weights = np.array([0.2, 0.1])
        self.bias = -0.20000000000000004

    def predict(self, X):
        print(self.weights)
        print(self.bias)
        linear_output = np.dot(X, self.weights) + self.bias
        return np.array([self.activation_function(x) for x in linear_output])


# # AND
# # 0 and 0 = 0
# # 0 and 1 = 0
# # 1 and 0 = 0
# # 1 and 1 = 1

# dane treningowe
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 0, 0, 1])
print(X.dtype)  # int64

p = Perceptron(learning_rate=0.1, epochs=10)
p.fit(X, y)

# testowanie perceptronu
predictions = p.predict(X)
print("Przeiwdywane wyniki:", predictions)  # Przeiwdywane wyniki: [0 0 0 1]
