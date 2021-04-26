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
        #get_gold_price_from_web()[1]
        c.execute("insert into gold_price (ID, date, price) values (NULL, ?, ?)",
                 (get_gold_price_from_web()[0], get_gold_price_from_web()[1]))

        connection.commit()
        connection.close()
        print()
        time.sleep(3)




def select_operation():

    connection = sqlite3.connect('gold.db')
    c = connection.cursor()
    c.execute("SELECT * FROM gold_price")
    print(c.fetchall())
    connection.commit()
    connection.close()


# if __name__ == '__main__':
select_operation()
# connect_to_database()
# add_table()
#insert_into_table()
#dynamic_data_insert()
