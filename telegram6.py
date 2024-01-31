import asyncio
import logging
import time

from aiogram.enums import ParseMode
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, BotCommand

from aiogram import Bot, Dispatcher, F, types
from aiogram.filters.command import Command
from aiogram.fsm.state import StatesGroup, State

import config

available_food_names = ["Суши", "Спагетти", "Хачапури", "Шаурма", "Хот-дог"]
available_food_sizes = ["Маленькую", "Среднюю", "Большую", "Супер большая"]


def make_row_keyboard(items: list[str]) -> ReplyKeyboardMarkup:
    row = [KeyboardButton(text=item) for item in items]
    return ReplyKeyboardMarkup(keyboard=[row], resize_keyboard=True)


class OrderFood(StatesGroup):
    choosing_food_name = State()  # 1
    choosing_food_size = State()  # 2


logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.token)
dp = Dispatcher()


@dp.message(
    OrderFood.choosing_food_name,
    F.text.in_(available_food_names),
)
async def food_chosen(message: Message, state: FSMContext):
    await state.update_data(chosen_food=message.text.lower())
    await message.answer(
        text="Спасибо. Теперь, пожалуйста, выберите размер порции:",
        reply_markup=make_row_keyboard(available_food_sizes)
    )
    await state.set_state(OrderFood.choosing_food_size)


# @dp.message(F.text)
# async def food_chosen_incorrectly(message: Message):
#     await message.answer(text="Ти надіслав текст")

@dp.message(OrderFood.choosing_food_name)
async def food_chosen_incorrectly(message: Message):
    await message.answer(
        text="Я не знаю такого блюда.\n\n"
             "Пожалуйста, выберите одно из названий из списка ниже:",
        reply_markup=make_row_keyboard(available_food_names)
    )


@dp.message(Command("food"), StateFilter(None))
async def cmd_food(message: Message, state: FSMContext):
    await message.answer(
        text="Оберіть їжу.",
        reply_markup=make_row_keyboard(available_food_names)
    )
    # Устанавливаем пользователю состояние "выбирает название"
    await state.set_state(OrderFood.choosing_food_name)


@dp.message(OrderFood.choosing_food_size, F.text.in_(available_food_sizes))
async def food_size_chosen(message: Message, state: FSMContext):
    user_data = await state.get_data()
    await message.answer(
        text=f"Вы выбрали {message.text.lower()} порцию {user_data['chosen_food']}.\n"
             f"Попробуйте теперь заказать напитки: /drinks",
        reply_markup=ReplyKeyboardRemove()
    )
    await state.clear()


@dp.message(OrderFood.choosing_food_size)
async def food_size_chosen_incorrectly(message: Message):
    await message.answer(
        text="Я не знаю такого размера порции.\n\n"
             "Пожалуйста, выберите один из вариантов из списка ниже:",
        reply_markup=make_row_keyboard(available_food_sizes)
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
