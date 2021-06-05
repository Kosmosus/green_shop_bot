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
        telebot.types.InlineKeyboardButton('🌱 Ассорти', callback_data='Assorti'),
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
        telebot.types.InlineKeyboardButton('🌱 Редис', callback_data='Redis'),
        telebot.types.InlineKeyboardButton('🌱 Морковь', callback_data='Morkov'))
    keyboard.row(telebot.types.InlineKeyboardButton('🌱 Бораго-огуречная трава', callback_data='Borago'))


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
        telebot.types.InlineKeyboardButton('🌱 Ассорти', callback_data='Assorti'),
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
        telebot.types.InlineKeyboardButton('🌱 Редис', callback_data='Redis'),
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
    bot.send_message(message.chat.id, '📞 +79534352922, +79534278732\n➡ https://www.instagram.com/greenlive71/\n'
                                      '➡ https://vk.com/myowncityfarm ')


# Редис
def redis(call):
    # Картинка
    photo = open('static/redis.png', 'rb')
    bot.send_photo(call.message.chat.id, photo)

    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Описание", callback_data='Redis_info')
    markup.add(item1)
    bot.send_message(call.message.chat.id, '_Вы выбрали пункт "Редис"._\n\n'
                                           '*Цена:* 150 руб.',
                     reply_markup=markup, parse_mode="Markdown")


def redis_info(call):
    bot.send_message(call.message.chat.id, '🌱 *Редис*\nНемного хрустящая и жгучая на вкус микрозелень, '
                                           'по вкусу похожа на сам корнеплод. Идеальная приправа к салатам '
                                           'и мясным блюдам. Микрозелень редиса – это хороший источник витамина С, '
                                           'энергии и углеводов. Он также содержит цинк, калий, фолиевую кислоту, '
                                           'марганец, медь, натрий, фосфор, клетчатку, рибофлавин, витамины B1 и B6, '
                                           'кальций, железо, магний и многое другое. Микрозелень редиса полезна '
                                           'своим улучшением процесса переваривания пищи благодаря тому, '
                                           'что в ее составе есть минералы, микроэлементы и эфирные масла, '
                                           'но при этом не вызывает вздутие как корнеплод. Редиска является '
                                           'натуральным мочегонным средством, обладает противовоспалительными '
                                           'свойствами, помогает предотвратить рак легких и способствует '
                                           'очищению крови.', parse_mode="Markdown")


# Горох
def goroh(call):
    # Картинка
    photo = open('static/goroh.png', 'rb')
    bot.send_photo(call.message.chat.id, photo)

    markup = types.InlineKeyboardMarkup(row_width=1)
    item2 = types.InlineKeyboardButton("Описание", callback_data='Goroh_info')
    markup.add(item2)
    bot.send_message(call.message.chat.id, '_Вы выбрали пункт "Горошек усатый"._\n\n'
                                           '*Цена:* 120 руб.',
                     reply_markup=markup, parse_mode="Markdown")


def goroh_info(call):
    bot.send_message(call.message.chat.id, '🌱 *Горох*\nПо вкусу микрогрин гороха слегка сладкий и имеет ореховый '
                                           'оттенок, который напоминает молодой зелёный горошек. В пищу употребляют '
                                           'молодые стебельки с листьями и усиками. Благодаря своей хрустящей '
                                           'структуре, горох хорошо сочетается со свежими овощами и является '
                                           'отличным украшением овощных супов. Польза микрозелени гороха в том, '
                                           'что она содержит клетчатку, белок, сложные углеводы. Она богата '
                                           'фолиевой кислотой и витаминами A, C, E, B1, B2, В3, В6. Горох '
                                           'способствует повышению иммунитета, улучшению здоровья глаз, контролю '
                                           'уровня сахара в крови, оказывает противораковый эффект и многое другое.',
                     parse_mode="Markdown")


# Горчица
def gorchitsa(call):
    # Картинка
    photo = open('static/gorchitsa.png', 'rb')
    bot.send_photo(call.message.chat.id, photo)

    markup = types.InlineKeyboardMarkup(row_width=1)
    item3 = types.InlineKeyboardButton("Описание", callback_data='Gorchitsa_info')
    markup.add(item3)
    bot.send_message(call.message.chat.id, '_Вы выбрали пункт "Горчица"._\n\n'
                                           '*Цена:* 150 руб.',
                     reply_markup=markup, parse_mode="Markdown")


