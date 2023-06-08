import requests
from time import sleep
import random
import datetime
import os

inputdirectory = os.getcwd().replace('"','')

def random_sleep():
    sleep_time = random.uniform(0.0, 3.0)
    sleep(sleep_time)

def check_if_exists(content):
    for filename in os.listdir(os.path.join(inputdirectory,'gifs')):
        if os.path.isfile(os.path.join(inputdirectory, 'gifs', filename)):
            with open(os.path.join(inputdirectory, 'gifs', filename), 'rb') as f:
                gif = f.read()
                if gif == content:
                    print("same image exist")
                    return True
    print("image doesnt exist")
    return False


def scrap_from_url():
    try:
        r = requests.get("https://ayva.itu.edu.tr/")
        random_sleep()
        print(r.content)
    except Exception as e:
        print("error occurred:", e)


while True:
    scrap_from_url()
