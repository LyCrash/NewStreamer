"""
Kafka Producer

Extract news data from NewsAPI (https://newsapi.org) and send to Kafka.
"""

import time
import json
import requests
from kafka import KafkaProducer
import os
from dotenv import load_dotenv

KAFKA_BOOTSTRAP_SERVER = "localhost:9092"
KAFKA_TOPIC = "newsapi"

def kafka_producer() -> KafkaProducer:
    return KafkaProducer(
        bootstrap_servers=[KAFKA_BOOTSTRAP_SERVER],
        value_serializer=lambda x: json.dumps(x).encode("utf-8")
    )

def get_news(endpoint: str) -> list[dict]:
    """
    Request data from NewsAPI and return list of articles
    """
    response = requests.get(endpoint, timeout=10)
    response.raise_for_status()
    data = response.json()

    articles = []
    for article in data.get("articles", []):
        articles.append({
            "created_at": time.strftime("%Y-%m-%d %H:%M:%S"),
            "source": article["source"]["name"],
            "author": article.get("author"),
            "title": article.get("title"),
            "description": article.get("description"),
            "url": article.get("url"),
            "published_at": article.get("publishedAt")
        })

    return articles

def main():
    # Find the .env file and load the variables into the environment
    load_dotenv()
    newsapi_key = os.getenv("NEWSAPI_KEY")

    # Launch the kafka producer
    producer = kafka_producer()

    countries = ["us", "fr", "de"]
    poll_interval = 300  # 5 minutes (important: rate limits)

    while True:
        for country in countries:
            endpoint = (
                f"https://newsapi.org/v2/top-headlines"
                f"?country={country}&apiKey={newsapi_key}"
            )

            articles = get_news(endpoint)
            print("Articles scrapped successfully !")

            for article in articles:
                producer.send(KAFKA_TOPIC, value=article)
                print(f"Published: {article['title']}")

        producer.flush()
        print(f"Waiting {poll_interval} seconds...\n")
        time.sleep(poll_interval)

if __name__ == "__main__":
    main()
