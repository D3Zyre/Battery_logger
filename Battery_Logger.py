import csv
import psutil
import time
import datetime


def get_battery_info():
    """ Returns a tuple of the form:
    (battery%, seconds_to_empty, is_connected_to_power)
    
    Note: seconds_to_empty will only be a number if the OS knows time to empty, otherwise it could be:
    "POWERTIMEUNKNOWN" or "POWERTIMEUNLIMITED"
    """
    return tuple(psutil.sensors_battery())

def append_to_csv(battery_info, log_path):
    """
    """
    csv_header = "Datetime,Battery %,Seconds To Empty,Is Connected to Power"
    create_file = False # whether we need to create the file

    with open(log_path, "a") as file:
        pass # creating the file if it didn't exist, otherwise this does nothing
    with open(log_path, "r") as file:
        first_line = file.readline()
        if first_line != csv_header+"\n": # checking to see if the file has the correct header, if it doesn't then we assume it has just been created, and will be overwritten
            create_file = True
    if create_file:
        with open(log_path, "w") as file:
            file.write(csv_header+"\n") # create file and add the header
    with open(log_path, "a") as file:
        file.write("{},{},{},{}\n".format(datetime.datetime.today(), battery_info[0], battery_info[1], battery_info[2]))

def main():
    append_to_csv(get_battery_info(),"Battery_Log.csv")

if __name__ == "__main__":
    main()

