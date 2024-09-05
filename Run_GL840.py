#! /usr/bin/env python3

import GL840.DataAcquisition as Daq
import GL840.MongoDBHandler as Mongo
import GL840.Converter as Converter
import datetime
from os.path import exists
import os
from GL840.Warning import DataWarning

def run():
    # The length of channel name must be the number of enabled channels
    channel_name = [f"Ch{i+1}" for i in range(28)]
    # channel_name[0] = "Temperature_1"
    mongo = Mongo.MongoDBPusher()
    config = Daq.GL840Configuration(
        "192.168.1.11", 80, username="GL840", password="GL840", channels=28)
    # config.channel_status = [True, False, True] + [False for i in range(17)]
    config.channel_status = [True for i in range(28)]
    config.channel_name = channel_name
    dt_now = datetime.datetime.now()

    dirname=f"/Users/nanograms/work/quicklook/GL840Data/{dt_now.year:04}{dt_now.month:02}{dt_now.day:02}"
    if not exists(dirname):
        os.makedirs(dirname)

    # filename_prefex=f"{dt_now.year:04}{dt_now.month:02}{dt_now.day:02}_{dt_now.hour:02}{dt_now.minute:02}{dt_now.second:02}_"
    Oxygen = DataWarning(lambda x: (Converter.conversion_OX600(x) < 19.0), [1400, 2800, 1400, 2800], [0.1, 0.1, 0.1, 0.1], message="Oxygen !!")
    # Heater = DataWarning(lambda x: (x > 0.0), [1200, 600], [0.5, 0.5], 100, message="Heater")

    daq = Daq.DataAcquisition(config)
        # config, csv_file_base=f"/Users/nanograms/work/quicklook/GL840Data/{dt_now.year:04}{dt_now.month:02}{dt_now.day:02}/{dt_now.hour:02}{dt_now.minute:02}{dt_now.second:02}_", mongo=mongo, overwrite=False, num_event_per_file=1000, warning=True)
    # daq.set_function(0, Converter.Unity)
    # daq.set_function(4, Oxygen)
    # daq.set_function(1, Heater)
    daq.initialize_single()
    while 1:
        try:
            daq.data_acquire(1, 5)
        except KeyboardInterrupt:
            break
    daq.finalize_single(True)


if __name__ == "__main__":
    run()
