import asyncio
import logging
import random
import time

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, FSInputFile, URLInputFile, BufferedInputFile
from aiogram.utils.keyboard import InlineKeyboardBuilder

import config


kb = [
    [KeyboardButton(text="Hey"), KeyboardButton(text="Hey3")],
    [KeyboardButton(text="Hey4"), KeyboardButton(text="Hey7")]
]
keyboard = ReplyKeyboardMarkup(keyboard=kb)

logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=config.token)
# Диспетчер
dp = Dispatcher()

# Здесь хранятся пользовательские данные.
# Т.к. это словарь в памяти, то при перезапуске он очистится
user_data = {}
text = "asdf"

def get_keyboard():
    buttons = [
        [
            types.InlineKeyboardButton(text="-1", callback_data="num_decr"),
            types.InlineKeyboardButton(text="+1", callback_data="num_incr")
        ],
        [types.InlineKeyboardButton(text="Подтвердить", callback_data="num_finish")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


async def update_num_text(message: types.Message, new_value: int):
    await message.edit_text(
        f"Укажите число: {new_value}",
        reply_markup=get_keyboard()
    )



@dp.message(Command("numbers"))
async def cmd_numbers(message: types.Message):
    user_data[message.from_user.id] = 0
    await message.answer("Укажите число: 0", reply_markup=get_keyboard())


@dp.callback_query(F.data.startswith("num_"))
async def callbacks_num(callback: types.CallbackQuery):
    user_value = user_data.get(callback.from_user.id, 0)
    action = callback.data.split("_")[1]

    if action == "incr":
        user_data[callback.from_user.id] = user_value+1
        await update_num_text(callback.message, user_value+1)
    elif action == "decr":
        user_data[callback.from_user.id] = user_value-1
        await update_num_text(callback.message, user_value-1)
    elif action == "finish":
        await callback.message.edit_text(f"Итого: {user_value}")

    await callback.answer()

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


@dp.message(Command("answer"))
async def cmd_answer(message: types.Message):
    print()
    await message.answer("Это простой ответ")

@dp.message(F.text)
async def cmd_answer(message: types.Message):
    print(message.text)
    await message.answer(f"Привіт, {message.text}")
    photo = open('photo.jpg', 'rb')
    await message.answer_photo(BufferedInputFile(photo.read(), filename="image from photo.jpg"), caption="Изображение из буфера")

@dp.callback_query(F.data == "random_value")
async def send_random_value(callback: types.CallbackQuery):

    await callback.message.answer(str(random.randint(1, 10)))


@dp.callback_query(F.data == "num_incr")
async def send_random_value(callback: types.CallbackQuery):
    text = "asdf"
    await callback.message.answer("https://mastergroosha.github.io/aiogram-3-guide/buttons/")

@dp.message(Command("random", "random1"))
async def cmd_random(message: types.Message):
    buttons = [
        [
            InlineKeyboardButton(text="-1", callback_data="num_decr"),
            InlineKeyboardButton(text="+1", callback_data="num_incr")
        ],
        [
            InlineKeyboardButton(text="Подтвердить", callback_data="num_finish"),
            InlineKeyboardButton(text="Подтвердить2", callback_data="num_finish"),
            InlineKeyboardButton(text="Подтвердить3", callback_data="num_finish"),
            InlineKeyboardButton(text="Подтвердить4", callback_data="num_finish")
        ]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)


    await message.answer(
        "frqeerhgthjyutrkyujryu",
        reply_markup=keyboard
    )

@dp.message(Command("random"))
async def cmd_random(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Нажми меня",
        callback_data="random_value")
    )
    await message.answer(
        "Нажмите на кнопку, чтобы бот отправил число от 1 до 10",
        reply_markup=builder.as_markup()
    )

@dp.message(Command("reply"))
async def cmd_reply(message: types.Message):
    await message.reply('Это ответ с "ответом"')
# Запуск процесса поллинга новых апдейтов

@dp.callback_query(F.data == "random_value")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer(str(random.randint(1, 10)))
    await callback.answer(
        text="Спасибо, что воспользовались ботом!",
        show_alert=True
    )
    # или просто await callback.answer()

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())