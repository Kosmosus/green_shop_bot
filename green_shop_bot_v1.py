import telebot
from telebot import types

bot = telebot.TeleBot('1637177992:AAF0EK96jgeBS95Mj04BxV8nP4GWJKonyZ0')


#  Приветствие
@bot.message_handler(commands=['start'])
def welcome(message):
    #  стикер при первом запуске бота
    sti = open('static/hello.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    #  клавиатура над полем ввода
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item0 = types.KeyboardButton("К началу ↑")
    item00 = types.KeyboardButton("☎ Контакты")
    markup.add(item0, item00)

    # приветствие
    bot.send_message(message.chat.id, "Здравствуйте, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы "
                                      "помочь Вам в выборе микрозелени."
                     .format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)

    #  создание кнопок под сообщением
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('🌱 Редис', callback_data='Redis'),
        telebot.types.InlineKeyboardButton('🌱 Горох', callback_data='Goroh'))
    keyboard.row(
        telebot.types.InlineKeyboardButton('🌱 Горчица', callback_data='Gorchitsa'),
        telebot.types.InlineKeyboardButton('🌱 Кресс-салат', callback_data='Kress_salat'))
    keyboard.row(
        telebot.types.InlineKeyboardButton('🌱 Капуста листовая', callback_data='Kapusta_listovaya'),
        telebot.types.InlineKeyboardButton('🌱 Кинза (кориандр)', callback_data='Kinza'))
    keyboard.row(
        telebot.types.InlineKeyboardButton('🌱 Брокколи', callback_data='Brokkoli'),
        telebot.types.InlineKeyboardButton('🌱 Морковь', callback_data='Morkov'))
    keyboard.row(
        telebot.types.InlineKeyboardButton('🌱 Подсолнечник', callback_data='Podsolnechnik'),
        telebot.types.InlineKeyboardButton('🌱 Cвекла', callback_data='Svekla'))
    keyboard.row(
        telebot.types.InlineKeyboardButton('🌱 Базилик', callback_data='Bazilik'),
        telebot.types.InlineKeyboardButton('🌱 Руккола', callback_data='Rukkola'))
    keyboard.row(telebot.types.InlineKeyboardButton('🌱 Бораго (огуречная трава)', callback_data='Borago'))

    # сообщение
    bot.send_message(message.chat.id, '*Выберите микрозелень* ↓', reply_markup=keyboard, parse_mode='Markdown')


#  Приветствие при нажатии кнопки "К началу ↑"
@bot.message_handler(commands=['text'])
def welcome_new(message):
    #  клавиатура над полем ввода
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item0 = types.KeyboardButton("К началу ↑")
    item00 = types.KeyboardButton("☎ Контакты")
    markup.add(item0, item00)

    # приветствие
    bot.send_message(message.chat.id, "Здравствуйте ещё раз, {0.first_name}!"
                     .format(message.from_user), parse_mode='html', reply_markup=markup)

    #  создание кнопок под сообщением
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('🌱 Редис', callback_data='Redis'),
        telebot.types.InlineKeyboardButton('🌱 Горох', callback_data='Goroh'))
    keyboard.row(
        telebot.types.InlineKeyboardButton('🌱 Горчица', callback_data='Gorchitsa'),
        telebot.types.InlineKeyboardButton('🌱 Кресс-салат', callback_data='Kress_salat'))
    keyboard.row(
        telebot.types.InlineKeyboardButton('🌱 Капуста листовая', callback_data='Kapusta_listovaya'),
        telebot.types.InlineKeyboardButton('🌱 Кинза (кориандр)', callback_data='Kinza'))
    keyboard.row(
        telebot.types.InlineKeyboardButton('🌱 Брокколи', callback_data='Brokkoli'),
        telebot.types.InlineKeyboardButton('🌱 Морковь', callback_data='Morkov'))
    keyboard.row(
        telebot.types.InlineKeyboardButton('🌱 Подсолнечник', callback_data='Podsolnechnik'),
        telebot.types.InlineKeyboardButton('🌱 Cвекла', callback_data='Svekla'))
    keyboard.row(
        telebot.types.InlineKeyboardButton('🌱 Базилик', callback_data='Bazilik'),
        telebot.types.InlineKeyboardButton('🌱 Руккола', callback_data='Rukkola'))
    keyboard.row(telebot.types.InlineKeyboardButton('🌱 Бораго (огуречная трава)', callback_data='Borago'))

    # сообщение
    bot.send_message(message.chat.id, '*Выберите микрозелень* ↓', reply_markup=keyboard, parse_mode='Markdown')


#  Основное дерево бота
@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    try:
        if call.message:
            # Редис
            if call.data == 'Redis':
                redis(call)
            # Горох
            elif call.data == 'Goroh':
                goroh(call)
            # Горчица
            elif call.data == 'Gorchitsa':
                gorchitsa(call)
            # Кресс-салат
            elif call.data == 'Kress_salat':
                kress_salat(call)
            # Капуста листовая
            elif call.data == 'Kapusta_listovaya':
                kapusta_listovaya(call)
            # Кинза
            elif call.data == 'Kinza':
                kinza(call)
            # Брокооли
            elif call.data == 'Brokkoli':
                brokkoli(call)
            # Морковь
            elif call.data == 'Morkov':
                morkov(call)
            # Подсолнечник
            elif call.data == 'Podsolnechnik':
                podsolnechnik(call)
            # Свекла
            elif call.data == 'Svekla':
                svekla(call)
            # Базилик
            elif call.data == 'Bazilik':
                bazilik(call)
            # Руккола
            elif call.data == 'Rukkola':
                rukkola(call)
            # Богаро
            elif call.data == 'Borago':
                borago(call)

    except Exception as e:
        print(repr(e))


# Контакты
def my_info(message):
    bot.send_message(message.chat.id, '📞 Телефон\n➡Инстаграм')


# Редис
def redis(call):
    pass


# Горох
def goroh(call):
    pass


# Горчица
def gorchitsa(call):
    pass


# Кресс-салат
def kress_salat(call):
    pass


# Капуста листовая
def kapusta_listovaya(call):
    pass


# Кинза
def kinza(call):
    pass


# Брокооли
def brokkoli(call):
    pass


# Морковь
def morkov(call):
    pass


# Подсолнечник
def podsolnechnik(call):
    pass


# Свекла
def svekla(call):
    pass


# Базилик
def bazilik(call):
    pass


# Руккола
def rukkola(call):
    pass


# Богаро
def borago(call):
    pass













@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'К началу ↑':
            welcome_new(message)
        elif message.text == '☎ Контакты':
            my_info(message)
        else:
            bot.send_message(message.chat.id, 'Выберите один вариант из предложенных выше, пожалуйста.')


# RUN
bot.polling(none_stop=True)