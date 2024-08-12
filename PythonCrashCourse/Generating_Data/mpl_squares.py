import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

# plt.style.use("_mpl-gallery")
plt.style.use("seaborn")    
fig, ax = plt.subplots()
ax.scatter(2, 5, s=200)
ax.scatter(input_values, squares, s=100)
ax.plot(input_values, squares, linewidth=3)

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=12)
ax.set_ylabel("Square of Value", fontsize=18)

ax.tick_params(labelsize=12)


plt.show()  