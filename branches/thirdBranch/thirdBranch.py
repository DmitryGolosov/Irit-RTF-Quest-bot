import telebot
import time
from telebot import types
from database.usersDatabase import UsersData


def get_remove_markup():
    return types.ReplyKeyboardRemove()


def get_portrait_markup():
    portrait_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    portrait1 = types.KeyboardButton("1 портрет")
    portrait2 = types.KeyboardButton("2 портрет")
    portrait3 = types.KeyboardButton("3 портрет")
    portrait_markup.add(portrait1)
    portrait_markup.add(portrait2)
    portrait_markup.add(portrait3)
    return portrait_markup


def get_return_btn():
    return_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item0 = types.KeyboardButton("Вернуться к выбору портрета")
    return_markup.add(item0)
    return return_markup


def run(message, users: UsersData, bot: telebot.TeleBot, to_start):
    users.set_branch(message.chat.id, 3)
    if message.text == 'Вернуться к выбору портрета':
        bot.send_message(message.chat.id, "Поднявшись на 4 этаж, ты заходишь в первый же коридор. Ты замираешь в "
                                          "удивлении: на стенах висят портреты людей. Интересно, кто они?",
                         reply_markup=get_portrait_markup())
        return

    if message.text == 'Известные выпускники ИРИТ-РТФ':
        bot.send_message(message.chat.id, "Осмотреть 4 этаж, пройтись по коридору")
        bot.send_message(message.chat.id, "Поднявшись на 4 этаж, ты заходишь в первый же коридор. Ты замираешь в "
                                          "удивлении: на стенах висят портреты людей. Интересно, кто они?",
                         reply_markup=get_portrait_markup())
        return
    if message.text == '1 портрет':
        bot.send_message(message.chat.id, 'С первого портрета на тебя смотрит серьёзный мужчина. Ты читаешь табличку '
                                          'под фото:"Андрей Николаевич Гавриловский, 15 марта 1963 год. Девелопер, '
                                          'владелец бизнес-центра "Высоцкий", директор магазина "Бабушкин комод". '
                                          'Трудовая деятельность Гавриловского Андрея В 1986-1987 гг. '
                                          'Андрей Гавриловский работает мастером Свердловского приборостроительного завода.',
                         reply_markup=get_remove_markup())
        time.sleep(5)
        bot.send_message(message.chat.id, 'В 1987-1991 гг. Андрей Гавриловский - секретарь комитета комсомола '
                                          'Свердловского приборостроительного завода.')
        time.sleep(5)
        bot.send_message(message.chat.id, 'С 1991 года Андрей Гавриловский начинает развивать свой бизнес в сфере '
                                          'девелопмента, Андрей Гавриловский - девелопер бизнес-центров «Антей» и '
                                          '«Высоцкий», а также жилого комплекса на ул.Рощинской.',
                         reply_markup=get_return_btn())
        return
    if message.text == '2 портрет':
        bot.send_message(message.chat.id, 'На следующем портрете ты видишь женщину: Урывская Лидия, 25 Марта 1987 год. '
                                          'Руководитель проекта Контур.Ритейл в компании СКБ Контур. '
                                          '\n\t\t\tТрудовая деятельность. '
                                          'В 2009 году получила образование в УГТУ УПИ. С 2008 по 2013 год работала в '
                                          'Сбербанке. В 2013 году перешла на работу в СКБ Контур. На 14 июля 2015 года '
                                          'Лидия Урывская работает руководителем проекта Контур. Ритейл в компании '
                                          'СКБ Контур.', reply_markup=get_remove_markup())
        time.sleep(5)
        bot.send_message(message.chat.id, 'СКБ Контур - один из первых разработчиков программного обеспечения в России. '
                                          'С 1988 года помогает бизнесу легче взаимодействовать с государством и '
                                          'контрагентами, упрощать внутренние процессы.',
                         reply_markup=get_return_btn())
        return
    if message.text == '3 портрет':
        bot.send_message(message.chat.id, 'Со следующего портрета на тебя смотрит мужчина: Антипинский Андрей Сергеевич, '
                                          '27 сентября 1974 год. Генеральный директор ООО "УЦСБ". '
                                          '\n\t\t\tТрудовая деятельность\n '
                                          'С июня 2000 года занимает должность заместителя директора в фонде '
                                          '“Международный центр развития – Снежинск”. С октября 2001 г. - руководитель '
                                          'проекта корпоративной информационной системы, ООО "Управляющая компания '
                                          'технологии Урала".', reply_markup=get_remove_markup())
        time.sleep(5)
        bot.send_message(message.chat.id, 'Ноябрь 2002 г. - июнь 2004 г. - директор регионального представительства '
                                          'компании “Фронтстеп СНГ”. 2004 - 2007 гг. - директор представительства '
                                          'ЗАО “Открытые технологии”, специализацией которой является системная '
                                          'интеграция. В январе 2004 г. получил сертификат специалиста по управлению '
                                          'проектами - Certificated Project Management Specialist IPMA-Sovnet .')
        time.sleep(5)
        bot.send_message(message.chat.id, 'С мая 2007 г. по настоящее время - генеральный директор ООО «УЦСБ» '
                                          '(Уральский центр систем безопасности). Компания УЦСБ специализируется на '
                                          'создании, модернизации и обслуживании базовых инфраструктурных элементов '
                                          'предприятий и организаций, включая: информационные и инженерно-технические '
                                          'системы, решения по обеспечению информационной и технической безопасности.')
        time.sleep(5)
        bot.send_message(message.chat.id, 'В 1997 году с отличием окончил радиотехнический факультет Уральского '
                                          'государственного технического университета. В 2002 году получил диплом с '
                                          'отличием Уральского государственного экономического университета, факультет '
                                          '"Экономика предприятия".', reply_markup=get_return_btn())
        return

    bot.send_message(message.chat.id, "Команда не реализована")

