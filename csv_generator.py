import csv
import random
import string

def create_csv_file(filename,data):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)


def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str
    
    
data = [['Date,','Store_ID','Product_ID' ,'Quantity_Sold','Revenue']]

for _ in range(2000):

    year=random.randint(0,26) + 1997
    mont=random.randint(1,13)
    if mont==2:
        day = random.randint(1,29)
    elif mont % 2:
        day = random.randint(1,32)
    else:
        day = random.randint(1,31)
    rng = random.randint(0,100)
    if rng > 95:
        Date = f'{day}-{mont}-{year}'
    else:
        Date = f'{year}-{mont}-{day}'
        
    Store_ID = random.randint(0,60)
    Product_ID = random.randint(0,60)
    Quantity_Sold=random.randint(0,60)
    Revenue=random.randint(100,3000)
    apend_data=[Date,Store_ID,Product_ID,Quantity_Sold,Revenue]
    
    
    rng = random.randint(0,100)
    if rng > 95:
        error_selected=apend_data.index(random.choice(apend_data))
        if rng % 2:
            apend_data[error_selected]=None
        else:
            apend_data[error_selected]=get_random_string(random.randint(3,12))
    data.append(apend_data)
create_csv_file('.\eval_3\Apli_BD\sales_data.csv',data)
