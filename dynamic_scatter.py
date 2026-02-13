import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
sc = ax.scatter([], [])

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_title("Dynamic Scatter Plot")

def update(frame):
    x = np.random.rand(50)
    y = np.random.rand(50)
    sc.set_offsets(np.c_[x, y])
    return sc,

ani = FuncAnimation(fig, update, frames=50, interval=500)

plt.show()
