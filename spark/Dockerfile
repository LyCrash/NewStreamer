FROM apache/spark:3.5.0

WORKDIR /app

# Copier le jar Elasticsearch
COPY elasticsearch-spark-30_2.12-8.12.0.jar /opt/spark/jars/

# Copier le script Spark
COPY news_analysis.py /app/news_analysis.py
RUN mkdir -p /app/spark/output && chmod -R 777 /app/spark
# Ne rien lancer automatiquement
CMD ["sleep", "infinity"]
