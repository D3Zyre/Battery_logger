import csv
import psutil
import wmi
import time
import datetime


def get_battery_info():
    """ Returns a dict() of the form:
        batt_dict = {"power online":PowerOnline,
                    "discharging":Discharging,
                    "charging":Charging,
                    "voltage":Voltage,
                    "discharge rate":DischargeRate,
                    "charge rate":ChargeRate,
                    "remaining capacity":RemainingCapacity,
                    "active":Active,
                    "critical":Critical,
                    "full charge capacity":FullChargedCapacity,
                    "battery percentage":battery_percentage,
                    "seconds to empty":seconds_to_empty,
                    "is connected to power":is_connected_to_power}

    Note: seconds_to_empty will only be a number if the OS knows time to empty, otherwise it could be:
    "POWERTIMEUNKNOWN" or "POWERTIMEUNLIMITED"
    """

    batt_stats = wmi.WMI(moniker = "//./root/wmi").ExecQuery("Select * from BatteryStatus where Voltage > 0")[0]
    PowerOnline = batt_stats.PowerOnline
    Discharging = batt_stats.Discharging
    Charging = batt_stats.Charging
    Voltage = batt_stats.Voltage
    DischargeRate = batt_stats.DischargeRate
    ChargeRate = batt_stats.ChargeRate
    RemainingCapacity = batt_stats.RemainingCapacity
    Active = batt_stats.Active
    Critical = batt_stats.Critical
    batt_stats2 = wmi.WMI(moniker = "//./root/wmi").ExecQuery("Select * from BatteryFullChargedCapacity")[0]
    FullChargedCapacity = batt_stats2.FullChargedCapacity
    batt_stats3 = tuple(psutil.sensors_battery())
    battery_percentage = batt_stats3[0]
    seconds_to_empty = batt_stats3[1]
    is_connected_to_power = batt_stats3[2]
    batt_dict = {"power online":PowerOnline,
                "discharging":Discharging,
                "charging":Charging,
                "voltage":Voltage,
                "discharge rate":DischargeRate,
                "charge rate":ChargeRate,
                "remaining capacity":RemainingCapacity,
                "active":Active,
                "critical":Critical,
                "full charge capacity":FullChargedCapacity,
                "battery percentage":battery_percentage,
                "seconds to empty":seconds_to_empty,
                "is connected to power":is_connected_to_power}

    return batt_dict

def append_to_csv(battery_info, log_path):
    """
    writes the battery stats to a csv file, appends if it already exists, creates the file if it doesn't
    """
    csv_header = "Datetime,Battery %,Power Online,Discharging,Charging,Voltage (mV),Discharge Rate (mW),Charge Rate (mW),Remaining Capacity (mWh),Active,Critical,Full Charge Capacity (mWh),Seconds to Empty,Is Connected to Power" # 14 things
    create_file = False # whether we need to create the file

    #TODO: probably fix this weirdness with a proper os.path.isfile() call

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
        file.write("{},{},{},{},{},{},{},{},{},{},{},{},{},{}\n".format(datetime.datetime.today(), battery_info["battery percentage"], battery_info["power online"], battery_info["discharging"], battery_info["charging"], battery_info["voltage"], battery_info["discharge rate"], battery_info["charge rate"], battery_info["remaining capacity"], battery_info["active"], battery_info["critical"], battery_info["full charge capacity"], battery_info["seconds to empty"], battery_info["is connected to power"]))

def main():
    append_to_csv(get_battery_info(),"Battery_Log.csv")

if __name__ == "__main__":
    main()

