# Importing everything
import fastf1 as ff1
from fastf1 import plotting
from matplotlib import pyplot as plt
import pandas as pd

# DPI value for plotting
dpi_val = 1500

# Specify year, location, session (race, qualifying, etc.), and driver name
year_use = 2022
location_use = "Monaco"
session_use = "r"
driver_use = "PER"

# Color for the velocity and acceleration graphs
vel_color = "r"
acc_color = "r"

# Matplotlib setting to use LaTeX font for plots
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.sans-serif": ["Computer Modern Roman"]})

# Set up plotting
plotting.setup_mpl()

# Enabling cache for faster telemetry loading
ff1.Cache.enable_cache(
    'C:/path_to_cache/cache')

# Get rid of some pandas warnings that are not relevant
pd.options.mode.chained_assignment = None


# Getting the fastest lap of the driver for the given session, year, and location
def f1_analysis(year, location, session, driver):
    # Getting race specified by user
    race = ff1.get_session(year, location, session)
    race.load()

    # Getting all the race laps with telemetry included
    laps_race = race.load_laps(with_telemetry=True)

    # Isolating the telemetry of the driver provided by the user
    laps_driver_race = laps_race.pick_driver(driver)

    # Getting the fastest lap of the driver
    fastest_driver_race = laps_driver_race.pick_fastest()

    # Getting the car data for the driver's fastest lap
    telemetry_driver_race = fastest_driver_race.get_car_data().add_distance()

    return telemetry_driver_race


# Creating a DataFrame with time in seconds and velocity in m/s
def speed_time_csv(year, location, session, driver):
    time_old = f1_analysis(year, location, session, driver).Date
    # Want to use the 0th index in time as zero, then base everything else off of that
    time_base = time_old[0].timestamp()

    time_use = pd.Series(len(time_old), name='Time')
    i = 0
    while i <= len(time_old) - 1:
        time_use[i] = time_old[i].timestamp() - time_base
        i = i + 1

    # Convert speed from km/hr to m/s
    speed_old = f1_analysis(year, location, session, driver).Speed
    speed_use = speed_old * (1000 / 3600)  # Convert from km/hr to m/s
    time_use = time_use
    vel_frame = pd.merge(time_use, speed_use, right_index=True, left_index=True)
    return vel_frame


# Taking the velocity vs. time DataFrame and converting it to acceleration vs. time
def accel_time_csv(year, location, session, driver):
    vel_frame = speed_time_csv(year, location, session, driver)

    time = vel_frame.iloc[:, 0]
    vel = vel_frame.iloc[:, 1]

    i = 0
    acc = []

    while i <= len(vel_frame) - 2:
        # Calculating acceleration using forward center finite difference
        acc.append((vel[i + 1] - vel[i]) / (time[i + 1] - time[i]))
        i = i + 1

    # Removing the first entry of time since we are dealing with acceleration
    time_use = time[1:]
    time_old = pd.DataFrame(time_use, columns=['Time'])

    acc_old = pd.DataFrame(acc, columns=['Acceleration'])
    acc_frame = pd.merge(time_old, acc_old, right_index=True, left_index=True)

    return acc_frame


# Calling speed method and writing to csv
speed_data = speed_time_csv(year_use, location_use, session_use, driver_use)

acc_data = accel_time_csv(year_use, location_use, session_use, driver_use)

# Writing to CSV file (might need to include 'f' flag)
speed_data.to_csv('C:/save_path/{driver_use.lower()}_vel_time_data.csv')

# Plotting velocity vs. time
plt.plot(speed_data['Time'], speed_data['Speed'], vel_color, label=driver_use)
plt.grid()
plt.legend(loc='best')
plt.xlabel("Time (sec)")
plt.ylabel("Velocity (m/s)")
plt.title("Velocity vs. Time Graph, F1 Edition")

# (might need to include 'f' flag)
path = 'C:/save_path/{driver_use.lower()}_vel_time.jpg'

plt.savefig(path, dpi=dpi_val)
plt.show()

# Writing to CSV file (might need to include 'f' flag)
acc_data.to_csv('C:/save_path/{driver_use.lower()}_acc_time_data.csv')

### Plotting acceleration vs. time ###

plt.plot(acc_data['Time'], acc_data['Acceleration'], acc_color, label=driver_use)
plt.grid()
plt.legend(loc='best')
plt.xlabel("Time (sec)")
plt.ylabel("Acceleration $\displaystyle(m/s^2)$")
plt.title("Acceleration vs. Time Graph, F1 Edition")

# (might need to include 'f' flag)
path = 'C:/save_path/{driver_use.lower()}_acc_time.jpg'

plt.savefig(path, dpi=dpi_val)
plt.show()

print("\nProgram executed")
