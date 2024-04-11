from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json
from pyspark.sql.types import StructType, StringType, IntegerType, DoubleType

spark = SparkSession.builder \
    .appName("Streaming from Kafka") \
    .master("spark://spark-master:7077") \
    .config("spark.streaming.stopGracefullyOnShutdown", True) \
    .config('spark.jars.packages', 'org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.1') \
    .config("spark.sql.shuffle.partitions", 4) \
    .getOrCreate()
    
df =spark  \
  .readStream \
  .format("kafka") \
  .option("kafka.bootstrap.servers", "kafka:9093") \
  .option("subscribe", "sales_stream") \
  .load()
  

schema = StructType() \
    .add("timestamp", IntegerType()) \
    .add("store_id", IntegerType()) \
    .add("product_id", StringType()) \
    .add("quantity_sold", IntegerType()) \
    .add("revenue", DoubleType())

# Convert value column to JSON and apply schema
df = df.selectExpr("CAST(value AS STRING)") \
    .select(from_json("value", schema).alias("data")) \
    .select("data.*")

# Print schema of DataFrame for debugging
df.printSchema()

# Start the computation
query = df \
    .writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

# Wait for the termination of the query
query.awaitTermination()