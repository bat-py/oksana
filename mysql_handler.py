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

    # id_cityname_dict gets dict like: {'id': 'cityname', ...}
    cursor.execute("SELECT * FROM city")
    id_cityname_tuple = cursor.fetchall()
    id_cityname_dict = {}
    for i in id_cityname_tuple:
        id_cityname_dict[i[0]] = i[1]

    cursor.execute("SELECT * FROM products ORDER BY city;")
    products_tuple = cursor.fetchall()

    city_ids = set()
    for i in products_tuple:
        city_ids.add(i[4])

    products_types = set()
    for i in products_tuple:
        products_types.add(i[1])

    # Gets list like: [ [{}, {}, ...], [...], ... ]
    products_list_by_city = []
    for i in city_ids:
        product_by_city = []
        for product in products_tuple:
            if i == product[4]:
                product_by_type = []

                for type in products_types:
                    if type == product[1]:
                        p_dict = {}
                        p_dict['product_name'] = product[1]
                        p_dict['product_massa'] = product[2]
                        p_dict['product_price'] = product[3]
                        p_dict['product_city'] = id_cityname_dict[product[4]]
                        product_by_type.append(p_dict)
                product_by_city.append(product_by_type)
        products_list_by_city.append(product_by_city)
    print(products_list_by_city)
    return products_list_by_city


