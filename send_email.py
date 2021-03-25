import requests
from dotenv import load_dotenv
load_dotenv()
import os

mailgun_api=os.environ['MAILGUN_API']
mailgun_domain=os.environ['MAILGUN_DOMAIN']

#
def send_email(recipient_addresses):
    """Send an email to target email addresses.

    Parameters:
    recipient_addresses (list): Target email address strings.

    Returns:
    Response code.

    """
    return requests.post(
        f"https://api.mailgun.net/v3/{mailgun_domain}/messages",
        auth=("api", mailgun_api),
        data={"from": f"Sender <elliotn@{mailgun_domain}>",
              "to": recipient_addresses,
              "subject": "Hello",
              "text": "Testing some Mailgun awesomness!"})


print(send_email(["test@domain.com", "test2@domain.com"]))
