import requests

# [ADVANCED] Trafic routier parisien
# url = https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/comptages-routiers-permanents/records?limit=20

# Flights: aviationstack api
# api_key = '41595288962800cd1756fc53d2f20442'
# url = 'https://api.aviationstack.com/v1/flights'
# params = {
#   'access_key': api_key
# }
# api_result = requests.get(url, params)


# NEWS API
api_key = 'd8918bd42ba043dd8d48974c64c86a13'
url = ('https://newsapi.org/v2/everything?'
       'q=Apple&'
       'from=2026-01-04&'
       'sortBy=popularity&'
       'apiKey=d8918bd42ba043dd8d48974c64c86a13')

api_result = requests.get(url)

api_response = api_result.json()

print(api_response)