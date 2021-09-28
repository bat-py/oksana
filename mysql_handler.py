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
        cursor.execute("SELECT text FROM bot_messages WHERE text_id = %s", (i, ))
        text.append(cursor.fetchone())

    connection.close()
    return text

def get_cities():
    connection = connection_creator()
    cursor = connection.cursor()

