from slack_sdk import WebClient


class SlackHandler:
    def __init__(self, token):
        self.client = WebClient(token=token)

    def send_message(self, channel, message):
        self.client.chat_postMessage(channel=channel, text=message)
