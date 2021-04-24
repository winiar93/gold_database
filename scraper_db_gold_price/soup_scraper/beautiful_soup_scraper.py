import bs4
from bs4 import BeautifulSoup
import requests
import lxml
from datetime import date
import time
import matplotlib.pyplot as plt
import csv
import re
import ast

def get_gold_price_from_web():

    today = date.today()
    r = requests.get('https://www.coininvest.com/pl/wykresy/kurs-zlota/')
    soup = bs4.BeautifulSoup(r.text, 'xml')
    price = soup.find('div', {'class': 'live_metal_prices_li_in'}).find('span').text
    return {today.strftime("%d/%m/%y"): ast.literal_eval((price.replace('zł', '')).replace(",","."))}


def get_gold_price_all_time():

    while True:
        print(get_gold_price_from_web())
        time.sleep(4)


def collect_gold_data():

    while True:
        with open('data_gold.csv', 'a') as goldfile:
            goldfile.write(str(get_gold_price_from_web())+"\n")
        print(get_gold_price_from_web())
        time.sleep(4)

if __name__ == '__main__':
    get_gold_price_from_web()
    get_gold_price_all_time()
    collect_gold_data()

#print(collect_gold_data())