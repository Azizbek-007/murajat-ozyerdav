from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline import lang_btn, groupin_btn, murajat_btn
from keyboards.default import services_btn, back_btn
from utils.db_api import register_user, update_lang, get_answer, user_lang
from lang.message import lang
from aiogram.dispatcher import FSMContext
from states.form import Form
from loader import dp, bot
import re


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    print(lang.get('menu').get(user_lang(message.from_id)))
    register_user(
        message.from_id, 
        message.from_user.username, 
        message.from_user.first_name, 
        message.from_user.last_name)
    await message.answer("O'zin'izge qolay tildi tanlan':", reply_markup=lang_btn)

@dp.callback_query_handler(lambda call: call.data == 'murajatOK')
async def murjat_ok(call: types.CallbackQuery):
    await call.message.answer("​Ҳүрметли пуқара сиздиң мүрәжатиниз корип шығылмақта. Тез арада тийсли канийгелерден жуап алсасиз", reply_markup=services_btn)
    await call.message.copy_to(-818177578, reply_markup=groupin_btn(call.from_user.id))
    await call.message.delete()

@dp.callback_query_handler(lambda call: call.data == 'murajatNO')
async def murjat_NO(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("menu", reply_markup=services_btn)

@dp.callback_query_handler(lambda call: 'lang=' in call.data)
async def set_lang (call: types.CallbackQuery):
    lang = call.data.split('=')[1]
    update_lang(call.from_user.id, lang)
    await call.message.answer("menu", reply_markup=services_btn(lang))

@dp.callback_query_handler(lambda call: 'ok' in call.data)
async def ok_question(call: types.CallbackQuery):
    user_id = call.data.split('=')[1]
    await call.message.copy_to(-1001537252769)
    await bot.send_message(user_id, "Сиздин муражатиниз каралип шигилмакта хам тез арада тийсли канийгелрден жуап аласиз", reply_markup=services_btn)
    await call.message.delete()

@dp.callback_query_handler(lambda call: 'no' in call.data)
async def no_question(call: types.CallbackQuery):
    user_id = call.data.split('=')[1]
    await bot.send_message(user_id, "Ҳүрметли пуқара сиздиң мүрәжатиниз бизлер арқалы шешилмейди. Муражатинизди тийсли макемелерге жиберунызды усинис етемиз", reply_markup=services_btn)
    await call.message.delete()

@dp.message_handler(lambda msg: msg.text == lang.get('back').get(user_lang(msg.from_id)), state='*')
async def back_def(msg: types.Message, state: FSMContext):
    userLang = user_lang(msg.from_id)
    usertext = lang.get('back_text').get(userLang)
    await msg.answer(usertext, reply_markup=services_btn(userLang))
    await state.finish()

@dp.message_handler(lambda msg: msg.text in lang.get('menu').get(user_lang(msg.from_id)))
async def servoces_answer(msg: types.Message):
    userLang = user_lang(msg.from_id)
    usertext = lang.get('menu').get(userLang)
    text = msg.text
    if text == usertext[0]:
        await msg.answer(
            text=lang.get('ques1').get(userLang),
            reply_markup=back_btn(userLang))
        await Form.FIO.set()
    elif text == usertext[3]:
        await msg.answer("Муражат №7 дизимге алинди. Пуқара (ФИО, Тел Номер) Муражат мазмуни")
    elif len(get_answer(text)) > 0:
        await msg.answer(get_answer(text))

@dp.message_handler(state=Form.FIO)
async def send_msg_group(msg: types.Message, state: FSMContext):
    await state.update_data(FIO=msg.text)
    await Form.next()
    userLang = user_lang(msg.from_id)
    usertext = lang.get('ques2').get(userLang)
    await msg.answer(usertext, reply_markup=back_btn(userLang))

@dp.message_handler(state=Form.PHONE)
async def set_phone_number(msg: types.Message, state: FSMContext):
    await state.update_data(phone=msg.text)
    await Form.next()
    userLang = user_lang(msg.from_id)
    usertext = lang.get('ques3').get(userLang)
    await msg.answer(usertext, reply_markup=back_btn(userLang))

@dp.message_handler(state=Form.MUAJAT)
async def set_phone_number(msg: types.Message, state: FSMContext):
    data = await state.get_data()
    await msg.answer(f"{data['FIO']}\n{data['phone']}\n\n{msg.text}", reply_markup=murajat_btn('kk'))
    await state.finish()
