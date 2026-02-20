import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

fig, ax = plt.subplots()
x_data, y_data = [], []
line, = ax.plot([], [])

def update(frame):
    x_data.append(frame)
    y_data.append(random.randint(0, 10))
    line.set_data(x_data, y_data)
    ax.relim()
    ax.autoscale_view()
    return line,

ani = animation.FuncAnimation(fig, update, frames=range(50), interval=500)
plt.show()