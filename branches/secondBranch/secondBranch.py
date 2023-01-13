import telebot
import time
from telebot import types
from database.usersDatabase import UsersData


def get_remove_markup():
    return types.ReplyKeyboardRemove()


def get_first_markup():
    fst_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    key1 = types.KeyboardButton('Да')
    key2 = types.KeyboardButton('Нет')
    fst_markup.add(key1, key2)
    return fst_markup


def get_second_markup():
    second_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    key_end = types.KeyboardButton('Встать в конец')
    key_begin = types.KeyboardButton('Встать ближе')
    second_markup.add(key_end)
    second_markup.add(key_begin)
    return second_markup


def get_poem_markup():
    poem = types.ReplyKeyboardMarkup(resize_keyboard=True)
    frst = types.KeyboardButton("1 Про природу")
    scnd = types.KeyboardButton("2 Про любовь")
    thrd = types.KeyboardButton("3 Смешной")
    poem.add(frst)
    poem.add(scnd)
    poem.add(thrd)
    return poem


def get_fourth_markup():
    fourth_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    key1 = types.KeyboardButton('Слушать внимательно')
    key2 = types.KeyboardButton('Отвлечься')
    fourth_markup.add(key1)
    fourth_markup.add(key2)
    return fourth_markup

def get_present_markup():
    present_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Постараться')
    btn2 = types.KeyboardButton('Забить')
    present_markup.add(btn1)
    present_markup.add(btn2)
    return present_markup

def get_sixth_markup():
    markup6 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('да')
    item2 = types.KeyboardButton('нет')
    markup6.add(item1, item2)
    return markup6

def get_seven_markup():
    markup7 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    key_yes = types.KeyboardButton('Да, рискнуть')
    key_no = types.KeyboardButton('Нет, не рисковать')
    markup7.add(key_yes)
    markup7.add(key_no)
    return markup7

def get_eight_markup():
    markup8 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_yes = types.KeyboardButton('Да, заглянуть')
    item_no = types.KeyboardButton('Нет, не заглядывать')
    markup8.add(item_yes, item_no)
    return markup8

def get_nine_markup():
    markup9 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_yes = types.KeyboardButton('ДА')
    item_no = types.KeyboardButton('НЕТ')
    markup9.add(item_yes, item_no)
    return markup9

def get_tenth_markup():
    markup10 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('День радио')
    item2 = types.KeyboardButton('День инженера')
    item3 = types.KeyboardButton('День забытого пропуска')
    markup10.add(item1)
    markup10.add(item2)
    markup10.add(item3)
    return markup10

def get_day_radio_markup():
    dayR = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_yes = types.KeyboardButton('Да, хочу')
    btn_no = types.KeyboardButton('Нет, не хочу')
    dayR.add(btn_yes)
    dayR.add(btn_no)
    return dayR

