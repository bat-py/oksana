from pyrogram import Client, filters
import tgcrypto
import mysql_handler as sql

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

        msg_header = f'{messages[0][0]}\n\n{messages[1][0]}\n\n{messages[2][0]}\n\n'
        msg_cities = 3
        msg_list_commands = f'{messages[3][0]}\n\n{messages[4][0]}'
        message.reply_text(msg_header+msg_list_commands)


app.run()
