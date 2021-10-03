import mysql_handler as sql
import crypto_price
import random


class Random:
    def __init__(self):
        self.letters = list(map(chr, range(ord('A'), ord('Z') + 1)))

    def str6(self):
        random_str = ''
        for i in range(0, 6):
            random_str += random.choice(self.letters)

        return random_str


class PaymentMethods:
    def __init__(self, numbers, message, messages, cities, choosen_city_id, choosen_product_type_id, choosen_fasovka_id, choosen_district_id, choosen_payment_method_id, state=None):
        self.numbers = numbers
        self.message = message
        self.messages = messages
        self.cities = cities
        self.choosen_city_id = choosen_city_id
        self.choosen_product_type_id = choosen_product_type_id
        self.choosen_fasovka_id = choosen_fasovka_id
        self.choosen_district_id = choosen_district_id
        self.choosen_payment_method_id = choosen_payment_method_id
        self.product_info = sql.get_product_info(choosen_city_id, choosen_product_type_id, choosen_fasovka_id)
        self.state = state

    def one(self, wrong_requst= None):
        # Part msg: Your balance, more_lines
        msg1 = f"{self.messages[14]}\n\n"

        # Part message into ----------:
        msg2_city = f"{self.messages[2]} {self.cities[self.choosen_city_id]}"
        msg2_product = f"{self.messages[3]} {sql.get_product_name_by_id(self.choosen_product_type_id)}"
        msg2_fasovka = f"{self.messages[5]} {self.product_info[2]} шт за {self.product_info[3]} руб"
        msg2 = f"{self.numbers['more_lines']}\n{msg2_city}\n{msg2_product}\n{msg2_fasovka}\n{self.numbers['more_lines']}\n\n\n"

        # Pay with balance
        msg3 = f"{self.messages[15]}\n{self.numbers['more_lines']}\n{self.messages[16]} {self.product_info[3]} рублей\n\n{self.messages[17]}\n{self.numbers['more_lines']}\n\n"

        # Pay button and list_commands
        msg4 = f"{self.messages[18]}\n\n{self.messages[8]}"

        msg = msg1 + msg2 + msg3 + msg4
        self.message.reply_text(msg)

    def eleven(self, wrong_requst=None, short_page=None):
        if not short_page:
            # Gets (cource, price_in_crypto):
            crypto_info = crypto_price.get_cource('ltc', self.product_info[3])

            # Wallets
            wallets_list = []
            wallets_tuple = sql.get_wallet_address(self.choosen_payment_method_id)
            if wallets_tuple:
                wallets_list.extend(wallets_tuple[0].split(','))
            wallets_list = [i.strip() for i in wallets_list]

            # Info in more_lines (use_more_commission)
            msg1_wallet = f"<b>Кошелек:</b> {random.choice(wallets_list)}"
            msg1_summa = f"<b>Сумма:</b> {crypto_info[1]} LTC"
            msg1_course = f"<b>Курс:</b> {crypto_info[0]} RUB/LTC"
            msg1 = f"<b>Переведите LTC</b>\n{self.numbers['more_lines']}\n{msg1_wallet}\n{msg1_summa}\n{msg1_course}\n{self.numbers['more_lines']}\n"

            # Остальное меню до list_commands
            msg2 = f"{self.messages[19]}\n\n"
            # Commands list
            msg3 = f"{self.messages[8]}"
            # Order bot
            msg4 = f"\n\n{self.messages[13]}"

            if wrong_requst:
                msg = msg1 + msg2 + msg3 + msg4
            else:
                msg = msg1 + msg2 + msg3

            self.message.reply_text(msg)
        # Если отправил "!myltc"
        else:
            msg1 = f"{sql.get_wallet_address(self.choosen_payment_method_id)[0]}\n\n1⃣: Проверить оплату\n\n"
            msg2 = self.messages[8]
            self.message.reply_text(msg1 + msg2)

    def twelve(self, wrong_requst= None, short_page=None):
        if not short_page:
            # Gets (cource, price_in_crypto):
            crypto_info = crypto_price.get_cource('btc', self.product_info[3])

            # Wallets
            wallets_list = []
            wallets_tuple = sql.get_wallet_address(self.choosen_payment_method_id)
            if wallets_tuple:
                wallets_list.extend(wallets_tuple[0].split(','))
            wallets_list = [i.strip() for i in wallets_list]

            # Info in more_lines (use_more_commission)
            msg1_wallet = f"<b>Кошелек:</b> {random.choice(wallets_list)}"
            msg1_summa = f"<b>Сумма:</b> {crypto_info[1]} BTC"
            msg1_course = f"<b>Курс:</b> {crypto_info[0]} RUB/BTC"
            msg1 = f"<b>Переведите BTC</b>\n{self.numbers['more_lines']}\n{msg1_wallet}\n{msg1_summa}\n{msg1_course}\n{self.numbers['more_lines']}\n"

            # Остальное меню до list_commands
            msg2 = f"{self.messages[19]}\n\n".replace('myltc', 'mybtc')
            # Commands list
            msg3 = f"{self.messages[8]}"
            # Order bot
            msg4 = f"\n\n{self.messages[13]}"

            if wrong_requst:
                msg = msg1 + msg2 + msg3 + msg4
            else:
                msg = msg1 + msg2 + msg3

            self.message.reply_text(msg)


        # Если отправил "!mybtc"
        else:
            msg1 = f"{sql.get_wallet_address(self.choosen_payment_method_id)[0]}\n\n1⃣: Проверить оплату\n\n"
            msg2 = self.messages[8]
            self.message.reply_text(msg1 + msg2)


    def thirteen(self, wrong_requst= None, inner_payment=None):
        if not inner_payment:
            addt_messeges = sql.get_bot_messages('warning_auto_change', 'warning_may_change_price', 'thirteen_page_buttons')
            # Warnings part
            msg1 = f"{addt_messeges[0]}\n{self.numbers['more_lines']}\n{addt_messeges[1]}\n{self.numbers['more_lines']}\n"

            # Price part
            msg2 = f"<b>Цена товара : {self.product_info[3]} RUB</b>\n{self.numbers['more_lines']}\n<b>Выберите обменный пункт</b>\n{self.numbers['more_lines']}\n"

            # Comission info part
            msg3_3 = f"<b>FastChange (CARD/TELE2) RUB</b>\nСумма к оплате ПРИМЕРНО: {round(self.product_info[3]*1.12, 2)} RUB\n\n"
            msg3_4 = f"<b>getBTC (CARD/Тинькофф Мобайл) RUB</b>\nСумма к оплате ПРИМЕРНО: {round(self.product_info[3]*1.13, 2)} RUB\n\n"
            msg3_5 = f"<b>Exchanger Charlie RUB</b>\nСумма к оплате ПРИМЕРНО: {round(self.product_info[3]*1.14, 2)} RUB\n\n"
            msg3_6 = f"<b>Exchanger Alfa RUB</b>\nСумма к оплате ПРИМЕРНО: {round(self.product_info[3]*1.16, 2)} RUB\n\n"
            msg3 = msg3_3 + msg3_4 + msg3_5 + msg3_6

            # Buttons
            msg4 = addt_messeges[2]

            # Command list + order_bot
            msg5 = f"\n\n{self.messages[8]}\n\n{self.messages[13]}"

            msg = msg1 + msg2 + msg3 + msg4 + msg5
            self.message.reply_text(msg)

        # Срабатывает если быврал какую нибудь метод оплаты (3: Fastchange, 4: GetBTC, 5: Exchanger CHarlie, 6: Exchanger Alfa
        else:
            random = Random().str6()

            sql.change_user_state(self.message.chat.id, self.state + f';pp{random}')
            self.inner_thirteen(random)


    def inner_thirteen(self, random_application, cancel=None):
        pass

    def fourteen(self, wrong_requst= None):
        # Вернет сообщение: "Unknown error occured! Details : 400"
        if self.message.text == '3':
            addt_messeges = sql.get_bot_messages('warning_auto_change', 'error_400')

            # Warnings part
            msg1 = f"{addt_messeges[0]}\n{self.numbers['more_lines']}\n{addt_messeges[1]}\n\n3⃣: Exchanger Charlie RUB\n\n"
            # List_commands
            msg2 = self.messages[8]

            self.message.reply_text(msg1 + msg2)

        else:
            addt_messeges = sql.get_bot_messages('warning_auto_change', 'warning_may_change_price')
            # Warnings part
            msg1 = f"{addt_messeges[0]}\n{self.numbers['more_lines']}\n{addt_messeges[1]}\n{self.numbers['more_lines']}\n"

            # Price part
            msg2_real = f"<b>Цена товара : {self.product_info[3]} RUB</b>\n{self.numbers['more_lines']}\n<b>Выберите обменный пункт</b>\n{self.numbers['more_lines']}\n"
            msg2_with_comission = f"<b>Exchanger Charlie RUB</b>\nСумма к оплате ПРИМЕРНО: {self.product_info[3]*1.18} RUB\n\n"
            msg2 = msg2_real + msg2_with_comission

            # Button №3
            msg3 = '3⃣: Exchanger Charlie RUB\n\n'
            # List_commands
            msg4 = self.messages[8]

            self.message.reply_text(msg1 + msg2 + msg3 + msg4)

    def fifteen(self, wrong_requst= None):
        if self.message.text == '3':
            # pp3 это для страницы 15 (qiwi)
            random = Random().str6()

            sql.change_user_state(self.message.chat.id, self.state + f';pp{random}')
            self.inner_fifteen(random)

        else:
            addt_messeges = sql.get_bot_messages('warning_auto_change', 'warning_may_change_price')
            # Warnings part
            msg1 = f"{addt_messeges[0]}\n{self.numbers['more_lines']}\n{addt_messeges[1]}\n{self.numbers['more_lines']}\n"

            # Price part
            msg2_real = f"<b>Цена товара : {self.product_info[3]} RUB</b>\n{self.numbers['more_lines']}\n<b>Выберите обменный пункт</b>\n{self.numbers['more_lines']}\n"
            msg2_with_comission = f"<b>getBTC (CARD/Тинькофф Мобайл) RUB</b>\nСумма к оплате ПРИМЕРНО: {self.product_info[3]*1.15} RUB\n\n"
            msg2 = msg2_real + msg2_with_comission

            # Button №3
            msg3 = '3⃣: getBTC (CARD/Тинькофф Мобайл) RUB\n\n'
            # List_commands
            msg4 = self.messages[8]

            self.message.reply_text(msg1 + msg2 + msg3 + msg4)

    # Отравить сообщения про заявку
    def inner_fifteen(self, random_application, cancel=None):
        # Если отправил любое сообщение кроме "2"
        if not cancel:
            addt_messeges = sql.get_bot_messages('warning_auto_change', 'qiwi_info')
            # Warnings part
            msg1 = f"{addt_messeges[0]}\n{self.numbers['more_lines']}\n<b>Вы выбрали обменный пункт getBTC (CARD/Тинькофф Мобайл)</b>\n{self.numbers['more_lines']}\n"

            # Wallets
            wallets_list = []
            wallets_tuple = sql.get_wallet_address(self.choosen_payment_method_id)
            if wallets_tuple:
                wallets_list.extend(wallets_tuple[0].split(','))
            wallets_list = [i.strip() for i in wallets_list]

            # Номер Заявки, Qiwi wallet, price, time
            msg2_req = f"✅ <b>Номер вашей заявки:</b> {random_application}\n"
            msg2_qiwi = f"✅ <b>Номер кошелька Qiwi:</b> {random.choice(wallets_list)}\n"
            msg2_price = f"✅ <b>Сумма для пополнения:</b> {int(self.product_info[3] * 1.16)}\n"
            msg2_time = f"✅ <b>До конца оплаты:</b> 1 час\n"
            msg2 = msg2_req + msg2_qiwi + msg2_price + msg2_time + self.numbers['more_lines'] + '\n'

            # Qiwi_zInfo
            msg3 = f"{addt_messeges[1]}\n\n"

            # Buttons
            msg4 = "1⃣: Проверить оплату\n2⃣: Отменить заявку\n\n"

            # command list
            msg5 = self.messages[8]
            self.message.reply_text(msg1 + msg2 + msg3 + msg4 + msg5)

        else:
            sql.change_user_state(self.message.chat.id, '#')
            # Warnings part
            addt_messeges = sql.get_bot_messages('warning_auto_change')
            msg1 = f"{addt_messeges[0]}\n{self.numbers['more_lines']}\n"

            # Your application(заявка) canceled
            msg2 = f"Ваша заявка № {random} успешно удалена!\nВы будете возвращены в главное меню.\n\n"

            # List_commands
            msg3 = self.messages[8]

            self.message.reply_text(msg1 + msg2+ msg3)