import time
import sys

from scraper_db_gold_price.soup_scraper.beautiful_soup_scraper import get_gold_price_from_web

if __name__ == '__main__':

    from optparse import OptionParser

    parser = OptionParser()
    parser.add_option("-r", "--read", dest="read_data", action="store_true",)
    parser.add_option("-l", "--loop", dest="read_loop", action="store_true")
    parser.add_option("-i", "--interval", action="store", type="int", dest="interval")



    options, args = parser.parse_args()

    #print(options)
    if options.read_data:
        print(get_gold_price_from_web())
    if options.read_loop:
        while True:
            print(get_gold_price_from_web())
            time.sleep(2)
    if options.interval:
        while True:
            print(get_gold_price_from_web())
            time.sleep(options.interval)