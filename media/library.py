class Photo:
    def __init__(self):
        self.widgets()

    def widgets(self):
        self.staff_msg = None
        self.staff_tok =  "AgACAgIAAxkBAAII_2Q3ahYR7vH-OJmJPMwGRGkvO9s7AAJYwTEbXOvASYZ6VSb3vCf3AQADAgADcwADLwQ"

        self.text1_msg = None
        self.text1_tok = "AgACAgIAAxkBAAIEXmQ12ifAFCnHQj0USn57jELbfjIPAALayjEbWnawST3JfIrPSO6EAQADAgADcwADLwQ"

        self.text2_msg = None
        self.text2_tok = "AgACAgIAAxkBAAIEYGQ12nKDcW6qxM2brJVhhOqnqbLLAALbyjEbWnawSZENN-GXy-T0AQADAgADcwADLwQ"

        self.test1_msg = None
        self.test1_tok = "AgACAgIAAxkBAAIEYmQ12rRm6TfNHkiVbWnIutc0XXAFAALcyjEbWnawSTAygpOKK1hMAQADAgADcwADLwQ"

        self.test2_msg = None
        self.test2_tok = "AgACAgIAAxkBAAIEZGQ12ytXaWwXEWlXgOctgdchLzV1AALdyjEbWnawSYE5fINmEUtAAQADAgADcwADLwQ"

        self.test3_msg = None
        self.test3_tok = "AgACAgIAAxkBAAIEZmQ127ydFeE3r8oDTEiqyX7v2RDEAALeyjEbWnawSS9H1fiTxUxVAQADAgADcwADLwQ"

        self.about_msg = None
        self.about_tok = "AgACAgIAAxkBAAIEaGQ12_8drQh1vTQ2ybDPlKjFm7MOAALfyjEbWnawSXYX_FL1y6Y5AQADAgADcwADLwQ"

        self.product_msg = None
        self.product_tok = "AgACAgIAAxkBAAIEamQ13DEmEzeAaAS-avvqPyaxXRC-AALgyjEbWnawSSxmN4-yfAT1AQADAgADcwADLwQ"

        self.link_msg = None
        self.link_tok = "AgACAgIAAxkBAAIEbGQ13FE9eYqFwQ8V5Sq7zYA-rpfpAALhyjEbWnawSWvu0v95eBDUAQADAgADcwADLwQ"

        self.faq_msg = None
        self.faq_tok = "AgACAgIAAxkBAAIEbmQ13dvUCyGy8CsfUfjULIoKOCoGAALmyjEbWnawSb8sCpH76q96AQADAgADcwADLwQ"


