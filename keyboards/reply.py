from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from data.loader import db

def generate_main_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    order = KeyboardButton(text='🛍 Заказать')
    my_orders = KeyboardButton(text='📖 Мои заказы')
    filials = KeyboardButton(text='🍕 Наши филиалы')
    feedback = KeyboardButton(text='☎ Обратная связь')
    info = KeyboardButton(text='ℹ Информация')
    settings = KeyboardButton(text='⚙ Настройки')
    markup.row(order)
    markup.row(my_orders, filials)
    markup.row(feedback, info)
    markup.row(settings)
    return markup



def generate_delivery_types():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    delivery = KeyboardButton(text='🚗 Доставка')
    self_delivery = KeyboardButton(text='🏃‍♀️Самовывоз')
    back_btn = KeyboardButton(text='🏠 Главное меню')
    markup.row(delivery, self_delivery)
    markup.row(back_btn)
    return markup


def generate_filials_list():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    back_btn = KeyboardButton(text='🚗 к выбору доставки')
    filials = db.get_filials_names()  # [(максимка), (чиланзар), ()]
    buttons = []
    for filial in filials:
        btn = KeyboardButton(text=filial[0]) # (максимка) -> максимка
        buttons.append(btn)
    markup.add(back_btn)
    markup.add(*buttons)
    return markup


def generate_categories():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    cart = KeyboardButton(text='🛒 Корзина')
    back_btn = KeyboardButton(text='◀ к филиалам')
    main_btn = KeyboardButton(text='🏠 Главное меню')
    categories = [i[0] for i in db.get_categories()]
    buttons = []
    for category in categories:
        btn = KeyboardButton(text=category)
        buttons.append(btn)
    markup.add(back_btn, cart, *buttons, main_btn)
    return markup

def generate_information():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    filials = KeyboardButton(text='🏘 Филиалы')
    moby_app = KeyboardButton(text='️📱Мобильное приложение')
    public = KeyboardButton(text='📑 Публичная оферта')
    main_btn = KeyboardButton(text='🏠 Главное меню')
    markup.row(filials)
    markup.row(moby_app)
    markup.row(public)
    markup.row(main_btn)
    return markup

def generate_filials_information():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    back_btn = KeyboardButton(text='◀️ Назад')
    filials = db.get_filials_names()  # Получение списка названий филиалов
    buttons = []
    for filial in filials:
        btn = KeyboardButton(text=f'🏘{filial[0]}')
        buttons.append(btn)
    markup.add(back_btn)
    markup.add(*buttons)
    return markup

