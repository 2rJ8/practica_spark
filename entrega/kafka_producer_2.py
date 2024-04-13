from time import sleep
from json import dumps
from kafka import KafkaProducer
from datetime import datetime
import random

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: dumps(x).encode('utf-8'))

while True:
    
    #[TODO]Tienes que cambiarlo para hacer todos los campos random
    message = {
        "timestamp": int(datetime.now().timestamp()),
        "store_id": random.randint(0,60),
        "product_id": random.randint(0,60),
        "quantity_sold": random.randint(1,100),
        "revenue": random.randint(300,50000)
    }
    producer.send('sales_stream', value=message)
    sleep(1)  # Adjust frequency as needed