class Text:
    def __init__(self):
        self.text1_t = f'''Добро пожаловать в наш уникальный IT офис, который создан
для вдохновения и максимальной продуктивности наших сотрудников!
Наш офис расположен в современном здании с большими окнами, которые 
позволяют естественному свету проникать в помещение. Мы стремимся к 
экологичности, поэтому в нашем офисе используются энергоэффективные 
светодиодные лампы и система управления температурой помещения, что 
позволяет сэкономить энергию и создать комфортную атмосферу.

В нашем офисе есть несколько зон для работы и отдыха. У нас есть комнаты 
для проведения совещаний и обсуждения проектов, а также зоны отдыха и 
кухня с необходимым оборудованием для приготовления пищи и перекусов
'''
        self.text2_t = f'''Каждый новый сотрудник в “Smart Solutions” играет важную роль, потому что 
он может внести свой вклад в работу компании и помочь ей достичь своих 
целей. Вы – наш новый сотрудник можете иметь свежий взгляд на проблемы 
компании, предлагать новые идеи и подходы к их решению
Кроме того, вы можете внести свой вклад в командную работу и культуру 
компании. Вы можете помочь создать более продуктивную, креативную и 
дружественную атмосферу на рабочем месте.
'''
        self.video1_t = 'Тут видео'
        self.test1_t = f'''Вопрос: Каковы преимущества использования Agile методологии разработки
программного обеспечения в IT компаниях?
1. Увеличение затрат на разработку
2. Ускорение разработки и более частые релизы
3. Увеличение количества багов в итоговом продукте
4. Ограничение возможностей команды разработчиков
'''
        self.test2_t = f'''Как Зовут CEO компании?
1. Иванов Иван Иванович
2. Алексеев Олег Николаевич
3. Петров Федор Олегович
4. Иванов Дмитрий Владимирович
'''
        self.test3_t = f'''Какая из перечисленных задач НЕ относится к нашей компании?
1. разработка программного обеспечения
2. Разработка и поддержка веб-сайта компании
3. Создание мобильных приложений
4. Проведение бухгалтерского учета и составление отчетности
'''
        self.win_t = f'''Поздравляем с успешным прохождением теста!'''
        self.about_t = f'''"Smart Solutions" - это компания, специализирующаяся на предоставлении широкого 
спектра IT-услуг. Основана в 2010 году Александром Смирновым, который 
ранее работал в крупных IT-компаниях и имел богатый опыт в области разработки 
программного обеспечения и консалтинга.

За годы своей работы "Smart Solutions" стала одним из лидеров рынка IT-услуг 
благодаря своим инновационным решениям и высокому качеству работы. 
Компания имеет офисы в нескольких городах России и СНГ, 
а также зарубежные филиалы в Европе и Азии.

Продуктовая линейка "Smart Solutions" включает в себя различные IT-услуги, которые 
помогают бизнесу автоматизировать процессы и повышать эффективность работы. 
Компания предоставляет услуги по разработке программного обеспечения для разных 
платформ (Windows, iOS, Android), созданию веб-сайтов и интернет-магазинов, 
мобильных приложений, а также IT-консалтингу и SEO-оптимизации.

"Smart Solutions" предлагает своим клиентам индивидуальный подход к каждому 
проекту, а также высококвалифицированных специалистов, которые готовы помочь в 
решении любых задач. Компания работает с крупными корпоративными клиентами, а 
также с малым и средним бизнесом. 

"Smart Solutions" стремится к постоянному развитию и внедрению новых технологий, 
чтобы быть лучшей в своей области и помочь своим клиентам достичь успеха.
'''
        self.product_t = f'''Как ранее говорилось, что “Smart Solutions” уже не первый год на рынке и тут 
представлены наши примеры продуктов:
1. Платформа онлайн-курсов для изучения новых языков. Эта платформа 
предоставляет пользователям доступ к качественным курсам от 
опытных преподавателей со всего мира. Пользователи могут выбирать 
курсы по своим интересам и уровню подготовки, а также общаться с 
преподавателями и другими учениками через онлайн-чат и форумы.

2. Онлайн-сервис для планирования путешествий. Этот сервис позволяет 
пользователям создавать путеводители для своих путешествий, 
включая маршруты, бронирование гостиниц, билетов на транспорт и 
экскурсий. Пользователи также могут получать рекомендации и отзывы 
от других путешественников и делиться своими путеводителями с 
другими.

3. Платформа онлайн-обучения для улучшения здоровья и фитнеса. 
Эта платформа предоставляет пользователям доступ к различным 
программам тренировок и диет, а также персональным тренерам и 
диетологам. Пользователи могут отслеживать свой прогресс, 
обмениваться опытом с другими участниками и получать поддержку 
от сообщества.

Хотим заметить, что это лишь малая часть наших разработок и в данный момент мы 
продолжаем сотрудничать со многими нашими клиентами
'''



        self.link_t = f'''Наши официальные ссылки и контакты для связи сотрудников с компанией:
Номер телефона: +7 (123) 456 78 90  
Почта: smart@sol.ru
Telegram: t.me/smart/solutions
Группа Вконтакте: vc.com/smart24
'''
        self.faq_t = f'''Графики работы и расположения офисов:
1) г. Москва Пресненская наб., 8 стр 1б,  5 этаж:	(пн-пт) с 9:00 до 17:00 
2) г. Смоленск ул. Октябрьской Революции, д.9,к.8, 2 этаж (пн-пт) с 8:30 до 16:00

Основные методы адаптации новых сотрудников:
1 Организация ознакомительного тура. Проведение экскурсии по офису и 
представление новым сотрудникам основных процессов работы и политик 
компании.
2 Назначение наставника. Предоставление новым сотрудникам опытного 
наставника.
3 Проведение интеграционных мероприятий. Организация мероприятий, 
направленных на укрепление командного духа и сближение новых сотрудников с 
коллективом. 
'''


photo = Photo()
text = Text()
