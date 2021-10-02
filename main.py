from pyrogram import Client, filters
import tgcrypto
import mysql_handler as sql
import payment_methods as pm
import json

with open('numbers.json', 'r') as n:
    numbers = json.load(n)

months = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']


def get_cities_list(without_number=None):
    '''
    returns dict like: {1: '7️⃣ Moscow', ... }
    '''

    # returns tuple: ( (1, 'Moscow'), ... )
    city_tuple = sql.get_cities()

    city_dict = {}

    if without_number:
        for city_id, city in city_tuple:
            for i in city:
                city_dict[city_id] = city
    else:
        # returns dict(id:'witch graphic nubmers'):  { 1 : '7️⃣ Moscow', ... }
        for city_id, city in city_tuple:
            for i in city:
                city_dict[city_id] = numbers[str(city_id)] + ': ' + city
    return city_dict

# with_wrong_request: Вместо Отзывы покупателей, Оставить отзыв и Баланс будет wrong_request
def main_menu(client, message, with_wrong_request= None):
    # message.forward('me')        # all messages saves in Избранное
    messages = sql.get_bot_messages('main_menu_comments',
                                    'main_menu_balance',
                                    'main_menu_city',
                                    'list_commands',
                                    'order_bot',
                                    'wrong_request'
                                    )
    if with_wrong_request:
        msg_header = f'{messages[5]}\n\n'
        msg_list_commands = f'\n{messages[3]}'
    else:
        msg_header = f'{messages[0]}\n\n{messages[1]}\n\n{messages[2]}\n\n'
        msg_list_commands = f'\n{messages[3]}\n\n{messages[4]}'

    # gets dict like: {1: '7️⃣ Moscow', ... }
    city_dict = get_cities_list()

    # makes cities list to send main menu
    msg_cities = ''
    for i, city in city_dict.items():
        msg_cities += city+'\n'

    message.reply_text(msg_header + msg_cities + msg_list_commands)


def disput_menu(client, message):
    messages = sql.get_bot_messages('disput_menu',
                                    'list_commands'
                                    )
    msg = messages[0] + '\n\n' + messages[1]
    message.reply_text(msg)


def help_menu(client, message):
    messages = sql.get_bot_messages('help_menu',
                                    'list_commands'
                                    )
    msg = messages[0] + '\n\n' + messages[1]
    message.reply_text(msg)


def get_price(client, message):
    messages = sql.get_bot_messages('now_in_stock',
                                    'main_menu_balance',
                                    'main_menu_city',
                                    'list_commands',
                                    'order_bot'
                                    )

    # Gets list like: [ [ [{},] [{}], ...], [...], ... ] - every second step list is one city, every third step list is type product, every dict is product
    products_list = sql.get_price()


    # Gets str like: city1:product1, product2; ...  msg_prices_by_city is part of 'msg' string
    msg_products_by_city = ''

#    for i in products_list:
#        print(i)
#        print('\n\n')

    for group_city in products_list:
        msg_products_by_city += numbers['three_line'] + '<b>' + group_city[0][0]['product_city'] + '</b>' + numbers['three_line'] + '\n\n'
        for product_type in group_city:
            msg_products_by_city += '<b>' + product_type[0]['product_name'] + '</b>' + '\n'
            for product in product_type:
                mesg_product = f"{product['product_massa']} г за {product['product_price']} руб"
                msg_products_by_city += mesg_product + '\n'
            msg_products_by_city += '\n'



    # gets dict like: {1: '7️⃣ Moscow', ... }
    city_dict = get_cities_list()
    # makes cities list to send main menu
    msg_cities = ''
    for i, city in city_dict.items():
        msg_cities += city+'\n'

    msg = f'{messages[0]}\n\n{msg_products_by_city}\n\n{messages[1]}\n\n{messages[2]}\n\n{msg_cities}\n\n{messages[3]}\n\n{messages[4]}'
    message.reply_text(msg)


def leave_comment(client, message):
    messages = sql.get_bot_messages('leave_comment',
                                    'list_commands'
                                    )

    msg = messages[0] + '\n\n' + messages[1]
    message.reply_text(msg)


def wrong_request(client, message):
    messages = sql.get_bot_messages('wrong_request',
                                    'list_commands'
                                    )

    # gets dict like: {1: '7️⃣ Moscow', ... }
    city_dict = get_cities_list()
    # makes cities list to send main menu
    msg_cities = ''
    for i, city in city_dict.items():
        msg_cities += city+'\n'

    msg = messages[0] + '\n\n' + msg_cities + '\n' + messages[1]
    message.reply_text(msg)


