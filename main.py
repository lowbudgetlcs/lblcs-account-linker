import csv
import os
import time
from dotenv import load_dotenv
import requests

load_dotenv(".env")

riot_token = os.getenv("RIOT_TOKEN")
enpoint = os.getenv("ENDPOINT")
headers = {"X-Riot-Token": riot_token}

with open('users.csv',encoding = "utf8") as file:
    reader = csv.DictReader(file)
    list = list(reader)

for row in list:
    if row['riot_puuid'] == '':
        url = f"{enpoint}/{row['League Name']}/{row['Tag']}"
        response = requests.get(url,headers=headers)
        if response.status_code != 200:
            print('something went wrong')
            print(response.status_code)
            print(response.text)
        else:
            data = response.json()
            row['riot_puuid'] = data['puuid']
        print(row)
        time.sleep(1)

keys = list[0].keys()
with open('users_new.csv','w',newline='', encoding="utf8") as output_file:
    dict_writer = csv.DictWriter(output_file,keys)
    dict_writer.writeheader()
    dict_writer.writerows(list)


