import sys
try:
    from pptx import Presentation
    from pptx.util import Inches, Pt
    from pptx.dml.color import RGBColor
    from pptx.enum.text import PP_ALIGN
    from pptx.enum.shapes import MSO_SHAPE
except ModuleNotFoundError:
    print("\n[!] Ошибка: библиотека 'python-pptx' не установлена.")
    print("Пожалуйста, установите её с помощью команды в терминале / PowerShell:")
    print("    pip install python-pptx\n")
    sys.exit(1)

def create_presentation():
    prs = Presentation()
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
        cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(0.35))
        tf_cat = cat_box.text_frame
        tf_cat.word_wrap = True
        p_cat = tf_cat.paragraphs[0]
        p_cat.text = category_text.upper()
        p_cat.font.size = Pt(11)
        p_cat.font.bold = True
        p_cat.font.color.rgb = ACCENT_GOLD

        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.75), Inches(11.7), Inches(0.75))
        tf_title = title_box.text_frame
        tf_title.word_wrap = True
        p_title = tf_title.paragraphs[0]
        p_title.text = title_text
        p_title.font.size = Pt(24)
        p_title.font.bold = True
        p_title.font.color.rgb = WHITE

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
    add_card(slide1, Inches(1.0), Inches(1.0), Inches(11.333), Inches(5.5), BG_CARD)

    tb = slide1.shapes.add_textbox(Inches(1.5), Inches(1.3), Inches(10.333), Inches(4.9))
    tf = tb.text_frame
    tf.word_wrap = True

    p = tf.paragraphs[0]
    p.text = "Министерство просвещения РК | Управление образования области Улытау\nКГКП «Жезказганский высший политехнический колледж»"
    p.font.size = Pt(13)
    p.font.color.rgb = ACCENT_GOLD
    p.font.bold = True

    p2 = tf.add_paragraph()
    p2.text = "Специальность: Программное обеспечение"
    p2.font.size = Pt(13)
    p2.font.color.rgb = TEXT_MUTED
    p2.space_after = Pt(18)

    p3 = tf.add_paragraph()
    p3.text = "Бизнес модель «Онлайн школа по программированию-Синтаксис»"
    p3.font.size = Pt(28)
    p3.font.bold = True
    p3.font.color.rgb = WHITE
    p3.space_after = Pt(24)

    p4 = tf.add_paragraph()
    p4.text = "Выполнили: студенты группы ПО-32\nЦерр Данил, Деревянко Илья, Захарко Ильяс, Рахимбаева Назгуль"
    p4.font.size = Pt(14)
    p4.font.color.rgb = TEXT_LIGHT
    p4.space_after = Pt(14)

    p5 = tf.add_paragraph()
    p5.text = "Проверила: преподаватель Айтжанова А. А.\nЖезказган — 2026"
    p5.font.size = Pt(13)
    p5.font.color.rgb = ACCENT_TEAL


    # ------------------ SLIDE 2: KEY VALUES ------------------
    slide2 = prs.slides.add_slide(blank_layout)
    add_bg(slide2)
    add_header(slide2, "1. Ключевые ценности")

    values = [
        ("💳 Гибкая система оплаты", "В виде ежемесячной или разовой подписки."),
        ("🔍 Полная прозрачность обучения", "Честный подход без ложных обещаний «легкого программирования»."),
        ("💻 Акцент на практику", "Упор на практические навыки (70% практики / 30% теории) в программе."),
        ("🏆 Мотивация и Хакатоны", "Мотивация студентов проверять полученные знания в различных «Хакатонах»."),
        ("📜 Подлинные сертификаты", "Выдача официального документа об окончании с проверкой подлинности через QR-код.")
    ]

    top_pos = 1.6
    for title, desc in values:
        add_card(slide2, Inches(0.8), Inches(top_pos), Inches(11.733), Inches(0.95))
        tb = slide2.shapes.add_textbox(Inches(1.0), Inches(top_pos + 0.1), Inches(11.333), Inches(0.75))
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

        top_pos += 1.08


    # ------------------ SLIDE 3: CUSTOMER SEGMENTS ------------------
    slide3 = prs.slides.add_slide(blank_layout)
    add_bg(slide3)
    add_header(slide3, "2. Сегменты потребителей")

    # Card 1: Start
    add_card(slide3, Inches(0.8), Inches(1.6), Inches(5.7), Inches(5.2))
    tb1 = slide3.shapes.add_textbox(Inches(1.1), Inches(1.9), Inches(5.1), Inches(4.6))
    tf1 = tb1.text_frame
    tf1.word_wrap = True

    p = tf1.paragraphs[0]
    p.text = "🎯 На старте проекта"
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = ACCENT_GOLD
    p.space_after = Pt(14)

    items1 = [
        ("Дети и подростки от 10 до 18 лет", "Основная аудитория учеников, стремящихся научиться программированию и цифровой грамотности."),
        ("Их родители", "Заинтересованы в полезном досуге и будущей профессии ребенка.")
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
        p_t.space_after = Pt(14)

    # Card 2: Strategic Plan
    add_card(slide3, Inches(6.833), Inches(1.6), Inches(5.7), Inches(5.2))
    tb2 = slide3.shapes.add_textbox(Inches(7.133), Inches(1.9), Inches(5.1), Inches(4.6))
    tf2 = tb2.text_frame
    tf2.word_wrap = True

    p = tf2.paragraphs[0]
    p.text = "🚀 Стратегический план"
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = ACCENT_TEAL
    p.space_after = Pt(14)

    items2 = [
        ("Курсы для взрослой аудитории", "При масштабировании проекта — помощь тем, кому нужна смена специальности."),
        ("Грамотность в работе с ИИ", "Обучение работе с искусственным интеллектом для взрослых и специалистов.")
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
        p_t.space_after = Pt(14)


    # ------------------ SLIDE 4: CHANNELS ------------------
    slide4 = prs.slides.add_slide(blank_layout)
    add_bg(slide4)
    add_header(slide4, "3. Каналы взаимодействия")

    ch_cards = [
        ("🎧 Discord", "Уроки & Демонстрация", "Платформа с удобными функциями и голосовыми чатами для проведения онлайн-уроков, демонстрации экрана наставнику в хорошем качестве — абсолютно необходимая функция для работы."),
        ("📱 Instagram, Telegram, TikTok", "Продвижение & Реклама", "Площадки с высокой концентрацией молодой и взрослой аудитории, где проще всего разместить рекламу и привлечь целевой интерес."),
        ("🏫 Школы Казахстана", "Сотрудничество & Продвижение", "Партнерство со школами, так как подростки ищут возможности обучиться актуальному программированию взамен устаревших программ конкуррентов."),
        ("🚶‍♂️ Промоутеры", "Офлайн-активность", "Работа промоутеров для локального распространения информации и прямого привлечения.")
    ]

    positions = [(0.8, 1.6), (6.833, 1.6), (0.8, 4.3), (6.833, 4.3)]
    for (name, tag, desc), (l, t) in zip(ch_cards, positions):
        add_card(slide4, Inches(l), Inches(t), Inches(5.7), Inches(2.5))
        tb = slide4.shapes.add_textbox(Inches(l + 0.25), Inches(t + 0.2), Inches(5.2), Inches(2.1))
        tf = tb.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        p.text = name
        p.font.size = Pt(17)
        p.font.bold = True
        p.font.color.rgb = ACCENT_GOLD

        p2 = tf.add_paragraph()
        p2.text = tag
        p2.font.size = Pt(12)
        p2.font.bold = True
        p2.font.color.rgb = ACCENT_TEAL
        p2.space_after = Pt(6)

        p3 = tf.add_paragraph()
        p3.text = desc
        p3.font.size = Pt(12)
        p3.font.color.rgb = TEXT_LIGHT


    # ------------------ SLIDE 5: CUSTOMER RELATIONS ------------------
    slide5 = prs.slides.add_slide(blank_layout)
    add_bg(slide5)
    add_header(slide5, "4. Отношения с клиентами")

    add_card(slide5, Inches(0.8), Inches(1.6), Inches(11.733), Inches(5.2))
    tb = slide5.shapes.add_textbox(Inches(1.1), Inches(1.85), Inches(11.133), Inches(4.7))
    tf = tb.text_frame
    tf.word_wrap = True

    p = tf.paragraphs[0]
    p.text = "🎯 Принципы честности и доверия (Против избитых штампов)"
    p.font.size = Pt(19)
    p.font.bold = True
    p.font.color.rgb = ACCENT_GOLD
    p.space_after = Pt(8)

    p_quote = tf.add_paragraph()
    p_quote.text = "«Мы не используем громкие обещания вроде \"Профессия будущего\" или \"Гарантированное трудоустройство\" — в большинстве случаев это обман. Программирование — это сложно, но мы стремимся максимально упростить сложное и предоставить настоящие навыки.»"
    p_quote.font.size = Pt(13)
    p_quote.font.color.rgb = TEXT_MUTED
    p_quote.space_after = Pt(16)

    p_rel_head = tf.add_paragraph()
    p_rel_head.text = "Основные механизмы удержания и контроля:"
    p_rel_head.font.size = Pt(16)
    p_rel_head.font.bold = True
    p_rel_head.font.color.rgb = WHITE
    p_rel_head.space_after = Pt(8)

    rel_points = [
        "Геймификация и интерактив для удержания внимания детей.",
        "Ежемесячные отчеты родителям об успеваемости и прогрессе ребенка.",
        "Контроль всего процесса обучения.",
        "Предоставление официального документа (сертификата) с проверкой подлинности по QR-коду."
    ]
    for pt in rel_points:
        p_pt = tf.add_paragraph()
        p_pt.text = f"• {pt}"
        p_pt.font.size = Pt(13)
        p_pt.font.color.rgb = TEXT_LIGHT
        p_pt.space_after = Pt(4)


    # ------------------ SLIDE 6: REVENUE STREAMS & CALC ------------------
    slide6 = prs.slides.add_slide(blank_layout)
    add_bg(slide6)
    add_header(slide6, "5. Потоки дохода и Расчет выручки")

    courses = [
        ("Frontend Junior", "23 000 ₸ / мес", "4 месяца обучения", "23 000 ₸ × 12 чел × 4 гр - 10% = 993 600 ₸ / мес"),
        ("UI/UX Дизайн", "19 000 ₸ / мес", "4 месяца обучения", "19 000 ₸ × 12 чел × 4 гр - 10% = 820 800 ₸ / мес"),
        ("Основы Python", "27 000 ₸ / мес", "5 месяцев обучения", "27 000 ₸ × 12 чел × 4 гр - 10% = 1 166 400 ₸ / мес")
    ]

    for i, (c_name, c_price, c_dur, c_calc) in enumerate(courses):
        left_val = Inches(0.8 + i * 4.0)
        add_card(slide6, left_val, Inches(1.6), Inches(3.733), Inches(3.6))

        tb = slide6.shapes.add_textbox(left_val + Inches(0.2), Inches(1.8), Inches(3.333), Inches(3.2))
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
        p2.space_after = Pt(4)

        p3 = tf.add_paragraph()
        p3.text = c_dur
        p3.font.size = Pt(12)
        p3.font.color.rgb = ACCENT_TEAL
        p3.space_after = Pt(10)

        p4 = tf.add_paragraph()
        p4.text = f"Расчет:\n{c_calc}"
        p4.font.size = Pt(12)
        p4.font.color.rgb = TEXT_LIGHT

    # Bottom summary box
    add_card(slide6, Inches(0.8), Inches(5.35), Inches(11.733), Inches(1.5))
    tb_sum = slide6.shapes.add_textbox(Inches(1.1), Inches(5.45), Inches(11.133), Inches(1.3))
    tf_sum = tb_sum.text_frame
    tf_sum.word_wrap = True

    p_s1 = tf_sum.paragraphs[0]
    p_s1.text = "💰 Итого суммарный доход в месяц: 2 980 800 ₸"
    p_s1.font.size = Pt(20)
    p_s1.font.bold = True
    p_s1.font.color.rgb = ACCENT_GOLD

    p_s2 = tf_sum.add_paragraph()
    p_s2.text = "• Скидки: 10% при разовой оплате всего курса | 20% реферальный промокод выпускника для знакомых на 1-й месяц.\n• Перспектива: Индивидуальное наставничество при масштабировании на взрослую аудиторию."
    p_s2.font.size = Pt(12)
    p_s2.font.color.rgb = TEXT_LIGHT


    # ------------------ SLIDE 7: RESOURCES & ACTIONS ------------------
    slide7 = prs.slides.add_slide(blank_layout)
    add_bg(slide7)
    add_header(slide7, "6. Ключевые ресурсы & 7. Ключевые действия")

    # Left: Resources
    add_card(slide7, Inches(0.8), Inches(1.6), Inches(5.7), Inches(5.2))
    tb1 = slide7.shapes.add_textbox(Inches(1.1), Inches(1.85), Inches(5.1), Inches(4.7))
    tf1 = tb1.text_frame
    tf1.word_wrap = True

    p = tf1.paragraphs[0]
    p.text = "🧩 Ключевые ресурсы"
    p.font.size = Pt(19)
    p.font.bold = True
    p.font.color.rgb = ACCENT_GOLD
    p.space_after = Pt(10)

    res_items = [
        ("Команда", "3 куратора-преподавателя (ведут по 4 группы) + 1 администратор."),
        ("Техническая база", "Сайт, хостинг, веб-приложение, Телеграм бот."),
        ("Методическая база", "Уникальные учебные программы (70% практика / 30% теория), хакатоны и мероприятия."),
        ("При масштабировании", "Найм преподавателей и SMM-специалистов (на старте реклама ведется администратором).")
    ]
    for title, desc in res_items:
        p_s = tf1.add_paragraph()
        p_s.text = f"• {title}: {desc}"
        p_s.font.size = Pt(12)
        p_s.font.color.rgb = TEXT_LIGHT
        p_s.space_after = Pt(8)

    # Right: Actions
    add_card(slide7, Inches(6.833), Inches(1.6), Inches(5.7), Inches(5.2))
    tb2 = slide7.shapes.add_textbox(Inches(7.133), Inches(1.85), Inches(5.1), Inches(4.7))
    tf2 = tb2.text_frame
    tf2.word_wrap = True

    p = tf2.paragraphs[0]
    p.text = "⚙️ Ключевые действия"
    p.font.size = Pt(19)
    p.font.bold = True
    p.font.color.rgb = ACCENT_TEAL
    p.space_after = Pt(10)

    act_items = [
        "Заработок стартового капитала на фриланс-проектах группой.",
        "Создание полной программы обучения и загрузка на платформу.",
        "Регистрация проекта как ИП по упрощёнке.",
        "Проведение маркетинговой кампании.",
        "Административная работа, контроль оплат и отчеты родителям.",
        "Организация соревнований и хакатонов для ровесников."
    ]
    for act in act_items:
        p_s = tf2.add_paragraph()
        p_s.text = f"• {act}"
        p_s.font.size = Pt(12)
        p_s.font.color.rgb = TEXT_LIGHT
        p_s.space_after = Pt(6)


    # ------------------ SLIDE 8: KEY PARTNERS ------------------
    slide8 = prs.slides.add_slide(blank_layout)
    add_bg(slide8)
    add_header(slide8, "8. Ключевые партнёры")

    part_cards = [
        ("🖥️ Инфраструктура", "Хостинг-провайдеры", "Обеспечение стабильной работы веб-сайта, платформы обучения и Телеграм-бота."),
        ("🎓 Образование & Продвижение", "Школы Казахстана", "Привлечение школьников и проведение совместных открытых уроков и цифровой грамотности."),
        ("📣 Инфлюенсеры & Маркетинг", "Instagram & Telegram", "Сотрудничество с инфлюенсерами, рекламными площадками и работа промоутеров."),
        ("🤝 Партнерство с онлайн-школами", "Коллаборации", "Возможно сотрудничество с другими онлайн-школами, дополняющими наши курсы.")
    ]

    positions = [(0.8, 1.6), (6.833, 1.6), (0.8, 4.3), (6.833, 4.3)]
    for (category, title, desc), (l, t) in zip(part_cards, positions):
        add_card(slide8, Inches(l), Inches(t), Inches(5.7), Inches(2.5))
        tb = slide8.shapes.add_textbox(Inches(l + 0.25), Inches(t + 0.2), Inches(5.2), Inches(2.1))
        tf = tb.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        p.text = category
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = ACCENT_GOLD

        p2 = tf.add_paragraph()
        p2.text = title
        p2.font.size = Pt(18)
        p2.font.bold = True
        p2.font.color.rgb = WHITE
        p2.space_after = Pt(4)

        p3 = tf.add_paragraph()
        p3.text = desc
        p3.font.size = Pt(12)
        p3.font.color.rgb = TEXT_LIGHT


    # ------------------ SLIDE 9: EXPENSES & NET PROFIT ------------------
    slide9 = prs.slides.add_slide(blank_layout)
    add_bg(slide9)
    add_header(slide9, "9. Структура расходов и Расчет прибыли")

    # Left: Costs list
    add_card(slide9, Inches(0.8), Inches(1.6), Inches(5.7), Inches(5.2))
    tb1 = slide9.shapes.add_textbox(Inches(1.1), Inches(1.85), Inches(5.1), Inches(4.7))
    tf1 = tb1.text_frame
    tf1.word_wrap = True

    p = tf1.paragraphs[0]
    p.text = "📋 Ежемесячные затраты"
    p.font.size = Pt(19)
    p.font.bold = True
    p.font.color.rgb = ACCENT_GOLD
    p.space_after = Pt(10)

    costs = [
        ("Зарплата кураторов (3 чел)", "750 000 ₸", "3 × 250 000 ₸"),
        ("Зарплата администратора", "280 000 ₸", "1 администратор"),
        ("Хостинг", "20 000 ₸", "Поддержка сайта"),
        ("Буст Discord сервера", "17 000 ₸", "Улучшение качества связи"),
        ("Реклама и промоутеры", "300 000 ₸", "Маркетинговый бюджет"),
        ("Подоходный налог (ИП 4%)", "119 300 ₸", "4% от дохода 2 980 800 ₸")
    ]
    for c_name, c_val, c_sub in costs:
        p_c = tf1.add_paragraph()
        p_c.text = f"• {c_name}: {c_val}"
        p_c.font.size = Pt(13)
        p_c.font.bold = True
        p_c.font.color.rgb = WHITE

        p_sub = tf1.add_paragraph()
        p_sub.text = f"   ({c_sub})"
        p_sub.font.size = Pt(11)
        p_sub.font.color.rgb = TEXT_MUTED

    # Right: Profit formula & Capital
    add_card(slide9, Inches(6.833), Inches(1.6), Inches(5.7), Inches(5.2))
    tb2 = slide9.shapes.add_textbox(Inches(7.133), Inches(1.85), Inches(5.1), Inches(4.7))
    tf2 = tb2.text_frame
    tf2.word_wrap = True

    p = tf2.paragraphs[0]
    p.text = "💵 Расчет чистой прибыли"
    p.font.size = Pt(19)
    p.font.bold = True
    p.font.color.rgb = ACCENT_TEAL
    p.space_after = Pt(8)

    p_f = tf2.add_paragraph()
    p_f.text = "2 980 800 − 119 300 − 750 000 − 280 000 − 20 000 − 17 000 − 300 000"
    p_f.font.size = Pt(11)
    p_f.font.color.rgb = TEXT_MUTED
    p_f.space_after = Pt(6)

    p_np = tf2.add_paragraph()
    p_np.text = "Чистая прибыль в месяц:"
    p_np.font.size = Pt(14)
    p_np.font.color.rgb = WHITE

    p_np_val = tf2.add_paragraph()
    p_np_val.text = "1 494 500 ₸"
    p_np_val.font.size = Pt(28)
    p_np_val.font.bold = True
    p_np_val.font.color.rgb = ACCENT_GOLD
    p_np_val.space_after = Pt(16)

    p_cap_head = tf2.add_paragraph()
    p_cap_head.text = "💼 Стартовый капитал:"
    p_cap_head.font.size = Pt(15)
    p_cap_head.font.bold = True
    p_cap_head.font.color.rgb = WHITE

    p_cap_desc = tf2.add_paragraph()
    p_cap_desc.text = "• Для запуска не требуется кредит.\n• Стартовый капитал в 1 500 000 ₸ формируется самостоятельно в течение полугода путем заработка на фриланс-биржах."
    p_cap_desc.font.size = Pt(12)
    p_cap_desc.font.color.rgb = TEXT_LIGHT


    # ------------------ SLIDE 10: CONCLUSION ------------------
    slide10 = prs.slides.add_slide(blank_layout)
    add_bg(slide10)
    add_header(slide10, "Заключение")

    add_card(slide10, Inches(1.0), Inches(1.6), Inches(11.333), Inches(5.2), BG_CARD)
    tb = slide10.shapes.add_textbox(Inches(1.4), Inches(2.0), Inches(10.533), Inches(4.4))
    tf = tb.text_frame
    tf.word_wrap = True

    p1 = tf.paragraphs[0]
    p1.text = "📌 Подводя итог"
    p1.font.size = Pt(22)
    p1.font.bold = True
    p1.font.color.rgb = ACCENT_GOLD
    p1.space_after = Pt(16)

    p2 = tf.add_paragraph()
    p2.text = "При правильном выполнении указанных шагов, этот бизнес-проект вполне рентабелен и имеет высокий потенциал для успешного запуска и дальнейшего масштабирования."
    p2.font.size = Pt(18)
    p2.font.color.rgb = TEXT_LIGHT
    p2.space_after = Pt(36)

    p3 = tf.add_paragraph()
    p3.text = "Спасибо за внимание!"
    p3.font.size = Pt(36)
    p3.font.bold = True
    p3.font.color.rgb = ACCENT_TEAL
    p3.alignment = PP_ALIGN.CENTER

    prs.save("презентация_синтаксис.pptx")
    print("Successfully generated презентация_синтаксис.pptx")

if __name__ == '__main__':
    create_presentation()