def get_feedbacks(client, message):
    messages = sql.get_bot_messages('show_more',
                                    'list_commands'
                                    )

    state = sql.get_user_state(message.chat.id)[0]
    states = state.split(';')
    if not states.count('999'):
        sql.change_user_state(message.chat.id, '999')
        feedbacks = sql.get_feedbacks(message.chat.id, 1)
        # now we shoud get 1-5 last comments
    else:
        sql.change_user_state(message.chat.id, state+';999')
        page = states.count('999') + 1
        feedbacks = sql.get_feedbacks(message.chat.id, page)

    feedbacks = list(feedbacks)
    feedbacks.reverse()

    feedbacks_msg = ''
    for i in feedbacks:
        msg = f"{numbers['two_line']}От <b>{i[1]}</b> {i[2].day} {months[ i[2].month-1 ]}{numbers['two_line']}\n{i[3]}\n\n"
        feedbacks_msg += msg

    msg = messages[0] + '\n\n' + feedbacks_msg + messages[1]
    message.reply_text(msg)


def choise_city(client, message):
    """
    Срабатывает после получения чисел 1-25
    """
    state = sql.get_user_state(message.chat.id)[0]

    # Returns all needed bot messages
    messages = sql.get_bot_messages('main_menu_balance', 'you_choise', 'city', 'product', 'district',
                                    # 6:
                                    'massa', 'choose_product', 'choose_payment', 'list_commands', 'no_in_stock', 'wrong_request',
                                    # 11:
                                    'choose_fasovka', 'choose_district', 'order_bot', 'your_balance', 'pay_with_balance',
                                    # 16:
                                    'needed_balance', 'needed_balance_continue', 'pay', 'use_more_commission',
                                    )

    cities = get_cities_list(without_number=1)
    cities_id = list(map(lambda city: str(city[0]), cities.items()))

    # В базе state будет храниться как "c1;p1;". Запуститься если пользователь выбрал город
    if not state.startswith('c') and message.text in cities_id:
        # I use in sql.get_products_in_city function SORT BY product, so it returns only one product if there ara many one typy product с разными фасофками: ((1, 'Альпийские камни'), (2, 'Оффлайн ТВ(САМОЕ МОЩНОЕ ТВ)'))
        products_list_in_city = sql.get_products_in_city(message.text)

        sql.change_user_state(message.chat.id, 'c' + str(message.text))
        # Если у указанного города есть товар в наличии
        if products_list_in_city:
            # shows main_menu_balance, you_choise and city in more_lines
            msg1 = f"{messages[0]}\n\n{messages[1]} \"{cities[int(message.text)]}\".\n\n{numbers['more_lines']}\n{messages[2]} {cities[int(message.text)]}\n{numbers['more_lines']}\n\n"

            # Gets list like:
            msg2_part = ''
            for num, product_name in products_list_in_city:
                msg2_part += f"{numbers[str(num)]}: {product_name}\n"

            msg2 = f"{messages[6]}\n\n{msg2_part}\n{messages[8]}"
            message.reply_text(msg1+msg2)
        else:
            msg = f"{messages[9]}\n\n{messages[8]}"
            message.reply_text(msg)
            sql.change_user_state(message.chat.id, '#')

    # Запуститься после того как он выбрал тип продукта (2: альпийские кам.  10: Офлайн ...)
    elif len(state.split(';')) == 1:
        choosen_city_id = int(state.replace('c', ''))
        products_list_in_city = sql.get_products_in_city(choosen_city_id)

        # Gets dict like: { '2' : 'Альпийские камни', ... }
        products_list_in_city_dict = {}
        for id_, product_name in products_list_in_city:
            products_list_in_city_dict[str(id_)] = product_name

        # If member choise correct product type:
        if message.text in list(map(lambda product: str(product[0]), products_list_in_city)):
            # Changing user's state to 'c1p2' (1 - id city, 2 - product type)
            sql.change_user_state(message.chat.id, state+';p'+str(message.text))
            choosen_product_type_id = message.text

            # Part message Balance, You choise "product name"
            msg1 = f"{messages[0]}\n\n{messages[1]} \"{products_list_in_city_dict[message.text]}\".\n\n"


            # Part message into ----------:
            msg2 = f"{numbers['more_lines']}\n{messages[2]} {cities[choosen_city_id]}\n{messages[3]} {products_list_in_city_dict[message.text]}\n{numbers['more_lines']}"

            # Part choose_fasovka
            # Gets product's tuple list of fasovka by one type product in city: ((2, 2, 1(massa), 0.33(products_massa.massa_gr), 1050, 1), ...)
            fasovkas_in_city_in_type = sql.get_fasovkas_in_city_in_type(choosen_city_id, choosen_product_type_id)
            msg_part_fasovkas_list = ''
            for product_data in fasovkas_in_city_in_type:
                number = numbers[str(product_data[2])]
                fasovka = f"{product_data[3]} шт за {product_data[4]} руб\n"
                msg_part_fasovkas_list += number + ': ' + fasovka

            msg3 = f"\n\n{messages[11]}\n\n{msg_part_fasovkas_list}\n"

            message.reply_text(msg1 + msg2 + msg3 + messages[8])

        # If member choise wrong number of product type or send random message
        else:
            # Gets list like:
            product_list = ''
            for num, product_name in products_list_in_city:
                product_list += f"{numbers[str(num)]}: {product_name}\n"


            msg = f"{messages[10]}\n\n{product_list}\n{messages[8]}"
            message.reply_text(msg)

    # Запуститься если пользователь выбрал фасофку (If state like 'c1p2'
    elif len(state.split(';')) == 2:
        state_list = state.split(';')
        choosen_city_id = int(state_list[0].replace('c', ''))
        choosen_product_type_id = int(state_list[1].replace('p', ''))

        # Gets product's tuple list of fasovka by one type product in city: ((2, 1, 2, 0.33, 1050, 1), (3, 2, 20, 2, 1350, 1), ...)
        aviable_fasovkas = sql.get_fasovkas_in_city_in_type(choosen_city_id, choosen_product_type_id)

