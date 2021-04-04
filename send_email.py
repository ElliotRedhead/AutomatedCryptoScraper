import os
import requests
from dotenv import load_dotenv
load_dotenv()

mailgun_api = os.environ["MAILGUN_API"]
mailgun_domain = os.environ["MAILGUN_DOMAIN"]


# Currently emails go to spam, and using a sandbox domain should not be used in production.

def send_email(recipient_addresses, subject, text):
    """Send an email to target email addresses.

    Parameters:
    recipient_addresses (list): Target email address strings.

    Returns:
    Response code.

    """
    auth = ("api", mailgun_api)
    data = {
        "from": f"Automated Binance Announcement <mailgun@{mailgun_domain}>",
        "to": recipient_addresses,
        "subject": subject,
        "text": text
        }
    return requests.post(
        f"https://api.mailgun.net/v3/{mailgun_domain}/messages",
        auth=auth,
        data=data
        )

def construct_coin_announcement(coin, users_dicts):
    recipient_addresses = []
    for user_dict in users_dicts:
        recipient_addresses.append(user_dict['email'])
    subject = f"Binance: {coin} Coin Innovation Zone Listing"
    text = f"A coin ({coin}) has been announced for release on the Binance Innovation zone. \n View the new crypto listings news here: https://www.binance.com/en/support/announcement/c-48?navId=48"

    send_email(recipient_addresses, subject, text)