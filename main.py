from aiogram.dispatcher.filters import Text
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.storage import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import markups as nav
from markups import *

TOKEN = '5015849769:AAFNs-hiQMVkEEA6C6LcCjsnNN4YAzzkWdI'


bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await bot.send_message(message.from_user.id, "Привет {0.first_name} я Бот предназначен для безукоризненного подчинения Валерчику".format(message.from_user), reply_markup=nav.mainMenu)


@dp.message_handler()
async def bot_message(message: types.Message):
    if message.text == 'Большые бабки':
        await message.answer('Введи 20к', reply_markup=nav.otherMenu)
        await Money._20k.set()


@dp.message_handler(state=Money._20k)
async def _20k(message: types.Message, state: FSMContext):
    global __20k
    if message.text != "FUCK GO BACK":
        if message.text.isdigit() == True:
            __20k = message.text
            await Money.next()
            await message.answer("Введите 10к", reply_markup=nav.otherMenu)
        else:
            await message.answer("Ты походу туповат вводи числа!")
            await message.answer("Введи 20к", reply_markup=nav.otherMenu)
            await Money._20k.set()
    else:
        await message.answer("Введи 20к", reply_markup=nav.otherMenu)
        await Money._20k.set()


@dp.message_handler(state=Money._10k)
async def _10k(message: types.Message, state: FSMContext):
    global __10k
    __10k = message.text
    if message.text != "FUCK GO BACK":
        if message.text.isdigit() == True:
            await Money.next()
            await message.answer("Введите 5к", reply_markup=nav.otherMenu)
        else:
            await message.answer("Only numbers!")
            await message.answer("Введи 10к", reply_markup=nav.otherMenu)
            await Money._10k.set()
    else:
        await message.answer("Введи 20к", reply_markup=nav.otherMenu)
        await Money._20k.set()


@dp.message_handler(state=Money._5k)
async def _5k(message: types.Message, state: FSMContext):
    global __5k
    if message.text != "FUCK GO BACK":
        if message.text.isdigit() == True:
            __5k = message.text
            await Money._2k.set()
            await message.answer("Введите 2к", reply_markup=nav.otherMenu)
        else:
            await message.answer("Тяжело быть человеком с двух сначным Iq")
            await message.answer("Введите 5к", reply_markup=nav.otherMenu)
            await Money._5k.set()
    else:
        await message.answer("Введите 10к", reply_markup=nav.otherMenu)
        await Money._10k.set()


@dp.message_handler(state=Money._2k)
async def _2k(message: types.Message, state: FSMContext):
    global __2k
    __2k = message.text
    if message.text != "FUCK GO BACK":
        if message.text.isdigit() == True:
            await Money.next()
            await message.answer("Введите 1к", reply_markup=nav.otherMenu)
        else:
            await message.answer("Мне нахуй не нужны буквы")
            await message.answer("Введи 2к", reply_markup=nav.otherMenu)
            await Money._2k.set()
    else:
        await message.answer("Введите 5к", reply_markup=nav.otherMenu)
        await Money._5k.set()


@dp.message_handler(state=Money._1k)
async def _1k(message: types.Message, state: FSMContext):
    global __1k
    __1k = message.text
    if message.text != "FUCK GO BACK":
        if message.text.isdigit() == True:
            await Money.next()
            await message.answer("Введите 500тг", reply_markup=nav.otherMenu)
        else:
            await message.answer("I like numbers")
            await message.answer("Введи 1к", reply_markup=nav.otherMenu)
            await Money._1k.set()
    else:
        await message.answer("Введите 2к", reply_markup=nav.otherMenu)
        await Money._2k.set()


@dp.message_handler(state=Money._500tg)
async def _500tg(message: types.Message, state: FSMContext):
    global __500tg
    __500tg = message.text
    global nal
    if message.text != "FUCK GO BACK":
        if message.text.isdigit() == True:
            nal = int(__20k) * 20000 + int(__10k) * 10000 + int(__5k) * \
                5000 + int(__2k) * 2000 + int(__1k) * 1000 + int(__500tg) * 500
            await message.answer("Весь нал что есть у тебя на кармане:  " + str(nal) + "тг")
            await message.answer("Введи сколько акша в первой кассе", reply_markup=nav.otherMenu)
            await Money.next()
        else:
            await message.answer("ЧИЛСА ЦЫФРЫ ЧИЛСА ЦЫФРЫ ЧИЛСА ЦЫФРЫ ЧИЛСА ЦЫФРЫ НАААХУУУЙ БУКВЫ")
            await message.answer("Введите 500тг", reply_markup=nav.otherMenu)
            await Money._500tg.set()
    else:
        await message.answer("Введите 1к", reply_markup=nav.otherMenu)
        await Money._1k.set()

