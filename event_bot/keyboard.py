from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

button = KeyboardButton('/event')
button2 = KeyboardButton('/help')

event_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(button, button2)
