import plotly.express as px

from random_walk import RandomWalk

rw = RandomWalk(5000)
rw.fill_walk()

fig = px.scatter(x=rw.x_values, y=rw.y_values)

fig.show()