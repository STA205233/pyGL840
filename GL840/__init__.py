"""
GL840
==

Tools for GL840.

Modules
--
DataAcquisition
    Acquire the data and put into mongoDB.
Converter
    Convert the voltage data into the pressure data.
MongoDBHandler
    Python interface for HSQuickLook.
ServerSimulator
    Simulates the server function of GL840

---------------------
Author: Shota Arai
Date: 2022/11/30
"""

from typing import Literal
SPECIAL_VALUE = Literal["+++++++", "Off"]
