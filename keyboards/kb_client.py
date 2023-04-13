from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from media.library import *
from media.base import *

class Menu:
    def __init__(self):
        self.main_window = InlineKeyboardMarkup(row_width=2)
        self.widgets()

    def widgets(self):
        self.main_window.add(
            InlineKeyboardButton(text='Обучение', callback_data='text content request'),
            InlineKeyboardButton(text='О компании', callback_data='about us request'),
            InlineKeyboardButton(text='Коллеги', callback_data='staff request'),
            InlineKeyboardButton(text='Контакты', callback_data='link request'),
            InlineKeyboardButton(text='FAQ', callback_data='FAQ request'),
            InlineKeyboardButton(text='Сообщения', callback_data='spam request'),
            InlineKeyboardButton(text='Тех.Поддержка', callback_data='tp')
        )


class Other:
    def __init__(self):
        self.faq_window = InlineKeyboardMarkup(row_width=2)
        self.link_window = InlineKeyboardMarkup(row_width=2)
        self.product_window = InlineKeyboardMarkup(row_width=1)
        self.about_window = InlineKeyboardMarkup(row_width=1)
        self.spam_window = InlineKeyboardMarkup(row_width=1)
        self.widgets()

    def widgets(self):
        self.about_window.add(
            InlineKeyboardButton(text='Продукты', callback_data='product request'),
            InlineKeyboardButton(text='Выход', callback_data='start request')
        )
        self.product_window.add(
            InlineKeyboardButton(text='Назад', callback_data='about us request'),
            InlineKeyboardButton(text='Выход', callback_data='start request')
        )
        self.faq_window.add(InlineKeyboardButton(text='Выход', callback_data='start request'))
        self.link_window.add(InlineKeyboardButton(text='Выход', callback_data='start request'))
        self.spam_window.add(InlineKeyboardButton(text='Выход', callback_data='start request'))


class Learn:
    def __init__(self):
        self.first_text_window = InlineKeyboardMarkup(row_width=1)
        self.second_text_window = InlineKeyboardMarkup(row_width=1)
        self.widgets()

    def widgets(self):
        self.first_text_window.add(
            InlineKeyboardButton(text='Cлeдующий', callback_data='sec text content request'),
            InlineKeyboardButton(text='Выход', callback_data='start request')
        )
        self.second_text_window.add(
            InlineKeyboardButton(text='Cлeдующий', callback_data='first question request'),
            InlineKeyboardButton(text='Выход', callback_data='start request')
        )


class Test:
    def __init__(self):
        self.first_test_window = InlineKeyboardMarkup(row_width=2)
        self.first_wrong_window = InlineKeyboardMarkup(row_width=2)
        self.second_test_window = InlineKeyboardMarkup(row_width=2)
        self.second_wrong__window = InlineKeyboardMarkup(row_width=2)
        self.third_test_window = InlineKeyboardMarkup(row_width=2)
        self.third_wrong_window = InlineKeyboardMarkup(row_width=2)
        self.win_window = InlineKeyboardMarkup(row_width=2)
        self.widgets()

    def widgets(self):
        self.first_test_window.add(
            InlineKeyboardButton(text='1', callback_data='first wrong request'),
            InlineKeyboardButton(text='2', callback_data='second question request'),
            InlineKeyboardButton(text='3', callback_data='first wrong request'),
            InlineKeyboardButton(text='4', callback_data='first wrong request'),
            InlineKeyboardButton(text='Выход', callback_data='start request')
        )
        self.first_wrong_window.add(InlineKeyboardButton(text='Назад', callback_data='first question request'))

        self.second_test_window.add(
            InlineKeyboardButton(text='1', callback_data='third question request'),
            InlineKeyboardButton(text='2', callback_data='second wrong request'),
            InlineKeyboardButton(text='3', callback_data='second wrong request'),
            InlineKeyboardButton(text='4', callback_data='second wrong request'),
            InlineKeyboardButton(text='Выход', callback_data='start request')
        )
        self.second_wrong__window.add(InlineKeyboardButton(text='Назад', callback_data='second question request'))

        self.third_test_window.add(
            InlineKeyboardButton(text='1', callback_data='third wrong request'),
            InlineKeyboardButton(text='2', callback_data='third wrong request'),
            InlineKeyboardButton(text='3', callback_data='third wrong request'),
            InlineKeyboardButton(text='4', callback_data='win request'),
            InlineKeyboardButton(text='Выход', callback_data='start request')
        )
        self.third_wrong_window.add(InlineKeyboardButton(text='Назад', callback_data='third question request'))

        self.win_window.add(InlineKeyboardButton(text='Выход', callback_data='start request'))


people = []
red = []

for item in proff.get():
    proff_text = f"{item['name']}"
    red.append(InlineKeyboardButton(text=proff_text, callback_data=f"{item['name']}"))
    people.append(f"{item['name']}")
key = InlineKeyboardMarkup(row_width=1)
key.add(*red)

menu = Menu()
other = Other()
learn = Learn()
test = Test()







