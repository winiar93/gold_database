import sqlite3
import time
from datetime import datetime
from scraper_db_gold_price.soup_scraper.beautiful_soup_scraper import get_gold_price_from_web


def connect_to_database():
    '''IF there is no database, sqlite create new one'''
    connection = sqlite3.connect('gold.db')


def add_table():
    connection = sqlite3.connect('gold.db')
    c = connection.cursor()
    c.execute("""CREATE TABLE gold_price (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                date varchar(255) NOT NULL,
                price int
                )""")
    connection.commit()
    connection.close()


def insert_into_table():
    connection = sqlite3.connect('gold.db')
    c = connection.cursor()
    c.execute("INSERT INTO gold_price VALUES (NULL,'tooday',56308888)")
    connection.commit()
    connection.close()


def dynamic_data_insert():
    while True:
        connection = sqlite3.connect('gold.db')
        c = connection.cursor()
        now = datetime.now()
        now.strftime("%m/%d/%Y, %H:%M:%S")
        take_date = str(now.strftime("%m/%d/%Y %H:%M:%S"))
        value = 2000
        # get_gold_price_from_web()[1]
        c.execute("insert into gold_price (ID, date, price) values (NULL, ?, ?)",
                  (get_gold_price_from_web()[0], get_gold_price_from_web()[1]))

        connection.commit()
        c.execute("SELECT * FROM gold_price ORDER BY ID DESC LIMIT 1")
        result = c.fetchone()
        print("Added values to gold_price table : ", str(result))
        connection.close()
        time.sleep(3)

x = 'SELECT * FROM gold_price'

class Read_data_from_db:

    def __init__(self, connection=sqlite3.connect('gold.db')):
        self.connection = connection

    def select_operation(self):
        c = self.connection.cursor()
        c.execute("SELECT * FROM gold_price")
        print(c.fetchall())
        self.connection.commit()
        self.connection.close()

    def read_any_information(self):
        c = self.connection.cursor()
        sql_select = input("Type sql operation : ")
        c.execute(sql_select)
        print(c.fetchall())
        self.connection.commit()
        self.connection.close()

# if __name__ == '__main__':
# select_operation()
# connect_to_database()
# add_table()
# insert_into_table()
grab_data_from_db = Read_data_from_db()

#grab_data_from_db.select_operation()
grab_data_from_db.read_any_information()
