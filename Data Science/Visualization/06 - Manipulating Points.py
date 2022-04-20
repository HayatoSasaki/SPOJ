import matplotlib.pyplot as plt

x = [1, 3, 5, 7, 9]
y = [2, 3, 7, 1, 0]
z = [1000, 500, 800, 300, 200]

title = "Scatterplot: Dispersion Graph"
xaxis = "X-Axis"
yaxis = "Y-Axis"

plt.title(title)
plt.xlabel(xaxis)
plt.ylabel(yaxis)

plt.scatter(x, y, label= "My stars", color="#FF3377", marker="*", s=z)
plt.plot(x, y, color="k", linestyle="--")
plt.legend()

plt.show()