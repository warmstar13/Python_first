from pathlib import Path
import csv

import matplotlib.pyplot as plt

path = Path(__file__).parent / "sitka_weather_07-2021_simple.csv"
lines = path.read_text().splitlines()

#print(lines)
reader = csv.reader(lines)
header_row = next(reader)
#print(header_row)

for index, column_header in enumerate(header_row):
    print(index, column_header)



highs = []
for row in reader:
    high = int(row[4])
    highs.append(high)

# print(highs)

plt.style.use('seaborn')

fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(highs, color='red')

ax.set_title("Daily High Temperatures, July 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel("Temperature F", fontsize=16)
ax.tick_params(labelsize=16)

# manager = plt.get_current_fig_manager()
# manager.full_screen_toggle()

plt.show()