from pathlib import Path
import json

import plotly.express as px

path = Path(__file__).parent / "eq_data_1_day_m1.geojson"

content = path.read_text()
all_eq_data = json.loads(content)

all_eq_dicts = all_eq_data['features']
# print(len(all_eq_dicts))

mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict["properties"]["mag"]
    lon = eq_dict["geometry"]["coordinates"][0]
    lat = eq_dict["geometry"]["coordinates"][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

# print(mags[:10])
# print(lons[:5])
# print(lats[:5])

title = "Global earthquakes"
fig = px.scatter_geo(lat=lats, lon=lons, title=title)


fig.show()


# path = Path(__file__).parent / "readable_eq_data.geojson"
# readable_content = json.dumps(all_eq_data, indent=4)
# path.write_text(readable_content)