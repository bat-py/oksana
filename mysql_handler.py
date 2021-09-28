import pymysql
from pymysql.cursors import DictCursor


def connection_creator():
    connection = pymysql.connect(
        host='archlinux.uz',
        user='crow',
        password='ifuckyou',
        db='oksana',
        charset='utf8mb4',
        #            cursorclass=DictCursor
    )

    return connection


def get_bot_messages(*args):
    connection = connection_creator()
    cursor = connection.cursor()

    text = []
    for i in args:
        cursor.execute("SELECT text FROM bot_messages WHERE text_id = %s;", (i, ))
        text.append(cursor.fetchone()[0])

    connection.close()
    return text


def get_cities():
    connection = connection_creator()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM city;")
    city = cursor.fetchall()

    connection.close()
    return city


def get_price():
    connection = connection_creator()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM products ORDER BY city;")
    prices_tuple = cursor.fetchall()

    cursor.execute("SELECT COUNT(id) FROM `products` GROUP BY city;")
    count_city = len(cursor.fetchall())

    prices_dict = {}
    city_ids = set()
    for i in prices_tuple:

        #prices_dict[]

