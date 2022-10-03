print("Importing Libraries...")
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import csv
import datetime

print("Processing Data...")
y1 = list() # the y coordinates to graph, % Battery
y2 = list() # the y coordinates to graph, Discharge Rate in W
y3 = list() # the y coordinates to graph, Charge Rate in W
x = list() # the x coordinates to graph, as dates
first_row = True
with open("Battery_Log.csv", "r") as file: # the file here is the file that is created by Battery_Logger.py by default
    read = csv.reader(file)
    for row in read:
        if first_row:
            first_row = False
        else:
            y1.append(float(row[1]))
            y2.append(float(row[6])/1000)
            y3.append(float(row[7])/1000)
            x.append(datetime.datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S.%f"))

print(len(x), "Points...")
print("Plotting...")
y1 = np.asarray(y1, np.int8) # percentages are from 0 to 100, so int8 is adequate

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%d/%m/%Y"))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())

plt.plot(x, y1)
plt.plot([x[0], x[-1]], [30, 30])
plt.plot([x[0], x[-1]], [80, 80])
plt.plot([x[0], x[-1]], [10, 10])
plt.plot(x, y2)
plt.plot(x, y3)
plt.gcf().autofmt_xdate()
plt.yticks(np.arange(0, 105, 5))
plt.xticks(np.arange(min(x), max(x)+datetime.timedelta(0.01), (max(x) - min(x)) / 20))
plt.title("Battery Percentage Over Time")
plt.xlabel("Time (date)")
plt.ylabel("Battery Percentage (0-100)")
plt.grid(axis = "y", linestyle = "--", linewidth = 0.5)
print("Done")
plt.show()

# TODO add legend
# TODO add stats
