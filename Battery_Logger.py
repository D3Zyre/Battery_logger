import psutil

print(tuple(psutil.sensors_battery())) # (battery%, seconds_until_empty, is_connected_to_power)
