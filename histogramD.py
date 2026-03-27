import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("data.csv")

plt.hist(data["MathScore"], bins=4, edgecolor='black')
plt.title('Static Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')

plt.show()