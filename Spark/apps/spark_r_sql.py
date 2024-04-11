from pyspark.sql import SparkSession
from pyspark.sql.functions import col,date_format


def init_spark():
  sql = SparkSession.builder\
    .master("spark://spark-spark-master-1:7077")\
    .appName("trip-app")\
    .config("spark.driver.extraClassPath", "/opt/spark-apps/postgresql-42.7.3.jar") \
    .config("spark.jars","postgresql-42.7.3.jar") \
    .getOrCreate()
  sc = sql.sparkContext
  return sql,sc

def main():
    url = "jdbc:postgresql://spark-database-1:5432/retail_db"
    properties = {
        "user": "postgres",
        "password": "casa1234",
        "driver": "org.postgresql.Driver"
    }
  
    sc = init_spark()
    table_name = "stores"
    
    df = sc[0].read.jdbc(url=url, table=table_name, properties=properties)
    df.filter((df.location != "") & (df.store_name != "") & (df.demographics != "")).distinct().write.csv("BORRAR")
    sc[0].stop()
  
  
if __name__ == '__main__':
  main()