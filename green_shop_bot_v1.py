import telebot
from telebot import types

bot = telebot.TeleBot('1637177992:AAF0EK96jgeBS95Mj04BxV8nP4GWJKonyZ0')


#  Приветствие
@bot.message_handler(commands=['start'])
def welcome(message):
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
        telebot.types.InlineKeyboardButton('🌱 Горошек усатый', callback_data='Goroh'))
    keyboard.row(
        telebot.types.InlineKeyboardButton('🌱 Горчица', callback_data='Gorchitsa'),
        telebot.types.InlineKeyboardButton('🌱 Кресс-салат', callback_data='Kress_salat'))
    keyboard.row(
        telebot.types.InlineKeyboardButton('🌱 Капуста краснокачанная', callback_data='Kapusta_listovaya'),
        telebot.types.InlineKeyboardButton('🌱 Кинза (кориандр)', callback_data='Kinza'))
    keyboard.row(
        telebot.types.InlineKeyboardButton('🌱 Брокколи', callback_data='Brokkoli'),
        telebot.types.InlineKeyboardButton('🌱 Морковь', callback_data='Morkov'))
    keyboard.row(
        telebot.types.InlineKeyboardButton('🌱 Подсолнечник', callback_data='Podsolnechnik'),
        telebot.types.InlineKeyboardButton('🌱 Мангольд (свекла)', callback_data='Svekla'))
    keyboard.row(
        telebot.types.InlineKeyboardButton('🌱 Базилик', callback_data='Bazilik'),
        telebot.types.InlineKeyboardButton('🌱 Руккола', callback_data='Rukkola'))
    keyboard.row(
        telebot.types.InlineKeyboardButton('🌱 Перила пурупурная (шисо)', callback_data='Perila'),
        telebot.types.InlineKeyboardButton('🌱 Амарант', callback_data='Amarant'))
    keyboard.row(
        telebot.types.InlineKeyboardButton('🌱 Мелисса', callback_data='Melissa'),
        telebot.types.InlineKeyboardButton('🌱 Микролук', callback_data='Microluk'))
    keyboard.row(
        telebot.types.InlineKeyboardButton('🌱 Бораго-огуречная трава', callback_data='Borago'),
        telebot.types.InlineKeyboardButton('🌱 Ассорти', callback_data='Assorti'))

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
        telebot.types.InlineKeyboardButton('🌱 Горошек усатый', callback_data='Goroh'))
    keyboard.row(
        telebot.types.InlineKeyboardButton('🌱 Горчица', callback_data='Gorchitsa'),
        telebot.types.InlineKeyboardButton('🌱 Кресс-салат', callback_data='Kress_salat'))
    keyboard.row(
        telebot.types.InlineKeyboardButton('🌱 Капуста краснокачанная', callback_data='Kapusta_listovaya'),
        telebot.types.InlineKeyboardButton('🌱 Кинза (кориандр)', callback_data='Kinza'))
    keyboard.row(
        telebot.types.InlineKeyboardButton('🌱 Подсолнечник', callback_data='Podsolnechnik'),
        telebot.types.InlineKeyboardButton('🌱 Мангольд (свекла)', callback_data='Svekla'))
    keyboard.row(
        telebot.types.InlineKeyboardButton('🌱 Базилик', callback_data='Bazilik'),
        telebot.types.InlineKeyboardButton('🌱 Руккола', callback_data='Rukkola'))
    keyboard.row(
        telebot.types.InlineKeyboardButton('🌱 Перила пурупурная (шисо)', callback_data='Perila'),
        telebot.types.InlineKeyboardButton('🌱 Амарант', callback_data='Amarant'))
    keyboard.row(
        telebot.types.InlineKeyboardButton('🌱 Мелисса', callback_data='Melissa'),
        telebot.types.InlineKeyboardButton('🌱 Микролук', callback_data='Microluk'))
    keyboard.row(
        telebot.types.InlineKeyboardButton('🌱 Ассорти', callback_data='Assorti'),
        telebot.types.InlineKeyboardButton('🌱 Морковь', callback_data='Morkov'))
    keyboard.row(telebot.types.InlineKeyboardButton('🌱 Бораго-огуречная трава', callback_data='Borago'))

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
            elif call.data == 'Redis_info':
                redis_info(call)
            # Горох
            elif call.data == 'Goroh':
                goroh(call)
            elif call.data == 'Goroh_info':
                goroh_info(call)
            # Горчица
            elif call.data == 'Gorchitsa':
                gorchitsa(call)
            elif call.data == 'Gorchitsa_info':
                gorchitsa_info(call)
            # Кресс-салат
            elif call.data == 'Kress_salat':
                kress_salat(call)
            elif call.data == 'Kress_salat_info':
                kress_salat_info(call)
            # Капуста листовая
            elif call.data == 'Kapusta_listovaya':
                kapusta_listovaya(call)
            elif call.data == 'Kapusta_listovaya_info':
                kapusta_listovaya_info(call)
            # Кинза
            elif call.data == 'Kinza':
                kinza(call)
            elif call.data == 'Kinza_info':
                kinza_info(call)
            # Морковь
            elif call.data == 'Morkov':
                morkov(call)
            elif call.data == 'Morkov_info':
                morkov_info(call)
            # Подсолнечник
            elif call.data == 'Podsolnechnik':
                podsolnechnik(call)
            elif call.data == 'Podsolnechnik_info':
                podsolnechnik_info(call)
            # Свекла
            elif call.data == 'Svekla':
                svekla(call)
            elif call.data == 'Svekla_info':
                svekla_info(call)
            # Базилик
            elif call.data == 'Bazilik':
                bazilik(call)
            elif call.data == 'Bazilik_info':
                bazilik_info(call)
            # Руккола
            elif call.data == 'Rukkola':
                rukkola(call)
            elif call.data == 'Rukkola_info':
                rukkola_info(call)
            # Перила пурупурная (шисо)
            elif call.data == 'Perila':
                perila(call)
            elif call.data == 'Perila_info':
                perila_info(call)
            # Амарант
            elif call.data == 'Amarant':
                amarant(call)
            elif call.data == 'Amarant_info':
                amarant_info(call)
            # Мелисса
            elif call.data == 'Melissa':
                melissa(call)
            elif call.data == 'Melissa_info':
                melissa_info(call)
            # Микролук
            elif call.data == 'Microluk':
                microluk(call)
            elif call.data == 'Microluk_info':
                microluk_info(call)
            # Богаро
            elif call.data == 'Borago':
                borago(call)
            elif call.data == 'Borago_info':
                borago_info(call)
            # Ассорти
            elif call.data == 'Assorti':
                assorti(call)

    except Exception as e:
        print(repr(e))


