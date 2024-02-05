import asyncio
import logging

from aiogram.filters import Command

from aiogram import Bot, Dispatcher, F, types
import config

logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.token)
dp = Dispatcher()



@dp.message(Command("start"))
async def send_random_value(message: types.Message):
    await message.answer("Okay")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
