from aiogram import types
from loader import dp, bot, admins
from keyboards.inline import admin_btn, cencel_btn
from utils.db_api import key_lang_list, key_answer_update, user_lang
from states import TextForm
from aiogram.dispatcher import FSMContext

@dp.message_handler(commands=['admin'], user_id=admins)
async def hello_Admin(msg: types.Message):
    btn = key_lang_list(msg.from_id)
    await msg.answer("Hello admin", reply_markup=admin_btn(btn))

@dp.callback_query_handler(lambda call: call.data == 'cencel', state='*')
async def cencell(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.delete()
    await call.message.answer("biykar etildi")
    btn = key_lang_list(call.from_user.id)
    await call.message.answer("Hello admin", reply_markup=admin_btn(btn))

@dp.callback_query_handler(lambda call: 'add=' in call.data)
async def add_key_for_text(call: types.CallbackQuery, state: FSMContext):
    menu_id = call.data.split('=')[1]
    await call.answer(menu_id)
    await state.update_data(cid=menu_id)
    await TextForm.next()
    await call.message.answer("Qaraqalpaq tilindegi kiril alfabetinde kiritin':", reply_markup=cencel_btn)
    await call.message.delete()

@dp.message_handler(state=TextForm.kkkl)
async def key_set_kkkl(msg: types.Message, state: FSMContext):
    await state.update_data(kkkl=msg.text)
    await TextForm.next()
    await msg.answer("Qaraqalpaq tilindegi latin alfabetinde kiritin':", reply_markup=cencel_btn)

@dp.message_handler(state=TextForm.kklt)
async def key_set_kklt(msg: types.Message, state: FSMContext):
    await state.update_data(kklt=msg.text)
    await TextForm.next()
    await msg.answer("O'zbek tilindegi kiril alfabetinde kiritin':", reply_markup=cencel_btn)
        
@dp.message_handler(state=TextForm.uzkl)
async def key_set_uzkl(msg: types.Message, state: FSMContext):
    await state.update_data(uzkl=msg.text)
    await TextForm.next()
    await msg.answer("O'zbek tilindegi latin alfabetinde kiritin':",reply_markup=cencel_btn)

@dp.message_handler(state=TextForm.uzlt)
async def key_set_uzlt(msg: types.Message, state: FSMContext):
    await state.update_data(uzlt=msg.text)
    await TextForm.next()
    await msg.answer("Rus tilinde kiritin'", reply_markup=cencel_btn)

@dp.message_handler(state=TextForm.ru)
async def key_set_uzlt(msg: types.Message, state: FSMContext):
    await state.update_data(ru=msg.text)
    data = await state.get_data()
    key_answer_update(data['kkkl'], data['cid'], 'kkkl')
    key_answer_update(data['kklt'], data['cid'], 'kklt')
    key_answer_update(data['uzkl'], data['cid'], 'uzkl')
    key_answer_update(data['uzlt'], data['cid'], 'uzlt')
    key_answer_update(data['ru'], data['cid'], 'ru')
    await msg.answer("mag'lumat qosildi")
    await state.finish()