from pathlib import Path
import csv

import matplotlib.pyplot as plt
from datetime import datetime


path = Path(__file__).parent / "death_valley_2021_simple.csv"
lines = path.read_text().splitlines()

#print(lines)
reader = csv.reader(lines)
header_row = next(reader)
#print(header_row)

# for index, column_header in enumerate(header_row):
#     print(index, column_header)



death_dates, death_highs = [], []
for row in reader:
    try:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[3])
    except ValueError:
        print(f"{current_date} is missing")
    else:
        death_highs.append(high)
        death_dates.append(current_date)
########################################################################


path = Path(__file__).parent / "sitka_weather_2021_simple.csv"
lines = path.read_text().splitlines()

#print(lines)
reader = csv.reader(lines)
header_row = next(reader)
#print(header_row)

# for index, column_header in enumerate(header_row):
#     print(index, column_header)



dates, highs = [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    high = int(row[4])
    highs.append(high)
    dates.append(current_date)

# print(highs)

# now making connection between 2 datasets

n, m = 0, 0
final_high, final_death_high, final_date = [], [], []
while n < len(dates) and m < len(death_dates):
    if dates[n] < death_dates[m]:
        n += 1
    elif dates[n] > death_dates[m]:
        m += 1
    else:
        final_high.append(highs[n])
        final_death_high.append(death_highs[m])
        final_date.append(dates[n])
        n += 1
        m += 1


# printing the diagramms

plt.style.use('seaborn')

fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(final_date, final_high, color='red')
ax.plot(final_date, final_death_high, color='blue')
ax.fill_between(final_date, final_high, final_death_high, facecolor='blue', alpha=0.1)

ax.set_title("Daily High Temperatures, 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()   # draws the dates diagonally
ax.set_ylabel("Temperature F", fontsize=16)
ax.tick_params(labelsize=16)

# manager = plt.get_current_fig_manager()
# manager.full_screen_toggle()

plt.show()