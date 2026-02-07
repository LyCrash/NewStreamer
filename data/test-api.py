import requests
import os
import json
from dotenv import load_dotenv
from datetime import datetime, timedelta

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

#country = "us"
# url = (f"https://newsapi.org/v2/top-headlines?"
#        f"country={country}&"
#        f"apiKey={api_key}")

topics = "technology OR AI OR innovation"
url = (f"https://newsapi.org/v2/everything?"
       f"q={topics}&"  # Broad tech topics for varied content
       f"language=en&"  # Consistent language for text analysis
       f"sortBy=publishedAt&"  # Good for time series analysis
       f"from={(datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')}&"  # Last 7 days
       f"to={datetime.now().strftime('%Y-%m-%d')}&"  # Up to today
       f"apiKey={api_key}")

try:
    # Make the API request
    api_result = requests.get(url)
    api_result.raise_for_status()  # Raise an exception for bad status codes
    
    api_response = api_result.json()
    
    # Print the response (optional)
    print("API Response received successfully!")
    
    # Create a filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"news_results_{timestamp}.json"

    # Define the filepath
    data_dir = "data"
    # Create the data directory if it doesn't exist
    os.makedirs(data_dir, exist_ok=True)
    filepath = os.path.join(data_dir, filename)
    
    # Save to JSON file
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(api_response, f, indent=4, ensure_ascii=False)
    
    print(f"Results saved to {filename}")
    
    # Optional: Print basic statistics
    if 'articles' in api_response:
        print(f"Number of articles retrieved: {len(api_response['articles'])}")
        
except requests.exceptions.RequestException as e:
    print(f"Error making API request: {e}")
except json.JSONDecodeError as e:
    print(f"Error decoding JSON response: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")