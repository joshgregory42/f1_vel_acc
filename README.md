# Formula One Velocity and Acceleration

## Abstract

This is a program to take any F1 session (i.e. race, qualifying, etc.) and extract a driver's fastest lap, then plot the velocity and acceleration profiles. You, as the user, are able to specify which driver you would like, which session, year, and location for the analysis. The program then takes those parameters and finds the fastest lap of the driver you indicate for the session you indicate. For example, if you input "LEC" (Charles Leclerc), "r" (race), "Monaco", 2022, the program will find Charles Leclerc's fastest lap of the Monaco Grand Prix in 2022.

## Required Software and Libraries

Python 3.10 is recommended. More recent versions may be used in the future as libraries such as FastF1 are updated to work with newer versions of Python (i.e. Python 3.11, 3.12, etc.). Other libraries that are necessary are:

* FastF1
  * This is the package that pulls all of the telemetry from the online server where it is stored. The documentation can be found [here](https://theoehrly.github.io/Fast-F1/).
* MatPlotLib
  * This library allows you to do all of the necessary plotting. More information can be found [here](https://matplotlib.org/).
* Pandas
  * This allows for storing of large datasets with easy manipulation. The documentation can be found [here](https://pandas.pydata.org/docs/).

## Cache

Since FastF1 is pulling a lot of data from a server, it is a good idea to create something called a "cache" on whatever machine you're running this program on. The cache is a fancy term for a folder that FastF1 can put all of the data into. Here's how it works. If you want Charles Leclerc's fastest lap of the Monaco Grand Prix in 2022, FastF1 pulls all of the data for all of the drivers for the race in Monaco 2022. This means that you're getting much more information than just Charles Leclerc's telemetry. If you save all of this information to a cache (just a folder on your computer), if you want a different driver's telemetry from the same race, maybe Sergio Perez's telemetry, FastF1 pulls that data from the cache instead of needing to sift through everything online. It's like the digital equivalent of copying all of the dictionary entries for the letter "A". If you know you need many definitions of the letter "A", you wouldn't want to get out the dictionary, find your word, write it down, then put the dictionary away, only to have to pull it back out again when you need the definition of another word. You'd just take the dictionary out, write down all of the words you think you'll need, and then reference those when you need to, saving a lot of time. The cache works in the exact same way, just digitally. And with actual F1 driver data. Which is pretty cool.

### How to Create the Cache

Wherever you have this program stored on your computer, make a new folder/directory and name it "cache". The program will take care of the rest.

## User Inputs

There are a few things that you, as the user, can change about the program to make it analyze different things. The first one you'll see is this:

```python
# DPI value for plotting
dpi_val = 1500
```

"DPI" stands for "dots per inch". It's the resolution of the images that are saved when the program is finished running. A higher DPI value gives you a crisper image, but takes longer to create. 1500 gives you really nice plots, but if that is taking too long feel free to reduce it. Next we have

```python
# Specify year, location, session (race, qualifying, etc.), and driver name
year_use = 2022
location_use = "Monaco"
session_use = "r"
driver_use = "PER"
```

This specifies the year, location, session, and driver name that will be used during the analysis. Note that for `location_use`, `session_use`, and `driver_use`, whatever is put in there must be in quotes. For example, if you want Monaco you must type `location_use = "Monaco"`. Typing `location_use = Monaco` will cause the program to crash.

```python
# Color for the velocity and acceleration graphs
vel_color = "r"
acc_color = "r"
```

Allows you to specify which color you want the velocity (`vel`) and acceleration (`acc`) plots to be in. Refer to the MatPlotLib documentation for different color codes.

```python
# Matplotlib setting to use LaTeX font for plots
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.sans-serif": ["Computer Modern Roman"]})
```

sets the program to use the LaTeX font, Computer Modern Roman Serif. This just makes the plots look really nice. It is optional and can be deleted/commented out if it is not wanted.

```python
# Enabling cache for faster telemetry loading
ff1.Cache.enable_cache(
    'C:/path_to_cache/cache')
```

is the path to the cache that was discussed earlier. `path_to_cache` should also be in the same directory as where this program is stored/saved to.

```python
# Writing to CSV file
speed_data.to_csv('save_path/{driver_use.lower()}_vel_time_data.csv')
```

Specifies the path to save the csv file with all of the driver data.

```python
path = 'path/{driver_use.lower()}_vel_time.jpg'
```

and

```python
acc_data.to_csv('save_path/{driver_use.lower()}_acc_time_data.csv')
```

and

```python
path = 'save_path/{driver_use.lower()}_acc_time.jpg'
```

all do the same thing as `speed_data.to_csv('save_path/{driver_use.lower()}_vel_time_data.csv')`, some of which specify the path to save the images (as JPG).
