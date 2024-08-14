from die import Die
import plotly.express as px
from pathlib import Path

die_1 = Die()
die_2 = Die()

results = []

for roll_num in range(10000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# print(results)

frequencies = []
max_res = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_res + 1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

title = "Diagram of rolling dice 10000 times"
labels = {"x": "result", "y": "frequency of result"}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.update_layout(xaxis_dtick=1)

# fig.show()
path = Path(__file__).parent / "dice_visual_d6.html"
fig.write_html(path)