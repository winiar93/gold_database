import time
import sys

from scraper_db_gold_price.soup_scraper.beautiful_soup_scraper import get_gold_price_from_web
from scraper_db_gold_price.sql_data_base.sql_demo import DataBaseController


if __name__ == '__main__':
    controlling = DataBaseController()

    from optparse import OptionParser

    parser = OptionParser()
    parser.add_option("-r", "--read", dest="read_data", action="store_true",)
    parser.add_option("-l", "--loop", dest="read_loop", action="store_true")
    parser.add_option("-i", "--interval", action="store", type="int", dest="interval")
    parser.add_option('-a', '--select_all', dest='select_all', action="store_true")
    parser.add_option('-d','--dynamic',dest="dynamic_insert",action="store_true")
    parser.add_option('-s','--save',dest="save_csv",action="store_true")
    parser.add_option('-q','--query',dest="sql_select",action="store_true")




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
    if options.select_all:
        controlling.select_all_operation()
    if options.dynamic_insert:
        print("saving scraped data in loop ...")
        controlling.dynamic_data_insert(options.dynamic_insert)
    if options.save_csv:
        print("Exporitng data to csv file")
        controlling.export_to_csv()
        print("Your file is ready")
    if options.sql_select:
        controlling.type_sql_query()
