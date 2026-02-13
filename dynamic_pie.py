import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

labels = ['A', 'B', 'C', 'D']

def update(frame):
    ax.clear()
    values = np.random.randint(10, 50, size=4)
    ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.set_title("Dynamic Pie Chart")

ani = FuncAnimation(fig, update, frames=50, interval=1000)

plt.show()
