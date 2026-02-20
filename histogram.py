import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(100)

plt.hist(data, bins=30)
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Static Histogram")
plt.show()