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

SPECIAL_VALUE: tuple[str, ...] = ("+++++++", "Off")
TIME_FORMAT = "%Y-%m-%d %H:%M:%S.%f"
ENCODE = "utf-8"
__all__ = ["SPECIAL_VALUE", "ENCODE", "Converter", "DataAcquisition", "MongoDBHandler", "ServerSimulator", "DocumentBuilder"]
