import matplotlib.pyplot as plt
from DataAnalyzer import DataAnalyzer
import Converter

if __name__ == "__main__":
    fig = plt.figure()
    ax = fig.add_subplot()
    ana = DataAnalyzer("/Users/nanograms/work/quicklook/GL840Data/20240606/170459")
    x = []
    y = []
    
    for dat in ana:
        try:
            y.append(Converter.VtoP(dat["Ch2"]))
            # y.append(dat["Ch18"])
        except:
            continue
        x.append(dat["Time"])
    ax.set_yscale("log")
    ax.plot(x, y)
    plt.show()
