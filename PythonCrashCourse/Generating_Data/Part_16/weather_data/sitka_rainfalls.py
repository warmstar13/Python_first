from pathlib import Path
import csv

import matplotlib.pyplot as plt
from datetime import datetime

path = Path(__file__).parent / "sitka_weather_2021_full.csv"

lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

for index, name in enumerate(header_row):
    print(index, name)

dates, rains = [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    current_rain = float(row[5])
    dates.append(current_date)
    rains.append(current_rain)


plt.style.use('seaborn')

fig, ax = plt.subplots(figsize=(16, 8))

ax.plot(dates, rains, color='red')

ax.set_title("Rains in sitka???", fontsize=20)
ax.set_xlabel("Dates", fontsize=30)
ax.set_ylabel("Water degree", fontsize=20)
ax.tick_params(labelsize=15)
fig.autofmt_xdate()


plt.show()