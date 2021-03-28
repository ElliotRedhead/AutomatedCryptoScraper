import db_functions
import os
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import json
from dotenv import load_dotenv
load_dotenv()

target_webpage = os.environ["TARGET_WEBPAGE"]


def scrape_page(url):
    # Query the website and return the HTML
    try:
        page_response = urlopen(url)
        # Parse the HTML using BeautifulSoup
        parsed_html = BeautifulSoup(page_response, "html.parser")
        # Find specific script tag
        target_tag = parsed_html.find(
            "script", type="application/json", id="__APP_DATA")
        target_json = json.loads(target_tag.string)
    except:
        print("A scraping error occurred, no results were produced.")
        # Log the error to a table
    return target_json


def get_target_dict(parsed_json):
    return(parsed_json["routeProps"]["b723"]["navDataResource"][0]["articles"][0])


if __name__ == "__main__":
    parsed_json = scrape_page(target_webpage)
    target_dict = get_target_dict(parsed_json)

    coin_regex = re.search(r"\(([A-Z]+)\)", target_dict["title"])
    coin = coin_regex.group()
    column_values = (target_dict["title"], coin, "now()")
    db_functions.insert_announcement_record("database", column_values)
