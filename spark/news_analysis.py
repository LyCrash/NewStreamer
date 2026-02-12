from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col, count, to_date, length, avg, lower, explode, split
)

spark = SparkSession.builder \
    .appName("NewsAPI Spark Analysis") \
    .config("spark.jars", "/opt/spark/jars/elasticsearch-spark-30_2.12-8.12.0.jar") \
    .config("spark.es.nodes", "elasticsearch") \
    .config("spark.es.port", "9200") \
    .config("spark.es.nodes.wan.only", "true") \
    .getOrCreate()


# ========================
# LOAD DATA FROM ELASTIC
# ========================
df = spark.read \
    .format("org.elasticsearch.spark.sql") \
    .option("es.resource", "newsapi-*") \
    .load()

df.cache()

print("=== SCHEMA ===")
df.printSchema()

# ========================
# 1. NEWS BY SOURCE
# ========================
news_by_source = df.groupBy("source") \
    .agg(count("*").alias("nb_news")) \
    .orderBy(col("nb_news").desc())

news_by_source.show(10)

news_by_source.coalesce(1).write \
    .mode("overwrite") \
    .option("header", "true") \
    .csv("spark/output/news_by_source")


# ========================
# 2. NEWS BY DAY
# ========================
news_by_day = df.withColumn(
    "date", to_date("published_at")
).groupBy("date") \
 .count() \
 .orderBy("date")

news_by_day.show()
news_by_day.coalesce(1).write \
    .mode("overwrite") \
    .option("header", "true") \
    .csv("spark/output/news_by_day")

# ========================
# 3. TOP AUTHORS
# ========================
top_authors = df.filter(col("author").isNotNull()) \
    .groupBy("author") \
    .count() \
    .orderBy(col("count").desc()) \
    .limit(20)
top_authors.show()

top_authors.coalesce(1).write \
    .mode("overwrite") \
    .option("header", "true") \
    .csv("spark/output/top_authors")

# ========================
# 4. TOP KEYWORDS
# ========================
keywords = df.select(
    explode(
        split(lower(col("title")), " ")
    ).alias("word")
)

filtered_keywords = keywords.filter(
    (length(col("word")) > 4) &
    (~col("word").isin(
        "about", "their", "there", "which", "would", "could", "https", "after"
    ))
)

top_keywords = filtered_keywords.groupBy("word") \
    .count() \
    .orderBy(col("count").desc()) \
    .limit(20)
top_keywords.show()

top_keywords.coalesce(1).write \
    .mode("overwrite") \
    .option("header", "true") \
    .csv("spark/output/top_keywords")

# ========================
# 5. CONTENT STATS
# ========================
content_stats = df.select(
    avg(length("content")).alias("avg_content_length"),
    avg(length("title")).alias("avg_title_length")
)

content_stats.show()

content_stats.coalesce(1).write \
    .mode("overwrite") \
    .option("header", "true") \
    .csv("spark/output/content_stats")
spark.stop()
