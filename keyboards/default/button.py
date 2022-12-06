from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from lang.message import lang

def services_btn (lang_user):
    a = []
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    for x in lang.get('menu').get(lang_user):
        a.append(KeyboardButton(x))
    return markup.add(*a)

def back_btn (lang_user): 
    return ReplyKeyboardMarkup(resize_keyboard=True).add(
        KeyboardButton(lang.get('back').get(lang_user)) 
    )

