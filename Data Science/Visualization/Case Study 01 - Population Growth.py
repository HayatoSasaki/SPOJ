import matplotlib.pyplot as plt

data = open('Data Science\Visualization\population_growth.csv').readlines()

x = []
y = []

for i in range(len(data)):
    if i != 0:
        linha = data[i].split(";")
        x.append(int(linha[0]))
        y.append(int(linha[1]))

title = "Population Growth 1980-2016"
xaxis = "Year"
yaxis = "Population in 100 millions"

plt.title(title)
plt.xlabel(xaxis)
plt.ylabel(yaxis)

plt.plot(x, y, color="k", linestyle="--") # Line Graph Version
plt.bar(x, y, color="#e4e4e4") # Bar Graph Version.

plt.show() # Show
#plt.savefig("Case Study 01 - Population Growth.png", dpi=300) # Save