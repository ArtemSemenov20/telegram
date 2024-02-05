import asyncio
import logging
import random

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, FSInputFile, URLInputFile, BufferedInputFile
from aiogram.utils.keyboard import InlineKeyboardBuilder

import config
from cod import get_map_cell



logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.token)
dp = Dispatcher()

cols, rows = 10, 10
maps = {}

def get_keyboard():
     # создаем кнопки
    buttons = [
        [
            types.InlineKeyboardButton(text='↑', callback_data='up',),
        ],
        [
            types.InlineKeyboardButton(text='←', callback_data='left',),
            types.InlineKeyboardButton(text='→', callback_data='right'),
        ],
        [
            types.InlineKeyboardButton(text='↓', callback_data='down', ),
        ],
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

def get_map_str(map_cell, player):
    # создаем строку для карты.
    map_str = ""
    # проходим по всей вертикали
    for y in range(rows * 2 - 1):
        # проходим по всей горизонтали
        for x in range(cols * 2 - 1):
            # если текущая ячейка в map_cell является True, тогда.
            if map_cell[x + y * (cols * 2 - 1)]:
                # добавляем символ.
                map_str += "⬛"
                # если координаты совпадают с координатами игрока, тогда.
            elif (x, y) == player:
                # мы должны добавить символ.
                map_str += "🔴"
                # или (во всех остальных случаях.)
            else:
                # добавляем символ.
                map_str += "⬜"
                # добавляем перенос строки в map_cell, после прохождения по всей горизонтали.
        map_str += "\n"
    # возвращаем то, что получилось, в карту.
    return map_str

@dp.message(Command("play"))
async def cmd_start(message: types.Message):
     # cоздаем лаберинт
     map_cell = get_map_cell(cols, rows)
     # содержет информацыю о лаберинте и где он находится
     user_data = {
          'map': map_cell,
          'x': 0,
          'y': 0
     }

     maps[message.chat.id] = user_data
     print(maps.keys())
     print(message.chat.id)
     await message.answer(get_map_str(map_cell, (0, 0)), reply_markup=get_keyboard())

@dp.callback_query()
async def callback_func(query: types.CallbackQuery, bot: Bot):
    print(maps.keys())
    print(query.message.chat.id)
    user_data = maps[query.message.chat.id]
    new_x, new_y = user_data['x'], user_data['y']


    if query.data == 'left':
        new_x -= 1
    if query.data == 'right':
        new_x += 1
    if query.data == 'up':
        new_y -= 1
    if query.data == 'down':
        new_y += 1

    user_data['x'], user_data['y'] = new_x, new_y
    maps[query.message.chat.id] = user_data
    await bot.edit_message_text(get_map_str(user_data['map'], (new_x, new_y)), query.message.chat.id, query.message.message_id,
                                reply_markup=get_keyboard())








async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