#        aviable_fasovkas_number = [str(i) for i in range(1, len(aviable_fasovkas)+1)]
        aviable_fasovkas_number = [str(i[2]) for i in aviable_fasovkas]

        # Запуститься если пользователь выбрал правильный номер фасофки и спросит выбрать район если у товара есть район:
        if message.text in aviable_fasovkas_number:
            product_info = sql.get_product_info(choosen_city_id, choosen_product_type_id, int(message.text))

            if product_info[5]:
                # Changing user's state to 'c1p2f1' (1 - id city, 2 - product type, 3 - fasovka)
                sql.change_user_state(message.chat.id, state+';f'+str(message.text))

                # Part message Balance, You choise "fasovka name"
                msg1 = f"{messages[0]}\n\n{messages[1]} \"{product_info[2]} шт за {product_info[3]} руб\".\n\n"

                # Part message into ----------:
                msg2_city = f"{messages[2]} {cities[choosen_city_id]}"
                msg2_product = f"{messages[3]} {sql.get_product_name_by_id(choosen_product_type_id)}"
                msg2_fasovka = f"{messages[5]} {product_info[2]} шт за {product_info[3]} руб"
                msg2 = f"{numbers['more_lines']}\n{msg2_city}\n{msg2_product}\n{msg2_fasovka}\n{numbers['more_lines']}\n"


                # Gets district list and adds to msg3_district
                # Gets tuple like  (2, 'Альпийские камни', 0.33, 1050, 'Красноярск', '11:Советский,...')q
                product_info = sql.get_product_info(choosen_city_id, choosen_product_type_id, message.text)
                districts = product_info[5].split(',')
                # Gets districts dict: {'11':'Советский', ...}
                districts_list = [dist.split(':') for dist in districts]

                districts_str = ''
                for dist in districts_list:
                    districts_str += f"{numbers[str(dist[0])]}: {dist[1]}\n"

                msg3 = f"{messages[12]}\n\n{districts_str}\n{messages[8]}"

                message.reply_text(msg1 + msg2 + msg3)

            # Запуститься если пользователь выбрал правильный номер фасофки и спросит выбрать метод оплаты (так как у него нету района)
            else:
                # Changing user's state to 'c1;p2;f1;0' (1 - id city, 2 - product type, 3 - fasovka, 0 - no district)
                sql.change_user_state(message.chat.id, state+';f'+str(message.text)+';0')
                show_payment_menu(client, message, messages, cities, choosen_city_id, choosen_product_type_id, int(message.text))

        # Запуститься если пользователь отправил неправильный номер фасовки
        else:
            # Gets product's tuple list of fasovka by one type product in city: ((2, 2, 1(massa), 0.33(products_massa.massa_gr), 1050, 1), ...)
            fasovkas_in_city_in_type = sql.get_fasovkas_in_city_in_type(choosen_city_id, choosen_product_type_id)
            msg_part_fasovkas_list = ''
            for product_data in fasovkas_in_city_in_type:
                number = numbers[str(product_data[2])]
                fasovka = f"{product_data[3]} шт за {product_data[4]} руб\n"
                msg_part_fasovkas_list += number + ': ' + fasovka


            msg = f"{messages[10]}\n\n{msg_part_fasovkas_list}\n{messages[8]}"
            message.reply_text(msg)

    # Запуститься если у товара есть район и  пользователь выбрал район (If state like 'c1;p2;f10'
    elif len(state.split(';')) == 3:
        state_list = state.split(';')
        choosen_city_id = int(state_list[0].replace('c', ''))
        choosen_product_type_id = int(state_list[1].replace('p', ''))
        choosen_fasovka_id = int(state_list[2].replace('f', ''))
        choosen_district_id = message.text.strip()

        # Gets tuple like  (2, 'Альпийские камни', 0.33, 1050, 'Красноярск', '11:Советский,...')q
        product_info = sql.get_product_info(choosen_city_id, choosen_product_type_id, choosen_fasovka_id)
        districts = product_info[5].split(',')

        # Gets ['11', ..]
        districts_id = []
        # Gets { '11' : 'Советский', }
        districts_dict = {}
        for dist in districts:
            num_distname = dist.split(':')
            districts_id.append(num_distname[0].strip())
            districts_dict[num_distname[0].strip()] = num_distname[1].strip()

        # Если пользователь выбрал существуюший номер района
        if choosen_district_id in districts_id:
            # Changing user's state to 'c1;p2;f1;d11' (1 - id city, 2 - product type, 3 - fasovka, 11 - id district)
            sql.change_user_state(message.chat.id, state + ';d' + choosen_district_id)
            show_payment_menu(client, message, messages, cities, choosen_city_id, choosen_product_type_id, choosen_fasovka_id, int(choosen_district_id))

        # Если отправил неправильный номер района:
        else:
            # Gets district list and adds to msg3_district
            # Gets tuple like  (2, 'Альпийские камни', 0.33, 1050, 'Красноярск', '11:Советский,...')q
            product_info = sql.get_product_info(choosen_city_id, choosen_product_type_id, choosen_fasovka_id)
            districts = product_info[5].split(',')
            # Gets districts dict: {'11':'Советский', ...}
            districts_list = [dist.split(':') for dist in districts]

            districts_str = ''
            for dist in districts_list:
                districts_str += f"{numbers[str(dist[0])]}: {dist[1]}\n"


            msg = f"{messages[10]}\n\n{districts_str}\n{messages[8]}\n\n{messages[13]}"
            message.reply_text(msg)

    # Запуститься после того как пользователь выбрал метод оплаты
    elif len(state.split(';')) == 4:
        state_list = state.split(';')
        choosen_city_id = int(state_list[0].replace('c', ''))
        choosen_product_type_id = int(state_list[1].replace('p', ''))
        choosen_fasovka_id = int(state_list[2].replace('f', ''))
        choosen_district_id = int(state_list[3].replace('d', ''))
        choosen_payment_method_id = message.text

        # Aviable payment methods tuple: ( (1, 'Оплатить балансом', 'wallet_adress'), ...)
        payment_methods_tuple = sql.get_payment_methods_list()
        payment_methods_id_list = list(map(lambda method: str(method[0]), payment_methods_tuple))

        # Если пользователь выбрал существующий номер метода оплаты
        if choosen_payment_method_id in payment_methods_id_list:
            # Changing user's state to 'c1;p2;f1;d11;m1' (1 - id city, 2 - product type, 3 - fasovka, 11 - id district, m1 - method 1)
            sql.change_user_state(message.chat.id, state + ';m' + choosen_payment_method_id)

            # Creating object, to send payment method page
            payment_page = pm.PaymentMethods(numbers, message, messages, cities, choosen_city_id,
                                             choosen_product_type_id, choosen_fasovka_id, choosen_district_id,
                                             choosen_payment_method_id)
            if choosen_payment_method_id == '1':
                payment_page.one()
            elif choosen_payment_method_id == '11':
                payment_page.eleven()
            elif choosen_payment_method_id == '12':
                payment_page.twelve()
            elif choosen_payment_method_id == '13':
                payment_page.thirteen()
            elif choosen_payment_method_id == '14':
                payment_page.fourteen()
            elif choosen_payment_method_id == '15':
                payment_page.fifteen()

        # Если пользователь выбрал неправильный номер метода
        else:
            # Part message "Choose payment method"
            # Gets ((1, 'Оплатить балансом', 'wallet_address'), (...), ...)
            payment_methods_tuple = sql.get_payment_methods_list()
            msg_payment_methods_list = ""
            for payment_method in payment_methods_tuple:
                msg_payment_methods_list += f"{numbers[str(payment_method[0])]}: {payment_method[1]}\n"

            msg = f"{messages[10]}\n\n{msg_payment_methods_list}\n{messages[8]}"
            message.reply_text(msg)

    # Запуститься после того как пользователь отправил что-то внутри метода оплаты
    elif len(state.split(';')) == 5:
        state_list = state.split(';')
        choosen_city_id = int(state_list[0].replace('c', ''))
        choosen_product_type_id = int(state_list[1].replace('p', ''))
        choosen_fasovka_id = int(state_list[2].replace('f', ''))
        choosen_district_id = int(state_list[3].replace('d', ''))
        choosen_payment_method_id = int(state_list[4].replace('m', ''))

        # чтобы не писал пользователь вернем ему обратно страницу метода "1: Оплатить балансом"
        payment_page = pm.PaymentMethods(numbers, message, messages, cities, choosen_city_id,
                                         choosen_product_type_id, choosen_fasovka_id, choosen_district_id,
                                         choosen_payment_method_id, state)

        # Если пользователь находится внутри метода "1: Оплатить балансом" и написал что-то
        if choosen_payment_method_id == 1:
            payment_page.one(wrong_requst=True)

        # Если пользователь находится внутри метода "11" и написал что-то
        elif choosen_payment_method_id == 11:
            payment_page.eleven(wrong_requst=True)

        # Если пользователь находится внутри метода "12" и написал что-то
        elif choosen_payment_method_id == 12:
            payment_page.twelve(wrong_requst=True)

        # Если пользователь находится внутри метода "13" и написал что-то
        elif choosen_payment_method_id == 13:
            pass

        # Если пользователь находится внутри метода "14" и написал что-то
        elif choosen_payment_method_id == 14:
            payment_page.fourteen(wrong_requst=True)

        # Если пользователь находится внутри метода "15" и написал что-то
        elif choosen_payment_method_id == 15:
            payment_page.fifteen(wrong_requst=True)

    elif len(state.split(';')) == 6:
        state_list = state.split(';')
        choosen_city_id = int(state_list[0].replace('c', ''))
        choosen_product_type_id = int(state_list[1].replace('p', ''))
        choosen_fasovka_id = int(state_list[2].replace('f', ''))
        choosen_district_id = int(state_list[3].replace('d', ''))
        choosen_payment_method_id = int(state_list[4].replace('m', ''))
        choosen_inner_payment_method_random = state_list[5].replace('pp', '')
        check_cancel_payment = message.text

        # чтобы не писал пользователь вернем ему обратно страницу метода "1: Оплатить балансом"
        payment_page = pm.PaymentMethods(numbers, message, messages, cities, choosen_city_id,
                                         choosen_product_type_id, choosen_fasovka_id, choosen_district_id,
                                         choosen_payment_method_id, state)

        # Срабатывает если он находиться внутри 15 метода -> 3: getBTC (CARD/Тинькофф Мобайл) RUB
        if len(choosen_inner_payment_method_random) and not choosen_inner_payment_method_random.isdigit():
            cancel = False
            # Если он выбрал "2: Отменить заявку"
            if check_cancel_payment == '2':
                cancel = True

            payment_page.inner_fifteen(choosen_inner_payment_method_random, cancel=cancel)

        # Если выбрал "1: Проверить заявку" или отправил любой другой смс
        else:
            payment_page.inner_fifteen(choosen_inner_payment_method_random)


