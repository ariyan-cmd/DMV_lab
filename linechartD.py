import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("data.csv")

x = data["StudentID"]
y = data["MathScore"]

plt.plot(x, y, marker='o', linestyle='-', color='b')
plt.title('Math Scores of Students')

plt.xticks(rotation=90)

plt.show()