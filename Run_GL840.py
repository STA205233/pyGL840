#! /usr/bin/env python3

import GL840.DataAcquisition as Daq
import GL840.MongoDBHandler as Mongo


def run():
    channel_name = [f"ch{i+1}" for i in range(2)]  # The length of channel name must be the number of enabled channels
    channel_name[0] = "Temperature_1"
    mongo = Mongo.MongoDBPusher()
    config = Daq.GL840Configuration("localhost", 6765)
    config.channel_status = [True, True, False] + [False for i in range(17)]
    daq = Daq.DataAcquisition(config, csv_file_base="test", mongo=mongo, override=False, num_event_per_file=10)
    daq.initialize_single()
    while 1:
        try:
            daq.data_acquire(1, 5)
        except KeyboardInterrupt:
            break
    daq.finalize_single(True)


if __name__ == "__main__":
    run()
