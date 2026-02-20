import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig, ax = plt.subplots()
data = []

def update(frame):
    ax.clear()
    data.append(np.random.randn())
    ax.hist(data, bins=20)
    ax.set_xlabel("Value")
    ax.set_ylabel("Frequency")
    ax.set_title("Dynamic Histogram")

ani = animation.FuncAnimation(fig, update, frames=range(100), interval=200)
plt.show()