# --- next ---


@dp.message_handler(state=Money.kasa1)
async def kasa1(message: types.Message, state: FSMContext):
    global kasa_1
    kasa_1 = message.text
    if message.text != "FUCK GO BACK":
        if message.text.isdigit() == True:
            await Money.next()
            await message.answer('Дай посмотреть что во второй кассе', reply_markup=nav.otherMenu)
        else:
            await message.answer("Ты походу туповат вводи цыфры!")
            await message.answer("Введи сколько акша в первой кассе", reply_markup=nav.otherMenu)
            await Money.kasa1.set()
    else:
        await message.answer("Введите 500тг", reply_markup=nav.otherMenu)
        await Money._500tg.set()


@dp.message_handler(state=Money.kasa2)
async def kasa2(message: types.Message, state: FSMContext):
    global kasa_2
    kasa_2 = message.text
    if message.text != "FUCK GO BACK":
        if message.text.isdigit() == True:
            await Money.next()
            await message.answer('Нахуй третью кассу', reply_markup=nav.otherMenu)
        else:
            await message.answer("Мой ночной кошмар это буквы")
            await message.answer('Дай посмотреть что во второй кассе', reply_markup=nav.otherMenu)
            await Money.kasa2.set()
    else:
        await message.answer("Введи сколько акша в первой кассе", reply_markup=nav.otherMenu)
        await Money.kasa1.set()


@dp.message_handler(state=Money.kasa3)
async def kasa3(message: types.Message, state: FSMContext):
    global kasa_3
    kasa_3 = message.text
    if message.text != "FUCK GO BACK":
        if message.text.isdigit() == True:
            await Money.next()
            await message.answer('Чё по мелочи', reply_markup=nav.otherMenu)
        else:
            await message.answer("НАПИШЫ ЁБАНОЕ ЧИСЛО!")
            await message.answer('Нахуй третью кассу', reply_markup=nav.otherMenu)
            await Money.kasa3.set()
    else:
        await message.answer('Дай посмотреть что во второй кассе', reply_markup=nav.otherMenu)
        await Money.kasa2.set()


@dp.message_handler(state=Money.meloch)
async def meloch(message: types.Message, state: FSMContext):
    global _meloch
    _meloch = message.text
    global mel
    if message.text != "FUCK GO BACK":
        if message.text.isdigit() == True:
            mel = int(kasa_1) + int(kasa_2) + int(kasa_3) + int(_meloch)
            await message.answer("Всё что есть:  " + str(mel) + "тг")
            await message.answer("Показать подробный отчёт  ", reply_markup=nav.fakeotherMenu)
            await Money.next()
        else:
            await message.answer("Похоже сомое врямя для РЕЗНИ")
            await message.answer('Чё по мелочи', reply_markup=nav.otherMenu)
            await Money.meloch.set()
    else:
        await message.answer('Чё по мелочи', reply_markup=nav.otherMenu)
        await Money.kasa3.set()

# --- final ---


@dp.message_handler(state=Money.final)
async def final(message: types.Message, state: FSMContext):
    if message.text != "FUCK GO BACK":
        if message.text == "Да":
            await message.answer(f"""
            Купюр наминалом 20к:  {str(int(__20k) * 20000)}тг ({__20k})
Купюр наминалом 10к:  {str(int(__10k) * 10000)}тг ({__10k})
Купюр наминалом 5к:  {str(int(__5k) * 5000)}тг ({__5k})
Купюр наминалом 2к:  {str(int(__2k) * 2000)}тг ({__2k})
Купюр наминалом 1к:  {str(int(__1k) * 1000)}тг ({__1k})
Купюр наминалом 500тг:  {str(int(__500tg) * 500)}тг ({__500tg})

Акша в первой кассе:  {kasa_1}тг
Бабла во второй кассе:  {kasa_2}тг
Залупная касса:  {kasa_3}тг
МЕЛОЧЬ  {_meloch}тг

Суммарно сколько налички:  {nal}тг
Вот столько мелочи:  {mel}тг
ВСЕ ДЕНИГИ МИРА:  {mel + nal}тг
""", reply_markup=nav.mainMenu)
            await message.answer("Введи 20к", reply_markup=nav.otherMenu)
            await Money._20k.set()
        elif message.text == "Нет":
            await message.answer("Введи 20к", reply_markup=nav.otherMenu)
            await Money._20k.set()
        elif message.text != "Да" or "Нет" or "FUCK GO BACK":
            await message.answer("Ой блять какой ты тупой")
            await message.answer("Показать подробный отчёт  ", reply_markup=nav.fakeotherMenu)
            await Money.final.set()
    else:
        await message.answer('Чё по мелочи', reply_markup=nav.otherMenu)
        await Money.meloch.set()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
