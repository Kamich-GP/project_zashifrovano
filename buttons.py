from telebot import types


# Кнопка отправки номера
def num_button():
    # Создаем пространство
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # Создаем сами кнопки
    number = types.KeyboardButton('Отправить номер', request_contact=True)
    # Добавляем кнопку в пространство
    kb.add(number)
    return kb


# Кнопка отправки локации
def loc_button():
    # Создаем пространство
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # Создаем сами кнопки
    location = types.KeyboardButton('Отправить локацию', request_location=True)
    # Добавляем кнопку в пространство
    kb.add(location)
    return kb


# Кнопки для админ-панели
def admin_buttons():
    # Создаем пространство
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # Создаем сами кнопки
    add_pr = types.KeyboardButton('Добавить продукт')
    del_pr = types.KeyboardButton('Удалить продукт')
    edit_pr = types.KeyboardButton('Изменить количество продукта')
    to_menu = types.KeyboardButton('На главную')
    # Объединяем кнопки с пространством
    kb.add(add_pr, edit_pr, del_pr)
    kb.row(to_menu)
    return kb


# Кнопки вывода товара
def main_menu_buttons(all_prods):
    # Создаем пространство
    kb = types.InlineKeyboardMarkup(row_width=2)
    # Создаем сами кнопки
    prod_buttons = [types.InlineKeyboardButton(text=f'{i[1]}',
                                               callback_data=f'{i[0]}')
                    for i in all_prods if i[2] > 0
                    ]
    cart = types.InlineKeyboardButton(text='Корзина', callback_data='cart')
    # Добавляем кнопки в пространство
    kb.add(*prod_buttons)
    kb.row(cart)
    return kb


# Кнопки с выбором количества
def count_buttons(amount=1, plus_or_minus=''):
    # Создаем пространство
    kb = types.InlineKeyboardMarkup(row_width=3)
    # Создаем сами кнопки
    minus = types.InlineKeyboardButton(text='-', callback_data='decrement')
    current_amount = types.InlineKeyboardButton(text=str(amount), callback_data=amount)
    plus = types.InlineKeyboardButton(text='+', callback_data='increment')
    to_cart = types.InlineKeyboardButton(text='Добавить в корзину', callback_data='to_cart')
    back = types.InlineKeyboardButton(text='Назад', callback_data='back')
    # Алгоритм добавления и отнятия количества
    if plus_or_minus == 'increment':
        amount += 1
        current_amount = types.InlineKeyboardButton(text=str(amount), callback_data=amount)
    elif plus_or_minus == 'decrement':
        if amount > 1:
            amount -= 1
            current_amount = types.InlineKeyboardButton(text=str(amount), callback_data=amount)
    # Добавляем кнопки в пространство
    kb.add(minus, current_amount, plus)
    kb.row(to_cart)
    kb.row(back)
    return kb


# Кнопки корзины
def cart_buttons():
    # Создаем пространство
    kb = types.InlineKeyboardMarkup(row_width=2)
    # Создаем сами кнопки
    order = types.InlineKeyboardButton(text='Оформить заказ', callback_data='order')
    back = types.InlineKeyboardButton(text='Назад', callback_data='back')
    clear = types.InlineKeyboardButton(text='Очистить корзину', callback_data='clear')
    # Добавляем кнопки в пространство
    kb.add(clear, back)
    kb.row(order)
    return kb
