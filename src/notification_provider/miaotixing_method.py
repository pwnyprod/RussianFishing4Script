import json
import logging
import os
from urllib import parse, request

from dotenv import load_dotenv
from notification_provider.abstract_messaging_method import MessagingMethod

logger = logging.getLogger(__name__)
class MiaotixingMethod(MessagingMethod):
    miao_code: str | None

    def __init__(self):
        load_dotenv()
        self.miao_code = os.getenv("MIAO_CODE")

    def send_message(self, message: str):
        """Send a notification Message to the user's miaotixing service."""
        text = "Cause of termination:" + message

        url = "http://miaotixing.com/trigger?" + parse.urlencode(
            {"id": self.miao_code, "text": text, "type": "json"}
        )

        with request.urlopen(url) as page:
            result = page.read()
            json_object = json.loads(result)
            if json_object["code"] == 0:
                print("A notification message to the user's miaotixing service.")
            else:
                print(
                    "Sending failed with error code:"
                    + str(json_object["code"])
                    + ", Description:"
                    + json_object["msg"]
                )
