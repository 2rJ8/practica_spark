import requests
import random
import csv
import string

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

response = requests.get(word_site)
WORDS = response.content.splitlines()
def RNG_word():
    return str(random.choice(WORDS))[2:-1]

def create_csv_file(filename,data):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)


def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

data = [['store_id','store_name','location','demographics']]

for i in range(2000):

    Store_ID = i
    store_name = f'{RNG_word()}_store'
    location= f'{RNG_word()}_{RNG_word()}_City'
    demographics=f'{RNG_word()}_{RNG_word()}_street_{random.randint(1,20)}'
    apend_data=[Store_ID,store_name,location,demographics]
    
    
    rng = random.randint(0,100)
    if rng > 95:
        error_selected=apend_data.index(random.choice(apend_data[1:]))
        if rng % 2:
            apend_data[error_selected]=None
        else:
            apend_data[error_selected]=get_random_string(random.randint(3,12))
    data.append(apend_data)
create_csv_file('./eval_3/Apli_BD/retail.csv',data)
