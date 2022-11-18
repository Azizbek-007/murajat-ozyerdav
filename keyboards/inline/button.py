from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from lang.message import lang

lang_btn = InlineKeyboardMarkup().add(
    InlineKeyboardButton(text="Каракалпак(кириллица)", callback_data="lang=kkkl")
    ).add(
    InlineKeyboardButton(text="Каракалпак(латиница)", callback_data="lang=kklt")
    ).add(
    InlineKeyboardButton(text="Узбек(кириллица)", callback_data="lang=uzkl")
    ).add(
    InlineKeyboardButton(text="Узбек(латиница)", callback_data="lang=uzlt")
    ).add(
    InlineKeyboardButton(text="Русский", callback_data="lang=ru")
    )

def groupin_btn (user_id):
    return InlineKeyboardMarkup().add(
    InlineKeyboardButton("Принято", callback_data=f"ok={user_id}"),
    InlineKeyboardButton("Отказано", callback_data=f"no={user_id}")
    )

def murajat_btn(lang):
    return InlineKeyboardMarkup().add(
        InlineKeyboardButton("Муражати жиберуди тастйқлау", callback_data="murajatOK")
    ).add(
        InlineKeyboardButton("Бийкралау", callback_data="murajatNO")
    )


def admin_btn(btn):
    markup = InlineKeyboardMarkup()
    for x in btn:
        markup.add(InlineKeyboardButton(f"{x[1]}", callback_data=f"add={x[0]}")) 
    return markup

cencel_btn = InlineKeyboardMarkup().add( InlineKeyboardButton("cencel", callback_data='cencel') )