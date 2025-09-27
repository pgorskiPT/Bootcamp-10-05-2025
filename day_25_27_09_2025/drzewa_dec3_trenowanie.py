import matplotlib.pyplot as plt
import numpy as np
from sklearn.tree import DecisionTreeClassifier, plot_tree

# uczenie nadzorowane
# [wiek, zarobki]
X = np.array([
    [25, 30],
    [40, 70],
    [35, 50],
    [50, 90],
    [20, 20],
])

# etykiety: 1 -> tak, 0 -> nie
y = np.array([0, 1, 1, 1, 0])

# budowa i trenowanie drzewa
tree = DecisionTreeClassifier(criterion='gini', max_depth=2)
tree.fit(X, y)

# predykcja
decision = tree.predict(np.array([[30, 40]])) # Pożyczka odrzucona
print("Pożyczka przyznana" if decision[0] == 1 else "Pożyczka odrzucona")

# wizualizacja drzewa
plt.figure(figsize=(8,5))
plot_tree(tree, feature_names=['wiek', "zarobki"],
          class_names=['odrzucona', 'przyznany'], filled=True)
plt.title("Drzewo decyzyjne: przyznawanie pożyczki")
plt.tight_layout()
plt.show()