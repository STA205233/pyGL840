#! /usr/bin/env python3

import GL840.DataAcquisition as Daq
import GL840.MongoDBHandler as Mongo
import GL840.Converter as Converter


def run():
    # The length of channel name must be the number of enabled channels
    channel_name = [f"Ch{i+1}" for i in range(20)]
    channel_name[0] = "Temperature_1"
    mongo = Mongo.MongoDBPusher()
    config = Daq.GL840Configuration(
        "192.168.0.1", 80, username="GL840", password="GL840")
    # config.channel_status = [True, False, True] + [False for i in range(17)]
    config.channel_status = [True for i in range(20)]
    config.channel_name = channel_name
    daq = Daq.DataAcquisition(
        config, csv_file_base="test", mongo=mongo, override=True, num_event_per_file=100)
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
