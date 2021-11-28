from transitions import Machine

from config import *

machine = Machine(model=bot, states=states, initial='start', transitions=transitions)


@bot.message_handler(commands=['start'])
def start_mes(message):
    bot.send_message(message.from_user.id, 'Какую вы хотите пиццу? Большую или маленькую?')
    bot.one()


@bot.message_handler(func=lambda message: bot.state == 'choose_pizza_size')
def pizza_size_reg(message):
    global size
    size = message.text
    bot.send_message(message.from_user.id, 'Как вы будете платить?')
    bot.two()


@bot.message_handler(func=lambda message: bot.state == 'choose_payment_method')
def payment_method_reg(message):
    global pay
    pay = message.text
    bot.send_message(message.from_user.id, 'Вы хотите ' + size.lower() + ' пиццу, оплата - ' + pay.lower() + '?')
    bot.three()


@bot.message_handler(func=lambda message: bot.state == 'check')
def check_order(message):
    if message.text == 'Да':
        bot.send_message(message.from_user.id, 'Спасибо за заказ')
        bot.four()
    else:
        bot.send_message(message.from_user.id, 'Давайте попробуем заново')
        bot.four()
        bot.send_message(message.from_user.id, 'Какую вы хотите пиццу? Большую или маленькую?')
        bot.one()


bot.polling(none_stop=True, interval=0)