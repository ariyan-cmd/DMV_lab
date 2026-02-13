import numpy as np
import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D', 'E']
values = np.random.randint(1, 20, size=5)

plt.bar(categories, values, color='skyblue')

plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Static Bar Chart Example')

plt.show()
