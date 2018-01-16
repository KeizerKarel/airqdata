#!/usr/bin/env python3

"""Access Civic Labs Belgium resources."""

import pandas as pd

from resources.utils import CACHE_DIR, retrieve

SENSOR_SHEET_URL = ("https://docs.google.com/spreadsheets/d/1J8WTKryYjZHfBQrMS"
                    "Yjwj6uLOBmWWLftaTqeicKVfYE/export?format=csv")

# TODO: Create Google docs sheet for Leuven and swap URL

SENSOR_INFO_CACHE_FILE = CACHE_DIR + "/civic_labs_sensors.csv"


def get_sensor_info(**retrieval_kwargs):
    """Download information on the sensors deployed in Civic Labs'
    InfluencAir project from its Google Sheet and cache it.

    Args:
        retrieval_kwargs: keyword arguments to pass to retrieve function

    Returns:
        Dataframe of sensors with chip ID, sensor IDs of PM sensors and
            humidity/temperature sensors, address, floor number and side
            of the building that the sensors are installed on

    Raises:
        KeyError if sheet structure does not match listed columns
    """
    sensor_info = retrieve(SENSOR_INFO_CACHE_FILE, SENSOR_SHEET_URL,
                           "Civic Labs sensor information",
                           read_func=pd.read_csv,
                           read_func_kwargs={"header": 1, "dtype": "object"},
                           **retrieval_kwargs)
    try:
        sensor_info = (sensor_info[["Chip ID", "PM Sensor ID",
                                    "Hum/Temp Sensor ID", "Address", "Floor",
                                    "Side (Street/Garden)"]]
                       .rename(columns={"Side (Street/Garden)": "Side"}))
    except KeyError:
        raise KeyError("Could not get columns. Check if the structure or "
                       "labels of the Civic Labs sensor Google Sheet have "
                       "changed.")
    return sensor_info


if __name__ == "__main__":
    sensor_info = get_sensor_info()
