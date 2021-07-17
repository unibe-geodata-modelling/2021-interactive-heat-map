# Class to create maps based on dataframe with corresponding time filter

from bokeh.io import output_file, show
from bokeh.layouts import layout
from bokeh.models import HoverTool, Div
from bokeh.plotting import figure
from bokeh.tile_providers import get_provider  # IDE May complain that it can not find the reference, but code works.

from color_factory import filter_points_by_color


def create_cws_map(df, suffix):
    """Reads in a data-frame and exports a html file, containing a bokeh map, placed within the 'docu' folder.

    Parameters
    ----------
    df : dataframe
        A dataframe that must contain the following columns:
        - geometry
        - p_id
        - lon
        - lat
        - ta_int

    suffix : str
        A string that will be appended to the title of the plots as well as the html file-names.
    """

    tile_provider = get_provider(
        "CARTODBPOSITRON_RETINA")  # More Providers https://docs.bokeh.org/en/latest/docs/reference/tile_providers.html

    # Range bounds supplied in web mercator coordinates
    p = figure(x_range=(825000, 833000), y_range=(5933000, 5935000),
               x_axis_type="mercator", y_axis_type="mercator",  # Changes axis to a more legible input
               x_axis_label="Longitude", y_axis_label="Latitude",
               sizing_mode="stretch_both")
    p.add_tile(tile_provider)

    # Filter point sto be added by color
    p = filter_points_by_color(df, p)

    # Add hover tools as a means for interactivity
    my_hover = HoverTool()  # https://automating-gis-processes.github.io/2016/Lesson5-interactive-map-bokeh.html#adding-interactivity-to-the-map

    # Specify what parameters should be displayed when hovering
    my_hover.tooltips = [('Id', '@p_id'), ('Temperature [C]', '@ta_int'), ('Longitude', '@lon'), ('Latitude', '@lat')]
    p.add_tools(my_hover)

    # Creating divs to serve as additional information
    div_title = Div(
        align="center",
        text="<h1>Citizen Weather Stations: " + suffix + ":00</h1>",
        sizing_mode="stretch_both"
    )
    div_subtitle = Div(
        align="center",
        text="Blue: Below 22 °C. <br> Orange: Between 22 °C and 28 °C. <br> Red: Above 28 °C.",
        sizing_mode="stretch_both"
    )

    # Arrange all the bokeh elements in a layout
    layout_plot = layout([
        [div_title],
        [div_subtitle],
        [p]
    ])

    # Specify output location and name
    output_file("../docu/Bern-CWS-Map_" + suffix + ".html")

    # Shows the result in the default browser and saves the file
    show(layout_plot)