def gorchitsa_info(call):
    bot.send_message(call.message.chat.id, '🌱 *Микрозелень горчицы*\nЗелень с пикантным островатым вкусом. '
                                           'Подходит к рыбным блюдам и салатам. Горчичная микрозелень богата белком, '
                                           'клетчаткой, фолиевой кислотой, кальцием и железом. Микрогрин горчицы '
                                           'полезен тем, что оказывает благоприятное влияние на состояние сосудов, '
                                           'улучшает аппетит и кровообращение. Горчица способна бороться с диабетом, '
                                           'стимулирует рост здоровых волос, помогает уменьшить заложенность носа, '
                                           'а также укрепляет иммунную систему, поскольку содержит витамин С.',
                     parse_mode="Markdown")


# Кресс-салат
def kress_salat(call):
    # Картинка
    photo = open('static/kress_salat.png', 'rb')
    bot.send_photo(call.message.chat.id, photo)

    markup = types.InlineKeyboardMarkup(row_width=1)
    item4 = types.InlineKeyboardButton("Описание", callback_data='Kress_salat_info')
    markup.add(item4)
    bot.send_message(call.message.chat.id, '_Вы выбрали пункт "Кресс-салат"._\n\n'
                                           '*Цена:* 150 руб.',
                     reply_markup=markup, parse_mode="Markdown")


def kress_salat_info(call):
    bot.send_message(call.message.chat.id, '🌱 *Кресс-салат*\nМикрозелень со специфическим запахом и острым '
                                           'горчичным привкусом. Хорошее дополнение к гарниру, соусу и салату. '
                                           'Вкус освежающий и легко различимый. Кресс-салат богат на каротин, '
                                           'витамины группы B, железо и магний. Также он одержит больше серы и '
                                           'натрия, в сравнении с другими овощами. Микрогрин кресс-салата улучшает '
                                           'работу желудочно-кишечного тракта, помогает наладить сон, и нормализует '
                                           'давление.', parse_mode="Markdown")


# Капуста листовая
def kapusta_listovaya(call):
    # Картинка
    photo = open('static/kapusta_listovaya.png', 'rb')
    bot.send_photo(call.message.chat.id, photo)

    markup = types.InlineKeyboardMarkup(row_width=1)
    item5 = types.InlineKeyboardButton("Описание", callback_data='Kapusta_listovaya_info')
    markup.add(item5)
    bot.send_message(call.message.chat.id, '_Вы выбрали пункт "Капуста краснокачанная"._\n\n'
                                           '*Цена:* 170 руб.',
                     reply_markup=markup, parse_mode="Markdown")


def kapusta_listovaya_info(call):
    bot.send_message(call.message.chat.id, '🌱 *Капуста листовая*\n Капусту используют в салатах и коктейлях, '
                                           'без термической обработки. Вкус ростков прекрасно сочетается со свежими '
                                           'овощами и травами. Как и другие виды капусты, невероятно полезна. '
                                           'Ростки содержат очень ценные витамины и минералы в огромных '
                                           'количествах. Капусту считают суперфудом, ведь в ней есть множество '
                                           'преимуществ для тела человека, включая снижение вреда холестерина для '
                                           'снижения риска сердечных заболеваний. Микрозелень содержит в сорок раз '
                                           'больше питательных веществ, чем взрослая капуста.', parse_mode="Markdown")


# Кинза
def kinza(call):
    # Картинка
    photo = open('static/kinza.png', 'rb')
    bot.send_photo(call.message.chat.id, photo)

    markup = types.InlineKeyboardMarkup(row_width=1)
    item6 = types.InlineKeyboardButton("Описание", callback_data='Kinza_info')
    markup.add(item6)
    bot.send_message(call.message.chat.id, '_Вы выбрали пункт "Кинза"._\n\n'
                                           '*Цена:* 180 руб.',
                     reply_markup=markup, parse_mode="Markdown")


def kinza_info(call):
    bot.send_message(call.message.chat.id, '🌱 *Микрозелень кориандра (кинзы)*\nКультура с ярко-выраженным пикантным '
                                           'вкусом и запахом пряностей. Кинза является отличным дополнением мясных '
                                           'блюд, особенно приготовленных на гриле. Микрозелень кинзы очень полезна '
                                           'для работы сердца и сосудов. В ее составе есть масса витаминов, а также '
                                           'фосфор и калий. Употребление кориандра в пищу способствует укреплению '
                                           'здоровья костей, зрения, нервной системы и т.д.', parse_mode="Markdown")


