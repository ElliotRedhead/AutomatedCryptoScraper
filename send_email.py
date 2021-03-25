import requests


def send_email():
    return requests.post(
        "https://api.mailgun.net/v3/domain/messages",
        auth=("api", "apikey"),
        data={"from": "Sender <mailgun@domain>",
              "to": ["recipient@domain.com"],
              "subject": "Hello",
              "text": "Testing some Mailgun awesomness!"})


send_email()
