# Create Map of CWS (Citizen Weather Stations) in Berne for the night of 26-27 of June, 2019.

import pandas as pd
import geopandas as gpd
from shapely.geometry import Point, Polygon
import matplotlib.pyplot as plt
# Unofficial Windows Binaries for Python Extension Packages - https://www.lfd.uci.edu/~gohlke/pythonlibs/
# How to Install GEOS: https://gis.stackexchange.com/questions/38899/geos-and-shapely-installation-on-windows
from map_factory import create_cws_map


print("Creating geometry...")
df = pd.read_csv("../data/sample_data.csv")
geometry = [Point(xy) for xy in zip(df['lon'], df['lat'])]
fig, ax = plt.subplots(figsize=(15, 15))

print("Creating new geo_df...")
geo_df = gpd.GeoDataFrame(df, crs='epsg:4326', geometry=geometry)

# Remove columns where temperature is NaN
invalid_measurements = geo_df['ta_int'] != 'NAN'
geo_df = geo_df[invalid_measurements]

# Create data for hourly filtering:
column_22 = geo_df['time'] == '2019-06-26 22:00:00'
column_23 = geo_df['time'] == '2019-06-26 23:00:00'
column_00 = geo_df['time'] == '2019-06-27 00:00:00'
column_01 = geo_df['time'] == '2019-06-27 01:00:00'
column_02 = geo_df['time'] == '2019-06-27 02:00:00'
column_03 = geo_df['time'] == '2019-06-27 03:00:00'
column_04 = geo_df['time'] == '2019-06-27 04:00:00'
column_05 = geo_df['time'] == '2019-06-27 05:00:00'

geo_df_bokeh = geo_df.to_crs("EPSG:3785")  # https://spatialreference.org/ref/epsg/etrs89-etrs-laea/


# print("Reading basemap for Berne...")
# bern_map = gpd.read_file('../data/UrbanAtlas_Bern_reduced.shp') # It's in EPSG:3035 https://spatialreference.org/ref/epsg/etrs89-etrs-laea/

# print("Plotting with pyplot...")
# geo_df_alternative = geo_df.to_crs("EPSG:3035")
# bern_map.plot(ax=ax, alpha=0.4, color="grey")
# geo_df_alternative.plot(ax=ax, marker='*', color='green', markersize=5)
# plt.legend(prop={'size': 50})
# plt.show()


print("Creating hourly maps...")
create_cws_map(geo_df_bokeh[column_22], "26.06.19 - 22")
create_cws_map(geo_df_bokeh[column_23], "26.06.19 - 23")
create_cws_map(geo_df_bokeh[column_00], "27.06.19 - 00")
create_cws_map(geo_df_bokeh[column_01], "27.06.19 - 01")
create_cws_map(geo_df_bokeh[column_02], "27.06.19 - 02")
create_cws_map(geo_df_bokeh[column_03], "27.06.19 - 03")
create_cws_map(geo_df_bokeh[column_04], "27.06.19 - 04")
create_cws_map(geo_df_bokeh[column_05], "27.06.19 - 05")


print("Script finished.")

#The message attempts to be self explanatory. In order to connect real python callbacks to UI events, there has to be a real Python process running to execute the callback code. That process is the Bokeh server, and to use it you would run your code similar to: