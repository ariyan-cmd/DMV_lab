import numpy as np
import matplotlib.pyplot as plt

# Data
labels = ['A', 'B', 'C', 'D']
values = np.random.randint(10, 50, size=4)

# Plot
plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)

plt.title('Static Pie Chart Example')
plt.axis('equal')  # Makes circle perfectly round
plt.show()
