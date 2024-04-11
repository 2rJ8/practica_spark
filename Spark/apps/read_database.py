from pyspark.sql import SparkSession

def read_from_postgres():
    spark = SparkSession.builder \
        .appName("ReadFromPostgres") \
        .config("spark.driver.extraClassPath", "/opt/spark-apps/postgresql-42.7.3.jar") \
        .master("spark://spark-master:7077") \
        .config("spark.jars","postgresql-42.7.3.jar") \
        .getOrCreate()

    # Define connection properties
    jdbc_url = "jdbc:postgresql://spark-database-1:5432/retail_db"
    connection_properties = {
        "user": "postgres",
        "password": "casa1234",
        "driver": "org.postgresql.Driver"
    }

    # Define table name
    table_name = "ExampleData"

    try:
        # Read data from PostgreSQL table into a DataFrame
        df = spark.read.jdbc(url=jdbc_url, table=table_name, properties=connection_properties)

        # Show the DataFrame
        df.show()

    except Exception as e:
        print("Error reading data from PostgreSQL:", e)

    finally:
        # Stop SparkSession
        spark.stop()

if __name__ == "__main__":
    read_from_postgres()