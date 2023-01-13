import telebot
from telebot import types
from database.usersDatabase import UsersData


def get_remove_markup():
    return types.ReplyKeyboardRemove()


def get_reply2():
    reply2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item9 = types.KeyboardButton('Ёмкое, красивое название, легко запомнить')
    item10 = types.KeyboardButton('Отражало принадлежность к радиотехническому факультету')
    reply2.add(item9)
    reply2.add(item10)
    return reply2


def get_reply3():
    reply3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item11 = types.KeyboardButton('Да')
    item12 = types.KeyboardButton('Нет')
    reply3.add(item11, item12)
    return reply3


def get_reply4():
    reply4 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item13 = types.KeyboardButton('Присоединиться к ребятам')
    item14 = types.KeyboardButton('Лечь спать')
    reply4.add(item13)
    reply4.add(item14)
    return reply4


def get_reply5():
    reply5 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item15 = types.KeyboardButton('Каменщик')
    item16 = types.KeyboardButton('Стропольщик')
    item17 = types.KeyboardButton('Бетонщик')
    reply5.add(item15)
    reply5.add(item16)
    reply5.add(item17)
    return reply5


def on_start_impuls_branch(message, users, bot):
    users.set_student_team(message.chat.id, "impuls")

    bot.send_photo(message.chat.id, open("Использованные/фото колонна.jpg", "rb"))
    bot.send_message(message.chat.id,
                     '"Очень давно, когда наш любимый радиотехнический институт был лишь факультетом, был создан '
                     'студенческий строительный отряд "Импульс" - самый первый в Свердловской области отряд, '
                     'прославленный по всей стране. Создали отряд 12 апреля 1964 года и до сегодняшних дней он '
                     'продолжает свою деятельность. Первые отряды сформировали из лучших студентов радиотехнического, '
                     'механико-машиностроительного и физико-технического факультетов. На радиотехническом факультете '
                     'сформировали три отряда: с первого курса - РТ-1, со второго - РТ-2 и с третьего - РТ-3."',
                     reply_markup=get_remove_markup())
    bot.send_message(message.chat.id,
                     'Тебя хлопают по плечу. Ты оборачиваешься и видишь своего одногруппника Пашу. \n- Привет! '
                     'Выбираешь студотряд? Я состою в ССО ИМПУЛЬС. Я много читал про него. Как думаешь, почему отряд '
                     'получил именно такое название?',
                     reply_markup=get_reply2())



