import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

df[['MathScore', 'PhysicsScore', 'ChemistryScore' ,'ProgrammingScore']].boxplot()

plt.xlabel('subject')
plt.ylabel('scores')
plt.title('Box plot of student scores')
plt.show()