def show_payment_menu(client, message, messages, cities, choosen_city_id, choosen_product_type_id, choosen_fasovka_id, choosen_district_id= None):
    product_info = sql.get_product_info(choosen_city_id, choosen_product_type_id, choosen_fasovka_id)

    # Part message "Choose payment method"
    msg3_choose_payment_message = f"\n{messages[7]}\n\n"
    # Gets ((1, 'Оплатить балансом', 'wallet_address'), (...), ...)
    payment_methods_tuple = sql.get_payment_methods_list()
    msg3_payment_methods_list = ""
    for payment_method in payment_methods_tuple:
        msg3_payment_methods_list += f"{numbers[str(payment_method[0])]}: {payment_method[1]}\n"

    msg3 = msg3_choose_payment_message + msg3_payment_methods_list

    # Если есть район, тогда отправиться "Вы выбрали: ИМЯ_РАЙОНА"
    if choosen_district_id:
        districts = product_info[5].split(',')

        # Gets { '11' : 'Советский', }
        districts_dict = {}
        for dist in districts:
            num_distname = dist.split(':')
            districts_dict[num_distname[0].strip()] = num_distname[1].strip()

        # Part message You choise "district"
        msg1 = f"{messages[1]} {districts_dict[str(choosen_district_id)]}\n\n"

        # Part message into ----------:
        msg2_city = f"{messages[2]} {cities[choosen_city_id]}"
        msg2_product = f"{messages[3]} {sql.get_product_name_by_id(choosen_product_type_id)}"
        msg2_district = f"{messages[4]} {districts_dict[str(choosen_district_id)]}"
        msg2_fasovka = f"{messages[5]} {product_info[2]} шт за {product_info[3]} руб"
        msg2 = f"{numbers['more_lines']}\n{msg2_city}\n{msg2_product}\n{msg2_district}\n{msg2_fasovka}\n{numbers['more_lines']}\n"

        # Part message commands_list and order_bot
        msg4 = f"\n{messages[8]}\n\n{messages[13]}"

        message.reply_text(msg1 + msg2 + msg3 + msg4)

    # Если у выбранного товара нету района
    else:
        # Part message Balance, You choise "fasovka name"
        msg1 = f"{messages[0]}\n\n{messages[1]} \"{product_info[3]} шт за {product_info[4]} руб\".\n\n"

        # Part message into ----------:
        msg2_city = f"{messages[2]} {cities[choosen_city_id]}"
        msg2_product = f"{messages[3]} {sql.get_product_name_by_id(choosen_product_type_id)}"
        msg2_fasovka = f"{messages[5]} {product_info[2]} шт за {product_info[3]} руб"
        msg2 = f"{numbers['more_lines']}\n{msg2_city}\n{msg2_product}\n{msg2_fasovka}\n{numbers['more_lines']}\n"

        # Part message commands_list
        msg4 = f"\n{messages[8]}"

        message.reply_text(msg1 + msg2 + msg3 + msg4)


