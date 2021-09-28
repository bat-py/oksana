from pyrogram import Client, filters
import tgcrypto

import mysql_handler
import mysql_handler as sql
import json

with open('numbers.json', 'r') as n:
    numbers = json.load(n)

def get_cities_list():
    # returns tuple: ( (1, 'Moscow'), ... )
    city_tuple = sql.get_cities()

    city_dict = {}

    # returns dict(id:'witch graphic nubmers'):  { 1 : '7️⃣ Moscow', ... }
    for city_id, city in city_tuple:
        for i in city:
            city_dict[city_id] = numbers[str(city_id)] + ' ' + city
    print(city_dict)
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


app = Client("my_account")

@app.on_message()
def echo(client, message):
    if message.text == '$':
        disput_menu(client, message)

    elif message.text == '#':
        main_menu(client, message)

    elif message.text == '+':
        mysql_handler.get_price()

    elif message.text == '?':
        help_menu(client, message)


app.run()
