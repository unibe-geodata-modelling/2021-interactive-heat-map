# import data_reader
import matplotlib.pyplot as plt

import pandas as pd
# import descartes
import geopandas as gpd
from shapely.geometry import Point, Polygon
from geopandas import GeoDataFrame
import matplotlib.pyplot as plt
# all_measurements = data_reader.get_content()

# points = []
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


# coords = []
# print("Start extracting lon, lat")
# for date, measurement in all_measurements.items():
#     coords.append(
#             Coordinates(
#                 longitude=float(measurement['lon']),
#                 latitude=float(measurement['lat']),
#             ),
#     )
# print("extracted lon, lat")
# x = []
# y = []
# for point in coords:
#     x.append(point.longitude())
#     y.append(point.latitude())
# plt.scatter(x=x, y=y)
# plt.show()

print("Reading basemap for Berne...")
bern_map = gpd.read_file('../data/UrbanAtlas_Bern_reduced.shp')
#The file uses the EPSG:3035 https://spatialreference.org/ref/epsg/etrs89-etrs-laea/
# fig,ax = plt.subplots(figsize = (15,15))
# bern_map.plot(ax = ax)

print("Creating geometry...")
df = pd.read_csv("../data/sample_data.csv")
geometry = [Point(xy) for xy in zip(df['lon'], df['lat'])]
print("Creating new geo_df...")
geo_df = gpd.GeoDataFrame(df, crs='epsg:4326', geometry=geometry)
geo_df = geo_df.to_crs("EPSG:3035")

print("Plotting...")
fig, ax = plt.subplots(figsize=(15, 15))
bern_map.plot(ax=ax, alpha=0.4,color="grey")
geo_df.plot(ax=ax, marker='*', color='green', markersize=5)
# plt.legend(prop={'size': 50})
plt.show()


print("done")

# TODO Use basemap of Berne
# TODO Make points interactable
# TODO Display data on points
# TODO Get working with full dataset
# TODO what subset of fulldataset do we want?
#TODO Use geopandas to plot as map, e.g.:
# https://stackoverflow.com/questions/53233228/plot-latitude-longitude-from-csv-in-python-3-6#
# #this is a simple map that goes with geopandas
# world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
# gdf.plot(ax=world.plot(figsize=(10, 6)), marker='o', color='red', markersize=15);