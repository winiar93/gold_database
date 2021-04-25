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


def get_gold_price_from_web():
    r = requests.get('https://www.coininvest.com/pl/wykresy/kurs-zlota/')
    soup = bs4.BeautifulSoup(r.text, 'xml')
    now = datetime.now()
    price = soup.find('div', {'class': 'live_metal_prices_li_in'}).find('span').text
    return {now.strftime("%m/%d/%Y, %H:%M:%S"): ast.literal_eval((price.replace('zł', '')).replace(",", "."))}


def get_gold_price_all_time():
    while True:
        print(get_gold_price_from_web())
        time.sleep(4)


if __name__ == '__main__':
    get_gold_price_from_web()
    get_gold_price_all_time()


print(get_gold_price_from_web())
