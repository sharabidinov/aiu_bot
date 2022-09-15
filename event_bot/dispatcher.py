from aiogram import Bot, Dispatcher
import config

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware

if not config.BOT_TOKEN:
    exit("No token provided")

bot = Bot(token=config.BOT_TOKEN, parse_mode="HTML")

dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())

