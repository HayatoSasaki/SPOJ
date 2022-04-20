import matplotlib.pyplot as plt
import random

vector = [random.randint(0,50) for i in range(100)]

plt.title("Boxplot")

plt.boxplot(vector)
plt.show()