import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

x = df['StudyHoursPerWeek']
y = df['ProjectScore']

plt.scatter(x, y)
plt.xlabel('Study Hours Per Week')
plt.ylabel('Project Score')
plt.title('Study Hours vs Project Score')
plt.show()