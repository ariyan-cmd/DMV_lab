import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random

x = []
y = []

fig, ax = plt.subplots()

def update(frame):
    x.append(frame)
    y.append(random.randint(10, 30))

    ax.clear()
    ax.plot(x, y, marker='o')

    ax.set_xlabel("X values (Independent Variable)")
    ax.set_ylabel("Y values (Dependent Variable)")
    ax.set_title("Live Animated X-Y Plot")
    ax.grid(False)

ani = FuncAnimation(fig, update, interval=1000)

plt.show()