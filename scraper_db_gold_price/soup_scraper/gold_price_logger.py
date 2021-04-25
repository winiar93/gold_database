from typing import TextIO

import bs4
from bs4 import BeautifulSoup
import requests
import lxml
import time
from datetime import datetime
import matplotlib.pyplot as plt
import csv
import re
import ast

def start_loger():

        while True:

                r = requests.get('https://www.coininvest.com/pl/wykresy/kurs-zlota/')
                soup = bs4.BeautifulSoup(r.text, 'xml')
                now = datetime.now()
                price = soup.find('div', {'class': 'live_metal_prices_li_in'}).find('span').text

                with open("Output_gold.csv", "a") as text_file:
                        text_file.write(str(now.strftime("%m/%d/%Y/ %H:%M:%S")))
                        text_file.write(" ")
                        text_file.write(str(ast.literal_eval((price.replace('zł', '')).replace(",", ".")))+"\n")


                time.sleep(1)
                text_file.close()
                print({now.strftime("%m/%d/%Y, %H:%M:%S"): ast.literal_eval((price.replace('zł', '')).replace(",", "."))})


start_loger()