def run(message, users: UsersData, bot: telebot.TeleBot, to_start):
    users.set_branch(message.chat.id, 2)

    if message.text == 'Традиции ИРИТ-РТФ':
        bot.send_message(message.chat.id, "Ну вот и начался новый учебный год. Сегодня 1 сентября, впереди тебя ждет "
                                          "много всего интересного! Ты подходишь ко входу в институт и видишь большую "
                                          "толпу людей. Спросить у кого-нибудь, что тут происходит?",
                         reply_markup=get_first_markup())
        return
    if message.text == 'Нет':
        users.set_friend_name(message.chat.id, "Кристина")
        bot.send_message(message.chat.id, "Осмотрев толпу ты замечаешь, что некоторые ребята держат таблички с какими-то "
                                          "цифрами над головами. Видимо это номера академических групп. Ты находишь свою "
                                          "группу и знакомишься с наставниками.", reply_markup=get_remove_markup())
        time.sleep(5)
        bot.send_message(message.chat.id, "Всей большой толпой первокурсников вы идете на площадку рядом со зданием "
                                          "ИРИТ-РТФ. Там уже стоит сцена, все украшено плакатами и шариками. Встать "
                                          "ближе к сцене или в конец толпы?", reply_markup=get_second_markup())
        return

    if message.text == 'Да':
        users.set_friend_name(message.chat.id, "Артём")
        bot.send_message(message.chat.id, "-Привет! -ты подходишь к рыжему парню в джинсовке. - Расскажи, пожалуйста, "
                                          "что происходит? "
                                          "\n-О, привет! - задорно улыбается он. - Все просто, тут наставники групп "
                                          "находят своих первокурсников. Видишь, некоторые ребята держат в руках плакаты "
                                          "с цифрами? \n(Ты утвердительно киваешь.)",
                         reply_markup=get_remove_markup())
        time.sleep(5)
        bot.send_message(message.chat.id, f"-Вот, ищешь свою группу и подходишь к ребятам. "
                                          f"\n-Понял-(а), спасибо. Я кстати {message.from_user.first_name}. А тебя как зовут? \n"
                                          "-Я Артём, приятно познакомиться. Обменяемся контактами? - предлагает он. "
                                          "\nВы обмениваетесь телефонами и страничками в вк и ты идешь к своей группе.")
        time.sleep(5)
        bot.send_message(message.chat.id, "Всей большой толпой первокурсников вы идете на площадку рядом со зданием "
                                          "ИРИТ-РТФ. Там уже стоит сцена, все украшено плакатами и шариками. Встать "
                                          "ближе к сцене или в конец толпы?", reply_markup=get_second_markup())
        return

    if message.text == 'Встать в конец':
        bot.send_message(message.chat.id, "Ты встал-(а) в самый конец и ничего не услышал-(а), а оказывается разыгрывали "
                                          "футболку и обложку на студенческий...",
                         reply_markup=get_remove_markup())
        time.sleep(2)
        bot.send_message(message.chat.id, "Выступление закончилось и вы всей группой заходите в институт.")
        time.sleep(3)
        bot.send_photo(message.chat.id,
                       open("Использованные/литературный вечер.jpg", "rb"))
        bot.send_message(message.chat.id, 'Уже несколько недель ты ходишь на занятия и сегодня заметил-(а), что на '
                                          'информационном стенде висит огромный плакат "Литературный вечер". '
                                          'Тебе стало интересно, что это такое.')
        time.sleep(3)
        if users.get_friend_name(message.chat.id) == "Артём":
            bot.send_message(message.chat.id,
                             "-Слушай, Артем - обращаешься ты к другу, который зашел в институт вместе с "
                             "тобой, - может сходим туда вместе, посмотрим, что там да как?\n "
                             "-Давай, я как раз люблю поэзию! - Отвечает он.")
            time.sleep(5)
            bot.send_message(message.chat.id,
                             "Прочитав информацию о мероприятии, ты думаешь, какое стихотворение выучить "
                             "для вечера", reply_markup=get_poem_markup())

        elif users.get_friend_name(message.chat.id) == "Кристина":
            bot.send_message(message.chat.id, "Прочитав информацию о мероприятии, ты думаешь, какое стихотворение "
                                              "выучить для вечера",reply_markup=get_poem_markup())
            return
        return

    if message.text == 'Встать ближе':
        bot.send_message(message.chat.id, "С речью выступили преподаватели основных дисциплин и директор института. "
                                          "Рассказали немного об учебном процессе и пожелали хорошей и продуктивной учебы.",
                         reply_markup=get_remove_markup())
        time.sleep(2)
        bot.send_message(message.chat.id, "Выступление закончилось и вы всей группой заходите в институт.")
        time.sleep(3)
        bot.send_photo(message.chat.id,
                       open("Использованные/литературный вечер.jpg", "rb"))
        bot.send_message(message.chat.id, 'Уже несколько недель ты ходишь на занятия и сегодня заметил-(а), что на '
                                          'информационном стенде висит огромный плакат "Литературный вечер". '
                                          'Тебе стало интересно, что это такое.')
        time.sleep(3)
        if users.get_friend_name(message.chat.id) == "Артём":
            bot.send_message(message.chat.id,
                             "-Слушай, Артем - обращаешься ты к другу, который зашел в институт вместе с "
                             "тобой, - может сходим туда вместе, посмотрим, что там да как?\n "
                             "-Давай, я как раз люблю поэзию! - Отвечает он.")
            time.sleep(5)
            bot.send_message(message.chat.id,
                             "Прочитав информацию о мероприятии, ты думаешь, какое стихотворение выучить "
                             "для вечера", reply_markup=get_poem_markup())

        elif users.get_friend_name(message.chat.id) == "Кристина":
            bot.send_message(message.chat.id, "Прочитав информацию о мероприятии, ты думаешь, какое стихотворение "
                                              "выучить для вечера", reply_markup=get_poem_markup())
            return
        return

    if message.text == '1 Про природу' or message.text == '2 Про любовь' or message.text == '3 Смешной':
        if message.text == '1 Про природу':
            users.set_poem_state(message.chat.id, 1)
        if message.text == '2 Про любовь':
            users.set_poem_state(message.chat.id, 2)
        if message.text == '3 Смешной':
            users.set_poem_state(message.chat.id, 3)
        bot.send_photo(message.chat.id,
                       open("Использованные/лит.вечер.jpg", "rb"))
        bot.send_message(message.chat.id, "В назначенный день ты приходишь в аудиторию. Тут окна занавешены плотными "
                                          "шторами, висят желтые гирлянды, стоят светильники в виде свечей и канделябров."
                                          " Доска разрисована в литературной тематике.", reply_markup=get_remove_markup())
        time.sleep(5)
        if users.get_friend_name(message.chat.id) == "Артём":
            bot.send_message(message.chat.id, "Ты садишься с Артемом за парту и вы готовитесь к погружению в мир поэзии.")
        else:
            bot.send_message(message.chat.id, f"Ты подсаживаешься к девушке за парту и решаешь с ней познакомиться.\n "
                                              f"-Привет, я {message.from_user.first_name}. А тебя как зовут? "
                                              f"\n-Привет! Я Кристина. Ты тоже с первого курса? "
                                              f"\n-Да, - отвечаешь ты ей, - так волнительно, первый раз в таком участвую. "
                                              f"\n-Я тоже, но уверена, что нам понравится, - отвечает она и мило улыбается.")
        time.sleep(5)
        bot.send_message(message.chat.id, "Включается тихая музыка и к доске выходит ведущий. Слушать тех, кто выступает, "
                                          "внимательно или отвлечься?", reply_markup=get_fourth_markup())
        return

    if message.text == 'Слушать внимательно':
        bot.send_message(message.chat.id, "Звучат прекрасные стихи в исполнении талантливых ребят. Тут очередь подходит "
                                          "и к тебе. Ты выходишь на импровизированную сцену и рассказываешь стих",
                         reply_markup=get_remove_markup())
        time.sleep(3)
        if users.get_poem_state(message.chat.id) == 1:
            bot.send_message(message.chat.id,"Закончив читать, ты замечаешь, что слушатели восхитились красотой природы, "
                                             "которая описывалась в стихе. Им очень понравилось")
        if users.get_poem_state(message.chat.id) == 2:
            bot.send_message(message.chat.id, "Во время чтения ты поддался-(ась) эмоциям и чуть не прослезился-(ась). "
                                              "Посмотрев в зал ты убедился-(ась), что зрители прочувствовали этот стих "
                                              "вместе с тобой.")
        if users.get_poem_state(message.chat.id,) == 3:
            bot.send_message(message.chat.id, "На протяжении твоего выступления публика то и дело взрывалась от смеха, "
                                              "ты точно запомнишься им надолго")
        time.sleep(3)
        bot.send_message(message.chat.id, "Проходят дни, пролетают недели, на улице становится все холоднее и холоднее "
                                          "и появляется небольшая тревога. А все потому, что близится сессия... Но "
                                          "ничего, страх перед сессией скрасит предновогодняя суета. Ты решаешь помочь "
                                          "ребятам с украшением входа в любимый институт.")
        bot.send_message(message.chat.id, "Вы украшаете вход гирляндами, фигурами, рисуете на стеклах возле входа. "
                                          "А перед входом ставите ледяную скульптуру - символ наступающего года. "
                                          "Тут кто-то из друзей предлагает поучаствовать в тайном санте")
        bot.send_photo(message.chat.id,
                       open("Использованные/тайный _санта.jpg", "rb"))
        bot.send_message(message.chat.id, "Узнав условия этого мероприятия, ты решаешь подать заявку на участие. Через "
                                          "некоторое время тебе приходит информация о человеке, которому ты готовишь "
                                          "подарок. Постараться сделать хороший подарок на основе предпочтений получателя "
                                          "или забить?", reply_markup=get_present_markup())
        return

    if message.text == 'Отвлечься':
        bot.send_message(message.chat.id, f"Ты зазевался-(ась) и не заметил-(а) как уснул-(а)... Тебя будит "
                                          f"{users.get_friend_name(message.chat.id)}, когда уже все закончилось. Жаль, "
                                          f"что стих ты так и не рассказал-(а)", reply_markup=get_remove_markup())
        time.sleep(4)
        bot.send_message(message.chat.id, "Проходят дни, пролетают недели, на улице становится все холоднее и холоднее "
                                          "и появляется небольшая тревога. А все потому, что близится сессия... Но "
                                          "ничего, страх перед сессией скрасит предновогодняя суета. Ты решаешь помочь "
                                          "ребятам с украшением входа в любимый институт.")
        time.sleep(4)
        bot.send_message(message.chat.id, "Вы украшаете вход гирляндами, фигурами, рисуете на стеклах возле входа. "
                                          "А перед входом ставите ледяную скульптуру - символ наступающего года. "
                                          "(Тут кто-то из друзей предлагает поучаствовать в тайном санте)")
        time.sleep(4)
        bot.send_photo(message.chat.id,
                       open("Использованные/тайный _санта.jpg", "rb"))
        bot.send_message(message.chat.id, "Узнав условия этого мероприятия, ты решаешь подать заявку на участие. Через "
                                          "некоторое время тебе приходит информация о человеке, которому ты готовишь "
                                          "подарок. Постараться сделать хороший подарок на основе предпочтений получателя "
                                          "или забить?", reply_markup=get_present_markup())
        return

    if message.text == 'Постараться':
        bot.send_message(message.chat.id, 'Через некоторые время ты получаешь подарок от своего "Тайного Санты". Тебе '
                                          'очень понравился подарок и ты встретил новый год в хорошем настроении.',
                         reply_markup=get_remove_markup())
        time.sleep(3)
        bot.send_message(message.chat.id, "Проходят новогодние каникулы и сессия тоже позади, начался новый семестр. "
                                          "Ты замечаешь, что все вокруг снова начали суетиться. Ну конечно! Сегодня же "
                                          "день рождения ИРИТ-РТФ!")
        time.sleep(4)
        bot.send_message(message.chat.id, "Недалеко ты замечаешь ребят, которые раздают какие-то листочки. Подойдя к ним "
                                          "ты видишь, что это карта сегодняшних событий. Поучаствуем в празднике?",
                         reply_markup=get_sixth_markup())
        return
    if message.text == 'Забить':
        bot.send_message(message.chat.id, "Через несколько недель ты получаешь по почте пакет из пятерочки, в котором "
                                          "лежали *тут какой-то плохой подарок*",reply_markup=get_remove_markup())
        time.sleep(3)
        bot.send_message(message.chat.id, "Проходят новогодние каникулы и сессия тоже позади, начался новый семестр. "
                                          "Ты замечаешь, что все вокруг снова начали суетиться. Ну конечно! Сегодня же "
                                          "день рождения ИРИТ-РТФ!")
        time.sleep(4)
        bot.send_message(message.chat.id,
                         "Недалеко ты замечаешь ребят, которые раздают какие-то листочки. Подойдя к ним "
                         "ты видишь, что это карта сегодняшних событий. Поучаствуем в празднике?",
                         reply_markup=get_sixth_markup())
        return

    if message.text == 'да':
        bot.send_media_group(message.chat.id, [
            telebot.types.InputMediaPhoto(open("Использованные/др Радика 1.jpg", "rb")),
            telebot.types.InputMediaPhoto(open("Использованные/др Радика 2.jpg", "rb")), ])
        bot.send_message(message.chat.id, "Посмотрев на карту, ты видишь, что недалеко от тебя есть фотозона. Ты делаешь"
                                          " классные фотки со своими друзьями и идешь дальше. Рядом с фотозоной "
                                          "столпились ребята и ты решаешь посмотреть, что там за активность. А там "
                                          "оказался розыгрыш футболок и тетрадей с логотипами УрФУ. Нужно первым найти "
                                          "все 26 слов в филворде. Ты решаешь поучаствовать и находишь слова вторым-(ой). "
                                          "В итоге получаешь УрФУшную тетрадь. Вместе с друзьями ты решаешь сходить в "
                                          "аудиторию и послушать историю института.", reply_markup=get_remove_markup())
        time.sleep(5)
        bot.send_media_group(message.chat.id, [
            telebot.types.InputMediaPhoto(open("Использованные/день РТФ1.jpg", "rb")),
            telebot.types.InputMediaPhoto(open("Использованные/день РТФ2.jpg", "rb"))])
        bot.send_message(message.chat.id, "Время пролетело незаметно и уже спустя час фильм закончился. Ты узнал-(а) "
                                          "много нового, а на выходе из аудитории тоже раздавали приятные мелочи: ручки "
                                          "с логотипами института, значки и браслеты. Ты заходишь с друзьями в коворкинг"
                                          " и видишь, что начали разрезать большой торт. Вам раздали одноразовые тарелки"
                                          " с тортом. Это было очень вкусно. Удивительно, что торт достался всем! "
                                          "Праздник удался, это был супер день. Ты познакомился с "
                                          f"{users.get_friend_name(message.chat.id)}")
        time.sleep(5)
        bot.send_message(message.chat.id, "Спустя время ты, выглянув в окно, замечаешь, что на улице уже весна. В "
                                          "воздухе пахнет первыми цветами, весенней свежестью и выпечкой... Стоп! "
                                          "Что это за запах? Обернувшись ты видишь целую стопку... синих блинов?")
        time.sleep(3)
        bot.send_message(message.chat.id, f"В холле первого этажа ты замечаешь друга. -Хей, {users.get_friend_name(message.chat.id)},"
                                          f" что происходит? -О, это обычная масленица в Радике :) -А почему блины "
                                          f"синие? - в недоумении спрашиваешь ты -Это традиция! Чтобы каждый мог "
                                          f"издалека узнать студента радика по синему языку. Ты задумчиво побрел-(а) в "
                                          f"центр веселья. Рискнуть и съесть синий блин?", reply_markup=get_seven_markup())
        return

    if message.text == 'нет':
       bot.send_message(message.chat.id, "Ты решаешь не тратить на это время и прийти к окончанию мероприятия, чтобы "
                                         "поесть торт. Но увы, ты опоздал-(а) и торт тебе не достался.",
                        reply_markup=get_remove_markup())
       time.sleep(2)
       bot.send_message(message.chat.id, "Спустя время ты, выглянув в окно, замечаешь, что на улице уже весна. В "
                                         "воздухе пахнет первыми цветами, весенней свежестью и выпечкой... Стоп! "
                                         "Что это за запах? Обернувшись ты видишь целую стопку... синих блинов?")
       time.sleep(3)
       bot.send_message(message.chat.id,
                        f"В холле первого этажа ты замечаешь друга. "
                        f"\n-Хей, {users.get_friend_name(message.chat.id)},что происходит? "
                        f"\n-О, это обычная масленица в Радике :) "
                        f"\n-А почему блины синие? - в недоумении спрашиваешь ты "
                        f"\n-Это традиция! Чтобы каждый мог издалека узнать студента радика по синему языку. "
                        f"\nТы задумчиво побрел-(а) в центр веселья. Рискнуть и съесть синий блин?",
                        reply_markup=get_seven_markup())
       return

    if message.text == 'Да, рискнуть':
        bot.send_message(message.chat.id, "Мммм...Очень вкусно! Интересно, а язык действительно синий? Ты подходишь к "
                                          "зеркалу и удивляешься, что язык стал синего цвета. Необычно!")
        time.sleep(2)
        bot.send_message(message.chat.id, "Ты начинаешь слышать какой-то шум. Посмотреть что происходит?",
                         reply_markup=get_eight_markup())
        return

    if message.text == 'Нет, не рисковать':
        bot.send_message(message.chat.id, "Хммм, выглядит сомнительно, пожалуй откажусь.")
        time.sleep(2)
        bot.send_message(message.chat.id, "Ты начинаешь слышать какой-то шум. Посмотреть что происходит?",
                         reply_markup=get_eight_markup())
        return
    if message.text == "Да, заглянуть":
        bot.send_message(message.chat.id, "Ого, да в коворкинге весело! Столько различных конкурсов. Здесь и "
                                          "перетягивание каната, и лимбо, и метание сапога... Поучаствуем?",
                         reply_markup=get_nine_markup())
        return
    if message.text == 'ДА':
        bot.send_message(message.chat.id, "Это было классно, твоя команда победила в перетягивании каната! И вы выиграли "
                                          "мерч радика!", reply_markup=get_remove_markup())
        time.sleep(2)
        bot.send_message(message.chat.id, "Ты подходишь к выходу из института и замечаешь какую-то суету. Идет группа "
                                          "студентов с ведрами, тряпками и моющими средствами. "
                                          "\n-Привет! А что происходит? - решаешь спросить ты. "
                                          "\n-Приветик! Мы идем мыть памятник. - отвечает девушка из толпы. "
                                          "\n-Памятник? - говоришь ты в недоумении.- Что еще за памятник и зачем? "
                                          "\n-Как это зачем? - удивилась девушка. - Завтра же главный праздник в ИРИТ-РтФ! "
                                          "Скажи еще, что не знаешь об этом? "
                                          "\nТы пытаешься вспомнить, что завтра за день такой?",
                         reply_markup=get_tenth_markup())
        return

    if message.text == 'НЕТ':
        bot.send_message(message.chat.id, "Ты решаешь остаться в стороне и понаблюдать за играми... Оказывается, "
                                          "раздавали подарки :(", reply_markup=get_remove_markup())
        time.sleep(2)
        bot.send_message(message.chat.id, "Ты подходишь к выходу из института и замечаешь какую-то суету. Идет группа "
                                          "студентов с ведрами, тряпками и моющими средствами. "
                                          "\n-Привет! А что происходит? - решаешь спросить ты. "
                                          "\n-Приветик! Мы идем мыть памятник. - отвечает девушка из толпы. "
                                          "\n-Памятник? - говоришь ты в недоумении.- Что еще за памятник и зачем? "
                                          "\n-Как это зачем? - удивилась девушка. - Завтра же главный праздник в ИРИТ-РтФ! "
                                          "Скажи еще, что не знаешь об этом? "
                                          "\nТы пытаешься вспомнить, что завтра за день такой?",
                         reply_markup=get_tenth_markup())
        return

    if message.text == "Нет, не заглядывать":
        bot.send_message(message.chat.id, "Ты решаешь не смотреть, что там шумит, а спросить у проходящего мимо студента. "
                                          "Оказывается там было что-то веселое...", reply_markup=get_remove_markup())
        time.sleep(2)
        bot.send_message(message.chat.id, "Ты подходишь к выходу из института и замечаешь какую-то суету. Идет группа "
                                          "студентов с ведрами, тряпками и моющими средствами. "
                                          "\n-Привет! А что происходит? - решаешь спросить ты. "
                                          "\n-Приветик! Мы идем мыть памятник. - отвечает девушка из толпы. "
                                          "\n-Памятник? - говоришь ты в недоумении.- Что еще за памятник и зачем? "
                                          "\n-Как это зачем? - удивилась девушка. - Завтра же главный праздник в ИРИТ-РтФ! "
                                          "Скажи еще, что не знаешь об этом? "
                                          "\nТы пытаешься вспомнить, что завтра за день такой?",
                         reply_markup=get_tenth_markup())
        return
    if message.text == 'День инженера' or message.text == 'День забытого пропуска':
        bot.send_message(message.chat.id, '-А ты точно студент ИРИТ-РТФ??? - прищурилась девушка. - Ну ладно, просвещу '
                                          'тебя, завтра 7 мая День радио. Хочешь помочь с подготовкой?',
                         reply_markup=get_day_radio_markup())
        return
    if message.text == 'День радио':
        bot.send_message(message.chat.id, "-Ну конечно! - с восторгом сказала девушка.- Хочешь помочь с подготовкой?",
                         reply_markup=get_day_radio_markup())
        return

    if message.text == 'Да, хочу':
        bot.send_media_group(message.chat.id, [
            telebot.types.InputMediaPhoto(open("Использованные/Попов 1.jpg", "rb")),
            telebot.types.InputMediaPhoto(open("Использованные/Попов 2.jpg", "rb")),
            telebot.types.InputMediaPhoto(open("Использованные/Попов 3.jpg", "rb"))])

        bot.send_message(message.chat.id, "-Супер! Пошли с нами. "
                                          "\nДойдя до памятника, ты понял-(а), что это памятник Александру Степановичу "
                                          "Попову - создателю радио. Ну что ж, приступим к приборке. Спустя время ты "
                                          "смотришь на результат и испытываешь удовлетворение: и сам памятник и "
                                          "территория вокруг блестят от чистоты. Понадеемся, что и птицы оценят наши "
                                          "старания и хотя бы пару дней будут смотреть на памятник издалека во избежание "
                                          "неприятных инцидентов.",
                         reply_markup=get_remove_markup())
        time.sleep(5)
        bot.send_media_group(message.chat.id, [
            telebot.types.InputMediaPhoto(open("Использованные/День Радио.jpg", "rb")),
            telebot.types.InputMediaPhoto(open("Использованные/День Радио2.jpg", "rb")),
            telebot.types.InputMediaPhoto(open("Использованные/День Радио3.jpg", "rb"))])

        bot.send_message(message.chat.id, "По возвращении в институт тебе предложили помочь с украшением самого здания "
                                          "Радиофака. Весь оставшийся день вы развешивали плакаты, надували шарики, "
                                          "украшали вход и этажи. Завтрашний день должен быть очень насыщенным.")
        time.sleep(4)
        bot.send_media_group(message.chat.id, [
            telebot.types.InputMediaPhoto(open("Использованные/День Радио4.jpg", "rb")),
            telebot.types.InputMediaPhoto(open("Использованные/День Радио5.jpg", "rb")),
            telebot.types.InputMediaPhoto(open("Использованные/День Радио6.jpg", "rb"))])

        bot.send_message(message.chat.id, "Ну вот и наступил праздник. Ты подходишь ко входу в институт и видишь, что "
                                          "там уже собирается народ: тут и студенты, и преподаватели, и выпускники. "
                                          "Все собрались на концерт, посвященный Дню радио. Концерт проходит на площадке "
                                          "перед университетом. Это яркое и захватывающее зрелище. Студенты готовят песни, "
                                          "танцы, сценки и стендапы и все посвящено празднику.")
        time.sleep(4)
        bot.send_media_group(message.chat.id, [
            telebot.types.InputMediaPhoto(open("Использованные/Шествие 1.jpg", "rb")),
            telebot.types.InputMediaPhoto(open("Использованные/Шествие 2.jpg", "rb")),
            telebot.types.InputMediaPhoto(open("Использованные/Шествие 3.jpg", "rb"))])

        bot.send_message(message.chat.id, "После насыщенного концерта начинается шествие. Вы стройной колонной идете по "
                                          "проспекту Ленина, поете песни, произносите кричалки. По всей колонне волной "
                                          "проносятся главные слова института: РТФ! УрФУ! Попов! Всей дружной толпой вы "
                                          "дошли до памятника. Здесь вы все вместе поздравляете друг друга с праздником "
                                          "и делитесь впечатлениями.")
        time.sleep(4)
        bot.send_message(message.chat.id, "Ты замечаешь знакомую рыжую голову Артёма. "
                                          "\n-Артём! - зовешь ты друга. -Привет! И ты тут. "
                                          "\n-Привет! Конечно, это же главный праздник радистов - отвечает парень. "
                                          "\n-Привет, ребята, - к нам подходит Кристина. - Тут так весело! "
                                          "\n-Ага, а еще веселее было, когда раньше ребята забирались на шею памятнику и,"
                                          " размахивая знаменем, кричали факультетские кричалки, - хохотнул Артём. "
                                          "\n-Действительно, забавная традиция! - отвечаешь ты.")
        time.sleep(5)
        bot.send_media_group(message.chat.id, [
            telebot.types.InputMediaPhoto(open("Использованные/Шествие 4.jpg", "rb")),
            telebot.types.InputMediaPhoto(open("Использованные/Шествие 5.jpg", "rb")),
            telebot.types.InputMediaPhoto(open("Использованные/Шествие 6.jpg", "rb"))])

        bot.send_message(message.chat.id, "Шествие заканчивается у памятника Попову. Рядом с ним с площадки в небо "
                                          "запускаю салют, чтобы весь город мог насладиться атмосферой праздника. "
                                          "Это был незабываемый день...")
        time.sleep(3)
        bot.send_message(message.chat.id, "Ну вот и подошел к концу учебный год, ты отлично закрыл-(а) сессию. А самое "
                                          "главное, что ты погрузился-(ась) в основные традиции нашего дорогого института. "
                                          "Познакомился-(ась) с новыми людьми и просто классно провел-(а) время!")
        return

    if message.text == 'Нет, не хочу':
        bot.send_message(message.chat.id, "-Хм, жаль...Ну ладно, надеюсь, что завтра мы все сможем повеселиться! - "
                                          "крикнула студентка, догоняя группу других ребят.")
        time.sleep(2)
        bot.send_media_group(message.chat.id, [
            telebot.types.InputMediaPhoto(open("Использованные/День Радио4.jpg", "rb")),
            telebot.types.InputMediaPhoto(open("Использованные/День Радио5.jpg", "rb")),
            telebot.types.InputMediaPhoto(open("Использованные/День Радио6.jpg", "rb"))])

        bot.send_message(message.chat.id, "Ну вот и наступил праздник. Ты подходишь ко входу в институт и видишь, что "
                                          "там уже собирается народ: тут и студенты, и преподаватели, и выпускники. "
                                          "Все собрались на концерт, посвященный Дню радио. Концерт проходит на площадке "
                                          "перед университетом. Это яркое и захватывающее зрелище. Студенты готовят песни, "
                                          "танцы, сценки и стендапы и все посвящено празднику.")
        time.sleep(4)
        bot.send_media_group(message.chat.id, [
            telebot.types.InputMediaPhoto(open("Использованные/Шествие 1.jpg", "rb")),
            telebot.types.InputMediaPhoto(open("Использованные/Шествие 2.jpg", "rb")),
            telebot.types.InputMediaPhoto(open("Использованные/Шествие 3.jpg", "rb"))])

        bot.send_message(message.chat.id,
                         "После насыщенного концерта начинается шествие. Вы стройной колонной идете по "
                         "проспекту Ленина, поете песни, произносите кричалки. По всей колонне волной "
                         "проносятся главные слова института: РТФ! УрФУ! Попов! Всей дружной толпой вы "
                         "дошли до памятника. Здесь вы все вместе поздравляете друг друга с праздником "
                         "и делитесь впечатлениями.")
        time.sleep(4)
        bot.send_message(message.chat.id, "Ты замечаешь знакомую рыжую голову Артёма. "
                                          "\n-Артём! - зовешь ты друга. -Привет! И ты тут. "
                                          "\n-Привет! Конечно, это же главный праздник радистов - отвечает парень. "
                                          "\n-Привет, ребята, - к нам подходит Кристина. - Тут так весело! "
                                          "\n-Ага, а еще веселее было, когда раньше ребята забирались на шею памятнику и,"
                                          " размахивая знаменем, кричали факультетские кричалки, - хохотнул Артём. "
                                          "\n-Действительно, забавная традиция! - отвечаешь ты.")
        time.sleep(5)
        bot.send_media_group(message.chat.id, [
            telebot.types.InputMediaPhoto(open("Использованные/Шествие 4.jpg", "rb")),
            telebot.types.InputMediaPhoto(open("Использованные/Шествие 5.jpg", "rb")),
            telebot.types.InputMediaPhoto(open("Использованные/Шествие 6.jpg", "rb"))])

        bot.send_message(message.chat.id, "Шествие заканчивается у памятника Попову. Рядом с ним с площадки в небо "
                                          "запускаю салют, чтобы весь город мог насладиться атмосферой праздника. "
                                          "Это был незабываемый день...")
        time.sleep(3)
        bot.send_message(message.chat.id, "Ну вот и подошел к концу учебный год, ты отлично закрыл-(а) сессию. А самое "
                                          "главное, что ты погрузился-(ась) в основные традиции нашего дорогого института. "
                                          "Познакомился-(ась) с новыми людьми и просто классно провел-(а) время!")
        return

    bot.send_message(message.chat.id, "Команда не реализована")
