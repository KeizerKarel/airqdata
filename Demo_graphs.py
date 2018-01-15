# PM sensor scripts
#%matplotlib inline
from matplotlib import pyplot as plt
import pandas as pd

from resources import civiclabs
from resources import luftdaten
pd.set_option("display.max_rows", 10)

# Civic Labs Resources
## Download list of sensors from Civic Labs' Google sheet
sensors = civiclabs.get_sensors(refresh_cache=True)
# print(sensors.head(4))

# print(len(sensors))

demo_chip_id = sensors["Chip ID"][3]  ## or give luftdaten sensor ID here.
demo_sensor_id = sensors["PM Sensor ID"][3]
"""print(demo_chip_id, demo_sensor_id)

print(sensors[sensors["PM Sensor ID"] == "6561"])"""

# Luftdaten.info resources
## Create a Sensor object and get the sensor's current data


demo_sensor = luftdaten.Sensor("6561", refresh_cache=True)
# print(demo_sensor)
# print(demo_sensor.metadata)

print(demo_sensor.url)

print(demo_sensor.current_values)


# Retrieve data history
## Data are retrieved from cache or server and then cleaned (see luftdaten.Sensor.clean_data).


demo_sensor.get_data(start_date="2017-12-01", end_date="2018-01-14")


# Inspect, summarize and plot data


print(demo_sensor.measurements)

print(type(demo_sensor.measurements))

#describe(demo_sensor.measurements)

demo_sensor.plot_measurements()


#Inspect, summarize and plot hourly means


"""demo_sensor.hourly_means
describe(demo_sensor.hourly_means)
demo_sensor.plot_hourly_means()"""


#Check distribution of sample intervals


"""demo_sensor.intervals.sort_values(ascending=False).head(10)"""


# List sensors near a given location
## Defaults to searching within an 8 kilometer radius around the center of Brussels
"""near = luftdaten.search_proximity()
near"""


## Sensors near Antwerp


"""luftdaten.search_proximity(lat=51.22, lon=4.41, radius=20)
(near_sensors, hourly_means) = luftdaten.evaluate_near_sensors(start_date="2017-09-10",
                                                 end_date="2017-09-13",
                                                 quiet=True)
hourly_means"""