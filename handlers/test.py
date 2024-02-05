from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove

from keyboards.for_questions import get_yes_no_kb


router2 = Router()


@router2.message(Command("start2"))  # [2]
async def cmd_start(message: Message):
    await message.answer(
        "Clicked start2!",
        reply_markup=get_yes_no_kb()
    )
