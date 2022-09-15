from aiogram import Bot, types
from config import BOT_TOKEN
import keyboard as kb

import datetime

from aiogram import types
from bot import BotDB
from dispatcher import dp

from utils import *

bot = Bot(token=BOT_TOKEN)


@dp.message_handler(commands="start")
async def start(message: types.Message):
    state = dp.current_state(user=message.from_user.id)

    # await message.reply("Первая инлайн кнопка", reply_markup=kb.inline_kb1)
    await message.bot.send_message(message.from_user.id,
                                   "<b>Welcome!</b> To record an event, use <i>'/event'</i> command",
                                   reply_markup=kb.event_kb)
    await state.set_state(States.all()[0])


@dp.message_handler(commands="start", state=States.STATE_0)
async def start(message: types.Message):
    await message.bot.send_message(message.from_user.id,
                                   "The bot is already started. To record an event, use <i>'/event'</i> command")


@dp.message_handler(commands="help", state=States.STATE_0)
async def help(message: types.Message):
    await message.bot.send_message(message.from_user.id,
                                   '''
                               To record an event, use <i>'/event'</i> command. The date and time formats are:
                               
                               <b>For date:</b>
                               <code>-12/10</code>
                               <code>-12 10</code>
                               <code>-12 october</code>
                               <code>-12/october</code>
                               
                               <b>For time:</b>
                               <code>-12:30</code>
                               <code>-12:30 am or pm</code>
                               <code>-12 am or pm</code>
                               <code>-12 30</code> 
                               <code>-12-30</code>''')


@dp.message_handler(commands=("event"), commands_prefix="/!", state=States.STATE_0)
async def record_start(message: types.Message):
    state = dp.current_state(user=message.from_user.id)

    await bot.send_message(message.from_user.id, 'Enter the <u><b>name</b></u> of the event:', 'HTML')
    await state.set_state(States.all()[1])


@dp.message_handler(state=States.STATE_1)
async def name(message: types.Message):
    state = dp.current_state(user=message.from_user.id)
    global name_
    name_ = message.text

    await message.reply('Enter the <u><b>date</b></u> of the event:', reply=False)
    await state.set_state(States.all()[2])


@dp.message_handler(state=States.STATE_2[0])
async def date(message: types.Message):
    state = dp.current_state(user=message.from_user.id)
    date_ = message.text
    result = datetime.datetime(1111, 1, 1)

    for format in ('%d/%m%Y', '%d %m%Y', '%d %B%Y', '%d/%B%Y'):
        try:
            date = datetime.date.today()
            year = date.strftime("%Y")
            result = datetime.datetime.strptime(date_ + str(year), format)
        except ValueError:
            pass

    global datee_
    datee_ = result.date()

    await message.reply('Enter the <u><b>time</b></u> of the event:', reply=False)
    await state.set_state(States.all()[3])


@dp.message_handler(state=States.STATE_3[0])
async def time(message: types.Message):
    state = dp.current_state(user=message.from_user.id)
    time_ = message.text
    result2 = datetime.datetime(1111, 1, 1)

    for format in ('%H:%M', '%I:%M %p', '%I %p', '%H %M', '%H-%M'):
        try:
            result2 = datetime.datetime.strptime(time_, format)
        except ValueError:
            pass

    global timee_
    timee_ = str(result2.time())

    await message.reply('Enter the <u><b>place</b></u> of the event:', reply=False)
    await state.set_state(States.all()[4])


@dp.message_handler(state=States.STATE_4[0])
async def place(message: types.Message):
    state = dp.current_state(user=message.from_user.id)
    place_ = message.text

    await state.set_state(States.all()[0])

    await message.reply('Record of the <u><b>event</b></u> is added successfully!', reply=False)

    BotDB.add_record(name_, datee_, timee_, place_)

