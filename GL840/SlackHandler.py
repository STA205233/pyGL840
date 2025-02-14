from slack_sdk import WebClient


class SlackHandler:
    def __init__(self, token):
        self.client = WebClient(token=token)

    def send_message(self, channel, message):
        return self.client.chat_postMessage(channel=channel, text=message)
    
    def delete_message(self, channel, ts):
        return self.client.chat_delete(channel=channel, ts=ts)

    def test(self):
        response = self.client.auth_test()
        return response["ok"]
