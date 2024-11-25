import matplotlib.pyplot as plt
from pathlib import Path

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=20)
# ax.scatter(x_values, y_values, color="blue", s=10)
# ax.plot(x_values, y_values)

ax.axis([0, 1100, 0, 1100000])
ax.ticklabel_format(style="plain")

# plt.show()

path = Path(__file__).parent / "squares_plot.png"
plt.savefig(path, bbox_inches="tight")