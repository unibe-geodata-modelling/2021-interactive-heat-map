from bokeh.io import save
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, output_file, show
from bokeh.tile_providers import get_provider
# import data_reader
import matplotlib.pyplot as plt
from bokeh.models import HoverTool
import pandas as pd
# import descartes
import geopandas as gpd
from shapely.geometry import Point, Polygon
from geopandas import GeoDataFrame
import matplotlib.pyplot as plt
import hvplot.pandas
from geopandas_view import view as vw
import folium #https://anitagraser.com/2019/10/31/interactive-plots-for-geopandas-geodataframe-of-linestrings/
from IPython.core.display import display, HTML

#How to Install GEOS: https://gis.stackexchange.com/questions/38899/geos-and-shapely-installation-on-windows

# all_measurements = data_reader.get_content()

# points = []
# for measurement in all_measurements:
#     print(measurement)


####
# class Coordinates:
#     def __init__(self, longitude, latitude):
#         self._longitude = longitude
#         self._latitude = latitude
#
#     def longitude(self):
#         return self._longitude
#
#     def latitude(self):
#         return self._latitude

# coords = []
# print("Start extracting lon, lat")
# for date, measurement in all_measurements.items():
#     coords.append(
#             Coordinates(
#                 longitude=float(measurement['lon']),
#                 latitude=float(measurement['lat']),
#             ),
#     )


print("Reading basemap for Berne...")
bern_map = gpd.read_file('../data/UrbanAtlas_Bern_reduced.shp')
#The file uses the EPSG:3035 https://spatialreference.org/ref/epsg/etrs89-etrs-laea/


print("Creating geometry...")
df = pd.read_csv("../data/sample_data.csv")
geometry = [Point(xy) for xy in zip(df['lon'], df['lat'])]
fig, ax = plt.subplots(figsize=(15, 15))

print("Creating new geo_df...")
geo_df = gpd.GeoDataFrame(df, crs='epsg:4326', geometry=geometry)
geo_df_1 = geo_df.to_crs("EPSG:3035")

print("Plotting...")
# bern_map.plot(ax=ax, alpha=0.4, color="grey")
# geo_df_1.plot(ax=ax, marker='*', color='green', markersize=5)
# plt.legend(prop={'size': 50})
# plt.show()

# TODO Set to Switzerland standard, mouse-over text of loggers, verify that locations are correct
print("Setting up Bokeh...") # Source https://docs.bokeh.org/en/latest/docs/user_guide/geo.html




# p.scatter(x=df['lon'], y=df['lat'], source=source)

geo_df_bokeh = geo_df.to_crs("EPSG:3785") # https://spatialreference.org/ref/epsg/etrs89-etrs-laea/

# create a Python dict as the basis of your ColumnDataSource
data = {'x_values': geo_df_bokeh['geometry'].x,
        'y_values': geo_df_bokeh['geometry'].y,
        'p_id': geo_df_bokeh['p_id'],
        'ta_int': geo_df_bokeh['ta_int']}

# create a ColumnDataSource by passing the dict
source = ColumnDataSource(data=data)

print("Rendering Bokeh Map...")
tile_provider = get_provider("CARTODBPOSITRON_RETINA") #Many Provider Variants https://docs.bokeh.org/en/latest/docs/reference/tile_providers.html

# range bounds supplied in web mercator coordinates
p = figure(x_range=(825000, 833000), y_range=(5933000, 5935000),
           x_axis_type="mercator", y_axis_type="mercator", # Notice that passing x_axis_type="mercator" and y_axis_type="mercator" to figure generates axes with latitude and longitude labels, instead of raw Web Mercator coordinates.
           x_axis_label="Longitude", y_axis_label="Latitude")
p.add_tile(tile_provider)
p.circle(x='x_values', y='y_values', source=source)

my_hover = HoverTool() # https://automating-gis-processes.github.io/2016/Lesson5-interactive-map-bokeh.html#adding-interactivity-to-the-map
my_hover.tooltips = [('pid of Loggers', '@p_id'), ('Temp', '@ta_int')]
p.add_tools(my_hover)


output_file("Bern-Map.html")
show(p)


####
# print(gpd.datasets.available)
# world = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
# world.plot(figsize=(12,8))
# vw(world)
# plt.show()

# TODO Make points interactable
# TODO Display data on points
# TODO Get working with full dataset
#TODO Use geopandas to plot as map, e.g.:
# https://stackoverflow.com/questions/53233228/plot-latitude-longitude-from-csv-in-python-3-6#

# Simple Geoplot plotting: https://hub.gke2.mybinder.org/user/geopandas-geopandas-tw1klifg/lab/tree/doc/source/gallery/plotting_with_geoplot.ipynb
#Jupyter Notebook alternative, not quite what I want: https://towardsdatascience.com/how-to-produce-interactive-matplotlib-plots-in-jupyter-environment-1e4329d71651

# !!! Interesting alternative? https://lets-plot.org/#geospatial

print("done")