#from soup_scraper.beautiful_soup_scraper import get_gold_price_from_web


import argparse
import sys

def showtop():
    print(get_gold_price_from_web())

def showtwo():
    print(get_gold_price_from_web(), 2)

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

parser_showtop20 = subparsers.add_parser('--get', help='show one value')
parser_showtop20.set_defaults(func=showtop)


parser_listapps = subparsers.add_parser('--show', help='show cos tam 2')
parser_listapps.set_defaults(func=showtwo)


if len(sys.argv) <= 1:
    sys.argv.append('--help')

options = parser.parse_args()

options.func()

if __name__ == "__main__":
    from scraper_db_gold_price.soup_scraper.beautiful_soup_scraper import get_gold_price_from_web
