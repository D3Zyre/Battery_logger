import psutil
import time
import datetime

print(tuple(psutil.sensors_battery())) # (battery%, seconds_until_empty, is_connected_to_power)

def get_battery_info():
    """ Returns a tuple of the form:
    (battery%, seconds_to_empty, is_connected_to_power)
    
    Note: seconds_to_empty will only be a number if the OS knows time to empty, otherwise it could be:
    "POWERTIMEUNKNOWN" or "POWERTIMEUNLIMITED"
    """
    return tuple(psutil.sensors_battery())

def append_to_csv():
    """ Don't forget to create the csv if it doesn't exist already
    """
    pass

