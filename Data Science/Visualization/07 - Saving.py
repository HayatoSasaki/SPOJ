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

plt.scatter(x, y, label= "My Hexas", color="#000000", marker="h", s=z)
plt.plot(x, y, color="k", linestyle="--")
plt.legend()

# plt.savefig("graph1.png") | Save as .png
# plt.savefig("graph1.pdf") | Save as .pdf
plt.savefig("graph1.png", dpi=300)