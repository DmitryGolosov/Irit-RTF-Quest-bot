from app.responseData import ResponseData
from app.database.usersDatabase import UsersData
from app.branches.firstBranch import firstBranch


def get_reply2() -> list[str]:
    return ["1. Ёмкое, красивое название ...", "2. Отражало принадлежность ..."]


def get_reply3() -> list[str]:
    return ["Да", "Нет"]


def get_reply4() -> list[str]:
    return ["Присоединиться к ребятам", "Лечь спать"]


def get_reply5() -> list[str]:
    return ["Каменщик", "Стропольщик", "Бетонщик"]


def on_start_impuls_branch(user_id: int, users: UsersData) -> list[ResponseData]:
    users.set_student_team(user_id, "impuls")
    return [ResponseData(user_id,
                         has_text=True,
                         text='Очень давно, когда наш любимый радиотехнический институт был лишь факультетом, был создан '
                     'студенческий строительный отряд "Импульс" - самый первый в Свердловской области отряд, '
                     'прославленный по всей стране. Создали отряд 12 апреля 1964 года и до сегодняшних дней он '
                     'продолжает свою деятельность. Первые отряды сформировали из лучших студентов радиотехнического, '
                     'механико-машиностроительного и физико-технического факультетов. На радиотехническом факультете '
                     'сформировали три отряда: с первого курса - РТ-1, со второго - РТ-2 и с третьего - РТ-3.'),
            ResponseData(user_id,
                         has_text=True,
                         text='Тебя хлопают по плечу. Ты оборачиваешься и видишь своего одногруппника Пашу. \n- Привет! '
                     'Выбираешь студотряд? Я состою в ССО ИМПУЛЬС. Я много читал про него. Как думаешь, почему отряд '
                     'получил именно такое название?\n'
                              '1. Ёмкое, красивое название, легко запомнить'
                              '\n2. Отражало принадлежность к радиотехническому факультету',
                         has_keyboard=True,
                         keyboard_items=get_reply2())]

def run(user_id: int, request: str, users: UsersData) -> list[ResponseData]:
    # --------------------Если это не соообщение, а начало общения -------------
    if users.get_student_team(user_id) == "ns":
        return on_start_impuls_branch(user_id, users)

    # --------------------- Логика ответа на сообщения ------------------------
    if request == '1. Ёмкое, красивое название ...':
        return [ResponseData(user_id, has_text=True,
                             text='Название "Импульс" действительно красивое и простое, но основной причиной стало '
                                  'отражение принадлежности к радиотехническому факультету'),
                ResponseData(user_id, has_text=True,
                             text='Каждое лето мы работаем, - говорит Паша, - ездим на целину и зарабатываем. Первая '
                                  'Целина ССО "Импульс" прошла в Казахстане (Актюбинская область, Карабулатский район, '
                                  'совхоз им. ХХII партсъезда). Первый командир – Каменев Виктор, первый комиссар – '
                                  'Слепеньков Анатолий. - Ну что, поедем на целину?',
                             has_keyboard=True,
                             keyboard_items=get_reply3())]
    if request == '2. Отражало принадлежность ...':
        return [ResponseData(user_id, has_text=True,
                             text='- Всё верно! Ребятам хотелось, чтобы в названии отражалась принадлежность отряда к '
                                  'радиотехническому факультету, поэтому уже в поезде первокурсники придумали отряду '
                                  'простое и красивое название "Импульс"'),
                ResponseData(user_id, has_text=True,
                             text='Каждое лето мы работаем, - говорит Паша, - ездим на целину и зарабатываем. Первая '
                                  'Целина ССО "Импульс" прошла в Казахстане (Актюбинская область, Карабулатский район, '
                                  'совхоз им. ХХII партсъезда). Первый командир – Каменев Виктор, первый комиссар – '
                                  'Слепеньков Анатолий. - Ну что, поедем на целину?', has_keyboard=True,
                             keyboard_items=get_reply3())]
    if request == "Да":
        return [ResponseData(user_id, has_text=True,
                             text='Ты решаешь, что поездка на целину хороший способ немного подзаработать и соглашаешься.'),
                ResponseData(user_id, has_image=True,
                             images_path=["C:/Users/ДМИТРИЙ/PycharmProjects/Quest/app/Использованные/Импульс2.jpg"]),
                ResponseData(user_id, has_text=True,
                             text="Ты едешь на поезде с ребятами на целину. В поезде очень весело! Все примеряют свои "
                                  "новые целинки (зеленые курточки, которые выдают в студотрядах) Ты замечаешь, что "
                                  "ребята собираются в группу, чтобы петь песни под гитару и рассказывать дорожные байки. "
                                  "Присоединишься к ним или ляжешь спать?",
                             has_keyboard=True,
                             keyboard_items=get_reply4())]
    if request == "Нет":
        users.set_student_team(user_id, "ns")
        return [ResponseData(user_id, has_text=True,
                             text="Ты решаешь, что не хочешь проводить жаркое лето на целине, прощаешься с Пашей и "
                                  "продолжаешь прогулку по коридорам любимого института.")] \
            + firstBranch.run(user_id, "Студотряды", users)
    
    if request == 'Присоединиться к ребятам':
        return [ResponseData(user_id, has_text=True,
                             text='Ты присоединился к ребятам и вы всю ночь пели песни от "Как здорово, что все мы '
                                  'здесь сегодня собрались" Олега Митяева до "Катюши" Блантера.В процессе ты завел новые '
                                  'знакомства и стал еще ближе с соотрядниками.'),
                ResponseData(user_id, has_image=True,
                             images_path=["C:/Users/ДМИТРИЙ/PycharmProjects/Quest/app/Использованные/Импульс.jpg"]),
                ResponseData(user_id, has_text=True,
                             text='Вы сходите с поезда в совхозе Горьговской области и готовитесь к работе. Тут можно '
                                  'освоить профессию каменщика, стропальщика, бетонщика. А работы здесь... От уборки '
                                  'строительного мусора, кладки стен, установки перекрытий, кровли крыши до монтажа и '
                                  'установки камер наружного наблюдения. А если упорно обучаться всю смену одной из '
                                  'профессий, то можно и диплом по этой специальности получить. Что выберешь?',
                             has_keyboard=True,
                             keyboard_items=get_reply5())]
    if request == 'Каменщик' or request == 'Стропольщик' or request == 'Бетонщик':
        return [ResponseData(user_id, has_text=True,
                             text="После долгого рабочего дня вы все вместе собрались в старой школе, которую выделили "
                                  "вашему стройотряду как место проживания. Каждый вечер вас оценивали и выставляли КТУ "
                                  "(коэффициент трудового участия)."),
                ResponseData(user_id, has_text=True,
                             text="И так проходит каждый рабочий день всю смену. Если работаешь хорошо и отлично, то "
                                  "получаешь значки на целинку, приличную зарплату и по возможности диплом по освоенной "
                                  "специальности.")]

    return [ResponseData(user_id,
                         has_text=True,
                         text='Команда не реализована', do_not_change_keyboard=True)]