# Морковь
def morkov(call):
    # Картинка
    photo = open('static/morkov.png', 'rb')
    bot.send_photo(call.message.chat.id, photo)

    markup = types.InlineKeyboardMarkup(row_width=1)
    item7 = types.InlineKeyboardButton("Описание", callback_data='Morkov_info')
    markup.add(item7)
    bot.send_message(call.message.chat.id, '_Вы выбрали пункт "Морковь"._\n\n'
                                           '*Цена:* 170 руб.',
                     reply_markup=markup, parse_mode="Markdown")


def morkov_info(call):
    bot.send_message(call.message.chat.id, '🌱 *Морковь* — отличный источник витамина А, который помогает '
                                           'предотвратить потерю зрения, а клетчатка помогают пищеварению. '
                                           'Также в ней содержится витамин К, магний, кальций, фолиевая кислота и '
                                           'калий. Во всходах моркови содержится в пять раз больше витамина С, '
                                           'чем в плодах и вдобавок много калия и кальция.', parse_mode="Markdown")


# Подсолнечник
def podsolnechnik(call):
    # Картинка
    photo = open('static/podsolnechnik.png', 'rb')
    bot.send_photo(call.message.chat.id, photo)

    markup = types.InlineKeyboardMarkup(row_width=1)
    item8 = types.InlineKeyboardButton("Описание", callback_data='Podsolnechnik_info')
    markup.add(item8)
    bot.send_message(call.message.chat.id, '_Вы выбрали пункт "Подсолнечник"._\n\n'
                                           '*Цена:* 120 руб.',
                     reply_markup=markup, parse_mode="Markdown")


def podsolnechnik_info(call):
    bot.send_message(call.message.chat.id, '🌱 *Подсолнечник*\nХрустящий и сочный микрогрин, со вкусом молочных '
                                           'семечек подсолнуха. Поэтому он является отличным выбором практически '
                                           'для любого салатного микса. Даже детям нравится микрозелень подсолнечника. '
                                           'Подается к мясным и овощным блюдам. Подсолнечник очень полезен, так как '
                                           'в его состав входят йод, фосфор, магний, кальций и цинк, а также '
                                           'витамины E и K и фолиевая кислота. Он помогает бороться с болями в '
                                           'суставах, и полезен для нормализации кислотно-щелочного баланса.',
                     parse_mode="Markdown")


# Свекла
def svekla(call):
    # Картинка
    photo = open('static/svekla.png', 'rb')
    bot.send_photo(call.message.chat.id, photo)

    markup = types.InlineKeyboardMarkup(row_width=1)
    item9 = types.InlineKeyboardButton("Описание", callback_data='Svekla_info')
    markup.add(item9)
    bot.send_message(call.message.chat.id, '_Вы выбрали пункт "Мангольд (свёкла)"._\n\n'
                                           '*Цена:* 150 руб.',
                     reply_markup=markup, parse_mode="Markdown")


def svekla_info(call):
    bot.send_message(call.message.chat.id, '🌱 *Микрозелень свеклы*\nСочные красные ростки с темно-зелеными листочками '
                                           'станут отличным украшением первых блюд, салатов или бутербродов. По вкусу '
                                           'они слегка сладковатые и напоминают столовую свеклу. Микрозелень свеклы '
                                           'полезна тем, что оказывает на организм тонизирующее действие и укрепляет '
                                           'иммунитет. В молодых ростках содержаться витамины K, C и E, а также '
                                           'бета-каротин и лютеин. Она снижает вероятность развития сердечных '
                                           'заболеваний и инсульта, защищает от рака легких и полости рта, является '
                                           'хорошим антиоксидантом и повышает иммунную функцию.', parse_mode="Markdown")


# Базилик
def bazilik(call):
    # Картинка
    photo = open('static/bazilik.png', 'rb')
    bot.send_photo(call.message.chat.id, photo)

    markup = types.InlineKeyboardMarkup(row_width=1)
    item10 = types.InlineKeyboardButton("Описание", callback_data='Bazilik_info')
    markup.add(item10)
    bot.send_message(call.message.chat.id, '_Вы выбрали пункт "Базилик"._\n\n'
                                           '*Цена:* 180 руб.',
                     reply_markup=markup, parse_mode="Markdown")


