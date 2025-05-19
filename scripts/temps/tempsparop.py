import matplotlib.pyplot as plt

# Data
operations = [
    "Chiffrement", "Génération des clés", "Addition", "Soustraction",
    "Multiplication", "Division", "ET binaire", "OU binaire", "XOR binaire",
    "Égalité", "Inégalité", "Supérieur strict", "Supérieur ou égal", "Déchiffrement"
]

# Times for scale 1e3 (in original units)
times_1e3 = [
    3.535171,    # ms
    1.094957687 * 1000,  # s -> ms
    782.65927,   # ms
    762.669487,  # ms
    13.031773567 * 1000, # s -> ms
    74.999825657 * 1000, # s -> ms
    226.110589,  # ms
    228.170855,  # ms
    226.719395,  # ms
    349.682782,  # ms
    349.317717,  # ms
    414.95611,   # ms
    411.9551,    # ms
    0.071316     # µs -> ms (71.316 µs = 0.071316 ms)
]

# Times for scale 1e6 (in original units)
times_1e6 = [
    3.619915,    # ms
    1.08326463 * 1000,  # s -> ms
    814.207712,  # ms
    801.113175,  # ms
    14.055032123 * 1000, # s -> ms
    79.121153683 * 1000, # s -> ms
    241.049094,  # ms
    242.838415,  # ms
    241.592229,  # ms
    370.338026,  # ms
    366.521332,  # ms
    434.053627,  # ms
    432.027594,  # ms
    0.071877     # µs -> ms (71.877 µs = 0.071877 ms)
]

# Plotting
x = range(len(operations))
plt.figure(figsize=(12, 6))
plt.bar([i - 0.2 for i in x], times_1e3, width=0.4, label="Échelle 1e3")
plt.bar([i + 0.2 for i in x], times_1e6, width=0.4, label="Échelle 1e6")
plt.xticks(x, operations, rotation=45, ha="right")
plt.ylabel("Temps (ms)")
plt.title("Comparaison des performances des opérations homomorphes")
plt.grid()
plt.legend()
plt.tight_layout()
plt.show()
