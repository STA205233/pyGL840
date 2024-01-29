#! /usr/bin/env python3

import GL840.DataAcquisition as Daq
import GL840.MongoDBHandler as Mongo
import GL840.Converter as Converter
import datetime
from os.path import exists
import os

def run():
    # The length of channel name must be the number of enabled channels
    channel_name = [f"Ch{i+1}" for i in range(28)]
    channel_name[0] = "Temperature_1"
    mongo = Mongo.MongoDBPusher()
    config = Daq.GL840Configuration(
        "192.168.1.11", 80, username="GL840", password="GL840")
    # config.channel_status = [True, False, True] + [False for i in range(17)]
    config.channel_status = [True for i in range(20)]
    config.channel_name = channel_name
    dt_now = datetime.datetime.now()

    dirname=f"/Users/grams/Software/QL/GL840Data/{dt_now.year:04}{dt_now.month:02}{dt_now.day:02}"
    if not exists(dirname):
        os.mkdir(dirname)




    # filename_prefex=f"{dt_now.year:04}{dt_now.month:02}{dt_now.day:02}_{dt_now.hour:02}{dt_now.minute:02}{dt_now.second:02}_"
    

    daq = Daq.DataAcquisition(
        config, csv_file_base=f"/Users/grams/Software/QL/GL840Data/{dt_now.year:04}{dt_now.month:02}{dt_now.day:02}/{dt_now.hour:02}{dt_now.minute:02}{dt_now.second:02}_", mongo=mongo, override=True, num_event_per_file=10000)
    # daq.set_function(0, Converter.Unity)
    daq.initialize_single()
    while 1:
        try:
            daq.data_acquire(1, 5)
        except KeyboardInterrupt:
            break
    daq.finalize_single(True)


if __name__ == "__main__":
    run()
