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


connect = connection_creator()
cursor = connect.cursor()

ids1 = 'main_menu_comments'
sss1 = '<b>Отзывы покупателей</b> (отправьте 👉 9️⃣9️⃣9️⃣)\n</b>Оставить отзыв</b> (отправьте 👉 7️⃣7️⃣7️⃣)'

ids2 = 'main_menu_balance'
sss2 = '<b>Ваш баланс:</b> 0 RUB / 0.00 BTC / 0.00 LTC'

ids3 = 'main_menu_city'
sss3 = '<b>Для покупки отправьте цифру своего города из списка снизу:</b>'

ids4 = 'list_commands'
sss4 = '$ - Как оформить ненаход?\n# - В главное меню\n+ - Прайс\n? - Помощь'

ids5 = 'order_bot'
sss5 = '======================================================\nХочешь такого же бота? Пиши в Телеграм: '

cursor.execute("INSERT INTO bot_messages VALUES(%s, %s)", (ids5, sss5))
connect.commit()
connect.close()
