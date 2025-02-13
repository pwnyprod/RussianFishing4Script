import logging
import os
import smtplib
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from _socket import gaierror
from dotenv import load_dotenv

from notification_provider.abstract_messaging_method import MessagingMethod

logger = logging.getLogger(__name__)

class EmailMethod(MessagingMethod):
    def __init__(self, recipient: str):
        load_dotenv()

        self.recipient = recipient
        self.password = os.getenv("PASSWORD")
        self.smtp_server_name = os.getenv("SMTP_SERVER")
        self.sender = os.getenv("EMAIL")
        self._validate_smtp_connection()

    def send_message(self, message: str) -> None:
        msg = MIMEMultipart()
        msg["Subject"] = "RussianFishing4Script: Notification"
        msg["From"] = self.sender
        msg["To"] = self.recipient
        msg.attach(MIMEText(message, "html"))

        # send email with SMTP
        with smtplib.SMTP_SSL(self.smtp_server_name, 465) as smtp_server:
            # smtp_server.ehlo()
            smtp_server.login(self.sender, self.password)
            smtp_server.sendmail(self.sender, self.recipient, msg.as_string())
        print("A notification email has been sent to your email address")

    def _validate_smtp_connection(self) -> None:
        """Validate email configuration in .env."""
        logger.info("Validating SMTP connection")
        if not self.smtp_server_name:
            logger.error("SMTP_SERVER is not specified")
            sys.exit()
        try:
            with smtplib.SMTP_SSL(self.smtp_server_name, 465) as smtp_server:
                smtp_server.login(self.sender, self.password)
        except smtplib.SMTPAuthenticationError:
            logger.error("Email address or password not accepted")
            print(
                (
                    "Please configure your email address and password in .env\n"
                    "If Gmail is used, please refer to "
                    "https://support.google.com/accounts/answer/185833 \n"
                    "to get more information about app password authentication"
                )
            )
            sys.exit()
        except (TimeoutError, gaierror):
            logger.error("Invalid SMTP Server or connection timed out")
            sys.exit()