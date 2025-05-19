import matplotlib.pyplot as plt

# Données de mémoire (RSS en kB)
scale_factors = [1e3, 1e6, 1e9]
operations = ['Addition', 'Soustraction', 'Multiplication', 'Division']

rss_kb = {
    'Addition': [138328, 138452, 138240],
    'Soustraction': [139036, 139052, 138876],
    'Multiplication': [168524, 168560, 168592],
    'Division': [148416, 148100, 146212]
}

# Conversion en MB (1 MB = 1024 kB)
rss_mb = {op: [val/1024 for val in rss_kb[op]] for op in operations}

markers = {'Addition': 'o', 'Soustraction': 's', 'Multiplication': '^', 'Division': 'd'}
colors = {'Division': 'red', 'Multiplication': 'orange', 'Addition': 'blue', 'Soustraction': 'green'}

# Création du graphique
plt.figure()
plt.xscale('log')
plt.grid(True, which='major', linestyle='--', linewidth=0.5)
for op in operations:
    plt.plot(scale_factors, rss_mb[op], marker=markers[op], color=colors[op], linestyle='-',
             label=op)

plt.xlabel('Facteur d\'échelle')
plt.ylabel('Maximum resident set size (MB)')
plt.title('RSS par opération et facteur d\'échelle (en MB)')
plt.legend()
plt.tight_layout()
plt.show()