def bazilik_info(call):
    bot.send_message(call.message.chat.id, '🌱 *Базилик*\nЕще один популярный вид микрозелени. Существует много '
                                           'разных сортов базилика, которые отличаются по цвету и вкусу. Некоторые '
                                           'вкусы пряные и сладкие, а другие напоминают лимон и корицу. Отлично '
                                           'подходит ко всем блюдам, является прекрасным дополнением соленого творога '
                                           'и омлета. В микрозелени базилика содержится каротин, аскорбиновая '
                                           'кислота, витамины группы B и эфирные масла. Он хорошо сказывается на '
                                           'работе органов пищеварения. Микрогрин содержит антиоксиданты, борющиеся '
                                           'с болезнями, является отличным противовоспалительным средством, имеет '
                                           'антибактериальные свойства и помогает бороться со стрессом и депрессией.',
                     parse_mode="Markdown")


# Руккола
def rukkola(call):
    # Картинка
    photo = open('static/rukkola.png', 'rb')
    bot.send_photo(call.message.chat.id, photo)

    markup = types.InlineKeyboardMarkup(row_width=1)
    item11 = types.InlineKeyboardButton("Описание", callback_data='Rukkola_info')
    markup.add(item11)
    bot.send_message(call.message.chat.id, '_Вы выбрали пункт "Руккола"._\n\n'
                                           '*Цена:* 150 руб.',
                     reply_markup=markup, parse_mode="Markdown")


def rukkola_info(call):
    bot.send_message(call.message.chat.id, '🌱 *Руккола*\nМикрозелень рукколы отличается горьковатым вкусом, поэтому '
                                           'идеально подойдет к мясным и рыбным блюдам, особенно в составе соуса. '
                                           'Микрозелень рукколы считается одним из самых полезных для здоровья '
                                           'натуральных продуктов. Это отличный источник фолиевой кислоты, железа, '
                                           'меди, минералов и витаминов. Зелень полезна для укрепления иммунитета, '
                                           'поскольку содержит в себе аскорбиновую кислоту.', parse_mode="Markdown")


# Перила пурупурная (шисо)
def perila(call):
    # Картинка
    photo = open('static/perila.png', 'rb')
    bot.send_photo(call.message.chat.id, photo)

    markup = types.InlineKeyboardMarkup(row_width=1)
    item12 = types.InlineKeyboardButton("Описание", callback_data='Perila_info')
    markup.add(item12)
    bot.send_message(call.message.chat.id, '_Вы выбрали пункт "Перила пурупурная (шисо)"._\n\n'
                                           '*Цена:* 200 руб.',
                     reply_markup=markup, parse_mode="Markdown")


def perila_info(call):
    bot.send_message(call.message.chat.id, '🌱 *Шисо*\nШисо также известна, как японский базилик и является '
                                           'популярным кустарником в азиатских странах. Перилла овощная обладает '
                                           'восхитительным ароматом, похожим на анис и замечательно сочетается с '
                                           'рыбой. Микрозелень периллы овощной содержит кальций, железо, фосфор, '
                                           'клетчатку, калий и витамины A, C и K. Для получения максимальной пользы '
                                           'шисо рекомендуется употреблять в свежем виде. Она чаще всего используется '
                                           'в качестве гарнира и может быть посыпана поверх блюд из лапши, пасты, '
                                           'супов, суши и т.д.', parse_mode="Markdown")


# Амарант
def amarant(call):
    # Картинка
    photo = open('static/amarant.png', 'rb')
    bot.send_photo(call.message.chat.id, photo)

    markup = types.InlineKeyboardMarkup(row_width=1)
    item13 = types.InlineKeyboardButton("Описание", callback_data='Amarant_info')
    markup.add(item13)
    bot.send_message(call.message.chat.id, '_Вы выбрали пункт "Амарант"._\n\n'
                                           '*Цена:* 200 руб.',
                     reply_markup=markup, parse_mode="Markdown")


def amarant_info(call):
    bot.send_message(call.message.chat.id, '🌱 *Амарант*\nЗелень с розовыми листочками, которые обладают нежным '
                                           'вкусом с ореховым послевкусием. Кулинары любят использовать ее для '
                                           'украшения, так как она имеет яркий красно-розовый цвет и мягкий '
                                           'землистый вкус, сочетающийся как со сладкими, так и с солеными блюдами. '
                                           'Отлично подходит для приготовления полезных смузи. Микрозелень амаранта '
                                           'насыщенна витаминами. В ней содержатся фитостерины, которые обладают '
                                           'свойствами уменьшения холестерина и работают как средство, предотвращающее '
                                           'возникновение рака и сердечно-сосудистых заболеваний.',
                     parse_mode="Markdown")


