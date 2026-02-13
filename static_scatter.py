import numpy as np
import matplotlib.pyplot as plt

# Generate random data
x = np.random.rand(50)
y = np.random.rand(50)

# Create scatter plot
plt.scatter(x, y, color='blue')

plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Static Scatter Plot Example")

plt.show()
