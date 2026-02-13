import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)

fig, axs = plt.subplots(2, 2)

# Plot 1
axs[0, 0].plot(x, np.sin(x))
axs[0, 0].set_title("Sine")

# Plot 2
axs[0, 1].plot(x, np.cos(x))
axs[0, 1].set_title("Cosine")

# Plot 3
axs[1, 0].scatter(x, np.sin(x))
axs[1, 0].set_title("Scatter")

# Plot 4
axs[1, 1].bar(['A','B','C'], [3,7,5])
axs[1, 1].set_title("Bar")

plt.tight_layout()
plt.show()
