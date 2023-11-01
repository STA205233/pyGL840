import matplotlib.pyplot as plt
import pandas as pd
import datetime as dt
from typing import Union, Any, Optional
from sys import maxsize
import numpy as np


class DataAnalyzer():
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.skip = None
        self.deltatime: np.ndarray
        self.__init_time = False
        self.init_time: dt.datetime
        self.df: pd.DataFrame

    def load(self, skiprows: Optional[list[int] | int] = None, skip: Optional[int] = None, Range: tuple[int, int] = (0, maxsize), adjust_zero: bool = False):
        self.skip = skip
        if skip is not None:
            if skip < 2:
                raise ValueError("skip must be larger than 1.")
            if skiprows is not None:
                raise ValueError("index_col and skip cannot be set simultaniously.")
            with open(self.filename, "r") as fr:
                line = fr.readline()
                headers = line.strip().split(",")
                line = fr.readline()
                buf: list[Any] = []
                temp = 0
                self.__init_time = False
                if not adjust_zero:
                    self.init_time = dt.datetime.strptime(line.strip().split(",")[0], "%Y-%m-%d %H:%M:%S.%f")
                    self.__init_time = True
                deltatime_ = []
                for i in range(Range[1]):
                    if i < Range[0]:
                        i += 1
                    elif line == '':
                        break
                    elif temp == 0:
                        lines = line.strip().split(",")
                        if not self.__init_time:
                            self.init_time = dt.datetime.strptime(lines[0], "%Y-%m-%d %H:%M:%S.%f")
                            self.__init_time = True
                        deltatime_.append((dt.datetime.strptime(lines[0], "%Y-%m-%d %H:%M:%S.%f") - self.init_time).total_seconds())
                        buf.append(lines[1:])
                        line = fr.readline()
                        temp += 1
                        i += 1
                    elif temp == skip - 1:
                        line = fr.readline()
                        temp = 0
                        i += 1
                    else:
                        temp += 1
                        i += 1
                        line = fr.readline()

            self.df = pd.DataFrame(buf, dtype=float)
            self.df.columns = headers[1:]
            self.df.dropna(how="any", axis="columns", inplace=True)
            self.deltatime = np.array(deltatime_)
        else:
            if Range is not None:
                skiprows = Range[0] - 1
                nrows = Range[1] - Range[0] + 1
            if not adjust_zero:
                with open(self.filename, "r") as fp:
                    fp.readline()
                    self.init_time = dt.datetime.strptime(fp.readline().strip().split(",")[0], "%Y-%m-%d %H:%M:%S.%f")
                    self.__init_time = True
            self.df = pd.read_csv(self.filename, header=0, dtype={"Time": str}, skiprows=skiprows, nrows=nrows)
            self.df.dropna(how="any", axis="columns", inplace=True)
            with open(self.filename, "r") as fp:
                header = fp.readline().strip().split(",")
            self.df.columns = header
            if not self.__init_time:
                self.init_time = dt.datetime.strptime(self.df.at[0, "Time"], "%Y-%m-%d %H:%M:%S.%f")
            self.deltatime = self.df["Time"].map(lambda x: (dt.datetime.strptime(x, "%Y-%m-%d %H:%M:%S.%f") - self.init_time).total_seconds(), "ignore").to_numpy(dtype=float)
            self.df.drop("Time", axis=1, inplace=True)

    def find(self, second: float) -> int:
        for i in range(len(self.deltatime)):
            if self.deltatime[i] >= second:
                if self.skip is not None:
                    return i * self.skip
                else:
                    return i
        raise LookupError()

    def scatter(self, axes: Any, ch: Union[int, str], time_offset: float = 0, **kwargs: Any) -> None:
        if isinstance(ch, int):
            axes.scatter(self.deltatime + time_offset, self.df[self.df.columns.values[ch - 1]].to_numpy(), label=self.df.columns.values[ch - 1], ** kwargs)
        elif isinstance(ch, str):
            axes.scatter(self.deltatime + time_offset, self.df[ch].to_numpy(), label=ch, **kwargs)
        else:
            raise TypeError


if __name__ == "__main__":
    fig = plt.figure()
    ax = fig.add_subplot(111,)
    d = DataAnalyzer("Temperature/20230214-01.csv",)
    d.load(adjust_zero=False, skip=100)
    d.load(adjust_zero=False, Range=(d.find(300), maxsize))
    d.scatter(ax, 1, s=0.5, time_offset=0)
    d.scatter(ax, 3, s=0.5, time_offset=0)
    d.scatter(ax, 2, s=0.5, time_offset=0)
    d.scatter(ax, 4, s=0.5, time_offset=0)
    # d1 = Data_Analysis("")
    ax.set_ylabel("Temperature [degree]")
    ax.set_xlabel("Time [s]")
    ax.legend()
    # plt.savefig("20221011-02.pdf")
    plt.show()
