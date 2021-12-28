from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher.filters.state import StatesGroup, State


class Money(StatesGroup):
    _20k = State()
    _10k = State()
    _5k = State()
    _2k = State()
    _1k = State()
    _500tg = State()
    kasa1 = State()
    kasa2 = State()
    kasa3 = State()
    meloch = State()
    final = State()

btnMain = KeyboardButton('Главная')

# --- Main menu ---

btnBigMoney = KeyboardButton('Большые бабки')
mainMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnBigMoney)

# --- Other Menu ---

finish = KeyboardButton('FUCK GO BACK')
otherMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(finish)

# --- Fake Other Meny

yes = KeyboardButton('Да')
no = KeyboardButton('Нет')
finih = KeyboardButton('FUCK GO BACK')
fakeotherMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(yes, no, finih)


