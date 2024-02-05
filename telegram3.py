import asyncio
import logging
import random

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, FSInputFile, URLInputFile, BufferedInputFile
from aiogram.utils.keyboard import InlineKeyboardBuilder

import config



logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=config.token)
# Диспетчер
p = Dispatcher()

bul = True


def get_keyboard():
    buttons = [
        [
            types.InlineKeyboardButton(text="😊", callback_data="link1", url="https://surik00.gitbooks.io/aiogram-lessons/content/chapter5.html"),
            types.InlineKeyboardButton(text="❤", callback_data="link2", url="https://stackoverflow.com/questions/70291317/how-to-recive-multiply-urls-from-telegram-bot-using-aiogram")
        ],
        [types.InlineKeyboardButton(text="Подтвердить", callback_data="num_finish")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


@p.message(F.sticker)
async def send_random_value( message: types.Message):
    bul = True
    await message.answer("Smile face!")



@p.message(F.photo)
async def send_random_value( message: types.Message):
    print(bul)
    await message.answer(str(random.randint(1, 10)), reply_markup=get_keyboard())

@p.message(F.text.startswith("Hello"))
async def send_random_value(message: types.Message):
    bul = False
    print(bul)
    await message.answer(str(random.randint(1, 1000)) + str(bul))

@p.message(F.text == "or this or this")
async def cmd_answer(message: types.Message):
    if bul == True:
        print("Hi")
    print(bul)
    await message.answer("Hello.", reply_markup=get_keyboard())

@p.message(F.text == "photo")
async def cmd_answer(message: types.Message):
    photo = open('photo.jpg', 'rb')
    await message.answer_photo(BufferedInputFile(photo.read(), filename="image from photo.jpg"), caption="zdfhsdfvsfdbsdfb", reply_markup=get_keyboard())
    photo.close()


async def main():
    await p.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())