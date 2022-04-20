import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 7, 1, 0]

title = "Bar graph"
xaxis = "X-Axis"
yaxis = "Y-Axis"

plt.title(title)
plt.xlabel(xaxis)
plt.ylabel(yaxis)

plt.bar(x, y)
plt.show()