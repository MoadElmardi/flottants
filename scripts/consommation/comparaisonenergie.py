import matplotlib.pyplot as plt

# Données d'énergie en J
energy_add = [80.1121603994, 80.0011118517, 79.7540191899, 80.6018]
energy_sub = [80.3064684779, 79.9223336783, 80.4059850525, 79.8619891497]
energy_mul = [871.700999769, 884.8768128836, 901.0198634132, 897.0712]
energy_div = [4573.6718511471, 4568.795316273, 4635.9508968823, 4262.2348]

# Conversion en kJ
energy_add_kj = [e / 1000 for e in energy_add]
energy_sub_kj = [e / 1000 for e in energy_sub]
energy_mul_kj = [e / 1000 for e in energy_mul]
energy_div_kj = [e / 1000 for e in energy_div]

categories = ['Flottants\n(1e3)', 'Flottants\n(1e6)', 'Flottants\n(1e9)', 'Entiers']
x = range(len(categories))

plt.figure()
plt.plot(x, energy_add_kj, marker='s', color='blue', label='Addition')
plt.plot(x, energy_sub_kj, marker='o', color='green', label='Soustraction')
plt.plot(x, energy_mul_kj, marker='^', color='orange', label='Multiplication')
plt.plot(x, energy_div_kj, marker='d', color='red', label='Division')

plt.xticks(x, categories)
plt.xlabel("Catégorie")
plt.ylabel("Énergie nette (kJ)")
plt.title("Comparaison des énergies consommées entre l'utilisation des flottants et des entiers")
plt.legend()
plt.grid(linestyle='--', linewidth=0.5, alpha=0.7)
plt.ylim(0, max(energy_div_kj) * 1.1)

plt.tight_layout()
plt.show()