def run(message, users: UsersData, bot: telebot.TeleBot, to_start):
    # --------------------Если это не соообщение, а начало общения -------------
    if users.get_student_team(message.chat.id) == "ns":
        on_start_impuls_branch(message, users, bot)
        return

    # --------------------- Логика ответа на сообщения ------------------------
    if message.text == 'Ёмкое, красивое название, легко запомнить':
        bot.send_message(message.chat.id,
                         '- Название "Импульс" действительно красивое и простое, но основной причиной стало отражение '
                         'принадлежности к радиотехническому факультету',
                         reply_markup=get_remove_markup())
        bot.send_message(message.chat.id,
                         'Каждое лето мы работаем - говорит Паша - ездим на целину и можем заработать. Первая Целина '
                         'ССО "Импульс" прошла в Казахстане (Актюбинская область, Карабулатский район, совхоз им. '
                         'ХХII партсъезда). Первый командир – Каменев Виктор, первый комиссар – Слепеньков Анатолий. '
                         '\n- Ну что, поедем на целину?',
                         reply_markup=get_reply3())
        return
    if message.text == 'Отражало принадлежность к радиотехническому факультету':
        bot.send_message(message.chat.id,
                         '- Всё верно! Ребятам хотелось, чтобы в названии отражалась принадлежность отряда к '
                         'радиотехническому факультету, поэтому уже в поезде первокурсники придумали отряду простое и '
                         'красивое название "Импульс"',
                         reply_markup=get_remove_markup())
        bot.send_message(message.chat.id,
                         'Каждое лето мы работаем - говорит Паша - ездим на целину и можем заработать. Первая Целина '
                         'ССО "Импульс" прошла в Казахстане (Актюбинская область, Карабулатский район, совхоз им. '
                         'ХХII партсъезда). Первый командир – Каменев Виктор, первый комиссар – Слепеньков Анатолий. '
                         '\n- Ну что, поедем на целину?',
                         reply_markup=get_reply3())
        return
    if message.text == 'Присоединиться к ребятам':
        bot.send_message(message.chat.id,
                         'Ты присоединился к ребятам и вы всю ночь пели песни, от "Как здорово, что все мы здесь '
                         'сегодня собрались" Олега Митяева до "Катюши" Блантера. В процессе ты завел новые знакомства '
                         'и стал еще ближе с соотрядниками.',
                         reply_markup=get_remove_markup())
        bot.send_message(message.chat.id,
                         'Вы сходите с поезда в совхозе Горьговской области и готовитесь к работе. Тут можно освоить '
                         'профессию каменщика, стропальщика, бетонщика. А работы здесь... От уборки строительного '
                         'мусора, кладки стен, установки перекрытий, кровли крыши... до монтажа и установки камер '
                         'наружного наблюдения. А если упорно обучаться всю смену одной из профессий, то можно и '
                         'диплом по этой специальности получить. Что выберешь?',
                         reply_markup=get_reply5())
        return
    if message.text == 'Лечь спать':
        bot.send_photo(message.chat.id, open("Использованные/Импульс3.jpg", "rb"))
        bot.send_message(message.chat.id,
                         'Вы сходите с поезда в совхозе Горьговской области и готовитесь к работе. Тут можно освоить '
                         'профессию каменщика, стропальщика, бетонщика. А работы здесь... От уборки строительного '
                         'мусора, кладки стен, установки перекрытий, кровли крыши... до монтажа и установки камер '
                         'наружного наблюдения. А если упорно обучаться всю смену одной из профессий, то можно и '
                         'диплом по этой специальности получить. Что выберешь?',
                         reply_markup=get_reply5())
        return
    if message.text == 'Каменщик' or message.text == 'Стропольщик' or message.text == 'Бетонщик':
        bot.send_message(message.chat.id,
                         'После долгого рабочего дня вы все вместе собрались в старой школе, которую выделили вашему '
                         'стройотряду как место проживания. Каждый вечер вас оценивали и выставляли КТУ (коэффициент '
                         'трудового участия).',
                         reply_markup=get_remove_markup())
        bot.send_message(message.chat.id,
                         'И так проходит каждый рабочий день всю смену. Если работаешь хорошо и отлично, то получаешь '
                         'значки на целинку, приличную зарплату и по возможности диплом по освоенной специальности.')
        return
    if message.text == 'Да':
        bot.send_message(message.chat.id,
                         'Ты решаешь, что поездка на целину хороший способ немного подзаработать и соглашаешься.',
                         reply_markup=get_remove_markup())
        bot.send_photo(message.chat.id, open("Использованные/Импульс2.jpg", "rb"))
        bot.send_message(message.chat.id,
                         'Ты едешь на поезде с ребятами на целину. В поезде очень весело! Все примеряют свои новые '
                         'целинки (зеленые курточки, которые выдают в студотрядах) Ты замечаешь, что ребята '
                         'собираются в группу, чтобы петь песни под гитару и рассказывать дорожные байки. '
                         'Присоединишься к ним или ляжешь спать?',
                         reply_markup=get_reply4())
        return
    if message.text == 'Нет':
        bot.send_message(message.chat.id,
                         'Ты решаешь, что не хочешь проводить жаркое лето на целине, прощаешься с Пашей и продолжаешь '
                         'прогулку по коридорам любимого института.',
                         reply_markup=get_remove_markup())
        to_start(message)
        return
    bot.send_message(message.chat.id, "Команда не реализована")
