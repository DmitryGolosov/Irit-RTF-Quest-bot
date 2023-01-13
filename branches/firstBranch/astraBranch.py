import telebot
from telebot import types
from database.usersDatabase import UsersData


def get_remove_markup():
    return types.ReplyKeyboardRemove()


def get_reply4():
    reply4 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item13 = types.KeyboardButton('Присоединиться к ребятам')
    item14 = types.KeyboardButton('Лечь спать')
    reply4.add(item13)
    reply4.add(item14)
    return reply4


def get_reply6():
    reply6 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item18 = types.KeyboardButton('Цветок')
    item19 = types.KeyboardButton('Женское имя')
    item20 = types.KeyboardButton('Звезда в греческом языке')
    reply6.add(item18)
    reply6.add(item19)
    reply6.add(item20)
    return reply6


def get_reply7():
    reply7 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item21 = types.KeyboardButton('Потратишь время и подойдешь к вопросу творчески')
    item22 = types.KeyboardButton('Сделаешь все быстро и не особо креативно')
    reply7.add(item21)
    reply7.add(item22)
    return reply7


def get_reply8():
    reply8 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item23 = types.KeyboardButton('Поможешь ребятам раздать порции еды')
    item24 = types.KeyboardButton('Сядешь есть первый, не обращая внимания на других')
    reply8.add(item23)
    reply8.add(item24)
    return reply8


def get_reply9():
    reply9 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item25 = types.KeyboardButton('проявить инициативу')
    item26 = types.KeyboardButton('отсидеться в сторонке')
    reply9.add(item25)
    reply9.add(item26)
    return reply9


def get_reply10():
    reply10 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item27 = types.KeyboardButton('Брррр! Это было страшно, но захватывающе! День был насыщенным и интересным.')
    item28 = types.KeyboardButton('Страшные истории ты не послушал, ну и ладно, зато уснешь быстрее всех :)')
    reply10.add(item27)
    reply10.add(item28)
    return reply10


def get_reply11():
    reply11 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item29 = types.KeyboardButton('да')
    item30 = types.KeyboardButton('нет')
    reply11.add(item29, item30)
    return reply11


def on_start_astra_branch(message, users, bot):
    users.set_student_team(message.chat.id, "astra")

    bot.send_photo(message.chat.id, open("Использованные/Astra1.jpg", "rb"))
    bot.send_message(message.chat.id,
                     '"Самым первым женским педагогическим отрядом в Свердловской области, базирующимся на '
                     'радиотехническом факультете УрФУ, является СПО" Астра". Отряд появился 19 декабря 1981 года и '
                     'существует по сей день."')
    bot.send_photo(message.chat.id, open("Использованные/astra.jpg", "rb"))
    bot.send_message(message.chat.id,
                     "Тебе стало интересно, в честь чего отряд получил такое название?", reply_markup=get_reply6())


def count_score_and_send_result(message, users, bot):
    if users.get_astra_state(message.chat.id) >= 3:
        bot.send_message(message.chat.id,
                         'Так и прошла целая смена. Она была очень интересная и насыщенная событиями. Ты получил '
                         'много впечатлений и опыта, заветную целинку и стал настоящим бойцом!',
                         reply_markup=get_remove_markup())
    else:
        bot.send_message(message.chat.id,
                         'На смене ты был, но мало времени уделял своему отряду и ничего полезного не делал. Тебя не '
                         'наградили целинкой.',
                         reply_markup=get_remove_markup())


