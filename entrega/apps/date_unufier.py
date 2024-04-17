import os
import random
import string
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql import Window
def get_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def date_unifier (df,col,sav_col="timestamp_parsed",forat_1=None,format_2=None):
    df = df.withColumn('p1',F.to_date(F.col(col),forat_1))\
            .withColumn('p2',F.to_date(F.col(col),format_2))
    df = df.withColumn(sav_col,F.coalesce(F.col('p1'),F.col('p2')))\
            .drop(*['p1','p2'])
    return df

def drop_nonNum (df,col):
    
    w = Window().orderBy(F.lit('A'))
    df = df.withColumn("row_num", F.row_number().over(w))
    
    data=df.select(F.col(col).cast("int").isNotNull().alias("delete"))
    data = data.withColumn("row_num", F.row_number().over(w))
    
    df = df.join(data, "row_num", "inner")
    
    df=df.where(~df.delete == 'false')\
        .drop(*['row_num','delete'])
    return df

def drop_nonNum_2 (df,col):
    df = df.select("*").withColumn("row_num", F.monotonically_increasing_id())
    
    data=df.select("row_num",F.col(col).cast("int").isNotNull().alias("delete"))
    
    df = df.join(data, "row_num", "inner")
    
    df=df.where(~df.delete == 'false')\
        .drop(*['row_num','delete'])
    return df


def drop_Nan (df,col):
    
    w = Window().orderBy(F.lit('A'))
    df = df.withColumn("row_num", F.row_number().over(w))
    
    data=df.select(F.col(col).isNotNull().alias("delete"))
    data = data.withColumn("row_num", F.row_number().over(w))
    
    df = df.join(data, "row_num", "inner")
    
    df=df.where(~df.delete == 'false')\
        .drop(*['row_num','delete'])
    return df


def drop_Nan_2 (df,col):
    
    df = df.select("*").withColumn("row_num", F.monotonically_increasing_id())
    
    data=df.select("row_num",F.col(col).isNotNull().alias("delete"))
    
    df = df.join(data, "row_num", "inner")
    
    df=df.where(~df.delete == 'false')\
        .drop(*['row_num','delete'])
    return df

# Count words using PySpark
def clean_csv(filename):
    spark = SparkSession.builder \
            .master("spark://spark-master:7077") \
            .getOrCreate()
    
    df=spark.read.option("header", True).csv(filename)
    df.show()
    format_1="yyyy-MM-dd"
    format_2="dd-MM-yyyy"
    df = date_unifier(df,'Date','Date',format_1,format_2)
    df.show()
    for col in ['Store_ID','Product_ID','Quantity_Sold','Revenue']:
        df=drop_nonNum_2(df,col)
    df = drop_Nan_2(df,'Date')
    df.show()
    spark.stop()

if __name__ == "__main__":
    filename = "sales_data.csv"
    clean_csv(f'/opt/spark-data/{filename}')


