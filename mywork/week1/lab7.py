# Modify the code to ensure that the output is the current price in euro
# Author Andre Hoarau
import requests
url ="https://api.coindesk.com/v1/bpi/currentprice.json"
response = requests.get(url)
data = response.json()
print(data['bpi']['EUR']['rate_float'])