from pyrogram import Client, filters
import tgcrypto
import mysql_handler as sql
import json

with open('numbers.json', 'r') as n:
    numbers = json.load(n)

def get_cities_list():
    # returns
    list_cities = sql.get_cities()

    cities = []

    for n, city in enumerate(list_cities):
        num = str(n+1)
        number = ''
        for i in num:
            number += numbers[str(i)]

        cities.append(number + ' ' + city)

    return cities


app = Client("my_account")

@app.on_message()
def echo(client, message):
    if message.text == "#":
        # message.forward('me')        # all messages saves in Избранное
        messages = sql.get_bot_messages('main_menu_comments',
                                        'main_menu_balance',
                                        'main_menu_city',
                                        'list_commands',
                                        'order_bot'
                                        )

        msg_header = f'{messages[0]}\n\n{messages[1]}\n\n{messages[2]}\n\n'

        cities = get_cities_list()
        msg_cities = ''
        [msg_cities+city+'\n' for city in cities]
        print(msg_cities)
        msg_list_commands = f'{messages[3]}\n\n{messages[4]}'
        message.reply_text(msg_header+msg_cities+msg_list_commands)


app.run()
