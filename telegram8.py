import asyncio
import logging
import time

from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, BotCommand, \
    InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

from aiogram import Bot, Dispatcher, F, types
from aiogram.filters.command import Command
from aiogram.fsm.state import StatesGroup, State

import config

tic_tac_toe = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
dict = {"1 1": [0, 0], "1 2": [0, 1], "1 3": [0, 2], "2 1": [1, 0], "2 2": [1, 1], "2 3": [1, 2], "3 1": [2, 0],
        "3 2": [2, 1], "3 3": [2, 2]}


def get_keyboard(items: list[list[str]]):
    buttons = []
    for i in range(len(items)):
        list = []
        for j in range(len(items[i])):
            list.append(InlineKeyboardButton(text=items[i][j], callback_data=f"{i + 1} {j + 1}"), )
        buttons.append(list)

    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

class TicTacToe(StatesGroup):
    playing = State()


logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.token)
dp = Dispatcher()

a= 10
b = ""

a += 1

@dp.message(Command('tictactoe'))
async def cmd_food(message: Message, state: FSMContext):
    await message.answer(text="Починаємо гру.", reply_markup=get_keyboard(tic_tac_toe))
    await state.set_state(TicTacToe.playing)
    await state.update_data(field=tic_tac_toe)


@dp.callback_query(F.data, TicTacToe.playing)
async def cmd_game(callback: CallbackQuery, state: FSMContext):

    update_data = await state.get_data()
    field = update_data["field"]

    choose_field = dict[callback.data]
    first_index = choose_field[0]
    second_index = choose_field[1]

    field[first_index][second_index] = "X"

    await bot.edit_message_text("Обери ще щось.", callback.message.chat.id, callback.message.message_id,
                                reply_markup=get_keyboard(field))

    await state.update_data(field=field)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
