import matplotlib.pyplot as plt

x = [1, 2, 5]
y = [2, 3, 7]

title = "Line Graph"
xaxis = "X-Axis"
yaxis = "Y-Axis"

plt.title(title)
plt.xlabel(xaxis)
plt.ylabel(yaxis)

plt.plot(x, y)
plt.show()