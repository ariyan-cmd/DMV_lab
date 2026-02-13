import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
categories = ['A', 'B', 'C', 'D', 'E']
bars = ax.bar(categories, np.zeros(5), color='orange')

ax.set_ylim(0, 20)
ax.set_title("Dynamic Bar Chart")

def update(frame):
    new_values = np.random.randint(1, 20, size=5)
    for bar, new_val in zip(bars, new_values):
        bar.set_height(new_val)
    return bars

ani = FuncAnimation(fig, update, frames=50, interval=500)

plt.show()