# Мелисса
def melissa(call):
    # Картинка
    photo = open('static/melissa.png', 'rb')
    bot.send_photo(call.message.chat.id, photo)

    markup = types.InlineKeyboardMarkup(row_width=1)
    item14 = types.InlineKeyboardButton("Описание", callback_data='Melissa_info')
    markup.add(item14)
    bot.send_message(call.message.chat.id, '_Вы выбрали пункт "Мелисса"._\n\n'
                                           '*Цена:* 200 руб.',
                     reply_markup=markup, parse_mode="Markdown")


def melissa_info(call):
    bot.send_message(call.message.chat.id, '🌱 *Мелисса*\nМикрозелень мелиссы обладает сильным цитрусовым ароматом '
                                           'и вкусом лимона, что делает ее прекрасным выбором для украшения блюд. '
                                           'Благодаря богатому клетчаткой и аппетитному вкусу, мелисса способствует '
                                           'перевариванию пищи, особенно после переедания. Она широко используется в '
                                           'соках, десертах и смузи для усиления вкуса.',
                     parse_mode="Markdown")


# Микролук
def microluk(call):
    # Картинка
    photo = open('static/microluk.png', 'rb')
    bot.send_photo(call.message.chat.id, photo)

    markup = types.InlineKeyboardMarkup(row_width=1)
    item15 = types.InlineKeyboardButton("Описание", callback_data='Microluk_info')
    markup.add(item15)
    bot.send_message(call.message.chat.id, '_Вы выбрали пункт "Микролук"._\n\n'
                                           '*Цена:* 170 руб.',
                     reply_markup=markup, parse_mode="Markdown")


def microluk_info(call):
    bot.send_message(call.message.chat.id, '🌱 *Лук-шнит*\nИзящная микрозелень с черными семенами на кончиках с '
                                           'приятным запахом и привкусом лука. Идеально подходит для закусок. В '
                                           'молодых ростках содержатся витамины A, B, C, E, минералы и многое другое. '
                                           'Они полезны для здоровья кожи, глаз, костей, восстановления и развития '
                                           'тела, способствуют правильной работе различных функций организма и '
                                           'многому другому. В луке содержаться эфирные масла, которые оказывают '
                                           'противовирусное действие.', parse_mode="Markdown")


# Богаро
def borago(call):
    # Картинка
    photo = open('static/borago.png', 'rb')
    bot.send_photo(call.message.chat.id, photo)

    markup = types.InlineKeyboardMarkup(row_width=1)
    item16 = types.InlineKeyboardButton("Описание", callback_data='Borago_info')
    markup.add(item16)
    bot.send_message(call.message.chat.id, '_Вы выбрали пункт "Бораго-огуречная трава"._\n\n'
                                           '*Цена:* 180 руб.',
                     reply_markup=markup, parse_mode="Markdown")


def borago_info(call):
    bot.send_message(call.message.chat.id, '🌱 *Бораго (огуречная трава)*\nВкусная травка, для проращивания которой '
                                           'нужно немного терпения. Это микрозелень с привкусом и ароматом свежего '
                                           'огурца. Отличное дополнение к салату из свежих овощей. Микрозелень '
                                           'огуречной травы рекомендуется употреблять при лихорадке, кашле и '
                                           'депрессии. Это отличный источник сил, который помогает снять стресс, '
                                           'ускорить метаболизм и даже повысить иммунитет. Также бораго используется '
                                           'для «очистки крови», как успокаивающее средство и для стимуляции '
                                           'потоотделения. Огуречная трава увеличивает выработку грудного молока.',
                     parse_mode="Markdown")


# Ассорти
def assorti(call):
    # Картинка
    photo = open('static/assorti_big.png', 'rb')
    bot.send_photo(call.message.chat.id, photo)

    bot.send_message(call.message.chat.id, '_Большая коробка "ассорти" 200 гр. (10 видов микрозелени)._\n'
                                           '*Цена:* 400 руб.', parse_mode="Markdown")
    # Картинка
    photo = open('static/assorti_medium.png', 'rb')
    bot.send_photo(call.message.chat.id, photo)

    bot.send_message(call.message.chat.id, '_Средняя коробка "ассорти" 100 гр. (6 видов микрозелени)._\n'
                                           '*Цена:* 250 руб.', parse_mode="Markdown")
    # Картинка
    photo = open('static/assorti_small.png', 'rb')
    bot.send_photo(call.message.chat.id, photo)

    bot.send_message(call.message.chat.id, '_Маленькая коробка "ассорти" 50 гр. (4 вида микрозелени)._\n'
                                           '*Цена:* 150 руб.', parse_mode="Markdown")


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