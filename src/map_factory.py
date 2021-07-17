# Class to create maps based on dataframe with corresponding time filter
from bokeh.io import output_file, show
from bokeh.layouts import layout
from bokeh.models import ColumnDataSource, HoverTool, Div, Dropdown, RadioButtonGroup
from bokeh.plotting import figure
from bokeh.tile_providers import get_provider

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


    print("Rendering Bokeh Map...")
    tile_provider = get_provider(
        "CARTODBPOSITRON_RETINA")  # Many Provider Variants https://docs.bokeh.org/en/latest/docs/reference/tile_providers.html

    # range bounds supplied in web mercator coordinates
    p = figure(x_range=(825000, 833000), y_range=(5933000, 5935000),
               x_axis_type="mercator", y_axis_type="mercator",
               x_axis_label="Longitude", y_axis_label="Latitude",
               sizing_mode="stretch_both")
    p.add_tile(tile_provider)

    p = filter_points_by_color(df, p)

    my_hover = HoverTool()  # https://automating-gis-processes.github.io/2016/Lesson5-interactive-map-bokeh.html#adding-interactivity-to-the-map
    my_hover.tooltips = [('Id', '@p_id'), ('Temperature [C]', '@ta_int'), ('Longitude', '@lon'), ('Latitude', '@lat')]
    p.add_tools(my_hover)

    div = Div(
        align="center",
        text="<h1>Citizen Weather Stations: " + suffix + ":00</h1>",
        sizing_mode="stretch_both"
    )

    layout_plot = layout([
        [div],
        [p]
    ])

    output_file("../docu/Bern-CWS-Map_" + suffix + ".html")
    show(layout_plot)

    # LABELS = ["2019-06-26 12:00:00", "2019-06-26 13:00:00", "2019-06-26 14:00:00", "2019-06-26 15:00:00",
    #           "2019-06-26 16:00:00", "2019-06-26 17:00:00", "2019-06-26 18:00:00", "2019-06-26 19:00:00",
    #           "2019-06-26 20:00:00", "2019-06-26 21:00:00", "2019-06-26 22:00:00", "2019-06-26 23:00:00", ]
    # radio_button_group = RadioButtonGroup(labels=LABELS, active=0)
    # radio_button_group.js_on_click(CustomJS(code="""
    #     console.log('radio_button_group: active=' + this.active, this.toString())
    # """))

    # menu = [("26.06.19 12:00", "2019-06-26 12:00:00"), ("26.06.19 13:00", "2019-06-26 13:00:00"),
    #         ("26.06.19 14:00", "2019-06-26 14:00:00"), ("26.06.19 15:00", "2019-06-26 15:00:00"),
    #         ("26.06.19 16:00", "2019-06-26 16:00:00"), ("26.06.19 17:00", "2019-06-26 17:00:00"),
    #         ("26.06.19 18:00", "2019-06-26 18:00:00"), ("26.06.19 19:00", "2019-06-26 19:00:00"),
    #         ("26.06.19 20:00", "2019-06-26 20:00:00"), ("26.06.19 21:00", "2019-06-26 21:00:00"),
    #         ("26.06.19 22:00", "2019-06-26 22:00:00"), ("26.06.19 23:00", "2019-06-26 23:00:00"), ]
    #
    # dropdown = Dropdown(label="Select the time you wish to display", #https://docs.bokeh.org/en/latest/docs/user_guide/interaction/widgets.html#userguide-interaction-widgets
    #                     align="center", button_type="primary", menu=menu, sizing_mode="stretch_width"
    #                     )
    #
    # layout = layout([
    #     [div],
    #     # [radio_button_group],
    #     [p],
    #     [dropdown],
    # ])
