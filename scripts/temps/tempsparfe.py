import matplotlib.pyplot as plt

# Data for floating operations
scale_factors = [1e3, 1e6, 1e9]
times_sub_float = [1843.318, 1827.881, 1846.761]  # in ms
times_add_float = [1881.752, 1878.959, 1847.345]
times_mul_float = [14502.132, 14542.608, 14365.884]
times_div_float = [76862.485, 77630.935, 77440.680]

# Plot for floating-point operations
plt.figure()
plt.plot(scale_factors, times_sub_float, marker='o', color='green', label='Soustraction')
plt.plot(scale_factors, times_add_float, marker='o', color='blue', label='Addition')
plt.plot(scale_factors, times_mul_float, marker='o', color='orange', label='Multiplication')
plt.plot(scale_factors, times_div_float, marker='o', color='red', label='Division')
plt.xscale('log')
plt.xlabel("Facteur d'échelle")
plt.ylabel("Temps (ms)")
plt.title("Performances FheInt64 (Float)")
plt.grid()
plt.legend()
plt.tight_layout()
plt.show()

# Data for integer operations
ops_int = ['Soustraction', 'Addition', 'Multiplication', 'Division']
times_int = [1894.290, 1837.565, 14282.274, 72462.064]  # en ms

fig, ax = plt.subplots()
# on place la grille « en dessous » des artistes (barres)
ax.set_axisbelow(True)

# tracer la grille
ax.grid(True, which='major', linestyle='--', linewidth=0.5)

# dessiner les barres en zorder plus haut
ax.bar(ops_int, times_int, zorder=3)

ax.set_xlabel("Opération")
ax.set_ylabel("Temps (ms)")
ax.set_title("Performances FheUint64 (Entier)")

plt.tight_layout()
plt.show()
