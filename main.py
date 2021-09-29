from pyrogram import Client, filters
import tgcrypto

import mysql_handler
import mysql_handler as sql
import json

with open('numbers.json', 'r') as n:
    numbers = json.load(n)

def get_cities_list():
    '''
    returns dict like: {1: '7️⃣ Moscow', ... }
    '''

    # returns tuple: ( (1, 'Moscow'), ... )
    city_tuple = sql.get_cities()

    city_dict = {}

    # returns dict(id:'witch graphic nubmers'):  { 1 : '7️⃣ Moscow', ... }
    for city_id, city in city_tuple:
        for i in city:
            city_dict[city_id] = numbers[str(city_id)] + ' ' + city
    return city_dict


def main_menu(client, message):
    # message.forward('me')        # all messages saves in Избранное
    messages = sql.get_bot_messages('main_menu_comments',
                                    'main_menu_balance',
                                    'main_menu_city',
                                    'list_commands',
                                    'order_bot'
                                    )

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
    products_list = mysql_handler.get_price()


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


def show_comments(client, message):
    messages = sql.get_bot_messages('show_more',
                                    'list_commands'
                                    )

    state = sql.get_user_state(message.chat.id)[0]
    states = state.split(';')
    if not states.count('999'):
        sql.change_user_state(message.chat.id, '999')
        # now we shoud get 1-5 last comments
    else:
        # c = states.count('999')
        # now we should get c*(1-5)


    #

    msg = messages[0] + '\n\n' + messages[1]
    message.reply_text(msg)


def main_menus(client, message):
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


#def page_state(client, message, state):
    #state = sql.get_user_state(message.chat.id)

    #if not state:
    #    sql.add_user(message.chat.id)
    #    main_menu(client, message)
    #    return '#'
    #else:
    #    sql.change_user_state(message.chat.id, state)
    #    page_state(client, message)


#def page_state(client, message):
#    state = sql.get_user_state(message.chat.id)
#    print(state)


app = Client("my_account")


@app.on_message()
def echo(client, message):
    menues = ['$', '#', '+', '?', '777']

    check_user = sql.get_user_state(message.chat.id)
    if not check_user:
        sql.add_user(message.chat.id)
        main_menu(client, message)
    else:
        if message.text in menues:
            main_menus(client, message)
        elif message.text == '999':
            show_comments(client, message)


app.run()
