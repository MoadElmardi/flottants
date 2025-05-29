import matplotlib.pyplot as plt

# Données extraites
scales = [1e3, 1e6, 1e9]

# Erreurs absolues moyennes
abs_errors = {
    "Addition": [0.0003887313854319019, 0.00000034469867861652847, 0.00000000035721152702450353],
    "Soustraction": [0.0003065166711538525, 0.0000003472445560415149, 0.00000000032378111525233067],
    "Multiplication": [2446173.344767191, 2448615521.155403, 4536246380.31153],
    "Division": [2.729985919266952, 2.732283619266953, 2.7322859169669527]
}

# Erreurs relatives moyennes
rel_errors = {
    "Addition": [0.0000441811114794933, 0.000000023223350555323676, 0.000000000034627645086557793],
    "Soustraction": [0.000010184075981104356, 0.00000002125541434336404, 0.000000000022255931414194978],
    "Multiplication": [999.0041703264412, 999998.9943715902, 5931660.89715941],
    "Division": [0.9995989054301666, 0.99999959890543, 0.9999999995989053]
}

colors = {
    "Addition": "blue",
    "Soustraction": "green",
    "Multiplication": "red",
    "Division": "orange"
}

# Création des graphiques
fig1, ax1 = plt.subplots()
for op, values in abs_errors.items():
    ax1.plot(scales, values, marker='o', label=op, color=colors[op])
ax1.set_xscale('log')
ax1.set_yscale('log')
ax1.set_xlabel("Échelle (scale)")
ax1.set_ylabel("Erreur absolue moyenne")
ax1.set_title("Erreur absolue moyenne selon l'échelle")
ax1.legend()
ax1.grid(True)

fig2, ax2 = plt.subplots()
for op, values in rel_errors.items():
    ax2.plot(scales, values, marker='o', label=op, color=colors[op])
ax2.set_xscale('log')
ax2.set_yscale('log')
ax2.set_xlabel("Échelle (scale)")
ax2.set_ylabel("Erreur relative moyenne")
ax2.set_title("Erreur relative moyenne selon l'échelle")
ax2.legend()
ax2.grid(True)

plt.tight_layout()
plt.show()
