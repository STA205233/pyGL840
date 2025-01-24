#! /usr/bin/env python3

import GL840.MongoDBHandler as Mongo
import GL840.Warning as w
import os
import enum
import time
from GL840.Converter import conversion_OX600, conversion_PKR251
from typing import Callable
try:
    import GL840.SlackHandler as Slack
    from slack_sdk.errors import SlackClientError
    slack_ON = True
except ImportError:
    slack_ON = False

channel = "general"


class StatusSound:
    def __init__(self, frequency, second, volume) -> None:
        self.frequency = frequency
        self.second = second
        self.volume = volume


class STATUS(enum.Enum):
    Emergency = 3
    Warning = 2
    Information = 1
    Normal = 0


status_sound = {STATUS.Emergency: StatusSound([1000.0, 2000.0], [0.1, 0.1], 1), STATUS.Warning: StatusSound([440, 0], [1, 1], 1), STATUS.Information: None, STATUS.Normal: None}


class ErrorManager():
    def __init__(self, section_name: str, data_name: str, func: Callable[..., STATUS], slack: Slack.SlackHandler | None = None, slack_channel="", warning: w.Warning | None = None, unit: str = "", item_name: str = "", conv_func: Callable[..., float] = lambda x: x) -> None:
        self.status = STATUS.Normal
        self.func = func
        self.conv_func = conv_func
        self.slack = slack
        self.warning = warning
        self.section_name = section_name
        self.data_name = data_name
        self.unit = unit
        self.slack_channel = slack_channel
        if item_name == "":
            self.item_name = data_name
        else:
            self.item_name = item_name

    def __call__(self, data, **kwargs) -> None:
        value = self.func(data[self.section_name][self.data_name], **kwargs)
        if value == STATUS.Warning:
            status = STATUS.Warning
        elif value == STATUS.Emergency:
            status = STATUS.Emergency
        elif value == STATUS.Information:
            status = STATUS.Information
        elif value == STATUS.Normal:
            status = STATUS.Normal
        if self.status != status:
            if status != STATUS.Normal:
                string = f"{status.name}: {self.item_name} is {self.conv_func(data[self.section_name][self.data_name]):.2f} {self.unit}"
                self.__notify_slack(channel, string)
                if (status_sound[status] is not None) and (status.value > self.status.value):
                    self.__notify_sound(status_sound[status].frequency, status_sound[status].second, status_sound[status].volume, string, blocking=False)
                else:
                    print(string)
            else:
                string = f"Status goes back to normal\n{self.item_name} is {self.conv_func(data[self.section_name][self.data_name]):.2f} {self.unit}"
                self.__notify_slack(channel, string)
                if self.warning is not None:
                    self.warning.stop()
                print(string)
            self.status = status

    def __notify_slack(self, channel, string):
        if self.slack is not None:
            try:
                self.slack.send_message(channel, string)
            except SlackClientError as e:
                print(e)

    def __notify_sound(self, frequency, second, volume, message, blocking=False):
        if self.warning is not None:
            self.warning(frequency, second, volume, message, blocking)
        else:
            print(message)


def oxygen(v):
    value = conversion_OX600(v)
    if value < 18.0:
        return STATUS.Emergency
    elif value < 19.0:
        return STATUS.Warning
    else:
        return STATUS.Normal


def inner_pressure(v):
    value = conversion_PKR251(v)
    if value > 1.8 * 10**3:
        return STATUS.Emergency
    elif value > 1.5 * 10**3:
        return STATUS.Warning
    else:
        return STATUS.Normal


def __main():
    mongo = Mongo.MongoDBPuller("192.168.160.8", 27017, "GL840", "GL840")
    warning = w.Warning()
    if slack_ON:
        slack = Slack.SlackHandler(os.environ['SLACK_TOKEN'])
        if slack.test():
            print("Slack is ready.")
        else:
            print("Slack is not ready.")
            slack = None
    else:
        slack = None
    error_managers = []
    error_managers.append(ErrorManager("GL840", "Ch5", oxygen, slack, "general", warning, "%", "Oxygen", conversion_OX600))
    error_managers.append(ErrorManager("GL840", "Ch3", inner_pressure, slack, "general", warning, "hPa", "Inner Pressure", conversion_PKR251))
    while True:
        data = mongo.pull_one()
        if data is None:
            continue
        for error_manager in error_managers:
            error_manager(data)
        time.sleep(1)


if __name__ == "__main__":
    try:
        __main()
    except KeyboardInterrupt:
        pass
