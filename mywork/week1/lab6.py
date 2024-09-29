# Read JSON from internet
# Author Andre Hoarau
import requests
url ="https://api.coindesk.com/v1/bpi/currentprice.json"
response = requests.get(url)
data = response.json()
print (data)
