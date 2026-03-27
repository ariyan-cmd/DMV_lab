import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("data.csv")

labels = ["Maths","Physics","Chemistry","Programming"]
tmp_vals = data["MathScore"].mean(), data["PhysicsScore"].mean(), data["ChemistryScore"].mean(), data["ProgrammingScore"].mean()
values = tmp_vals

plt.pie(values, labels=labels, autopct='%1.1f%%')
plt.title('Mean Score Distribution')

plt.show()