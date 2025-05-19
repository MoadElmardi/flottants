import matplotlib.pyplot as plt
import numpy as np

# Données
scale_factors = [1e3, 1e6, 1e9]
ops = ['Division', 'Multiplication', 'Addition', 'Soustraction']

# Moyennes
power_means = {
    'Division': [60.0080136, 59.9768658, 60.2442898],
    'Multiplication': [61.5036358, 61.8148379, 62.5642319],
    'Addition': [43.7122469, 43.9312375, 43.8335770],
    'Soustraction': [43.8104136, 43.9519974, 44.1981029]
}
energy_means = {
    'Division': [4573.6718511471, 4568.7953162730, 4635.9508968823],
    'Multiplication': [871.700999769, 884.8768128836, 901.0198634132],
    'Addition': [80.1121603994, 80.0011118517, 79.7540191899],
    'Soustraction': [80.3064684779, 79.9223336783, 80.4059850525]
}

markers = {'Division': 'o', 'Multiplication': 's', 'Addition': '^', 'Soustraction': 'd'}
colors = {'Division': 'red', 'Multiplication': 'orange', 'Addition': 'blue', 'Soustraction': 'green'}

# 1) Courbes simples (sans barres d'erreur)
plt.figure()
plt.xscale('log')
plt.grid(True, which='major', linestyle='--', linewidth=0.5)
for op in ops:
    plt.plot(scale_factors, power_means[op], marker=markers[op], color=colors[op], linestyle='-', label=op)
plt.xlabel("Facteur d'échelle")
plt.ylabel("Puissance moyenne (W)")
plt.title("Puissance moyenne par facteur d'échelle")
plt.legend()
plt.tight_layout()
plt.show()

plt.figure()
plt.xscale('log')
plt.grid(True, which='major', linestyle='--', linewidth=0.5)
for op in ops:
    plt.plot(scale_factors, energy_means[op], marker=markers[op], color=colors[op], linestyle='-', label=op)
plt.xlabel("Facteur d'échelle")
plt.ylabel("Énergie moyenne (J)")
plt.title("Énergie moyenne par facteur d'échelle")
plt.legend()
plt.tight_layout()
plt.show()

# 2) Diagrammes en barres groupées
x = np.arange(len(scale_factors))
width = 0.2

plt.figure()
plt.grid(True, axis='y', linestyle='--', linewidth=0.5)
for i, op in enumerate(ops):
    plt.bar(x + (i-1.5)*width, power_means[op], color=colors[op], width=width, label=op)
plt.xticks(x, ['1e3','1e6','1e9'])
plt.xlabel("Facteur d'échelle")
plt.ylabel("Puissance moyenne (W)")
plt.title("Puissance moyenne par opération")
plt.legend()
plt.tight_layout()
plt.show()

plt.figure()
plt.grid(True, axis='y', linestyle='--', linewidth=0.5)
for i, op in enumerate(ops):
    plt.bar(x + (i-1.5)*width, energy_means[op], color=colors[op], width=width, label=op)
plt.xticks(x, ['1e3','1e6','1e9'])
plt.xlabel("Facteur d'échelle")
plt.ylabel("Énergie moyenne (J)")
plt.title("Énergie moyenne par opération")
plt.legend()
plt.tight_layout()
plt.show()
