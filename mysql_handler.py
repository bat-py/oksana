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


class SqlRequests:
    def get_bot_messages(self, text_code):
        connection = connection_creator()
        cursor = connection.cursor()

        cursor.execute("SELECT text FROM bot_messages WHERE text_code = %s", (text_code, ))

        return cursor.fetchone()
