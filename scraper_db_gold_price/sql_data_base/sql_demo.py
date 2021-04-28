import sqlite3
import time
from datetime import datetime
from scraper_db_gold_price.soup_scraper.beautiful_soup_scraper import get_gold_price_from_web

#Stworzyć jedna klase dla wszytkichg operacti -- Class DataBaseController
# w inicie sprawdzic czy jest tabel z gold price zrobic z ifem jest tak to nic nie robic jesli FALSE to tworzy

#x = 'SELECT * FROM gold_price'


class DataBaseController():

    GOLD_PRICE_TABLE_NAME = "gold_price"
    DATA_BASE_NAME = "gold.db"


    def __init__(self):
        self.connection = sqlite3.connect(self.DATA_BASE_NAME)
        #if
        self._create_gold_price_table()


    def _create_gold_price_table(self):
        connection = sqlite3.connect('gold.db')
        c = connection.cursor()
        c.execute(f"""CREATE TABLE {self.GOLD_PRICE_TABLE_NAME} (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    date varchar(255) NOT NULL,
                    price DECIMAL
                    )""")
        connection.commit()
        connection.close()

    def insert_into_table(self, date, value_pln):
        c = self.connection.cursor()
        #insert_command =
        c.execute("INSERT INTO gold_price VALUES (NULL,?,?)", (str(date), str(value_pln)))
        self.connection.commit()
        self.connection.close()

    def dynamic_data_insert(self,interval):
        while True:

            c = self.connection.cursor()
            now = datetime.now()
            now.strftime("%m/%d/%Y, %H:%M:%S")
            take_date = str(now.strftime("%m/%d/%Y %H:%M:%S"))
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

    def read_any_information(self):
        c = self.connection.cursor()
        sql_select = input("Type sql operation : ")
        c.execute(sql_select)
        print(c.fetchall())
        self.connection.commit()
        self.connection.close()



database_sql = DataBaseSqlOperations()
#database_sql.insert_into_table("27/04/2021 11:45", "2000")

need_more_information = ReadDataFromDatabase()
need_more_information.read_any_information()
#select * from gold_price order by ID desc limit 1