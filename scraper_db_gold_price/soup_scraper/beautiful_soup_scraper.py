import bs4
from bs4 import BeautifulSoup
import requests
import lxml
from datetime import date



def get_gold_price_from_web():

    today = date.today()
    r = requests.get('https://www.coininvest.com/pl/wykresy/kurs-zlota/')
    soup = bs4.BeautifulSoup(r.text, 'xml')
    price = soup.find('div', {'class': 'live_metal_prices_li_in'}).find('span').text
    return price, today.strftime("%d/%m/%y")


print(get_gold_price_from_web())
