import sys
import requests

try:
    responses = requests.get("https://api.coincap.io/v2/assets/bitcoin")
except requests.RequestException:
    sys.exit('API Request Error')

try:
    if len(sys.argv) == 1:
        sys.exit("Missing command-line argument")
    number = float(sys.argv[1])
except:
    sys.exit("Command-line argument is not a number")


data = responses.json()
price = float(data['data']['priceUsd'])

result = price * number
print(f"${result:,.4f}")
