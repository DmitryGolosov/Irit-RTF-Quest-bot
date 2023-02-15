import app.quest
from app.responseData import ResponseData
from app.database.usersDatabase import UsersData


def get_reply4() -> list[str]:
    return ["Присоединиться к ребятам", "Лечь спать"]


def get_reply6() -> list[str]:
    return ["Цветок", "Женское имя", "Звезда в греческом языке"]


def get_reply7() -> list[str]:
    return ["1. Потратишь время ...", "2. Сделаешь все быстро ..."]


def get_reply8() -> list[str]:
    return ["1. Поможешь ребятам ...", "2. Сядешь есть первый, ..."]


def get_reply9() -> list[str]:
    return ["проявить инициативу", "отсидеться в сторонке"]


def get_reply10() -> list[str]:
    return ["1. Брррр! Это было страшно, ...",
            "2. Страшные истории ты не послушал..."]


def get_reply11() -> list[str]:
    return ["да", "нет"]


def on_start_astra_branch(user_id: int, users: UsersData) -> list[ResponseData]:
    users.set_student_team(user_id, "astra")

    return [ResponseData(user_id,
                         has_text=True,
                         text='Самым первым женским педагогическим отрядом в Свердловской области, базирующимся на '
                              'радиотехническом факультете УрФУ, является СПО" Астра". Отряд появился 19 декабря 1981 '
                              'года и существует по сей день.'),
            ResponseData(user_id,
                         has_text=True,
                         text='Тебе стало интересно, в честь чего отряд получил такое название?',
                         has_keyboard=True,
                         keyboard_items=get_reply6())]


def count_score_and_send_result(user_id: int, users: UsersData) -> list[ResponseData]:
    if users.get_astra_state(user_id) >= 3:
        return [ResponseData(user_id,
                             has_text=True,
                             text='Так и прошла целая смена. Она была очень интересная и насыщенная событиями. '
                                  'Ты получил много впечатлений и опыта, заветную целинку и стал настоящим бойцом!')]
    else:
        return [ResponseData(user_id,
                             has_text=True,
                             text='На смене ты был, но мало времени уделял своему отряду и ничего полезного не делал. '
                                  'Тебя не наградили целинкой.')]


