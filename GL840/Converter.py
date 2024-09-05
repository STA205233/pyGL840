from typing import Literal, Optional
from math import log10
"""
This is for MPT 200 AR. These conversion rules are taken from https://www.pfeiffer-vacuum.com/filepool/file/digiline/pg0029ben_f.pdf?referer=1838&detailPdoId=13256&request_locale=en_US
"""
conversion: dict[str, list[float]] = {"Pa": [5.6, 9.333], "kPa": [7.4, 2.33], "Torr": [6.875, 11.46], "hPa": [6.8, 11.33], "mbar": [6.8, 11.33], "ubar": [5.0, 8.333], "mTorr": [5.075, 8.458]}
UNIT: Literal["Pa", "kPa", "Torr", "hPa", "mbar", "ubar", "mTorr"] = "Pa"


def VtoP(V: float) -> float:
    return 10**(1.667 * V - conversion[UNIT][1])


def PtoV(P: float) -> float:
    return 10**(conversion[UNIT][0] + 0.6 * log10(P))


"""
This is for General use.
"""


def Unity(V: float) -> float:
    return 1


def V(V: float) -> float:
    return V


class Linear():
    def __init__(self, coe: Optional[tuple[float, float]]) -> None:
        if coe is not None:
            self.coe = coe
        else:
            self.coe = (1., 1.)

    def __call__(self, value: float) -> float:
        return self.coe[1] * value + self.coe[0]

def conversion_OX600(v):
    R = 151.6
    I = 1000.0 * v / R
    return 25.0 * (I - 4.0) / (20.0 - 4.0)