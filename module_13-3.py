from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start_(message):
    print('Привет! Я бот, помогающий твоему здоровью')
    await message.answer('Привет! Я бот, помогающий твоему здоровью')

@dp.message_handler()
async def all_message(message):
    print('Введите команду /start  для  начала общения')
    await message.answer('Введите команду /start  для  начала общения')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
