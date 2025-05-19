import matplotlib.pyplot as plt

# Données initiales en kB
mem_add_kb = [138328, 138452, 138240, 138288]
mem_sub_kb = [139036, 139052, 138876, 139232]
mem_mul_kb = [168524, 168560, 168592, 168616]
mem_div_kb = [148476, 147832, 148672, 146332]


# Conversion en MB (divisé par 1024)
mem_add = [x / 1024 for x in mem_add_kb]
mem_sub = [x / 1024 for x in mem_sub_kb]
mem_mul = [x / 1024 for x in mem_mul_kb]
mem_div = [x / 1024 for x in mem_div_kb]

categories = ['Flottants\n(1e3)', 'Flottants\n(1e6)', 'Flottants\n(1e9)', 'Entiers']
x = range(len(categories))

plt.figure()
plt.plot(x, mem_add, marker='s', color='blue', label='Addition')
plt.plot(x, mem_sub, marker='o', color='green', label='Soustraction')
plt.plot(x, mem_mul, marker='^', color='orange', label='Multiplication')
plt.plot(x, mem_div, marker='d', color='red', label='Division')

plt.xticks(x, categories)
plt.xlabel("Catégorie")
plt.ylabel("Usage mémoire (MB)")
plt.title("Compraison des consommations en mémoire entre l'utilisation des flottants et des entiers")
plt.legend()
plt.grid(linestyle='--', linewidth=0.5, alpha=0.7)
# Faire commencer l'axe Y à 0
plt.ylim(0, max(mem_mul) + 10)
plt.tight_layout()
plt.show()
