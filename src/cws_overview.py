# Create Map of CWS (Citizen Weather Stations) in Bern for the night of 26-27 of June, 2019.

import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
from shapely.geometry import Point

from map_factory import create_cws_map

print("Creating geometry...")
df = pd.read_csv("../data/cws_bern_ta_level_o1_2019_Snippet_UTM.csv")

# Zip yields tuples, until a single input is exhausted. We need geometry for crs conversions.
geometry = [Point(xy) for xy in zip(df['lon'], df['lat'])]
fig, ax = plt.subplots(figsize=(15, 15))

print("Creating new geo dataframe...")
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

# Migrate to same CRS as OpenStreetMap
geo_df_bokeh = geo_df.to_crs("EPSG:3785")  # https://spatialreference.org/ref/epsg/etrs89-etrs-laea/

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
