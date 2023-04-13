from aiogram import types, Dispatcher
from create_bot import bot
from keyboards.kb_client import *
from media.library import *
from media.base import *


def len_dr(pasw, user):
    count = 0
    mas = cards.get()
    for b in mas:
        count += 1
        if pasw == b['idChat']:
            return True, count-1
        if pasw == b['idChat']:
            return 'q'
    return False


def counter(id, step):
    d = cards.get()
    for i in d:
        if i['idChat'] == id:
            indx = d.index(i)
            d.remove(i)
            i.update({'test': step})
            d.insert(indx, i)
            db.reference("/cards/").set(d)


async def start(message: types.Message):
    try:
        for i in cards.get():
            if i['idChat'] == message.from_user.id:
                return await message.answer(f'Здравствуй {message.from_user.first_name}\n Чем займемся? ', reply_markup=menu.main_window)
        await message.answer('Введите пароль')
    except TypeError:
        await check(message)


async def menu_window(message: types.Message):
    await message.answer(f'Здравствуй {message.from_user.first_name}\n Чем займемся? ', reply_markup=menu.main_window)
    await message.delete()


async def text1_call(callback: types.CallbackQuery):
    photo.text1_msg = await callback.message.answer_photo(photo.text1_tok)
    await callback.message.answer(text.text1_t, reply_markup=learn.first_text_window)


async def text2_call(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    photo.text2_msg = await callback.message.answer_photo(photo.text2_tok)
    counter(user_id, 1)
    await callback.message.answer(text.text2_t, reply_markup=learn.second_text_window)


async def test1_call(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    photo.test1_msg = await callback.message.answer_photo(photo.test1_tok)
    counter(user_id, 2)
    await callback.message.answer(text.test1_t, reply_markup=test.first_test_window)


async def false1_call(callback: types.CallbackQuery):
    await callback.message.answer('Нет. ', reply_markup=test.first_wrong_window)


async def test2_call(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    photo.test2_msg = await callback.message.answer_photo(photo.test2_tok)
    counter(user_id, 3)
    await callback.message.answer(text.test2_t, reply_markup=test.second_test_window)


async def false2_call(callback: types.CallbackQuery):
    await callback.message.answer('Нет. ', reply_markup=test.second_wrong__window)


async def test3_call(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    photo.test3_msg = await callback.message.answer_photo(photo.test3_tok)
    counter(user_id, 4)
    await callback.message.answer(text.test3_t, reply_markup=test.third_test_window)


async def false3_call(callback: types.CallbackQuery):
    await callback.message.answer('Нет. ', reply_markup=test.third_wrong_window)


async def win_call(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    counter(user_id, 5)
    await callback.message.answer(text.win_t, reply_markup=test.win_window)


async def about_call(callback: types.CallbackQuery):
    photo.about_msg = await callback.message.answer_photo(photo.about_tok)
    await callback.message.answer(text.about_t, reply_markup=other.about_window)


async def product_call(callback: types.CallbackQuery):
    photo.product_msg = await callback.message.answer_photo(photo.product_tok)
    await callback.message.answer(text.product_t, reply_markup=other.product_window)


async def staff_call(callback: types.CallbackQuery):
    await callback.message.answer('Наши сотрудники', reply_markup=key)


async def proff_call(callback: types.CallbackQuery):
    for man in cards.get():
        if man['prof'] == callback.data:
            staff_text = f"{man['fio']}\nТелеграм:{man['tg']}\nТелефон:{man['numberPhone']}"
            photo.staff_msg = await callback.message.answer_photo(photo.staff_tok)
            await callback.message.answer(staff_text)
    await callback.message.answer('Наши сотрудники', reply_markup=test.win_window)


async def link_call(callback: types.CallbackQuery):
    photo.link_msg = await callback.message.answer_photo(photo.link_tok)
    await callback.message.answer(text.link_t, reply_markup=other.link_window)


async def faq_call(callback: types.CallbackQuery):
    photo.faq_msg = await callback.message.answer_photo(photo.faq_tok)
    await callback.message.answer(text.faq_t, reply_markup=other.faq_window)


async def spam(callback: types.CallbackQuery):
    messa = db.reference('Massege')
    bo = messa.get()
    if len(bo):
        for i in bo[::-1]:
            if callback.from_user.id == i['id']:
                id_tip = i['id']
                text_tip = i['title']
                return await callback.bot.send_message(id_tip, f'Вам сообщение: {text_tip}', reply_markup=other.spam_window)
        await callback.message.answer('Ничего нет')


async def tp(callback: types.CallbackQuery):
    await callback.message.answer('Введите вопрос:')


async def start_call(callback: types.CallbackQuery):
    await callback.message.answer(f'Здравствуй {callback.from_user.first_name}\n Чем займемся? ', reply_markup=menu.main_window)


async def quest1(message: types.Message):
    await message.answer('88005553535', reply_markup=other.spam_window)


async def quest2(message: types.Message):
    await message.answer('Обратитесь к админу @dmikrit', reply_markup=other.spam_window)


async def check(message: types.Message):
    try:
        flag, indx = len_dr(message.text, message.from_user.id)
        d = cards.get()
        a = d[indx]
        d.remove(a)
        a.update({'idChat': message.from_user.id})
        a.update({'state': flag})
        d.insert(indx, a)
        db.reference("/cards/").set(d)
        await message.answer(f'Здравствуй {message.from_user.first_name}\n Чем займемся? ', reply_markup=menu.main_window)

    except TypeError:
        print(cards.get())
        if len(cards.get()):
            for i in cards.get():
                if i['idChat']:
                    if i['idChat'] == message.from_user.id:
                        return await message.answer(f'Здравствуй {message.from_user.first_name}\n Чем займемся? ', reply_markup=menu.main_window)
            await message.answer('Введите пароль')


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start, commands='start')
    dp.register_message_handler(menu_window, commands='menu')
    dp.register_callback_query_handler(text1_call, text='text content request')
    dp.register_callback_query_handler(text2_call, text='sec text content request')
    dp.register_callback_query_handler(test1_call, text='first question request')
    dp.register_callback_query_handler(false1_call, text='first wrong request')
    dp.register_callback_query_handler(test2_call, text='second question request')
    dp.register_callback_query_handler(false2_call, text='second wrong request')
    dp.register_callback_query_handler(test3_call, text='third question request')
    dp.register_callback_query_handler(false3_call, text='third wrong request')
    dp.register_callback_query_handler(win_call, text='win request')
    dp.register_callback_query_handler(about_call, text='about us request')
    dp.register_callback_query_handler(product_call, text='product request')
    dp.register_callback_query_handler(link_call, text='link request')
    dp.register_callback_query_handler(staff_call, text='staff request')
    for i in people:
        dp.register_callback_query_handler(proff_call, text=i)
    dp.register_callback_query_handler(faq_call, text='FAQ request')
    dp.register_callback_query_handler(spam, text='spam request')
    dp.register_callback_query_handler(tp, text='tp')
    dp.register_callback_query_handler(start_call, text='start request')
    dp.register_message_handler(quest1, lambda message: 'номер' in message.text.lower())
    dp.register_message_handler(quest2, lambda message: 'код' in message.text.lower())
    dp.register_message_handler(check)