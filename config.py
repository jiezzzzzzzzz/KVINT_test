import telebot
import os

token = os.environ['TOKEN']
bot = telebot.TeleBot(os.getenv('TOKEN'))


states = ['start', 'choose_pizza_size', 'choose_payment_method', 'check']
transitions = [
    {'trigger': 'one', 'source': 'start', 'dest': 'choose_pizza_size'},
    {'trigger': 'two', 'source': 'choose_pizza_size', 'dest': 'choose_payment_method'},
    {'trigger': 'three', 'source': 'choose_payment_method', 'dest': 'check'},
    {'trigger': 'four', 'source': 'check', 'dest': 'start'}
]

size = ''
pay = ''