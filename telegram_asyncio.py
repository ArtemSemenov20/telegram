import asyncio
import logging
import random
import time

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, FSInputFile, URLInputFile, BufferedInputFile
from aiogram.utils.keyboard import InlineKeyboardBuilder

import config

logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=config.token)
# Диспетчер
dp = Dispatcher()

async def long_running_algorithm():
    # Асинхронний алгоритм, який триває довше
    await asyncio.sleep(10)
    return "Готово!"

async def long_running_algorithm2(message: types.Message):
    # Асинхронний алгоритм, який триває довше
    await message.answer("Hello2")

# Хэндлер на команду /start
@dp.message(Command("start")) #/start
async def cmd_start(message: types.Message):

    time.sleep(5)
    await message.answer("Hello")

# Хэндлер на команду /start
@dp.message(Command("start2")) #/start
async def cmd_start(message: types.Message):
    result = await asyncio.gather(long_running_algorithm(), return_exceptions=True)
    await asyncio.gather(long_running_algorithm2(message), return_exceptions=True)

    await message.answer("Hello")

    await message.answer(result[0])


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())