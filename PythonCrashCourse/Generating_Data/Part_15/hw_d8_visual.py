from die import Die
import plotly.express as px

die_1 = Die(8)
die_2 = Die(8)

results = []

for roll_num in range(20000):
    sum = die_1.roll() + die_2.roll()
    results.append(sum)

frequencies = []
max_res = die_1.num_sides + die_2.num_sides
poss_res = range(2, max_res + 1)

for num in poss_res:
    frequency = results.count(num)
    frequencies.append(frequency)

title = "Throwing two D8 20000 times"
label = {"x":"result", "y":"frequency"}
fig = px.bar(x=poss_res, y=frequencies, title=title, labels=label)
fig.update_layout(xaxis_dtick=1)

fig.show()