from urllib.request import urlopen
from bs4 import BeautifulSoup
import sys
import re
import json

# Specify target URL
target_page = 'https://www.binance.com/en/support/announcement/c-48?navId=48'

# Query the website and return the HTML
page_response = urlopen(target_page)

# Open output file
if sys.argv[1:]:
    file_output_name = sys.argv[1]
else:
    file_output_name = "output"
# f = open(file_output_name+".json", "w+")

# Parse the HTML using BeautifulSoup
parsed_html = BeautifulSoup(page_response, "html.parser")
target_tag = parsed_html.find(
    "script", type="application/json", id="__APP_DATA")
target_json = json.loads(target_tag.string)

# f.write(target_tag.string)
print(target_json["routeProps"]["b723"]["navDataResource"][0]["articles"][0])
# for line in parsed_html:
#     f.write(line)

# f.close()
