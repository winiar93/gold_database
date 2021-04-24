import bs4
from bs4 import BeautifulSoup
import requests
import lxml
from datetime import date
import time


def get_gold_price_from_web():

    today = date.today()
    r = requests.get('https://www.coininvest.com/pl/wykresy/kurs-zlota/')
    soup = bs4.BeautifulSoup(r.text, 'xml')
    price = soup.find('div', {'class': 'live_metal_prices_li_in'}).find('span').text
    return {today.strftime("%d/%m/%y"): price}


def get_gold_price_all_time():

    while True:
        print(get_gold_price_from_web())
        time.sleep(3)


print(get_gold_price_all_time())