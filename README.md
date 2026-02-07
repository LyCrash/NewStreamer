# NewStreamer
Real-time news streaming pipeline that ingests NewsAPI top headlines (US, FR, DE) every 5 minutes, streams them through Kafka, processes them with Logstash, indexes them in Elasticsearch for search and analytics via Kibana, and enables further large-scale storage and transformations using Spark or Hadoop.
