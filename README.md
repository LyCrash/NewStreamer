# NEWStreamer 

**NEWStreamer** is a real-time news streaming pipeline that ingests technology-related articles from NewsAPI every 5 minutes, streams them through Kafka, processes them with Logstash, indexes them in Elasticsearch for search and analytics via Kibana, and is designed to be extended with Spark or Hadoop for large-scale processing and advanced analytics.

**Pipeline overview:**
NewsAPI → Kafka → Logstash → Elasticsearch → Kibana → Spark (Batch Analytics)
---

## 📌 TL;DR / Index

- [Project Overview](#project-overview)
- [Architecture & Design Choices](#architecture--design-choices)
  - [1. NewsAPI – Data Source](#1-newsapi--data-source)
  - [2. Kafka – Streaming Layer](#2-kafka--streaming-layer)
  - [3. Logstash – Stream Processing](#3-logstash--stream-processing)
  - [4. Elasticsearch – Storage & Search](#4-elasticsearch--storage--search)
  - [5. Kibana – Visualization & Analytics](#5-kibana--visualization--analytics)
  - [6. Spark / Hadoop – Future Extension](#6-spark--hadoop--future-extension)
- [Prerequisites](#prerequisites)
- [Steps to Launch the Project](#steps-to-launch-the-project)
- [Stopping the Pipeline](#stopping-the-pipeline)

---

## Project Overview

This project demonstrates a complete **real-time data engineering pipeline** built with widely used industry tools.  
It focuses on **continuous ingestion**, **stream processing**, **search and analytics**, and **scalability**.

The system periodically fetches news articles related to **technology, AI, and innovation**, streams them reliably through Kafka, processes them using Logstash, and stores them in Elasticsearch where they can be queried and visualized using Kibana dashboards.



## Architecture & Design Choices

### 1. NewsAPI – Data Source

**What it does**  
NewsAPI is used as the external data source providing real-world, continuously updated news articles.

**How it works**  
A Python Kafka producer queries the NewsAPI **`/v2/everything`** endpoint every **5 minutes (300 seconds)**.  
The query is configured to:
- Focus on **technology-related topics** (technology, AI, innovation)
- Use **English language articles** for consistent text analysis
- Fetch up to **100 articles per request**
- Sort articles by **publication date**
- Restrict results to the **last 7 days** to ensure relevance

**Why this choice**  
- Provides realistic unstructured text data
- Suitable for full-text search, fuzzy queries, and time-series analysis
- Free tier is sufficient for a streaming demo

Each fetched article is converted into a structured JSON message and sent to Kafka.

---

### 2. Kafka – Streaming Layer

**What it does**  
Kafka acts as the **central streaming backbone** of the pipeline.

**How it works**  
- The **Python producer** publishes messages to a predefined Kafka topic named **`newsapi`**
- Kafka stores messages in an append-only log
- Consumers can independently read the stream at their own pace

**Why Kafka**  
- Decouples data producers from consumers
- Provides fault tolerance and replayability
- Allows easy integration with multiple downstream systems (Logstash, Spark, etc.)

An interesting **Kafka consumer** script (independent from the pipeline) is also provided to manually inspect and experiment with streamed messages.

---

### 3. Logstash – Stream Processing

**What it does**  
Logstash consumes data from Kafka, applies transformations, and forwards it to Elasticsearch.

**How it works**  
Logstash subscribes to the `newsapi` Kafka topic and processes each message with the following logic:

- If the article contains a `published_at` field:
  - It is parsed as an ISO8601 date
  - Stored in the special `@timestamp` field
- Otherwise:
  - The `created_at` field is used as a fallback timestamp

This ensures that **all documents are time-aligned**, which is essential for time-series analysis and Kibana visualizations.

**Why Logstash**  
- Native Kafka integration
- Powerful filtering and transformation capabilities
- Designed for Elasticsearch ingestion

---

### 4. Elasticsearch – Storage & Search

**What it does**  
Elasticsearch stores indexed articles and enables fast search, aggregations, and analytics.

**Indexing strategy (configured in logstash output)**
- Monthly rolling indices: `newsapi-YYYY.MM`
This prevents indices from growing indefinitely and improves performance.

- Deterministic document IDs: `document_id = article URL`
This ensures **idempotent writes**:  
if NewsAPI returns the same article again, it updates the existing document instead of creating duplicates.

**Why this design**
- Scales well over time
- Avoids duplicate documents caused by periodic polling
- Aligns with Elasticsearch best practices

---

### 5. Kibana – Visualization & Analytics

**What it does**  
Kibana provides an interactive UI to explore and visualize data stored in Elasticsearch.

**What can be done**
- Full-text search on article titles and content
- Fuzzy and partial word matching
- Aggregations (articles per source, per day, etc.)
- Time-series visualizations (news volume over time)

Kibana dashboards turn raw streamed data into actionable insights.

---

### 6. Spark – Batch Analytics (Dockerized)
### 6. Spark – Batch Analytics (Dockerized)

Apache Spark is used in this project to perform **batch analytics** on data that has already been indexed in Elasticsearch.

The Spark job reads data directly from Elasticsearch indices (`newsapi-*`) using the Elasticsearch-Hadoop connector.  
It is executed **inside a Docker container**, ensuring full reproducibility without requiring a local Spark installation.

The batch processing computes several analytical results, including:
- Number of news articles per source
- Number of articles per day
- Top authors by article count
- Most frequent keywords in article titles
- Average length of article content and titles

The results are exported as **CSV files** to a shared Docker volume, making them directly accessible on the host machine.

This batch processing step is intentionally executed **after** the real-time streaming pipeline (Kafka → Logstash → Elasticsearch) to avoid race conditions and ensure that data is available before analysis.

Future work will include:
- Reading directly from Kafka topics
- Persisting data to distributed storage
- Performing large-scale transformations and analytics

---

## **Prerequisites**

- Docker & Docker Compose installed
- Create `.env` file on root folder and add your NEWSAPI_KEY 
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

8. Run Spark batch analytics (after data is indexed in Elasticsearch)
```bash
docker exec -it spark /opt/spark/bin/spark-submit /app/news_analysis.py

## **Stopping the pipeline**

9. To Stop all containers (data saved inside containers):
```bash
docker compose stop
```
10. To Stop & Delete all containers:
```bash
docker compose down -v
```