def main_menus(client, message, wrong_request= None):
    if message.text == '$':
        sql.change_user_state(message.chat.id, '$')
        disput_menu(client, message)

    elif message.text == '#':
        sql.change_user_state(message.chat.id, '#')
        main_menu(client, message)

    elif message.text == '+':
        sql.change_user_state(message.chat.id, '+')
        get_price(client, message)

    elif message.text == '?':
        sql.change_user_state(message.chat.id, '?')
        help_menu(client, message)

    elif message.text == '777':
        sql.change_user_state(message.chat.id, '777')
        leave_comment(client, message)



app = Client("my_account")


@app.on_message()
def echo(client, message):
    menues = ['$', '#', '+', '?', '777']
    check_user = sql.get_user_state(message.chat.id)
    numbers = [str(i) for i in range(1, 26)]


    if not check_user:
        sql.add_user(message.chat.id)
        main_menu(client, message)
    else:
        # Gets ('$',) or None
        state = sql.get_user_state(message.chat.id)[0]

        if message.text in menues:
            main_menus(client, message)
        elif message.text == '999':
            get_feedbacks(client, message)
        elif message.text in numbers:
            choise_city(client, message)
        # Если пользователь отправил неправильный код и если он не находится внутри города или в комментариях, тогда он срабатывает:
        elif not state.startswith('c') and not state.startswith('999'):
            main_menu(client, message, with_wrong_request= True)
        elif state.startswith('999'):
            get_feedbacks(client, message)
        elif state.startswith('c'):
            choise_city(client, message)

app.run()
