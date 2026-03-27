import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")

students = data["StudentID"]
math_scores = data["MathScore"]

plt.figure()
plt.step(students, math_scores, where='mid')

plt.xlabel("Student ID")
plt.ylabel("Math Score")
plt.title("Stair Chart of Math Scores")

plt.xticks(rotation=90)

plt.show()