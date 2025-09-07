# Symuluj 1000 scenariuszy inwestycyjnych dla portfela o początkowej wartości 10000 PLN
# przy średnim rocznym zwrocie 7% i odchyleniu standardowym 15%
# Oblicz wartośc portfela po 10 latach dla każdego scenariusza
# znajdż najlepszy , średni i najgorszy scenariusz
import numpy as np

initial_value = 10000
years = 10
annual_return = 0.07
annual_volaility = 0.15
simulations = 1000

np.random.seed(42)  # seed - zapewnia powtarzalnośc wyników

annual_growth_rates = np.random.normal(annual_return, annual_volaility, (years, simulations))
# Return the cumulative product of elements along a given axis.
values = initial_value * np.cumprod(1 + annual_growth_rates, axis=0)

# print(values)
final_values = values[-1]
# print(final_values)
print("Średnia wartość portfela po 10 latach:", np.mean(final_values))
print("Najlepszy scenariusz,  wartość portfela po 10 latach:", np.max(final_values))
print("NAjgorszy scenariusz, wartość portfela po 10 latach:", np.min(final_values))
# Średnia wartość portfela po 10 latach: 19619.038188903683
# Najlepszy scenariusz,  wartość portfela po 10 latach: 70912.47810765122
# NAjgorszy scenariusz, wartość portfela po 10 latach: 3710.4127579491196

# print(annual_growth_rates)
np.set_printoptions(threshold=np.inf, linewidth=150)
print(annual_growth_rates)
