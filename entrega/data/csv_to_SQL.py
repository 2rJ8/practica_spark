from data.SQL_operations import SQL_DB
from data.csv_operations import csv_op

def csv_to_SQL(tabla,data_csv,SQL_DB):
    data = data_csv.read_csv_file()
    for i,dat in enumerate(data):
        properties={}
        if i:
            for j,val in enumerate(dat):
                properties[data[0][j]]=val
            SQL_DB.insert_data(tabla,properties)