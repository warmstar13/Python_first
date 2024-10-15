from pathlib import Path
import csv

import matplotlib.pyplot as plt
from datetime import datetime


path = Path(__file__).parent / "sitka_weather_2021_simple.csv"
lines = path.read_text().splitlines()

#print(lines)
reader = csv.reader(lines)
header_row = next(reader)
#print(header_row)

for index, column_header in enumerate(header_row):
    print(index, column_header)



dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    high = int(row[4])
    low = int(row[5])
    highs.append(high)
    lows.append(low)
    dates.append(current_date)

# print(highs)

plt.style.use('seaborn')

fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(dates, highs, color='red')
ax.plot(dates, lows, color='blue')
ax.fill_between(dates, lows, highs, facecolor='blue', alpha=0.1)

ax.set_title("Daily High(Low) Temperatures, 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()   # draws the dates diagonally
ax.set_ylabel("Temperature F", fontsize=16)
ax.tick_params(labelsize=16)

# manager = plt.get_current_fig_manager()
# manager.full_screen_toggle()

plt.show()