# Контакты
def my_info(message):
    bot.send_message(message.chat.id, '📞 Телефон\n➡Инстаграм')


# Редис
def redis(call):
    # Картинка
    photo = open('static/redis.png', 'rb')
    bot.send_photo(call.message.chat.id, photo)


def redis_info(call):
    pass


# Горох
def goroh(call):
    # Картинка
    photo = open('static/goroh.png', 'rb')
    bot.send_photo(call.message.chat.id, photo)


def goroh_info(call):
    pass


# Горчица
def gorchitsa(call):
    # Картинка
    photo = open('static/gorchitsa.png', 'rb')
    bot.send_photo(call.message.chat.id, photo)


def gorchitsa_info(call):
    pass


# Кресс-салат
def kress_salat(call):
    # Картинка
    photo = open('static/kress_salat.png', 'rb')
    bot.send_photo(call.message.chat.id, photo)


def kress_salat_info(call):
    pass


# Капуста листовая
def kapusta_listovaya(call):
    # Картинка
    photo = open('static/kapusta_listovaya.png', 'rb')
    bot.send_photo(call.message.chat.id, photo)


def kapusta_listovaya_info(call):
    pass


# Кинза
def kinza(call):
    # Картинка
    photo = open('static/kinza.png', 'rb')
    bot.send_photo(call.message.chat.id, photo)


def kinza_info(call):
    pass


# Морковь
def morkov(call):
    # Картинка
    photo = open('static/morkov.png', 'rb')
    bot.send_photo(call.message.chat.id, photo)


def morkov_info(call):
    pass


# Подсолнечник
def podsolnechnik(call):
    # Картинка
    photo = open('static/podsolnechnik.png', 'rb')
    bot.send_photo(call.message.chat.id, photo)


def podsolnechnik_info(call):
    pass


# Свекла
def svekla(call):
    # Картинка
    photo = open('static/svekla.png', 'rb')
    bot.send_photo(call.message.chat.id, photo)


def svekla_info(call):
    pass


# Базилик
def bazilik(call):
    # Картинка
    photo = open('static/bazilik.png', 'rb')
    bot.send_photo(call.message.chat.id, photo)


def bazilik_info(call):
    pass


# Руккола
def rukkola(call):
    # Картинка
    photo = open('static/rukkola.png', 'rb')
    bot.send_photo(call.message.chat.id, photo)


def rukkola_info(call):
    pass


# Перила пурупурная (шисо)
def perila(call):
    # Картинка
    photo = open('static/perila.png', 'rb')
    bot.send_photo(call.message.chat.id, photo)


def perila_info(call):
    pass


# Амарант
def amarant(call):
    # Картинка
    photo = open('static/amarant.png', 'rb')
    bot.send_photo(call.message.chat.id, photo)


def amarant_info(call):
    pass


# Мелисса
def melissa(call):
    # Картинка
    photo = open('static/melissa.png', 'rb')
    bot.send_photo(call.message.chat.id, photo)


def melissa_info(call):
    pass


# Микролук
def microluk(call):
    # Картинка
    photo = open('static/microluk.png', 'rb')
    bot.send_photo(call.message.chat.id, photo)


def microluk_info(call):
    pass


# Богаро
def borago(call):
    # Картинка
    photo = open('static/borago.png', 'rb')
    bot.send_photo(call.message.chat.id, photo)


def borago_info(call):
    pass


# Ассорти
def assorti(call):
    # Картинка
    photo = open('static/assorti_big.png', 'rb')
    bot.send_photo(call.message.chat.id, photo)
    # Картинка
    photo = open('static/assorti_medium.png', 'rb')
    bot.send_photo(call.message.chat.id, photo)
    # Картинка
    photo = open('static/assorti_small.png', 'rb')
    bot.send_photo(call.message.chat.id, photo)


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