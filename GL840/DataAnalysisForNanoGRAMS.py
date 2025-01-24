import matplotlib.pyplot as plt
from GL840.MultiDataAnalyzer import MultiDataAnalyzer
from GL840.DataAnalyzer import DataAnalyzer
import Converter
import glob
import numpy as np
import datetime

def conversion_OX600(v):
  R = 151.6
  I = 1000.0 * v / R
  return 25.0 * (I - 4.0) / (20.0 - 4.0)

def plot_scatter_time_series(fig, ax, time, x, y):
    duration = (time[-1] - time[0])
    time_arr = (time - time[0]) / duration
    ax.scatter(x, y, c = time_arr)

if __name__ == "__main__":
    fig = plt.figure()
    ax = fig.add_subplot()
    ana = MultiDataAnalyzer("/Users/nanograms/work/quicklook/GL840Data/2025*")
    x = []
    y = []
    # y2 = []
    for dat in ana:
        if (dat["Time"] > datetime.datetime(2025, 1, 14, 13,30)):
            break
        elif(dat["Time"] < datetime.datetime(2025,1,14, 12,30)):
            continue
        try:
            # y.append(conversion_OX600(dat["Ch5"]))
            # y.append(Converter.VtoP(dat["Ch2"])/(dat["Ch21"]+273.15)) # P/T
            # y.append(Converter.VtoP(dat["Ch2"]))
            y.append(dat["Ch3"])
            # y2.append(dat["Ch21"]+273.15)
            # y.append(dat["Ch2"])
        except:
            continue
        x.append(dat["Time"])
    # ax.set_yscale("log")
    x = np.array(x)
    fig.autofmt_xdate()
    ax.set_ylabel("Inner Pressure[Pa]")
    ax.set_xlabel("Time")
    ax.scatter(x, y)
    ax.grid()
    # ax2 = ax.twinx()
    # ax2.set_ylabel("Temperature [Deg]")
    # ax.plot(x, y)
    # ax2.plot(x,y2, color="red")
    plt.show()
