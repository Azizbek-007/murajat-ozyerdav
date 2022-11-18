from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

services_btn = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton("Муражат етиу")
).add(
    KeyboardButton("Канийгелер менен байлансиу")
).add(
    KeyboardButton("Хизметлер"),
    KeyboardButton("Манзил")
)

back_btn = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton("Arqaga")
)

