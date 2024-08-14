import matplotlib.pyplot as plt
import plotly.express as px

from random_walk import RandomWalk

while True:
    rw = RandomWalk(5000)
    rw.fill_walk()

    plt.style.use("classic")
    fig, ax = plt.subplots(figsize=(10, 6), dpi=128)

    point_numbers = range(rw.num_points)
    # ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Greys, edgecolors='none', s=1)
    ax.plot(rw.x_values, rw.y_values, color="black")
    ax.scatter(0, 0, c="green", edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    ax.set_aspect("equal")

    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Do you want to continue?: (y/n)")
    if keep_running == 'n':
        break