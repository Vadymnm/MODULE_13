from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio


api = '7100837638:AAFH00gqytpiU6JKLVfdt6TrAAJDEg1GfI0'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = InlineKeyboardMarkup()
button = InlineKeyboardButton(text='Рассчитать', callback_data='Рассчитать')
kb.add(button)

button1 = InlineKeyboardButton(text='Формула  расчета', callback_data='formulas')
button2 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
markup = InlineKeyboardMarkup(resize_keyboard=True).row(button1, button2)

start_menu = InlineKeyboardMarkup(
    keyboard=[
        [button1, button2]
    ], resize_keyboard=True)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weigth = State()


@dp.message_handler(commands=['start'])
async def starter(message):
    await message.answer('Привет ! Я бот, помогающий твоему здоровью', reply_markup=kb)


@dp.callback_query_handler(text='Рассчитать')
async def main_menu(call):
    await call.message.answer('Выберите опцию:', reply_markup=markup)
    await call.answer()


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('муж:(10xВес(кг)+6,25хРост(см)+5хВозраст(лет)); (жен=муж-161)')
    await call.answer()


@dp.callback_query_handler(text='calories')
async def set_age(call, state):
    await call.message.answer('Введите свой возраст')
    data = await state.get_data()
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(first=message.text)
    data = await state.get_data()
    await message.answer('Введите свой рoст')
    await UserState.growth.set()
    print(data)


@dp.message_handler(state=UserState.growth)
async def set_weigth(message, state):
    await state.update_data(second=message.text)
    data = await state.get_data()
    await message.answer('Введите свой вес')
    await UserState.weigth.set()
    print(data)


@dp.message_handler(state=UserState.weigth)
async def send_calories(message, state):
    await state.update_data(third=message.text)
    data = await state.get_data()
    print(data)
    print('------------------------')
    list_ = list(data.values())
    print(list_)
    cal = 5*float(list_[0]) + 6.25 * float(list_[1]) + 10 * float(list_[2])
    print(f'If You are MAN - calories,  needed  for You:   {cal}')
    print(f'If You are WOMAN - calories,  needed  for You:   {cal-161}')
    await message.answer(f'If You are MAN - calories  needed  for You:   {cal}')
    await message.answer(f'If You are WOMAN - calories,  needed  for You:   {cal-161}')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
