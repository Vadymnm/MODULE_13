from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio


api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    growth = State()
    weigth = State()


@dp.message_handler(text=['Calories'])
async def set_age(message):
    await message.answer('Введите свой возраст')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(first=message.text)
    data = await state.get_data()
    await message.answer('Введите свой рoст')
    await UserState.growth.set()
#    print(data)


@dp.message_handler(state=UserState.growth)
async def set_weigth(message, state):
    await state.update_data(second=message.text)
    data = await state.get_data()
    await message.answer('Введите свой вес')
    await UserState.weigth.set()
#    print(data)


@dp.message_handler(state=UserState.weigth)
async def send_calories(message, state):
    await state.update_data(third=message.text)
    data = await state.get_data()
    await message.answer('Calories  calculation:')
    print('------------------------')
    list_ = list(data.values())
    cal = 5*float(list_[0]) + 6.25 * float(list_[1]) + 10 * float(list_[2])
    print(f'If You are MAN - calories,  needed  for You:   {cal}')
    print(f'If You are WOMAN - calories,  needed  for You:   {cal-161}')
    await message.answer(f'If You are MAN - calories  needed  for You:   {cal}')
    await message.answer(f'If You are WOMAN - calories,  needed  for You:   {cal-161}')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
