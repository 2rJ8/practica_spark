from data.SQL_operations import SQL_DB
from data.csv_to_SQL import *

DB_HOST = "localhost"
DB_USER = "postgres"
DB_PASSWORD = "casa1234"
DB_DATABASE = "retail_db"
DB_PORT= "5432"    
tabla="Stores"
MYSQL_DB=SQL_DB(DB_HOST,DB_USER,DB_PASSWORD,DB_DATABASE,DB_PORT)

MYSQL_DB.create_table(tabla,'store_id integer PRIMARY KEY','store_name VARCHAR(55)','location VARCHAR(55)','demographics VARCHAR(55)')
csv_data=csv_op('./eval_3/Apli_BD/retail.csv')
csv_to_SQL(tabla,csv_data,MYSQL_DB)
MYSQL_DB.close_connection()