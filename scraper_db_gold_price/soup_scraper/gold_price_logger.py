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


def start_loger(interval):
    counter = 0

    while True:
        r = requests.get('https://www.coininvest.com/pl/wykresy/kurs-zlota/')
        soup = bs4.BeautifulSoup(r.text, 'xml')
        now = datetime.now()
        price = soup.find('div', {'class': 'live_metal_prices_li_in'}).find('span').text

        with open("output_gold.csv", "a") as text_file:
            text_file.write(str(counter))
            text_file.write(",")
            text_file.write(str(now.strftime("%m/%d/%Y/ %H:%M:%S")))
            text_file.write(",")
            text_file.write(str(ast.literal_eval((price.replace('zł', '')).replace(",", "."))) + "\n")

        counter += 1
        time.sleep(interval)
        text_file.close()
        print({now.strftime("%m/%d/%Y, %H:%M:%S"): ast.literal_eval((price.replace('zł', '')).replace(",", "."))})


if __name__ == '__main__':
    start_loger()
