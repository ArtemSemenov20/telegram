import asyncio
import logging
from datetime import datetime

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.fsm.state import StatesGroup, State

import config

class OrderFood(StatesGroup):
    choosing_food_name = State()
    choosing_food_size = State()



food = {"cake": 50, "banana": 20}


logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=config.token)
# Диспетчер
dp = Dispatcher()

email = ""
dp["food"] = food


def get_keyboard(text1, text2):
    buttons = [
        [
            types.InlineKeyboardButton(text=text1, callback_data="buy_cake"),
            types.InlineKeyboardButton(text=text2, callback_data="buy_banana")
        ]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


@dp.message(Command("start"))
async def send_random_value( message: types.Message):
    await message.delete()
    await message.answer("Hello " + str(message.from_user.id))
    # with open("result.txt", "a") as file:
    #     file.write(f"_______________________________\n")
    #     file.write(f"Time: {datetime.now()}\n")
    #     file.write(f"ChatID: {message.chat.id}\n")
    #     file.write(f"UserID: {message.from_user.id}\n")
    #     file.write(f"Name: {message.chat.first_name}\n")
    #     file.write(f"Last name: {message.chat.last_name}\n")
    #     file.write(f"Full name: {message.chat.full_name}\n")
    # await message.answer("Hello " + str(message.chat.full_name))

@dp.message(Command("show_buttons"))
async def send_random_value( message: types.Message):
    await message.answer("Okay", reply_markup=get_keyboard("🌹", "🎂"))

@dp.message(Command("buy"))
async def send_random_value( message: types.Message):
    await message.answer("Okay", reply_markup=get_keyboard("🌹", "🎂"))

@dp.callback_query(F.data.startswith("buy")) #"buy_cake"
async def send_random_value(callback: types.CallbackQuery, food:dict):
    print(food[callback.data.split("_")[1]])
    print(food)

    await callback.message.delete()
    await callback.message.answer("Nice",reply_markup=get_keyboard("👌", "❤"))


@dp.callback_query(F.data == "link1")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("Nice",reply_markup=get_keyboard("👌", "❤"))

@dp.callback_query(F.data == "link2")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("Nice: " + str(callback.message.user_shared.user_id),reply_markup=get_keyboard("😊", "🤷‍"))

@dp.message(F.text.endswith("@gmail.com"))
async def cmd_answer(message: types.Message):
    await message.answer("You are in.")

@dp.message(Command("is_sign"))
async def cmd_answer(message: types.Message, email: str):
    if email:
        print("You are in system.")
        await message.answer("You are in system.")
    else:
        print("No, you arent in system.")
        await message.answer("No, you arent in system.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())