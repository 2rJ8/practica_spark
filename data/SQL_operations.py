import psycopg2

class SQL_DB:
    def __init__(self, host, user, password, database,port):
        self.connection = psycopg2.connect(
            host=host,
            user=user,
            port=port,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()

    def create_table(self,table,*atributes):
        create_table_query = f'CREATE TABLE IF NOT EXISTS {table} ('
        for i in atributes:
            create_table_query += f'{i} ,'
        create_table_query=create_table_query[:-1]
        create_table_query +=')'
        self.cursor.execute(create_table_query)
        self.connection.commit()

    def insert_data(self,table,item):
        if type(item) != dict:
            item=item.__dict__
        atributes=list(item.keys())
        atri= ''
        for i in atributes:
            atri += f'{i},'
        atri=atri[:-1]
        insert_query = f"INSERT INTO {table} ({atri}) VALUES ("
        data=list(item.values())
        data = tuple(data)
        fin ='%s)'
        for i in range (len(data)-1):
            fin = f'%s ,{fin}'
        insert_query += fin

        self.cursor.execute(insert_query, data)
        self.connection.commit()
        #Cogemos el id de la última fila insertada
        #item_id = self.cursor.lastrowid   , item_id
        return [*data]

    def get_all_data(self,table):
        select_all_query = f"SELECT * FROM {table}"
        self.cursor.execute(select_all_query)
        result = self.cursor.fetchall()
        items = []
        for row in result:            
            item = [*row[1:], row[0]]  #Cuidado con el orden
            items.append(item)
        return items

    def update_data(self,table,item):
        item=item.__dict__
        atri=list(item.keys())
        val=list(item.values())
        update_query = f"UPDATE {table} SET "
        fin = 'WHERE id=%s'
        for a in reversed(atri[:-1]):
            fin = f',{a}=%s {fin}'
        fin=fin[1:]
        update_query += fin
        self.cursor.execute(update_query, val)
        self.connection.commit()

    def delete_data(self, table,item_id):
        delete_query = f"DELETE FROM {table} WHERE id=%s"
        data = (item_id)
        self.cursor.execute(delete_query, data)
        self.connection.commit()
        
        
    def con_3(self,client):
            select_all_query = f"SELECT   r.rental_id as rentail,  r.rental_date as fecha,  c.name as cliente   FROM rentals as r,customers as c   WHERE c.customer_id = r.customer_id  AND c.name = '{client}'; "
            self.cursor.execute(select_all_query)
            result = self.cursor.fetchall()
            items = []
            for row in result:            
                items.append(row)
            return items
        
    def con_4(self,client):
            select_all_query = f"SELECT  ca.brand,  ca.model,  ca.year,  r.rental_date as fecha_alquiler,  c.name as cliente  FROM rentals as r,customers as c,cars as ca WHERE c.customer_id = r.customer_id AND r.car_id = ca.car_id AND c.  name = '{client}'; "
            self.cursor.execute(select_all_query)
            result = self.cursor.fetchall()
            items = []
            for row in result:            
                items.append(row)
            return items
        
    def con_5(self):
            select_all_query = f"SELECT   ca.brand,  ca.model,  ca.year  FROM cars as ca  WHERE ca.car_id in   (  SELECT    r.car_id   FROM rentals as r   GROUP BY r.car_id   HAVING COUNT(*) > 1); "
            self.cursor.execute(select_all_query)
            result = self.cursor.fetchall()
            items = []
            for row in result:            
                items.append(row)
            return items
          
    def con_7(self):
            select_all_query = f" SELECT    c.name  FROM customers as c   WHERE c.customer_id =    (   SELECT r.customer_id    FROM rentals as r    GROUP BY r.customer_id    ORDER BY COUNT(*) DESC LIMIT 1   );"
            self.cursor.execute(select_all_query)
            result = self.cursor.fetchall()
            items = []
            for row in result:            
                items.append(row)
                
            return items                
    def close_connection(self):
        self.cursor.close()
        self.connection.close()
