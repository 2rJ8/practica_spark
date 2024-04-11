import os
import random
import string
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql import functions as F

def get_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def to_date_(col, formats=("dd-MM-yyyy", "yyyy-MM-dd")):
    # Spark 2.2 or later syntax, for < 2.2 use unix_timestamp and cast
    return coalesce(*[to_date(col, f) for f in formats])

# Count words using PySpark
def clean_csv(filename):
    spark = SparkSession.builder \
            .master("spark://spark-master:7077") \
            .getOrCreate()
    
    df = spark.read.option("header", True).csv(filename)
    df=df.filter((col("Quantity_Sold").rlike("[^a-zA-Z]"))&(col("Product_ID").rlike("[^a-zA-Z]"))&(col("Store_ID").rlike("[^a-zA-Z]"))&(col("Revenue").rlike("[^a-zA-Z]")))
    df=df.withColumn("Date", to_date_("Date"))
    df.show()
    
    spark.stop()

if __name__ == "__main__":
    filename = "sales_data.csv"
    clean_csv(f'/opt/spark-data/{filename}')



'''
result_df \
    .write \
    .partitionBy('my_column') \
    .option('fs.s3a.committer.name', 'partitioned') \
    .option('fs.s3a.committer.staging.conflict-mode', 'replace') \
    .option("fs.s3a.fast.upload.buffer", "bytebuffer") \ # Buffer in memory instead of disk, potentially faster but more memory intensive
    .mode('overwrite') \
    .csv(path='s3a://mybucket/output', sep=',')
'''