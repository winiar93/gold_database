import sqlite3
import time
from datetime import date, datetime
from scraper_db_gold_price.soup_scraper.beautiful_soup_scraper import get_gold_price_from_web
import os.path

today = date.today()
print(today)
'''
x = 'SELECT * FROM gold_price'

'''


class DataBaseController():
    GOLD_PRICE_TABLE_NAME = "gold_price"
    DATA_BASE_NAME = "gold.db"
    DATA_BASE_FILE = "scraper_db_gold_price\sql_data_base\gold.db"
    QUERY_CHECK = f"PRAGMA table_info({GOLD_PRICE_TABLE_NAME})"

    def __init__(self):
        try:
            self.connection = sqlite3.connect(self.DATA_BASE_NAME)
            c = self.connection.cursor()
        except sqlite3.OperationalError:
            pass

        c.execute(self.QUERY_CHECK)

        if len(c.fetchall()) == 0:
            print("Data base is empty")
            self.connection = sqlite3.connect(self.DATA_BASE_NAME)
            c = self.connection.cursor()
            c.execute(f"""CREATE TABLE {self.GOLD_PRICE_TABLE_NAME} (
                                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                    time timestamp ,
                                    price REAL
                                    )""")
            print("Table was created")
            self.connection.commit()
            # self.connection.close()

    # def _create_gold_price_table(self):
    #     connection = sqlite3.connect('gold.db')
    #     c = connection.cursor()
    #     c.execute(f"""CREATE TABLE {self.GOLD_PRICE_TABLE_NAME} (
    #                 ID INTEGER PRIMARY KEY AUTOINCREMENT,
    #                 date varchar(255) NOT NULL,
    #                 price INT
    #                 )""")
    #     connection.commit()
    #     connection.close()

    def _insert_into_table_(self, value_pln):
        c = self.connection.cursor()
        c.execute("INSERT INTO 'gold_price' VALUES (NULL,?,?)", (today,value_pln))
        self.connection.commit()
        self.connection.close()

    def dynamic_data_insert(self, interval):
        while True:
            c = self.connection.cursor()
            now = datetime.now()
            now.strftime("%m/%d/%Y, %H:%M:%S")
            take_date = str(now.strftime("%m/%d/%Y"))
            value = 2000
            # get_gold_price_from_web()[1]
            c.execute("insert into gold_price (ID, date, price) values (NULL, ?, ?)",
                      (get_gold_price_from_web()[0], get_gold_price_from_web()[1]))

            self.connection.commit()
            c.execute("SELECT * FROM gold_price ORDER BY ID DESC LIMIT 1")
            result = c.fetchone()
            print("Added values to gold_price table : ", str(result))
            self.connection.close()
            time.sleep(interval)

    def select_operation(self):
        c = self.connection.cursor()
        c.execute("SELECT * FROM gold_price")
        print(c.fetchall())
        self.connection.commit()
        self.connection.close()

    def type_sql_query(self):
        c = self.connection.cursor()
        sql_select = input("Type sql operation : ")
        c.execute(sql_select)
        print(c.fetchall())
        self.connection.commit()
        self.connection.close()


controlling = DataBaseController()
#controlling._insert_into_table_(2000.9)
controlling.type_sql_query()
