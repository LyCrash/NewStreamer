# NEWStreamer 

Real-time news streaming pipeline that ingests NewsAPI top headlines (US, FR, DE) every 5 minutes, streams them through Kafka, processes them with Logstash, indexes them in Elasticsearch for search and analytics via Kibana, and enables further large-scale storage and transformations using Spark or Hadoop.

NewsAPI → Kafka → Logstash → Elasticsearch → Kibana Pipeline --> Spark or Hadoop

This project demonstrates a complete data pipeline:

1. News data is pulled from [**NewsAPI**](https://newsapi.org/) using a Python producer.
2. Data is sent to a **Kafka topic**.
3. **Logstash** consumes data from Kafka and indexes it into **Elasticsearch**.
4. **Kibana** is used to visualize the data with dashboards and queries.

---

## **Prerequisites**

- Docker & Docker Compose installed
- Python 3.10+ (with `venv` recommended)
- Required Python packages:

```bash
pip install -r requirements.txt
```
---

## **Steps to launch the project**

1. Start the full pipline with Docker compose
```bash
docker compose up -d
```
2. Create a Kafka topic "newsapi"
```bash
docker exec -it kafka /opt/kafka/bin/kafka-topics.sh --create --topic newsapi --bootstrap-server localhost:9092
```
3. Verify that the topic exists
```bash
docker exec -it kafka /opt/kafka/bin/kafka-topics.sh --list --bootstrap-server localhost:9092
```
4. Launch the kafka producer
```bash
python kafka/kafka-producer-newsapi.py
```
5. Check Logstash is consuming
```bash
docker logs logstash --tail 50
```
6. Check ElasticSearch Indices
```bash
curl http://localhost:9200/_cat/indices?v
```
7. Explore Data in Kibana: http://localhost:5601

8. To Stop all containers (data saved inside containers):
```bash
docker compose stop
```
9. To Stop & Delete all containers:
```bash
docker compose down -v
```
