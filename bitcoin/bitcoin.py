import json
import requests
import sys

if len(sys.argv) == 1:
    sys.exit("Missing command-line argument")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
else:
    if sys.argv[1].replace(".", "", 1).isnumeric():        #if removing the decimal for a float yields just a number:
        if float(sys.argv[1]) >= 0:
            try:
                response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
                data = response.json()
                usd_amount = data["bpi"]["USD"]["rate_float"]     #bpi --> usd --> rate_float
                converted_result = (float(sys.argv[1]) * usd_amount)
                print(f"${converted_result:,.4f}")                     #four decimal places, thousands separated with comma
            except requests.RequestException:
                None
    else:
        sys.exit("Command-line argument is not a number")
