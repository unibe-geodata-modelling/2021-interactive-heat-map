# Class to get coordinates and temperature from raw csv data
import logging
import os

script_dir = os.path.dirname(__file__)
logger = logging.getLogger(__name__)


def get_all_lines(filename='sample_data.csv'):
    """Gets and returns all lines from a csv file, excluding the header.

    Parameters
    ----------
    filename : str
        The file to get coordinates from. Must be placed in the data folder.

    Returns
    -------
    list
        A list of all coordinates.
    """

    with open(os.path.join(script_dir, '../data/' + filename)) as file:
        lines = file.readlines()
        lines.pop(0)
    return lines


def get_content():
    """Function to get all content and save them in an easy to read dictionary matter.

    Parameters
    ----------

    Returns
    -------
    list
        A dictionary of dictionaries (named by p_id and time_orig, separated by an underscore),
         which contains all deemed relevant entries:
            rounded_time: Time rounded to full hour by netAtmo.
            time_orig: Actual time of measurement.
            id: ID of the weather station
            lon: Longitude in decimal format.
            lat: Latitude in decimal format.
            altitude: Height in meters.
            z: Height coordinate (???). TODO What is this?
            temp: temperature in degrees Celsius.
            utm_x: Universal Transverse Mercator x coordinate.
            utm_y: Universal Transverse Mercator y coordinate.
    """

    content = {}
    lines = get_all_lines('sample_data.csv')
    skip_index = 0

    for line in lines:
        # Removing the lines that contain 'NAN'
        if 'NAN' in line:
            skip_index += 1
            continue
        fields = line.split(',')

        # Get line_id, located in the first column.
        dictionary_id = fields[2] + '_' + fields[1]

        # Create dictionary entry
        content[dictionary_id] = {
            'rounded_time': fields[0],
            'time_orig': fields[1],
            'id': fields[2],
            'lon': fields[3],
            'lat': fields[4],
            'altitude': fields[5],
            'z': fields[6],
            'temp': fields[7],
            'utm_x': fields[8],
            'utm_y': fields[9]
        }
    logger.error("Ignored {} lines due to containing \"NAN\" out of {} lines.".format(skip_index, len(lines)))
    return content


# For testing uncomment the following line:
get_content()