def run(user_id: int, request: str, users: UsersData) -> list[ResponseData]:
    # --------------------Если это не соообщение, а начало общения -------------
    if users.get_student_team(user_id) == "ns":
        return on_start_astra_branch(user_id, users)

    # --------------------- Логика ответа на сообщения ------------------------
    if request == 'Цветок':
        return [ResponseData(user_id,
                             has_text=True,
                             text='Бутон цветка Астра действительно похож на звезду, но ты читаешь дальше и понимаешь, '
                                  'что свое название студотряд получил в честь греческого слова aster - звезда. '
                                  'Командиром отряда стала Золотурина Екатерина, а комиссаром - Хренова Елена. Девиз '
                                  'отряда: Per aspera ad ASTRA - Сквозь тернии к звездам.'),
                ResponseData(user_id,
                             has_text=True,
                             text='Хей! - тебя окликнула одногруппница Катя. - Наконец-то закончился семестр, '
                                  'можно съездить на целину. Ты со мной?',
                             has_keyboard=True,
                             keyboard_items=get_reply11())]
    if request == 'Женское имя':
        return [ResponseData(user_id,
                             has_text=True,
                             text='Женское имя Астра прекрасно, как и студентки данного отряда, но ты читаешь дальше и '
                                  'понимаешь, что свое название студотряд получил в честь греческого слова aster - звезда. '
                                  'Командиром отряда стала Золотурина Екатерина, а комиссаром - Хренова Елена. Девиз отряда: '
                                  'Per aspera ad ASTRA - Сквозь тернии к звездам.'),
                ResponseData(user_id,
                             has_text=True,
                             text='Хей! - тебя окликнула одногруппница Катя. - Наконец-то закончился семестр, можно съездить '
                                  'на целину. Ты со мной?',
                             has_keyboard=True,
                             keyboard_items=get_reply11())]
    if request == 'Звезда в греческом языке':
        users.inc_astra_state(user_id, 1)
        return [ResponseData(user_id,
                             has_text=True,
                             text='Ты читаешь дальше. Действительно, свое название студотряд получил в честь греческого слова '
                                  'aster - звезда. Командиром отряда стала Золотурина Екатерина, а комиссаром - Хренова Елена. '
                                  'Девиз отряда: Per aspera ad ASTRA - Сквозь тернии к звездам.'),
                ResponseData(user_id,
                             has_text=True,
                             text='Хей! - тебя окликнула одногруппница Катя. - Наконец-то закончился семестр, можно съездить '
                                  'на целину. Ты со мной?',
                             has_keyboard=True,
                             keyboard_items=get_reply11())]
    if request == 'да':
        return [ResponseData(user_id,
                             has_text=True,
                             text='Ты решаешь, что поездка на целину хороший способ немного подзаработать и соглашаешься.'),
                ResponseData(user_id,
                             has_text=True,
                             text='Ты едешь на электричке с ребятами на целину. Вам очень весело! Все примеряют свои новые '
                                  'целинки (зеленые курточки, которые выдают в студотрядах) Ты замечаешь, что ребята '
                                  'собираются в группу, чтобы петь песни под гитару и рассказывать дорожные байки. '
                                  'Присоединишься к ним или ляжешь спать?',
                             has_keyboard=True,
                             keyboard_items=get_reply4())]
    if request == 'Присоединиться к ребятам':
        return [ResponseData(user_id,
                             has_text=True,
                             text='Ты присоединился к ребятам и вы всю дорогу пели песни, от "Как здорово, что все мы здесь '
                                  'сегодня собрались" Олега Митяева до "Катюши" Блантера. В процессе ты завел новые знакомства '
                                  'и стал еще ближе с соотрядниками.'),
                ResponseData(user_id,
                             has_text=True,
                             text='Вы всем отрядом приехали в ДОЛ "Мечта" в городе Ревда. Вас распределили вожатыми в отряды с '
                                  'пионерами. Впереди ждет интересная смена. Скоро лагерное творческое мероприятие, '
                                  'надо придумать с отрядом название и кричалку.'
                                  '\n1. Потратишь время и подойдешь к вопросу творчески'
                                  '\n2. Сделаешь все быстро и не особо креативно',
                             has_keyboard=True,
                             keyboard_items=get_reply7())]
    if request == 'Лечь спать':
        return [ResponseData(user_id,
                             has_text=True,
                             text='Вы всем отрядом приехали в ДОЛ "Мечта" в городе Ревда. Вас распределили вожатыми в отряды с '
                                  'пионерами. Впереди ждет интересная смена. Скоро лагерное творческое мероприятие, '
                                  'надо придумать с отрядом название и кричалку.',
                             has_keyboard=True,
                             keyboard_items=get_reply7())]
    if request == '2. Сделаешь все быстро ...':
        return [ResponseData(user_id,
                             has_text=True,
                             text='Вы решили не проявлять креатив, придумали обычное название и дали ребятам свободное время'),
                ResponseData(user_id,
                             has_text=True,
                             text='Настало время обеда. Последний раз вы ели в электричке и тебе не терпится поесть. Однако '
                                  'соотрядники ещё накрывают на стол.',
                             has_keyboard=True,
                             keyboard_items=get_reply8())]
    if request == '1. Потратишь время ...':
        users.inc_astra_state(user_id, 1)
        return [ResponseData(user_id,
                             has_text=True,
                             text='Вы хорошо постарались, придумали с ребятами интересное название и запоминающуюся кричалку и '
                                  'вас заметили старшие'),
                ResponseData(user_id,
                             has_text=True,
                             text='Настало время обеда. Последний раз вы ели в электричке и тебе не терпится поесть. Однако '
                                  'соотрядники ещё накрывают на стол.'
                                  '\n1. Поможешь ребятам раздать порции еды'
                                  '\n2. Сядешь есть первый, не обращая внимания на других',
                             has_keyboard=True,
                             keyboard_items=get_reply8())]
    if request == '1. Поможешь ребятам ...':
        users.inc_astra_state(user_id, 1)
        return [ResponseData(user_id,
                             has_text=True,
                             text='Отлично! Никто не остался без обеда. Тебя поблагодарили за помощь.'),
                ResponseData(user_id,
                             has_text=True,
                             text='Физкульт-привет! Пришло время спортивного мероприятия. Ты уже немного устал и думаешь, '
                                  'помочь своему отряду или они смогут справиться сами?',
                             has_keyboard=True,
                             keyboard_items=get_reply9())]
    if request == '2. Сядешь есть первый, ...':
        return [ResponseData(user_id,
                             has_text=True,
                             text='Ребятам не очень понравилось, что вы никак не помогли((('),
                ResponseData(user_id,
                             has_text=True,
                             text='Физкульт-привет! Пришло время спортивного мероприятия. Ты уже немного устал и думаешь, '
                                  'помочь своему отряду или они смогут справиться сами?',
                             has_keyboard=True,
                             keyboard_items=get_reply9())]
    if request == 'проявить инициативу':
        users.inc_astra_state(user_id, 1)
        return [ResponseData(user_id,
                             has_text=True,
                             text='Браво! Ваш отряд взял первое место! Так держать!'),
                ResponseData(user_id,
                             has_text=True,
                             text='Вечер - время собраться у костра, обсудить итоги дня и рассказать страшные лагерные байки. '
                                  'Примешь участие в разговоре?'
                                  '\n1. Брррр! Это было страшно, но захватывающе! День был насыщенным и интересным.'
                                  '\n2. Страшные истории ты не послушал, ну и ладно, зато уснешь быстрее всех :)',
                             has_keyboard=True,
                             keyboard_items=get_reply10())]
    if request == 'отсидеться в сторонке':
        return [ResponseData(user_id,
                             has_text=True,
                             text='Твоему отряду не удалось вырваться вперед.'),
                ResponseData(user_id,
                             has_text=True,
                             text='Вечер - время собраться у костра, обсудить итоги дня и рассказать страшные лагерные байки. '
                                  'Примешь участие в разговоре?'
                                  '\n1. Брррр! Это было страшно, но захватывающе! День был насыщенным и интересным.'
                                  '\n2. Страшные истории ты не послушал, ну и ладно, зато уснешь быстрее всех :)',
                             has_keyboard=True,
                             keyboard_items=get_reply10())]
    if request == 'нет':
        # TODO
        # users.set_student_team(user_id, "ns")
        return [ResponseData(user_id,
                             has_text=True,
                             text='Ты решаешь, что не хочешь проводить жаркое лето на целине, прощаешься с Катей и продолжаешь '
                                  'прогулку по коридорам любимого института.')] + app.quest.main_story(user_id, "Поехали", users)
    if request == '1. Брррр! Это было страшно, ...':
        users.inc_astra_state(user_id, 1)
        return count_score_and_send_result(user_id, users)
    if request == '2. Страшные истории ты не послушал...':
        return count_score_and_send_result(user_id, users)
    return [ResponseData(user_id, has_text=True, text='Команда не реализована', do_not_change_keyboard=True)]
