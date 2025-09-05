import matplotlib.pyplot as plt

# Données
categories = ['Flottants\n(1e3)', 'Flottants\n(1e6)', 'Flottants\n(1e9)', 'Entiers']
times_sub = [1843.318, 1827.881, 1846.761, 1894.290]
times_add = [1881.752, 1878.959, 1847.345, 1837.565]
times_mul = [14502.132, 14542.608, 14365.884, 14282.274]
times_div = [76862.485, 77630.935, 77440.680, 72462.064]

# Conversion en minutes
times_sub_min = [t/60000 for t in times_sub]
times_add_min = [t/60000 for t in times_add]
times_mul_min = [t/60000 for t in times_mul]
times_div_min = [t/60000 for t in times_div]

# Position des points
x = range(len(categories))

# Création du graphique
plt.figure()
plt.plot(x, times_sub_min, marker='o', color='green', label='Soustraction')
plt.plot(x, times_add_min, marker='s', color='blue', label='Addition')
plt.plot(x, times_mul_min, marker='^', color='orange', label='Multiplication')
plt.plot(x, times_div_min, marker='d', color='red', label='Division')

# Configuration des axes
plt.xticks(x, categories)
plt.xlabel("Catégorie")
plt.ylabel("Temps (min)")
plt.title("Performances selon type et facteur d'échelle")
plt.legend()
plt.grid(linestyle='--', linewidth=0.5, alpha=0.7)
plt.tight_layout()
plt.show()
