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

print("The sensor's URL is: " + demo_sensor.url)
print("The sensor currently reads for pm 2.5: " + str(demo_sensor.current_values['pm2.5']) + " and for pm 10: " + str(demo_sensor.current_values['pm10']))

# Retrieve data history
## Data are retrieved from cache or server and then cleaned (see luftdaten.Sensor.clean_data).


demo_sensor.get_data(start_date="2017-12-01", end_date="2018-01-14")


# Inspect, summarize and plot data


# print(demo_sensor.measurements)

print(demo_sensor.measurements.describe())
# describe(demo_sensor.measurements)

# demo_sensor.plot_measurements()


# Inspect, summarize and plot hourly means


# demo_sensor.hourly_means
print(demo_sensor.hourly_means.describe())
#demo_sensor.plot_hourly_means()

# Inspect, summarize and plot daily means
#demo_sensor.plot_daily_means()
print(demo_sensor.daily_means.describe())


#Check distribution of sample intervals


"""demo_sensor.intervals.sort_values(ascending=False).head(10)"""


# List sensors near a given location
## Defaults to searching within an 8 kilometer radius around the center of Brussels
lat_Leuven = 50.879018
lon_Leuven = 4.701167
rad_Leuven = 4

near = luftdaten.search_proximity(lat=lat_Leuven, lon=lon_Leuven, radius=rad_Leuven) # Set to Leuven in front of the city hall)
print(near)


## Sensors near Leuven

(near_sensors, hourly_means, daily_means) = luftdaten.evaluate_near_sensors(lat=lat_Leuven, lon=lon_Leuven, radius=rad_Leuven, start_date="2017-12-01", end_date="2018-01-14",
                                                 quiet=True)
#near_sensors
#hourly_means

print(hourly_means.describe())
#print(head(near_sensors))
#print(head(hourly_means))
