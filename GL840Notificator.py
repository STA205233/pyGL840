#! /usr/bin/env python3

import GL840.MongoDBHandler as Mongo
import GL840.Warning as w
import os
import enum
try:
    import GL840.SlackHandler as Slack
    slack_ON = True
except ImportError:
    slack_ON = False

channel = "grams"


class ALERTCATEGORY(enum.Enum):
    Warning = enum.auto(),
    Emergency = enum.auto(),
    Notice = enum.auto(),
    Information = enum.auto()


def __notify_slack(slack, item, value, channel, type=ALERTCATEGORY):
    if slack_ON:
        slack.send_message(channel, f"{type.name}: {item} is {value}")


def __notify_sound(warning, frequency, second, volume, message):
    warning(frequency, second, volume, message)


def __notify(slack, warning, data):
    if float(data["Oxygen"]) < 19:
        __notify_slack(slack, "Oxygen", data["Oxygen"], channel)
        __notify_sound(warning, [1000, 2000], [0.5, 0.5], 1, f"Oxygen is Low({data['Oxygen']})")


def __main():
    mongo = Mongo.MongoDBPuller("192.168.160.8", 27017, "GL840", "GL840")
    warning = w.Warning()
    if slack_ON:
        slack = Slack.SlackHandler(os.environ['SLACK_TOKEN'])
    else:
        slack = None
    while True:
        data = mongo.pull_one()
        __notify(slack, warning, data)


if __name__ == "__main__":
    try:
        __main()
    except KeyboardInterrupt:
        pass
