from bokeh.layouts import layout
from bokeh.models import ColumnDataSource, Dropdown, RadioButtonGroup, Div
from bokeh.plotting import figure, output_file, show
from bokeh.tile_providers import get_provider
from bokeh.models import HoverTool
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point, Polygon
import matplotlib.pyplot as plt
# Unofficial Windows Binaries for Python Extension Packages - https://www.lfd.uci.edu/~gohlke/pythonlibs/
# How to Install GEOS: https://gis.stackexchange.com/questions/38899/geos-and-shapely-installation-on-windows


print("Reading basemap for Berne...")
bern_map = gpd.read_file('../data/UrbanAtlas_Bern_reduced.shp') # It's in EPSG:3035 https://spatialreference.org/ref/epsg/etrs89-etrs-laea/

print("Creating geometry...")
df = pd.read_csv("../data/sample_data.csv")
geometry = [Point(xy) for xy in zip(df['lon'], df['lat'])]
fig, ax = plt.subplots(figsize=(15, 15))

print("Creating new geo_df...")
geo_df = gpd.GeoDataFrame(df, crs='epsg:4326', geometry=geometry)
geo_df_bokeh = geo_df.to_crs("EPSG:3785")  # https://spatialreference.org/ref/epsg/etrs89-etrs-laea/

geo_df_alternative = geo_df.to_crs("EPSG:3035")

# print("Plotting with pyplot...")
# bern_map.plot(ax=ax, alpha=0.4, color="grey")
# geo_df_alternative.plot(ax=ax, marker='*', color='green', markersize=5)
# plt.legend(prop={'size': 50})
# plt.show()

print("Setting up Bokeh...")  # Source https://docs.bokeh.org/en/latest/docs/user_guide/geo.html

# create a Python dict as the basis of your ColumnDataSource
data = {'x_values': geo_df_bokeh['geometry'].x,
        'y_values': geo_df_bokeh['geometry'].y,
        'p_id': geo_df_bokeh['p_id'],
        'ta_int': geo_df_bokeh['ta_int']}

# create a ColumnDataSource by passing the dict
source = ColumnDataSource(data=data)

print("Rendering Bokeh Map...")
tile_provider = get_provider("CARTODBPOSITRON_RETINA")  # Many Provider Variants https://docs.bokeh.org/en/latest/docs/reference/tile_providers.html

# range bounds supplied in web mercator coordinates
p = figure(x_range=(825000, 833000), y_range=(5933000, 5935000),
           x_axis_type="mercator", y_axis_type="mercator",  # Notice that passing x_axis_type="mercator" and y_axis_type="mercator" to figure generates axes with latitude and longitude labels, instead of raw Web Mercator coordinates.
           x_axis_label="Longitude", y_axis_label="Latitude",
           sizing_mode="stretch_both")
p.add_tile(tile_provider)
p.circle(x='x_values', y='y_values', source=source)

my_hover = HoverTool()  # https://automating-gis-processes.github.io/2016/Lesson5-interactive-map-bokeh.html#adding-interactivity-to-the-map
my_hover.tooltips = [('pid of Loggers', '@p_id'), ('Temp', '@ta_int')]
p.add_tools(my_hover)

div = Div(
    align="center",
    text="""
        <h1>Low-Cost Measurement Network in Bern:</h1>
        """,
    sizing_mode="stretch_both"
)

# LABELS = ["2019-06-26 12:00:00", "2019-06-26 13:00:00", "2019-06-26 14:00:00", "2019-06-26 15:00:00",
#           "2019-06-26 16:00:00", "2019-06-26 17:00:00", "2019-06-26 18:00:00", "2019-06-26 19:00:00",
#           "2019-06-26 20:00:00", "2019-06-26 21:00:00", "2019-06-26 22:00:00", "2019-06-26 23:00:00", ]
# radio_button_group = RadioButtonGroup(labels=LABELS, active=0)
# radio_button_group.js_on_click(CustomJS(code="""
#     console.log('radio_button_group: active=' + this.active, this.toString())
# """))

menu = [("26.06.19 12:00", "2019-06-26 12:00:00"), ("26.06.19 13:00", "2019-06-26 13:00:00"),
        ("26.06.19 14:00", "2019-06-26 14:00:00"), ("26.06.19 15:00", "2019-06-26 15:00:00"),
        ("26.06.19 16:00", "2019-06-26 16:00:00"), ("26.06.19 17:00", "2019-06-26 17:00:00"),
        ("26.06.19 18:00", "2019-06-26 18:00:00"), ("26.06.19 19:00", "2019-06-26 19:00:00"),
        ("26.06.19 20:00", "2019-06-26 20:00:00"), ("26.06.19 21:00", "2019-06-26 21:00:00"),
        ("26.06.19 22:00", "2019-06-26 22:00:00"), ("26.06.19 23:00", "2019-06-26 23:00:00"), ]

dropdown = Dropdown(label="Select the time you wish to display", #https://docs.bokeh.org/en/latest/docs/user_guide/interaction/widgets.html#userguide-interaction-widgets
                    align="center",
                    button_type="primary",
                    menu=menu,
                    sizing_mode="stretch_width"
                    )

layout = layout([
    [div],
    # [radio_button_group],
    [p],
    [dropdown],
])

output_file("Bern-Map.html")
show(layout)

# TODO Get working with full dataset

print("done")

# Make graphs for only the fitting time, orient yourself with gif
# Create graph Factory function
# Keep dropdown as variant that only works with js and explain the drawbacks of only using python

#The message attempts to be self explanatory. In order to connect real python callbacks to UI events, there has to be a real Python process running to execute the callback code. That process is the Bokeh server, and to use it you would run your code similar to: