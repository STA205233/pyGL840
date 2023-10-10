#! /usr/bin/env python3

import GL840.DataAcquisition as Daq
import GL840.MongoDBHandler as Mongo
import GL840.Converter as Converter


def run():
    channel_name = [f"ch{i+1}" for i in range(2)]
    channel_name[0] = "Temperature_1"
    mongo = Mongo.MongoDBPusher()
    config = Daq.GL840Configuration("localhost", 6765)
    config.channel_status = [True, True, False] + [False for i in range(17)]
    config.channel_name = channel_name
    daq = Daq.DataAcquisition(config, csv_file="test.csv", mongo=mongo)
    daq.initialize_single()
    while 1:
        try:
            daq.data_acquire(1, 5)
        except KeyboardInterrupt:
            break
    daq.finalize_single()

if __name__ == "__main__":
    run()