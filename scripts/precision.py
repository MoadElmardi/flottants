import matplotlib.pyplot as plt
import numpy as np

# Échelles utilisées
scales = [1e3, 1e6, 1e9]

# Erreurs absolues
abs_add = [0.0004068764687662707, 0.0000002982430187481455, 0.0000000003223467492929899]
abs_sub = [0.00034865621838836016, 0.00000029027399681691437, 0.0000000003435883244584659]
abs_mul = [0.0006434740706722341, 0.0000005689127919539238, 0.0000000005734222568998249]
abs_div = [0.4313254660287561, 0.4313254660287561, 0.4313254660287561]

# Erreurs relatives
rel_add = [0.00018919373392077194, 0.00000014560117190095577, 0.00000000013679153653248592]
rel_sub = [0.00046724666864017257, 0.00000027711296873082404, 0.0000000005139900047658411]
rel_mul = [0.0009161434081026343, 0.0000006887098756971314, 0.0000000007250872613337386]
rel_div = [0.32781721630865884, 0.32781721630865884, 0.32781721630865884]

# Création des sous-graphiques
fig, axs = plt.subplots(1, 2, figsize=(12, 5))

# Erreur absolue
axs[0].plot(scales, abs_add, 's-', color='blue', label='Addition')
axs[0].plot(scales, abs_sub, 'o-', color='green', label='Soustraction')
axs[0].plot(scales, abs_mul, '^-', color='orange', label='Multiplication')
axs[0].plot(scales, abs_div, 'd-', color='red', label='Division')
axs[0].set_xscale('log')
axs[0].set_yscale('log')
axs[0].set_xlabel("Échelle (scale)")
axs[0].set_ylabel("Erreur absolue moyenne")
axs[0].set_title("Erreur absolue moyenne selon l’échelle")
axs[0].grid(True, which="both", linestyle='--', linewidth=0.5)
axs[0].legend()

# Erreur relative
axs[1].plot(scales, rel_add, 's-', color='blue', label='Addition')
axs[1].plot(scales, rel_sub, 'o-', color='green', label='Soustraction')
axs[1].plot(scales, rel_mul, '^-', color='orange', label='Multiplication')
axs[1].plot(scales, rel_div, 'd-', color='red', label='Division')
axs[1].set_xscale('log')
axs[1].set_yscale('log')
axs[1].set_xlabel("Échelle (scale)")
axs[1].set_ylabel("Erreur relative moyenne")
axs[1].set_title("Erreur relative moyenne selon l’échelle")
axs[1].grid(True, which="both", linestyle='--', linewidth=0.5)
axs[1].legend()

plt.tight_layout()
plt.show()
