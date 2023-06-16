from aiogram.types import Message
from data.loader import bot, dp
from .text_handlers import start_register, show_main_menu
from data.loader import db
@dp.message_handler(commands=['start'])
async def command_start(message: Message):
    await message.answer('Добро пожаловать в бот доставки пиццы')
    # Начать регистрацию по номеру телефона
    user = db.get_user_by_id(message.chat.id)
    if user:
        await show_main_menu(message)
    else:
        await start_register(message)


@dp.message_handler(commands=['menu'])
async def command_menu(message: Message):
    await message.answer('https://telegra.ph/Nashe-menyu-06-03')

@dp.message_handler(regexp='☎ Обратная связь')
@dp.message_handler(commands=['feedback'])
async def command_feedback(message: Message):
    await message.answer('📲 <b>Единый call-центр:</b> 1234 или (71) 123-45-67')

