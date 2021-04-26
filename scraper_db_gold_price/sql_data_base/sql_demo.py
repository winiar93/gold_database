import sqlite3


def connect_to_database():
    '''IF there is no database, sqlite create new one'''
    connection = sqlite3.connect('gold.db')


def add_table():

    connection = sqlite3.connect('gold.db')
    c = connection.cursor()
    c.execute("""CREATE TABLE gold_price (
                id int NOT NULL,
                date varchar(255) NOT NULL,
                price int
                )""")
    connection.commit()
    connection.close()


def insert_into_table():
    connection = sqlite3.connect('gold.db')
    c = connection.cursor()
    c.execute("INSERT INTO gold_price VALUES (2,'tooday',16730)")
    connection.commit()
    connection.close()


def select_operation():

    connection = sqlite3.connect('gold.db')
    c = connection.cursor()
    c.execute("SELECT * FROM gold_price")
    print(c.fetchall())
    connection.commit()
    connection.close()


if __name__ == '__main__':
    select_operation()
    insert_into_table()
    connect_to_database()