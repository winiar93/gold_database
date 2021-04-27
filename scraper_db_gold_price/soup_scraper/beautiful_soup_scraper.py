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
import argparse, optparse
import sys
from optparse import OptionParser


def get_gold_price_from_web():
    r = requests.get('https://www.coininvest.com/pl/wykresy/kurs-zlota/')
    soup = bs4.BeautifulSoup(r.text, 'xml')
    now = datetime.now()
    price = soup.find('div', {'class': 'live_metal_prices_li_in'}).find('span').text
    data_package = [now.strftime("%m/%d/%Y %H:%M:%S"), ast.literal_eval((price.replace('zł', '')).replace(",", "."))]
    return data_package


def get_gold_price_all_time():
    while True:
        time.sleep(4)
        print(get_gold_price_from_web())



from optparse import OptionParser

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-r", "--read", dest="read_data", action="store_true")
    parser.add_option("-l", "--loop", dest="read_loop", action="store_true")


    options, args = parser.parse_args()

    if options.read_data:
        print(get_gold_price_from_web())
    if options.read_loop:
        while True:
            print(get_gold_price_from_web())
            time.sleep(2)