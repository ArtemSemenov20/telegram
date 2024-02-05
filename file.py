
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

from token import token

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=token)
# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")

@dp.message(Command("answer"))
async def cmd_answer(message: types.Message):
    await message.answer("Это простой ответ")

@dp.message(Command("reply"))
async def cmd_reply(message: types.Message):
    await message.reply('Это ответ с "ответом"')
# Запуск процесса поллинга новых апдейтов

async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())