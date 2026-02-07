import requests
import os
from dotenv import load_dotenv

# Find the .env file and load the variables into the environment
load_dotenv()

# [ADVANCED] Trafic routier parisien
# url = https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/comptages-routiers-permanents/records?limit=20

# Flights: aviationstack api
# api_key = os.getenv("FLIGHTS_KEY")
# url = 'https://api.aviationstack.com/v1/flights'
# params = {
#   'access_key': api_key
# }
# api_result = requests.get(url, params)


# NEWS API
api_key = os.getenv("NEWSAPI_KEY")
query = "Apple"
date = "2026-02-04"
url = (f"https://newsapi.org/v2/everything?"
       f"q={query}&"
       f"from={date}&"
       f"sortBy=popularity&"
       f"apiKey={api_key}")

api_result = requests.get(url)

api_response = api_result.json()

print(api_response)