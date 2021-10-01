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
        cursor.execute("SELECT text FROM bot_messages WHERE text_id = %s;", (i,))
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

    # id_productname_dict gets dict like: {'id': 'productname', ...}
    cursor.execute("SELECT * FROM products_types")
    id_productname_tuple = cursor.fetchall()
    id_productname_dict = {}
    for i in id_productname_tuple:
        id_productname_dict[i[0]] = i[1]

    #cursor.execute("SELECT * FROM products ORDER BY city;")
    cursor.execute("SELECT products.id, product, products_massa.massa_gr, price, city FROM products JOIN products_massa ON products.massa = products_massa.id ORDER BY city;")
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
                for type in products_types:
                    if type == product[1]:
                        p_dict = {}
                        p_dict['product_name'] = id_productname_dict[product[1]]
                        p_dict['product_massa'] = product[2]
                        p_dict['product_price'] = product[3]
                        p_dict['product_city'] = id_cityname_dict[product[4]]
                        product_by_city.append(p_dict)
        products_list_by_city.append(product_by_city)

    enable_cities = set()
    for city in products_list_by_city:
        enable_cities.add(city[0]['product_city'])

    enable_products = set()
    for product in products_list_by_city:
        enable_products.add(product[0]['product_name'])

    main = []
    for city in products_list_by_city:
        product = []
        for i in enable_products:
            ppp = []
            for p in city:
                if p['product_name'] == i:
                    ppp.append(p)
            if ppp:
                product.append(ppp)
        main.append(product)
    return main


def get_user_state(id):
    connection = connection_creator()
    cursor = connection.cursor()

    cursor.execute("SELECT state FROM user_state WHERE id = %s;", (id,))
    user_state = cursor.fetchone()

    connection.close()
    return user_state


def change_user_state(user_id, state):
    connection = connection_creator()
    cursor = connection.cursor()

    cursor.execute("UPDATE user_state SET state = %s WHERE id = %s", (state, user_id))

    connection.commit()
    connection.close()


def add_user(id):
    connection = connection_creator()
    cursor = connection.cursor()

    cursor.execute("INSERT INTO user_state VALUES (%s, %s);", (id, '#'))
    connection.commit()

    connection.close()


def get_feedbacks(user_id, page):
    connection = connection_creator()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM feedbacks ORDER BY date DESC ;")
    all_feedbacks = cursor.fetchall()
    connection.close()

    if page > len(all_feedbacks) / 5:
        page = 1
        change_user_state(user_id, '999')

    finish = page * 5
    start = finish - 5

    # returns tuple with 5 tuple objects: ((1, 'ДжетЛи', datetime.date(2021, 9, 21), 'В касание'), ... )
    return all_feedbacks[start: finish]


def get_products_in_city(city_id):
    connection = connection_creator()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT product, product_name FROM products, products_types WHERE products.product = products_types.id and products.city = %s GROUP BY product ",
        (int(city_id),))

    products = cursor.fetchall()
    connection.close()

    return products


def get_fasovkas_in_city_in_type(city_id, product_id):
    connection = connection_creator()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT products.id, product, massa, products_massa.massa_gr, price, city FROM products JOIN products_massa ON products.massa = products_massa.id WHERE city=%s and product=%s;",
        (city_id, product_id))
    fasovkas = cursor.fetchall()
    connection.close()

    return fasovkas


# Gets tuple like  (2, 'Альпийские камни', 0.33, 1050, 'Красноярск', '11:Советский;...')
def get_product_info(city_id, product_id, fasovka_id):
    connection = connection_creator()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT products.id, products_types.product_name, products_massa.massa_gr, price, city.city_name, districts FROM products JOIN products_massa ON products.massa = products_massa.id JOIN products_types ON products.product = products_types.id JOIN city ON products.city = city.id WHERE products.city = %s and product = %s AND massa = %s;",
        (city_id, product_id, fasovka_id))
    product_info = cursor.fetchone()
    connection.close()

    return product_info


def get_product_name_by_id(product_id):
    connection = connection_creator()
    cursor = connection.cursor()

    cursor.execute("SELECT product_name FROM `products_types` WHERE id = %s;",
                   (product_id, ))
    product_name = cursor.fetchone()[0]
    connection.close()

    return product_name