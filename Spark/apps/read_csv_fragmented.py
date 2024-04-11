from pyspark.sql import SparkSession

spark = SparkSession.builder \
        .master("spark://spark-master:7077") \
        .getOrCreate()
path="./borrar/"
#path="./test.csv"
df = spark.read.csv(path).selectExpr("_c0 as timestamp", "_c1 as store_id", "_c2 as product_id", "_c3 as quantity_sold", "_c4 as revenue")
df.show()