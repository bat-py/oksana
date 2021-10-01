import mysql_handler as sql
import crypto_price

class PaymentMethods:
    def __init__(self, numbers, message, messages, cities, choosen_city_id, choosen_product_type_id, choosen_fasovka_id, choosen_district_id, choosen_payment_method_id):
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

    def eleven(self, wrong_requst= None):
        # Gets (cource, price_in_crypto):
        crypto_info = crypto_price.get_cource('ltc', self.product_info[3])

        # Info in more_lines (use_more_commission)
        msg1_wallet = f"<b>Кошелек:</b> {sql.get_wallet_address(self.choosen_payment_method_id)[0]}"
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

    def twelve(self, wrong_requst= None):
        # Gets (cource, price_in_crypto):
        crypto_info = crypto_price.get_cource('btc', self.product_info[3])

        # Info in more_lines (use_more_commission)
        msg1_wallet = f"<b>Кошелек:</b> {sql.get_wallet_address(self.choosen_payment_method_id)[0]}"
        msg1_summa = f"<b>Сумма:</b> {crypto_info[1]} BTC"
        msg1_course = f"<b>Курс:</b> {crypto_info[0]} RUB/BTC"
        msg1 = f"<b>Переведите BTC</b>\n{self.numbers['more_lines']}\n{msg1_wallet}\n{msg1_summa}\n{msg1_course}\n{self.numbers['more_lines']}\n"

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

    def thirteen(self, wrong_requst= None):
        pass

    def fourteen(self, wrong_requst= None):
        pass

    def fifteen(self, wrong_requst= None):
        pass