def run(message, users: UsersData, bot: telebot.TeleBot, to_start):
    # --------------------Если это не соообщение, а начало общения -------------
    if users.get_student_team(message.chat.id) == "ns":
        on_start_astra_branch(message, users, bot)
        return

    # --------------------- Логика ответа на сообщения ------------------------
    if message.text == 'Цветок':
        bot.send_message(message.chat.id,
                         'Бутон цветка Астра действительно похож на звезду, но ты читаешь дальше и понимаешь, '
                         'что свое название студотряд получил в честь греческого слова aster - звезда. Командиром '
                         'отряда стала Золотурина Екатерина, а комиссаром - Хренова Елена. Девиз отряда: Per aspera '
                         'ad ASTRA - Сквозь тернии к звездам.')
        bot.send_message(message.chat.id,
                         'Хей! - тебя окликнула одногруппница Катя. - Наконец-то закончился семестр, можно съездить '
                         'на целину. Ты со мной?',
                         reply_markup=get_reply11())
        return
    if message.text == 'Женское имя':
        bot.send_message(message.chat.id,
                         'Женское имя Астра прекрасно, как и студентки данного отряда, но ты читаешь дальше и '
                         'понимаешь, что свое название студотряд получил в честь греческого слова aster - звезда. '
                         'Командиром отряда стала Золотурина Екатерина, а комиссаром - Хренова Елена. Девиз отряда: '
                         'Per aspera ad ASTRA - Сквозь тернии к звездам.')
        bot.send_message(message.chat.id,
                         'Хей! - тебя окликнула одногруппница Катя. - Наконец-то закончился семестр, можно съездить '
                         'на целину. Ты со мной?',
                         reply_markup=get_reply11())
        return
    if message.text == 'Звезда в греческом языке':
        users.inc_astra_state(message.chat.id, 1)
        bot.send_message(message.chat.id,
                         'Ты читаешь дальше. Действительно, свое название студотряд получил в честь греческого слова '
                         'aster - звезда. Командиром отряда стала Золотурина Екатерина, а комиссаром - Хренова Елена. '
                         'Девиз отряда: Per aspera ad ASTRA - Сквозь тернии к звездам.')
        bot.send_message(message.chat.id,
                         'Хей! - тебя окликнула одногруппница Катя. - Наконец-то закончился семестр, можно съездить '
                         'на целину. Ты со мной?',
                         reply_markup=get_reply11())
        return
    if message.text == 'да':
        bot.send_message(message.chat.id,
                         'Ты решаешь, что поездка на целину хороший способ немного подзаработать и соглашаешься.',
                         reply_markup=get_remove_markup())
        bot.send_message(message.chat.id,
                         'Ты едешь на электричке с ребятами на целину. Вам очень весело! Все примеряют свои новые '
                         'целинки (зеленые курточки, которые выдают в студотрядах) Ты замечаешь, что ребята '
                         'собираются в группу, чтобы петь песни под гитару и рассказывать дорожные байки. '
                         'Присоединишься к ним или ляжешь спать?',
                         reply_markup=get_reply4())
        return
    if message.text == 'Присоединиться к ребятам':
        bot.send_message(message.chat.id,
                         'Ты присоединился к ребятам и вы всю дорогу пели песни, от "Как здорово, что все мы здесь '
                         'сегодня собрались" Олега Митяева до "Катюши" Блантера. В процессе ты завел новые знакомства '
                         'и стал еще ближе с соотрядниками.')
        bot.send_message(message.chat.id,
                         'Вы всем отрядом приехали в ДОЛ "Мечта" в городе Ревда. Вас распределили вожатыми в отряды с '
                         'пионерами. Впереди ждет интересная смена. Скоро лагерное творческое мероприятие, '
                         'надо придумать с отрядом название и кричалку.',
                         reply_markup=get_reply7())
        return
    if message.text == 'Лечь спать':
        bot.send_message(message.chat.id,
                         'Вы всем отрядом приехали в ДОЛ "Мечта" в городе Ревда. Вас распределили вожатыми в отряды с '
                         'пионерами. Впереди ждет интересная смена. Скоро лагерное творческое мероприятие, '
                         'надо придумать с отрядом название и кричалку.',
                         reply_markup=get_reply7())
        return
    if message.text == 'Сделаешь все быстро и не особо креативно':
        bot.send_message(message.chat.id,
                         'Вы решили не проявлять креатив, придумали обычное название и дали ребятам свободное время',
                         reply_markup=get_remove_markup())
        bot.send_message(message.chat.id,
                         'Настало время обеда. Последний раз вы ели в электричке и тебе не терпится поесть. Однако '
                         'соотрядники ещё накрывают на стол.',
                         reply_markup=get_reply8())
        return
    if message.text == 'Потратишь время и подойдешь к вопросу творчески':
        users.inc_astra_state(message.chat.id, 1)
        bot.send_message(message.chat.id,
                         'Вы хорошо постарались, придумали с ребятами интересное название и запоминающуюся кричалку и '
                         'вас заметили старшие',
                         reply_markup=get_remove_markup())
        bot.send_message(message.chat.id,
                         'Настало время обеда. Последний раз вы ели в электричке и тебе не терпится поесть. Однако '
                         'соотрядники ещё накрывают на стол.',
                         reply_markup=get_reply8())
        return
    if message.text == 'Поможешь ребятам раздать порции еды':
        users.inc_astra_state(message.chat.id, 1)
        bot.send_message(message.chat.id,
                         'Отлично! Никто не остался без обеда. Тебя поблагодарили за помощь.',
                         reply_markup=get_remove_markup())
        bot.send_message(message.chat.id,
                         'Физкульт-привет! Пришло время спортивного мероприятия. Ты уже немного устал и думаешь, '
                         'помочь своему отряду или они смогут справиться сами?',
                         reply_markup=get_reply9())
        return
    if message.text == 'Сядешь есть первый, не обращая внимания на других':
        bot.send_message(message.chat.id, 'Ребятам не очень понравилось, что вы никак не помогли(((',
                         reply_markup=get_remove_markup())
        bot.send_message(message.chat.id,
                         'Физкульт-привет! Пришло время спортивного мероприятия. Ты уже немного устал и думаешь, '
                         'помочь своему отряду или они смогут справиться сами?',
                         reply_markup=get_reply9())
    if message.text == 'проявить инициативу':
        users.inc_astra_state(message.chat.id, 1)
        bot.send_message(message.chat.id,
                         'Браво! Ваш отряд взял первое место! Так держать!',
                         reply_markup=get_remove_markup())
        bot.send_message(message.chat.id,
                         'Вечер - время собраться у костра, обсудить итоги дня и рассказать страшные лагерные байки. '
                         'Примешь участие в разговоре?',
                         reply_markup=get_reply10())
        return
    if message.text == 'отсидеться в сторонке':
        bot.send_message(message.chat.id, 'Твоему отряду не удалось вырваться вперед.',
                         reply_markup=get_remove_markup())
        bot.send_message(message.chat.id,
                         'Вечер - время собраться у костра, обсудить итоги дня и рассказать страшные лагерные байки. '
                         'Примешь участие в разговоре?',
                         reply_markup=get_reply10())
        return
    if message.text == 'нет':
        bot.send_message(message.caht.id,
                         'Ты решаешь, что не хочешь проводить жаркое лето на целине, прощаешься с Катей и продолжаешь '
                         'прогулку по коридорам любимого института.')
        to_start(message)
        return
    if message.text == 'Брррр! Это было страшно, но захватывающе! День был насыщенным и интересным.':
        users.inc_astra_state(message.chat.id, 1)
        count_score_and_send_result(message, users, bot)
        return
    if message.text == 'Страшные истории ты не послушал, ну и ладно, зато уснешь быстрее всех :)':
        users.inc_astra_state(message.chat.id, 0)
        count_score_and_send_result(message, users, bot)
        return
    bot.send_message(message.chat.id, "Команда не реализована")
