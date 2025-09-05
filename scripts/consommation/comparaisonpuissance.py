import matplotlib.pyplot as plt

# Données de puissance (W)
categories = ['Flottants\n(1e3)', 'Flottants\n(1e6)', 'Flottants\n(1e9)', 'Entiers']
power_add = [43.7122469, 43.9312375, 43.8335770, 43.9929]
power_sub = [43.8104136, 43.9519974, 44.1981029, 43.6820]
power_mul = [61.5036358, 61.8148379, 62.5642319, 62.6618]
power_div = [60.0080136, 59.9768658, 60.2442898, 59.1415]

x = range(len(categories))

plt.figure()
plt.plot(x, power_add, marker='s', color='blue', label='Addition')
plt.plot(x, power_sub, marker='o', color='green', label='Soustraction')
plt.plot(x, power_mul, marker='^', color='orange', label='Multiplication')
plt.plot(x, power_div, marker='d', color='red', label='Division')

plt.xticks(x, categories)
plt.xlabel("Catégorie")
plt.ylabel("Puissance nette moyenne (W)")
plt.title("Comparaison des puissances moyennes entre l'utilisation des flottants et des entiers")
plt.legend()
plt.grid(linestyle='--', linewidth=0.5, alpha=0.7)

# Faire commencer l'axe Y à 0
max_power = max(power_mul + power_div + power_add + power_sub)
plt.ylim(0, max_power + 5)

plt.tight_layout()
plt.show()
