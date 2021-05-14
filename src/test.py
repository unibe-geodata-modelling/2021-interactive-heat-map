import data_reader
import matplotlib.pyplot as plt

import pandas as pd
from shapely.geometry import Point
import geopandas as gpd
from geopandas import GeoDataFrame


all_measurements = data_reader.get_content()

points = []
# for measurement in all_measurements:
#     print(measurement)


class Coordinates:
    def __init__(self, longitude, latitude):
        self._longitude = longitude
        self._latitude = latitude

    def longitude(self):
        return self._longitude

    def latitude(self):
        return self._latitude


coords = []
print("Start extracting lon, lat")
for date, measurement in all_measurements.items():
    coords.append(
            Coordinates(
                longitude=measurement['lon'],
                latitude=measurement['lat'],
            ),
    )

print("extracted lon, lat")
# Uncomment for testing
# print(coords)
x = []
y = []
for point in coords:
    x.append(point.longitude())
    y.append(point.latitude())
plt.scatter(x=x, y=y)
plt.show()

#TODO Use geopandas to plot as map, e.g.:
# https://stackoverflow.com/questions/53233228/plot-latitude-longitude-from-csv-in-python-3-6
# df = pd.read_csv("Long_Lats.csv", delimiter=',', skiprows=0, low_memory=False)
#
# geometry = [Point(xy) for xy in zip(df['Longitude'], df['Latitude'])]
# gdf = GeoDataFrame(df, geometry=geometry)
#
# #this is a simple map that goes with geopandas
# world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
# gdf.plot(ax=world.plot(figsize=(10, 6)), marker='o', color='red', markersize=15);


print("done")