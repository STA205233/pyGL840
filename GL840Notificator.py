#! /usr/bin/env python3

import GL840.MongoDBHandler as Mongo
import GL840.Warning as w
import os
import enum
import time
from GL840.Converter import conversion_OX600, conversion_PKR251, conversion_MPT200AR, conversion_APR262
from typing import Callable
try:
    import GL840.SlackHandler as Slack
    from slack_sdk.errors import SlackClientError
    slack_ON = True
except ImportError:
    slack_ON = False

slack_channel = "tesaaaaa"


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


class MODE(enum.Enum):
    Normal = 1
    Vacuuming = 2
    Filling = 3
    Experiment = 4


status_sound = {STATUS.Emergency: StatusSound([1000.0, 2000.0], [0.1, 0.1], 1), STATUS.Warning: StatusSound([440, 0], [1, 1], 1), STATUS.Information: None, STATUS.Normal: None}


class ErrorManager():
    def __init__(self, section_name: str, data_name: str, func: Callable[..., STATUS], slack: Slack.SlackHandler | None = None, slack_channel="", warning: bool = True, unit: str = "", item_name: str = "", conv_func: Callable[..., float] = lambda x: x) -> None:
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
        value = self.func(self.conv_func(data[self.section_name][self.data_name]), **kwargs)
        if value == STATUS.Warning:
            status = STATUS.Warning
        elif value == STATUS.Emergency:
            status = STATUS.Emergency
        elif value == STATUS.Information:
            status = STATUS.Information
        elif value == STATUS.Normal:
            status = STATUS.Normal
        if self.status != status:
            if status != STATUS.Normal and status != STATUS.Information:
                string = f"{status.name}: {self.item_name} is {self.conv_func(data[self.section_name][self.data_name]):.2e} {self.unit}"
                self.__notify_slack(slack_channel, string)
                print(string)
            elif status == STATUS.Normal:
                string = f"Status goes back to normal\n{self.item_name} is {self.conv_func(data[self.section_name][self.data_name]):.2e} {self.unit}"
                self.__notify_slack(slack_channel, string)
                print(string)
            else:
                string = f"Information: {self.item_name} is {self.conv_func(data[self.section_name][self.data_name]):.2e} {self.unit}"
                self.__notify_slack(slack_channel, string)
                print(string)
            self.status = status

    def __notify_slack(self, channel, string):
        if self.slack is not None:
            try:
                self.slack.send_message(channel, string)
            except SlackClientError as e:
                print(e)


class ErrorManagerCollection():
    def __init__(self, warning) -> None:
        self.__error_managers: list[ErrorManager] = []
        self.__status = STATUS.Normal
        self.__status_sound = STATUS.Normal
        self.__warning = warning

    def register(self, error_manager: ErrorManager) -> None:
        self.__error_managers.append(error_manager)

    def __call__(self, data, **kwargs) -> None:
        is_all_normal = True
        is_state_changed = False
        for error_manager in self.__error_managers:
            error_manager(data, **kwargs)
            if error_manager.status.value > self.__status.value:
                self.__status = error_manager.status
            if error_manager.warning:
                if error_manager.status.value > self.__status_sound.value:
                    self.__status_sound = error_manager.status
                    is_state_changed = True
                if error_manager.status != STATUS.Normal:
                    is_all_normal = False
        if is_all_normal:
            self.__status_sound = STATUS.Normal
            self.__warning.stop()
        else:
            sound = status_sound[self.__status_sound]
            if sound is not None and is_state_changed:
                self.__notify_sound(sound.frequency, sound.second, sound.volume, "")

    def __notify_sound(self, frequency, second, volume, message, blocking=False):
        if self.__warning is not None:
            self.__warning(frequency, second, volume, message, blocking)
        else:
            print(message)


def oxygen(value):
    if value < 0:
        return STATUS.Information
    elif value < 18.0:
        return STATUS.Emergency
    elif value < 19.0:
        return STATUS.Warning
    else:
        return STATUS.Normal


def outer_pressure(value):
    if value > 1e-2:
        return STATUS.Emergency
    elif value > 1e-3:
        return STATUS.Warning
    else:
        return STATUS.Normal


def inner_pressure_in_LAr(v):
    print(v)
    if v > 1.8:
        return STATUS.Emergency
    elif v > 1.5:
        return STATUS.Warning
    else:
        return STATUS.Normal


def inner_vacuum(value):
    if value > 1e3:
        return STATUS.Emergency
    elif value > 1e2:
        return STATUS.Warning
    else:
        return STATUS.Normal


def construct_error_managers(mode, warning, slack, slack_channel, mongo):
    error_managers = ErrorManagerCollection(warning)
    print("Condition to alert:")
    error_managers.register(ErrorManager("GL840", "Ch5", oxygen, slack, slack_channel, True, "%", "Oxygen", conversion_OX600))
    print("\tOxygen: 0--18% Emergency, 18--19% Warning")
    if (mode == MODE.Normal):
        pass
    elif (mode == MODE.Vacuuming):
        error_managers.register(ErrorManager("GL840", "Ch2", inner_vacuum, slack, slack_channel, True, "Pa", "Inner Vacuum", conversion_MPT200AR))
        print("\tInner Vacuum: 100--1000 Pa Warning, >1000 Pa Emergency")
    elif (mode == MODE.Filling or mode == MODE.Experiment):
        error_managers.register(ErrorManager("GL840", "Ch3", inner_pressure_in_LAr, slack, slack_channel, True, "Bar", "Inner Pressure"))
        print("\tInner Pressure: 1.5--1.8 Bar Warning, >1.8 Bar Emergency")
    if mode == MODE.Experiment:
        error_managers.register(ErrorManager("GL840", "Ch1", outer_pressure, slack, slack_channel, True, "Pa", "Outer Pressure", conversion_PKR251))
        print("\tOuter Pressure: 1e-3--1e-2 Pa Warning, >1e-2 Pa Emergency")
    return error_managers


def __main(mode):
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
    error_managers = construct_error_managers(mode, warning, slack, slack_channel, mongo)

    while True:
        data = mongo.pull_one()
        if data is None:
            continue
        error_managers(data)
        time.sleep(1)


def __select_mode() -> int:
    print("Select the mode")
    print("0: Exit")
    print("1: Normal mode (No vacuuming, no LAr in the chamber)")
    print("2: Vacuuming mode (No LAr in the chamber, vacuuming in progress)")
    print("3: Filling mode (LAr is being filled)")
    print("4: Experiment mode (LAr is in the chamber)")
    while True:
        try:
            mode = int(input())
            if mode < 0 or mode > 4:
                raise ValueError
            break
        except ValueError:
            print("Invalid input")
    return mode


if __name__ == "__main__":
    while True:
        mode = __select_mode()
        try:
            if mode == 0:
                break
            __main(MODE(mode))
        except KeyboardInterrupt:
            pass
