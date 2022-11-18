from aiogram.dispatcher.filters.state import StatesGroup, State

class Form(StatesGroup):
    prommis = State()
    FIO = State()
    PHONE = State()
    MUAJAT = State()

class TextForm(StatesGroup):
    kkkl = State()
    kklt = State()
    uzkl = State()
    uzlt = State()
    ru = State()