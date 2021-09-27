import pymysql
from pyrogram import Client, filters
import tgcrypto

app = Client("my_account")

@app.on_message()
def echo(client, message):
    #if message.text == ""
    #message.forward('me')        # all messages saves in Избранное

    if message.text == ''
    message.reply_text('hi')

app.run()