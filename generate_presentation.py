import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def create_presentation():
    prs = Presentation()
    # 16:9 widescreen format
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    # Theme colors
    BG_DARK = RGBColor(10, 22, 40)        # Deep Navy #0A1628
    BG_CARD = RGBColor(18, 35, 60)       # Card Navy #12233C
    ACCENT_GOLD = RGBColor(212, 168, 67)  # Gold #D4A843
    ACCENT_TEAL = RGBColor(26, 138, 138)  # Teal #1A8A8A
    TEXT_LIGHT = RGBColor(245, 247, 250) # Light Gray/White
    TEXT_MUTED = RGBColor(170, 185, 205) # Muted Text
    WHITE = RGBColor(255, 255, 255)

    blank_layout = prs.slide_layouts[6]

    def add_bg(slide, color=BG_DARK):
        background = slide.background
        fill = background.fill
        fill.solid()
        fill.fore_color.rgb = color

    def add_header(slide, title_text, category_text="БИЗНЕС-МОДЕЛЬ «СИНТАКСИС»"):
        # Category Eyebrow
        cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.5), Inches(11.7), Inches(0.4))
        tf_cat = cat_box.text_frame
        tf_cat.word_wrap = True
        p_cat = tf_cat.paragraphs[0]
        p_cat.text = category_text.upper()
        p_cat.font.size = Pt(11)
        p_cat.font.bold = True
        p_cat.font.color.rgb = ACCENT_GOLD
        p_cat.font.name = 'Arial'

        # Main Title
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.85), Inches(11.7), Inches(0.8))
        tf_title = title_box.text_frame
        tf_title.word_wrap = True
        p_title = tf_title.paragraphs[0]
        p_title.text = title_text
        p_title.font.size = Pt(26)
        p_title.font.bold = True
        p_title.font.color.rgb = WHITE
        p_title.font.name = 'Arial'

    def add_card(slide, left, top, width, height, bg_color=BG_CARD):
        shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, width, height)
        shape.fill.solid()
        shape.fill.fore_color.rgb = bg_color
        shape.line.color.rgb = RGBColor(35, 60, 95)
        shape.line.width = Pt(1)
        return shape

    # ------------------ SLIDE 1: TITLE ------------------
    slide1 = prs.slides.add_slide(blank_layout)
    add_bg(slide1, BG_DARK)

    # Decorative accent card
    add_card(slide1, Inches(1.0), Inches(1.2), Inches(11.333), Inches(5.1), BG_CARD)

    tb = slide1.shapes.add_textbox(Inches(1.5), Inches(1.6), Inches(10.333), Inches(4.3))
    tf = tb.text_frame
    tf.word_wrap = True

    p = tf.paragraphs[0]
    p.text = "КГКП «Жезказганский высший политехнический колледж»"
    p.font.size = Pt(14)
    p.font.color.rgb = ACCENT_GOLD
    p.font.bold = True

    p2 = tf.add_paragraph()
    p2.text = "Специальность: Программное обеспечение"
    p2.font.size = Pt(14)
    p2.font.color.rgb = TEXT_MUTED
    p2.space_after = Pt(20)

    p3 = tf.add_paragraph()
    p3.text = "Бизнес-модель «Онлайн-школа по программированию Синтаксис»"
    p3.font.size = Pt(30)
    p3.font.bold = True
    p3.font.color.rgb = WHITE
    p3.space_after = Pt(30)

    p4 = tf.add_paragraph()
    p4.text = "Выполнили студенты группы ПО-32:\nЦерр Данил, Деревянко Илья, Захарко Ильяс, Рахимбаева Назгуль"
    p4.font.size = Pt(14)
    p4.font.color.rgb = TEXT_LIGHT
    p4.space_after = Pt(15)

    p5 = tf.add_paragraph()
    p5.text = "Проверила: преподаватель Айтжанова А. А.\nЖезказган — 2026"
    p5.font.size = Pt(13)
    p5.font.color.rgb = ACCENT_TEAL


    # ------------------ SLIDE 2: KEY VALUES ------------------
    slide2 = prs.slides.add_slide(blank_layout)
    add_bg(slide2)
    add_header(slide2, "Ключевые ценности проекта")

    values = [
        ("💳 Гибкая система оплаты", "Ежемесячная или разовая подписка, делающая обучение доступным и удобным для семей с любым бюджетом."),
        ("🔍 Полная прозрачность", "Открытый доступ к материалам, четкие критерии оценки и регулярный контроль прогресса."),
        ("🤝 Комфортная среда", "Создание дружелюбных условий, поддерживающих мотивацию и вовлеченность каждого ученика."),
        ("🏆 Практика & Хакатоны", "Мотивация студентов проверять полученные навыки на реальных командных хакатонах и соревнованиях."),
        ("📜 Подлинные сертификаты", "Выдача персонального сертификата с верификацией подлинности через QR-код.")
    ]

    top_pos = 1.8
    for title, desc in values:
        add_card(slide2, Inches(0.8), Inches(top_pos), Inches(11.733), Inches(0.9))
        tb = slide2.shapes.add_textbox(Inches(1.0), Inches(top_pos + 0.1), Inches(11.333), Inches(0.7))
        tf = tb.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(16)
        p.font.bold = True
        p.font.color.rgb = ACCENT_GOLD

        p2 = tf.add_paragraph()
        p2.text = desc
        p2.font.size = Pt(13)
        p2.font.color.rgb = TEXT_LIGHT

        top_pos += 1.05


    # ------------------ SLIDE 3: CUSTOMER SEGMENTS ------------------
    slide3 = prs.slides.add_slide(blank_layout)
    add_bg(slide3)
    add_header(slide3, "Сегменты потребителей")

    # Card 1: Start
    add_card(slide3, Inches(0.8), Inches(1.8), Inches(5.7), Inches(5.0))
    tb1 = slide3.shapes.add_textbox(Inches(1.1), Inches(2.1), Inches(5.1), Inches(4.4))
    tf1 = tb1.text_frame
    tf1.word_wrap = True

    p = tf1.paragraphs[0]
    p.text = "🎯 На старте проекта"
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = ACCENT_GOLD
    p.space_after = Pt(14)

    items1 = [
        ("Дети и подростки (10–18 лет)", "Основная целевая аудитория, желающая освоить программирование, веб-разработку и IT-навыки."),
        ("Родители учеников", "Лица, принимающие решение и оплачивающие обучение. Заинтересованы в полезном досуге и перспективной профессии для ребенка.")
    ]
    for subtitle, text in items1:
        p_s = tf1.add_paragraph()
        p_s.text = f"• {subtitle}"
        p_s.font.size = Pt(15)
        p_s.font.bold = True
        p_s.font.color.rgb = WHITE

        p_t = tf1.add_paragraph()
        p_t.text = text
        p_t.font.size = Pt(13)
        p_t.font.color.rgb = TEXT_MUTED
        p_t.space_after = Pt(12)

    # Card 2: Scaling
    add_card(slide3, Inches(6.833), Inches(1.8), Inches(5.7), Inches(5.0))
    tb2 = slide3.shapes.add_textbox(Inches(7.133), Inches(2.1), Inches(5.1), Inches(4.4))
    tf2 = tb2.text_frame
    tf2.word_wrap = True

    p = tf2.paragraphs[0]
    p.text = "🚀 Стратегия масштабирования"
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = ACCENT_TEAL
    p.space_after = Pt(14)

    items2 = [
        ("Взрослая аудитория", "Люди, стремящиеся сменить специальность и войти в IT-сферу с нуля."),
        ("Работа с ИИ (AI Literacy)", "Курсы по грамотному применению искусственного интеллекта и нейросетей в профессиональной деятельности.")
    ]
    for subtitle, text in items2:
        p_s = tf2.add_paragraph()
        p_s.text = f"• {subtitle}"
        p_s.font.size = Pt(15)
        p_s.font.bold = True
        p_s.font.color.rgb = WHITE

        p_t = tf2.add_paragraph()
        p_t.text = text
        p_t.font.size = Pt(13)
        p_t.font.color.rgb = TEXT_MUTED
        p_t.space_after = Pt(12)


    # ------------------ SLIDE 4: CHANNELS & RELATIONS ------------------
    slide4 = prs.slides.add_slide(blank_layout)
    add_bg(slide4)
    add_header(slide4, "Каналы взаимодействия и Отношения с клиентами")

    add_card(slide4, Inches(0.8), Inches(1.8), Inches(5.7), Inches(5.0))
    tb1 = slide4.shapes.add_textbox(Inches(1.1), Inches(2.1), Inches(5.1), Inches(4.4))
    tf1 = tb1.text_frame
    tf1.word_wrap = True

    p = tf1.paragraphs[0]
    p.text = "📢 Каналы взаимодействия"
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = ACCENT_GOLD
    p.space_after = Pt(14)

    channels = [
        ("Социальные сети & Сообщества", "Instagram, Discord, YouTube, TikTok для охвата молодежи."),
        ("Партнерские сети", "Сотрудничество со школами и вузами Казахстана."),
        ("Офлайн-продвижение", "Работа промоутеров и распространение информационных материалов.")
    ]
    for title, desc in channels:
        p_s = tf1.add_paragraph()
        p_s.text = f"• {title}"
        p_s.font.size = Pt(15)
        p_s.font.bold = True
        p_s.font.color.rgb = WHITE

        p_t = tf1.add_paragraph()
        p_t.text = desc
        p_t.font.size = Pt(13)
        p_t.font.color.rgb = TEXT_MUTED
        p_t.space_after = Pt(10)

    add_card(slide4, Inches(6.833), Inches(1.8), Inches(5.7), Inches(5.0))
    tb2 = slide4.shapes.add_textbox(Inches(7.133), Inches(2.1), Inches(5.1), Inches(4.4))
    tf2 = tb2.text_frame
    tf2.word_wrap = True

    p = tf2.paragraphs[0]
    p.text = "🤝 Отношения с клиентами"
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = ACCENT_TEAL
    p.space_after = Pt(14)

    relations = [
        ("Геймификация и интерактив", "Вовлечение и удержание внимания детей через интерактивный формат."),
        ("Отчетность для родителей", "Ежемесячные отчеты об успеваемости и личном прогрессе каждого ребенка."),
        ("Контроль и дисциплина", "Доступ к следующему месяцу открывается только после оплаты — дисциплинирует учеников и снижает отвал.")
    ]
    for title, desc in relations:
        p_s = tf2.add_paragraph()
        p_s.text = f"• {title}"
        p_s.font.size = Pt(15)
        p_s.font.bold = True
        p_s.font.color.rgb = WHITE

        p_t = tf2.add_paragraph()
        p_t.text = desc
        p_t.font.size = Pt(13)
        p_t.font.color.rgb = TEXT_MUTED
        p_t.space_after = Pt(10)


    # ------------------ SLIDE 5: REVENUE STREAMS ------------------
    slide5 = prs.slides.add_slide(blank_layout)
    add_bg(slide5)
    add_header(slide5, "Потоки доходов и Направления обучения")

    courses = [
        ("Front-End Junior", "23 000 ₸ / мес", "Длительность: 4 месяца", "Основы HTML, CSS, JavaScript, верстка современных сайтов и интерактивных интерфейсов."),
        ("UI/UX Дизайн", "19 000 ₸ / мес", "Длительность: 4 месяца", "Проектирование пользовательских интерфейсов, работа в Figma, проведение UX-исследований."),
        ("Основы Python", "27 000 ₸ / мес", "Длительность: 5 месяцев", "Базовое программирование, алгоритмы, работа с данными и создание консольных/веб-приложений.")
    ]

    for i, (c_name, c_price, c_dur, c_desc) in enumerate(courses):
        left_val = Inches(0.8 + i * 4.0)
        add_card(slide5, left_val, Inches(1.8), Inches(3.733), Inches(4.2))

        tb = slide5.shapes.add_textbox(left_val + Inches(0.2), Inches(2.0), Inches(3.333), Inches(3.8))
        tf = tb.text_frame
        tf.word_wrap = True

        p1 = tf.paragraphs[0]
        p1.text = c_name
        p1.font.size = Pt(18)
        p1.font.bold = True
        p1.font.color.rgb = WHITE

        p2 = tf.add_paragraph()
        p2.text = c_price
        p2.font.size = Pt(20)
        p2.font.bold = True
        p2.font.color.rgb = ACCENT_GOLD
        p2.space_after = Pt(6)

        p3 = tf.add_paragraph()
        p3.text = c_dur
        p3.font.size = Pt(12)
        p3.font.color.rgb = ACCENT_TEAL
        p3.space_after = Pt(12)

        p4 = tf.add_paragraph()
        p4.text = c_desc
        p4.font.size = Pt(13)
        p4.font.color.rgb = TEXT_MUTED

    # Additional Stream
    add_card(slide5, Inches(0.8), Inches(6.15), Inches(11.733), Inches(0.8))
    tb_add = slide5.shapes.add_textbox(Inches(1.0), Inches(6.25), Inches(11.333), Inches(0.6))
    tf_add = tb_add.text_frame
    tf_add.word_wrap = True
    p_add = tf_add.paragraphs[0]
    p_add.text = "💡 Перспектива развития: Индивидуальное наставничество и VIP-форматы с выходом на взрослую аудиторию."
    p_add.font.size = Pt(14)
    p_add.font.bold = True
    p_add.font.color.rgb = ACCENT_GOLD


    # ------------------ SLIDE 6: RESOURCES & ACTIONS ------------------
    slide6 = prs.slides.add_slide(blank_layout)
    add_bg(slide6)
    add_header(slide6, "Ключевые ресурсы и Ключевые действия")

    add_card(slide6, Inches(0.8), Inches(1.8), Inches(5.7), Inches(5.0))
    tb1 = slide6.shapes.add_textbox(Inches(1.1), Inches(2.1), Inches(5.1), Inches(4.4))
    tf1 = tb1.text_frame
    tf1.word_wrap = True

    p = tf1.paragraphs[0]
    p.text = "🧩 Ключевые ресурсы"
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = ACCENT_GOLD
    p.space_after = Pt(14)

    resources = [
        ("Команда проекта", "3 куратора-преподавателя (ведут по 4 группы каждый) + 1 администратор."),
        ("Техническая база", "Официальный сайт, надежный хостинг и интерактивное веб-приложение."),
        ("Методическая база", "Уникальные авторские учебные программы с подходом 70% практики / 30% теории.")
    ]
    for title, desc in resources:
        p_s = tf1.add_paragraph()
        p_s.text = f"• {title}"
        p_s.font.size = Pt(15)
        p_s.font.bold = True
        p_s.font.color.rgb = WHITE

        p_t = tf1.add_paragraph()
        p_t.text = desc
        p_t.font.size = Pt(13)
        p_t.font.color.rgb = TEXT_MUTED
        p_t.space_after = Pt(10)

    add_card(slide6, Inches(6.833), Inches(1.8), Inches(5.7), Inches(5.0))
    tb2 = slide6.shapes.add_textbox(Inches(7.133), Inches(2.1), Inches(5.1), Inches(4.4))
    tf2 = tb2.text_frame
    tf2.word_wrap = True

    p = tf2.paragraphs[0]
    p.text = "⚙️ Ключевые действия"
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = ACCENT_TEAL
    p.space_after = Pt(14)

    actions = [
        ("Учебный процесс", "Проведение интерактивных онлайн-занятий и подробная проверка домашних заданий."),
        ("Техническое сопровождение", "Бесперебойная поддержка платформы и веб-сервисов."),
        ("Администрирование", "Контроль оплат, ведение базы учеников и регулярная подготовка отчетов для родителей.")
    ]
    for title, desc in actions:
        p_s = tf2.add_paragraph()
        p_s.text = f"• {title}"
        p_s.font.size = Pt(15)
        p_s.font.bold = True
        p_s.font.color.rgb = WHITE

        p_t = tf2.add_paragraph()
        p_t.text = desc
        p_t.font.size = Pt(13)
        p_t.font.color.rgb = TEXT_MUTED
        p_t.space_after = Pt(10)


    # ------------------ SLIDE 7: KEY PARTNERS ------------------
    slide7 = prs.slides.add_slide(blank_layout)
    add_bg(slide7)
    add_header(slide7, "Ключевые партнёры")

    partners = [
        ("💳 Финансы & Платежи", "Kaspi Bank", "Прием онлайн-платежей, удобный расчет для родителей через Kaspi Pay/QR."),
        ("🖥️ Инфраструктура", "Хостинг-провайдеры", "Обеспечение высокой доступности, быстрой загрузки и надежности веб-платформы."),
        ("🎓 Образование", "Школы и вузы РК", "Информационное сотрудничество, привлечение школьников и проведение совместных мероприятий."),
        ("📣 Маркетинг", "Рекламные площадки", "Эффективное продвижение, таргетированная реклама и работа локальных промоутеров.")
    ]

    positions = [(0.8, 1.8), (6.833, 1.8), (0.8, 4.4), (6.833, 4.4)]
    for (title, partner_name, desc), (l, t) in zip(partners, positions):
        add_card(slide7, Inches(l), Inches(t), Inches(5.7), Inches(2.3))
        tb = slide7.shapes.add_textbox(Inches(l + 0.3), Inches(t + 0.2), Inches(5.1), Inches(1.9))
        tf = tb.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(15)
        p.font.bold = True
        p.font.color.rgb = ACCENT_GOLD

        p2 = tf.add_paragraph()
        p2.text = partner_name
        p2.font.size = Pt(18)
        p2.font.bold = True
        p2.font.color.rgb = WHITE
        p2.space_after = Pt(4)

        p3 = tf.add_paragraph()
        p3.text = desc
        p3.font.size = Pt(13)
        p3.font.color.rgb = TEXT_MUTED


    # ------------------ SLIDE 8: EXPENSE STRUCTURE ------------------
    slide8 = prs.slides.add_slide(blank_layout)
    add_bg(slide8)
    add_header(slide8, "Структура расходов")

    # Monthly Costs Card
    add_card(slide8, Inches(0.8), Inches(1.8), Inches(5.7), Inches(5.0))
    tb1 = slide8.shapes.add_textbox(Inches(1.1), Inches(2.1), Inches(5.1), Inches(4.4))
    tf1 = tb1.text_frame
    tf1.word_wrap = True

    p = tf1.paragraphs[0]
    p.text = "📅 Ежемесячные затраты"
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = ACCENT_GOLD
    p.space_after = Pt(14)

    costs = [
        ("Зарплата кураторов (3 чел)", "750 000 ₸", "3 × 250 000 ₸ в месяц"),
        ("Зарплата администратора", "280 000 ₸", "1 специалист"),
        ("Хостинг и серверы", "20 000 ₸", "Поддержка веб-инфраструктуры"),
        ("Реклама и промоутеры", "120 000 ₸", "Ежемесячный маркетинговый бюджет")
    ]

    for name, val, sub in costs:
        p_s = tf1.add_paragraph()
        p_s.text = f"• {name}: {val}"
        p_s.font.size = Pt(15)
        p_s.font.bold = True
        p_s.font.color.rgb = WHITE

        p_t = tf1.add_paragraph()
        p_t.text = f"   ({sub})"
        p_t.font.size = Pt(12)
        p_t.font.color.rgb = TEXT_MUTED
        p_t.space_after = Pt(6)

    # Launch Costs & Summary Card
    add_card(slide8, Inches(6.833), Inches(1.8), Inches(5.7), Inches(5.0))
    tb2 = slide8.shapes.add_textbox(Inches(7.133), Inches(2.1), Inches(5.1), Inches(4.4))
    tf2 = tb2.text_frame
    tf2.word_wrap = True

    p = tf2.paragraphs[0]
    p.text = "⚡ Разовые расходы и Итого"
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = ACCENT_TEAL
    p.space_after = Pt(14)

    p_l1 = tf2.add_paragraph()
    p_l1.text = "• Первичная реклама и старт: 300 000 ₸"
    p_l1.font.size = Pt(15)
    p_l1.font.bold = True
    p_l1.font.color.rgb = WHITE

    p_l2 = tf2.add_paragraph()
    p_l2.text = "   Стартовый маркетинг для первого набора учеников."
    p_l2.font.size = Pt(12)
    p_l2.font.color.rgb = TEXT_MUTED
    p_l2.space_after = Pt(20)

    p_tot1 = tf2.add_paragraph()
    p_tot1.text = "Итого постоянные расходы:"
    p_tot1.font.size = Pt(14)
    p_tot1.font.color.rgb = TEXT_MUTED

    p_tot2 = tf2.add_paragraph()
    p_tot2.text = "1 170 000 ₸ / месяц"
    p_tot2.font.size = Pt(24)
    p_tot2.font.bold = True
    p_tot2.font.color.rgb = ACCENT_GOLD


    # ------------------ SLIDE 9: FINANCIAL RESULTS ------------------
    slide9 = prs.slides.add_slide(blank_layout)
    add_bg(slide9)
    add_header(slide9, "Финансовые результаты за 5 месяцев")

    # Top metrics row (3 cards)
    metrics = [
        ("144 → 115", "Студентов", "Плановый набор 144 места, с учетом 20% отвала фактически обучаются 115 человек"),
        ("11 649 000 ₸", "Общий доход", "Совокупный финансовый поток от подписок за 5 месяцев работы"),
        ("5 551 915 ₸", "Чистая прибыль", "С учетом всех расходов и налога ИП 4% с оборота (расходы: 6 097 085 ₸)")
    ]

    for i, (val, title, sub) in enumerate(metrics):
        left_val = Inches(0.8 + i * 4.0)
        add_card(slide9, left_val, Inches(1.8), Inches(3.733), Inches(2.2))
        tb = slide9.shapes.add_textbox(left_val + Inches(0.2), Inches(1.95), Inches(3.333), Inches(1.9))
        tf = tb.text_frame
        tf.word_wrap = True

        p1 = tf.paragraphs[0]
        p1.text = val
        p1.font.size = Pt(24)
        p1.font.bold = True
        p1.font.color.rgb = ACCENT_GOLD

        p2 = tf.add_paragraph()
        p2.text = title
        p2.font.size = Pt(16)
        p2.font.bold = True
        p2.font.color.rgb = WHITE
        p2.space_after = Pt(4)

        p3 = tf.add_paragraph()
        p3.text = sub
        p3.font.size = Pt(11)
        p3.font.color.rgb = TEXT_MUTED

    # Bottom Cards: Payback & Capital
    add_card(slide9, Inches(0.8), Inches(4.3), Inches(5.7), Inches(2.5))
    tb_pb = slide9.shapes.add_textbox(Inches(1.1), Inches(4.5), Inches(5.1), Inches(2.1))
    tf_pb = tb_pb.text_frame
    tf_pb.word_wrap = True

    p = tf_pb.paragraphs[0]
    p.text = "⚡ Высокая окупаемость"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = ACCENT_TEAL
    p.space_after = Pt(6)

    p_pb_desc = tf_pb.add_paragraph()
    p_pb_desc.text = "Проект самоокупаем с первого месяца!\nДоход 1-го месяца составляет 2,6 млн ₸, что полностью покрывает расходы и приносит >1,1 млн ₸ чистой прибыли."
    p_pb_desc.font.size = Pt(13)
    p_pb_desc.font.color.rgb = TEXT_LIGHT

    add_card(slide9, Inches(6.833), Inches(4.3), Inches(5.7), Inches(2.5))
    tb_cap = slide9.shapes.add_textbox(Inches(7.133), Inches(4.5), Inches(5.1), Inches(2.1))
    tf_cap = tb_cap.text_frame
    tf_cap.word_wrap = True

    p = tf_cap.paragraphs[0]
    p.text = "💼 Стартовый капитал"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = ACCENT_GOLD
    p.space_after = Pt(6)

    p_cap_desc = tf_cap.add_paragraph()
    p_cap_desc.text = "Для запуска не требуется привлекать заемные средства или кредиты.\nСтартовый капитал в размере 1 500 000 ₸ формируется команда самостоятельно."
    p_cap_desc.font.size = Pt(13)
    p_cap_desc.font.color.rgb = TEXT_LIGHT


    # ------------------ SLIDE 10: CONCLUSION ------------------
    slide10 = prs.slides.add_slide(blank_layout)
    add_bg(slide10)
    add_header(slide10, "Заключение и Перспективы")

    add_card(slide10, Inches(1.0), Inches(1.8), Inches(11.333), Inches(4.8), BG_CARD)
    tb = slide10.shapes.add_textbox(Inches(1.4), Inches(2.2), Inches(10.533), Inches(4.0))
    tf = tb.text_frame
    tf.word_wrap = True

    p1 = tf.paragraphs[0]
    p1.text = "📌 Главный итог"
    p1.font.size = Pt(22)
    p1.font.bold = True
    p1.font.color.rgb = ACCENT_GOLD
    p1.space_after = Pt(10)

    p2 = tf.add_paragraph()
    p2.text = "Начав с аудитории 10–18 лет и заручившись поддержкой школ и вузов Казахстана, мы создаем прочный фундамент для последующего выхода на рынок взрослого образования и обучения практической работе с искусственным интеллектом."
    p2.font.size = Pt(16)
    p2.font.color.rgb = TEXT_LIGHT
    p2.space_after = Pt(24)

    p3 = tf.add_paragraph()
    p3.text = "Спасибо за внимание!"
    p3.font.size = Pt(32)
    p3.font.bold = True
    p3.font.color.rgb = ACCENT_TEAL
    p3.alignment = PP_ALIGN.CENTER

    prs.save("презентация_синтаксис.pptx")
    print("Successfully generated презентация_синтаксис.pptx")

if __name__ == '__main__':
    create_presentation()
