# Class to create differing color of points, dependant upon measured temperature.
import numpy
from bokeh.models import ColumnDataSource


def filter_points_by_color(df, p):
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

    p : bokeh figure
        Bokeh figure for plotting that contains a tiled OpenStreetMap of Earth.

    Returns
    -------
    p : bokeh figure
        A bokeh figure that includes the different points, dissected by temperature.
    """

    # Convert list of strings to floats
    temp_floats = [float(x) for x in df['ta_int']]

    # Create boolean columns, that are as long as the float list (and the dataframe it originates from)
    column_cold = numpy.full(len(temp_floats), False)
    column_warm = numpy.full(len(temp_floats), False)
    column_hot = numpy.full(len(temp_floats), False)
    for index, temperature in enumerate(temp_floats):
        if temperature < 22:
            column_cold[index] = True
        elif temperature < 28:
            column_warm[index] = True
        else:
            column_hot[index] = True

    # Create Python dicts as basis of ColumnDataSource
    data_cold = {'x_values': df[column_cold]['geometry'].x,
            'y_values': df[column_cold]['geometry'].y,
            'p_id': df[column_cold]['p_id'],
            'lon': df[column_cold]['lon'],
            'lat': df[column_cold]['lat'],
            'ta_int': df[column_cold]['ta_int']}

    data_warm = {'x_values': df[column_warm]['geometry'].x,
            'y_values': df[column_warm]['geometry'].y,
            'p_id': df[column_warm]['p_id'],
            'lon': df[column_warm]['lon'],
            'lat': df[column_warm]['lat'],
            'ta_int': df[column_warm]['ta_int']}

    data_hot = {'x_values': df[column_hot]['geometry'].x,
            'y_values': df[column_hot]['geometry'].y,
            'p_id': df[column_hot]['p_id'],
            'lon': df[column_hot]['lon'],
            'lat': df[column_hot]['lat'],
            'ta_int': df[column_hot]['ta_int']}

    # Create a ColumnDataSource by passing the dict
    source_cold = ColumnDataSource(data=data_cold)
    source_warm = ColumnDataSource(data=data_warm)
    source_hot = ColumnDataSource(data=data_hot)

    # Create three different variants of circles in the figure, to account for temperature difference
    p.circle(x='x_values', y='y_values', source=source_cold, color="blue")
    p.circle(x='x_values', y='y_values', source=source_warm, color="orange")
    p.circle(x='x_values', y='y_values', source=source_hot, color="red")

    return p
