
// Global Tour Data
const TOUR_DATA = [
  {
    id: 1,
    title: "Футуристическая Астана",
    cat: "Архитектура",
    badge: "Хит",
    badgeClass: "teal",
    image: "https://images.unsplash.com/photo-1510664053238-66236357996d?auto=format&fit=crop&w=800&q=80",
    price: "15 000 ₸",
    time: "3 часа",
    transport: "Пешком",
    desc: "Погрузитесь в мир архитектуры будущего. Мы пройдем по 'Золотой оси' столицы, изучим философию Байтерека и узнаем, как Норман Фостер создал самый большой шатер в мире.",
    route: [
      { name: "Монумент Байтерек", detail: "Символ древа жизни и точка отсчета новой истории." },
      { name: "Бульвар Нуржол", detail: "Пешеходная галерея шедевров мировой архитектуры." },
      { name: "ТЦ Хан Шатыр", detail: "Уникальное здание в форме шатра с тропическим пляжем." }
    ]
  },
  {
    id: 2,
    title: "Огни левого берега",
    cat: "Ночной город",
    badge: "Новинка",
    badgeClass: "gold",
    image: "https://images.unsplash.com/photo-1609756184518-e24941914101?auto=format&fit=crop&w=800&q=80",
    price: "18 000 ₸",
    time: "2.5 часа",
    transport: "Авто",
    desc: "Когда солнце заходит, Астана превращается в город из фантастических фильмов. Магия неоновых огней и отражение небоскребов в реке Ишим.",
    route: [
      { name: "Набережная Ишима", detail: "Прогулка вдоль сияющей реки." },
      { name: "Мост Атырау", detail: "Световое шоу на самом красивом мосту города." },
      { name: "Площадь Независимости", detail: "Вечерняя панорама главных монументов." }
    ]
  },
  {
    id: 3,
    title: "Вкус великой степи",
    cat: "Гастрономия",
    badge: null,
    image: "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?auto=format&fit=crop&w=800&q=80",
    price: "25 000 ₸",
    time: "4 часа",
    transport: "Авто",
    desc: "Гастрономическое путешествие в сердце казахских традиций. Дегустация лучших блюд кочевой кухни в современной интерпретации.",
    route: [
      { name: "Центр кочевой кухни", detail: "Дегустация 5 видов национальных деликатесов." },
      { name: "Мастер-класс по баурсакам", detail: "Секреты идеального теста от бабушки." },
      { name: "Чайная церемония", detail: "Традиции казахского гостеприимства." }
    ]
  },
  {
    id: 4,
    title: "Бурабай: Маленькая Швейцария",
    cat: "Загородные поездки",
    badge: "Топ",
    badgeClass: "teal",
    image: "https://images.unsplash.com/photo-1586348943529-beaae6c28db9?auto=format&fit=crop&w=800&q=80",
    price: "35 000 ₸",
    time: "10 часов",
    transport: "Микроавтобус",
    desc: "Побег из шумного мегаполиса в край синих озер и хвойных лесов. Легенды скалы Окжетпес и чистейший воздух соснового бора.",
    route: [
      { name: "Поляна Абылай Хана", detail: "Историческое сердце курорта." },
      { name: "Восхождение на гору Болектау", detail: "Лучшая панорамная точка на озера." },
      { name: "Берег озера Боровое", detail: "Пикник и отдых у воды." }
    ]
  },
  {
    id: 5,
    title: "Энергия Будущего: EXPO",
    cat: "Архитектура",
    badge: "VIP",
    badgeClass: "gold",
    image: "https://images.unsplash.com/photo-1609756184568-12c5f7e719b6?auto=format&fit=crop&w=800&q=80",
    price: "14 000 ₸",
    time: "3 часа",
    transport: "Пешком",
    desc: "Исследование самого технологичного района города. Сфера 'Нур Алем' — единственное в мире здание-шар такого масштаба.",
    route: [
      { name: "Музей Нур Алем", detail: "8 этажей инноваций и энергии будущего." },
      { name: "Конгресс-центр", detail: "Архитектурные формы в стиле хай-тек." },
      { name: "Зона фонтанов", detail: "Музыкально-световое шоу на территории парка." }
    ]
  },
  {
    id: 6,
    title: "Тайны Старого Города",
    cat: "История",
    badge: null,
    image: "https://images.unsplash.com/photo-1510252194380-606041797c25?auto=format&fit=crop&w=800&q=80",
    price: "12 000 ₸",
    time: "3 часа",
    transport: "Пешком",
    desc: "Вернитесь на столетие назад. История купеческого Акмолинска и сталинской архитектуры Целинограда.",
    route: [
      { name: "Дом купца Кубрина", detail: "Жемчужина архитектуры начала XX века." },
      { name: "Старая площадь", detail: "Дух советской эпохи и здание Парламента." },
      { name: "Улица Мамбетова", detail: "Прогулка по самому уютному кварталу правого берега." }
    ]
  },
  {
    id: 7,
    title: "Мечети Астаны",
    cat: "Культура",
    badge: "Новинка",
    badgeClass: "teal",
    image: "https://images.unsplash.com/photo-1590073844006-33379778ae09?auto=format&fit=crop&w=800&q=80",
    price: "13 000 ₸",
    time: "3.5 часа",
    transport: "Авто",
    desc: "Посещение главных духовных центров столицы, включая самую большую мечеть в Центральной Азии.",
    route: [
      { name: "Главная республиканская мечеть", detail: "Масштаб и красота современной исламской архитектуры." },
      { name: "Мечеть Хазрет Султан", detail: "Белоснежная жемчужина классического стиля." },
      { name: "Мечеть Абу Насыр Аль-Фараби", detail: "Архитектурный ансамбль на левом берегу." }
    ]
  },
  {
    id: 8,
    title: "Фото-прогулка: Инста-локации",
    cat: "Lifestyle",
    badge: "Популярно",
    badgeClass: "gold",
    image: "https://images.unsplash.com/photo-1519125323398-675f0ddb6308?auto=format&fit=crop&w=800&q=80",
    price: "20 000 ₸",
    time: "2 часа",
    transport: "Пешком",
    desc: "Лучшие ракурсы города для ваших социальных сетей в сопровождении профессионального фотографа.",
    route: [
      { name: "Мост Атырау", detail: "Футуристичные линии и свет." },
      { name: "Пирамида (Дворец Мира)", detail: "Геометрия и масштаб." },
      { name: "Секретные крыши", detail: "Панорамный вид на город с высоты." }
    ]
  },
  {
    id: 9,
    title: "Сердце Евразии: Национальный музей",
    cat: "История",
    badge: null,
    image: "https://images.unsplash.com/photo-1582555172866-f73bb12a2ab3?auto=format&fit=crop&w=800&q=80",
    price: "11 000 ₸",
    time: "3 часа",
    transport: "Пешком",
    desc: "Путешествие сквозь века: от Золотого человека до современной истории Казахстана.",
    route: [
      { name: "Зал Золотого человека", detail: "Главное сокровище нации." },
      { name: "Зал этнографии", detail: "Быт и культура кочевников." },
      { name: "Зал современного искусства", detail: "Взгляд в будущее." }
    ]
  },
  {
    id: 10,
    title: "Вело-тур: Зеленый пояс",
    cat: "Lifestyle",
    badge: "Сезонный",
    badgeClass: "teal",
    image: "https://images.unsplash.com/photo-1541625602330-2277a1cd13a1?auto=format&fit=crop&w=800&q=80",
    price: "9 000 ₸",
    time: "2.5 часа",
    transport: "Велосипед",
    desc: "Активный отдых в парковой зоне Астаны. Свежий воздух и лучшие велодорожки города.",
    route: [
      { name: "Центральный парк", detail: "Старт маршрута среди вековых деревьев." },
      { name: "Триатлон парк", detail: "Спортивное сердце столицы." },
      { name: "Набережная", detail: "Финиш с видом на закат." }
    ]
  },
  {
    id: 11,
    title: "Коргалжын: Розовые фламинго",
    cat: "Загородные поездки",
    badge: "Экспедиция",
    badgeClass: "gold",
    image: "https://images.unsplash.com/photo-1520113412646-04fc68c04218?auto=format&fit=crop&w=800&q=80",
    price: "45 000 ₸",
    time: "12 часов",
    transport: "Внедорожник",
    desc: "Уникальный заповедник из списка ЮНЕСКО. Настоящее сафари в казахской степи.",
    route: [
      { name: "Визит-центр заповедника", detail: "Инструктаж и история края." },
      { name: "Озеро Тенгиз", detail: "Наблюдение за дикими птицами." },
      { name: "Степной обед", detail: "Пикник на природе." }
    ]
  },
  {
    id: 12,
    title: "Астана Опера: За кулисами",
    cat: "Культура",
    badge: "Exclusive",
    badgeClass: "teal",
    image: "https://images.unsplash.com/photo-1503095396549-80705bc06ee0?auto=format&fit=crop&w=800&q=80",
    price: "16 000 ₸",
    time: "2 часа",
    transport: "Пешком",
    desc: "Узнайте секреты одного из самых красивых оперных театров мира. Мы заглянем туда, куда не пускают обычных зрителей.",
    route: [
      { name: "Главный зал", detail: "Итальянская акустика и роскошный интерьер." },
      { name: "Мастерские костюмов", detail: "Где создается магия сцены." },
      { name: "Репетиционные залы", detail: "Будни артистов балета." }
    ]
  },
  {
    id: 13,
    title: "Шопинг-сопровождение",
    cat: "Lifestyle",
    badge: null,
    image: "https://images.unsplash.com/photo-1483985988355-763728e1935b?auto=format&fit=crop&w=800&q=80",
    price: "15 000 ₸",
    time: "4 часа",
    transport: "Авто",
    desc: "Гид по лучшим брендам и локальным дизайнерам в крупнейших ТРЦ города.",
    route: [
      { name: "Talan Gallery", detail: "Люксовый шопинг и бренды мирового уровня." },
      { name: "Абу Даби Плаза", detail: "Новейший шопинг-центр столицы." },
      { name: "Шоурумы КЗ дизайнеров", detail: "Уникальный стиль с национальным колоритом." }
    ]
  },
  {
    id: 14,
    title: "АЛЖИР: Память истории",
    cat: "История",
    badge: "Важно",
    badgeClass: "gold",
    image: "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?auto=format&fit=crop&w=800&q=80",
    price: "18 000 ₸",
    time: "5 часов",
    transport: "Авто",
    desc: "Мемориальный комплекс памяти жертв политических репрессий. Трагическая и важная страница истории.",
    route: [
      { name: "Музей памяти", detail: "Архивные документы и инсталляции." },
      { name: "Стена памяти", detail: "Почтение памяти погибших." },
      { name: "Вагон-узник", detail: "Реконструкция условий транспортировки." }
    ]
  },
  {
    id: 15,
    title: "Вертолетная прогулка",
    cat: "Lifestyle",
    badge: "Премиум",
    badgeClass: "teal",
    image: "https://images.unsplash.com/photo-1534447677768-be436bb09401?auto=format&fit=crop&w=800&q=80",
    price: "120 000 ₸",
    time: "40 минут",
    transport: "Вертолет",
    desc: "Весь город как на ладони. Самый эффектный способ увидеть масштаб Астаны.",
    route: [
      { name: "Аэродром", detail: "Предполетная подготовка." },
      { name: "Полет над левым берегом", detail: "Вид на небоскребы сверху." },
      { name: "Полет над Ишимом", detail: "Красота изгибов реки." }
    ]
  },
  {
    id: 16,
    title: "Винная Астана",
    cat: "Гастрономия",
    badge: "18+",
    badgeClass: "gold",
    image: "https://images.unsplash.com/photo-1510812431401-41d2bd2722f3?auto=format&fit=crop&w=800&q=80",
    price: "22 000 ₸",
    time: "3 часа",
    transport: "Авто",
    desc: "Дегустация казахстанских и мировых вин в лучших энотеках города с профессиональным сомелье.",
    route: [
      { name: "Энотека в центре", detail: "История виноделия в Казахстане." },
      { name: "Винный бар", detail: "Сет из 5 вин с гастро-парами." },
      { name: "Секретный бар", detail: "Авторские коктейли на основе вина." }
    ]
  },
  {
    id: 17,
    title: "Детская Астана: Квест",
    cat: "Lifestyle",
    badge: "Для детей",
    badgeClass: "teal",
    image: "https://images.unsplash.com/photo-1502086223501-7ea244391501?auto=format&fit=crop&w=800&q=80",
    price: "14 000 ₸",
    time: "2.5 часа",
    transport: "Пешком",
    desc: "Увлекательное приключение для самых маленьких путешественников в игровой форме.",
    route: [
      { name: "Поиск клада у Пирамиды", detail: "Загадки истории." },
      { name: "Океанариум Думан", detail: "Встреча с морскими жителями." },
      { name: "Парк аттракционов", detail: "Веселый финиш." }
    ]
  },
  {
    id: 18,
    title: "Вечерний пикник у реки",
    cat: "Lifestyle",
    badge: "Романтика",
    badgeClass: "gold",
    image: "https://images.unsplash.com/photo-1523906834658-6e24ef2386f9?auto=format&fit=crop&w=800&q=80",
    price: "19 000 ₸",
    time: "3 часа",
    transport: "Пешком",
    desc: "Идеальный вечер для пары. Уютный сет-ап на берегу Ишима с видом на закат.",
    route: [
      { name: "Секретная локация", detail: "Вдали от суеты." },
      { name: "Ужин под открытым небом", detail: "Изысканные закуски и музыка." },
      { name: "Фотосессия", detail: "Моменты на память." }
    ]
  },
  {
    id: 19,
    title: "Арт-галереи столицы",
    cat: "Культура",
    badge: null,
    image: "https://images.unsplash.com/photo-1499781350541-7783f6c6a0c8?auto=format&fit=crop&w=800&q=80",
    price: "10 000 ₸",
    time: "3 часа",
    transport: "Пешком",
    desc: "Знакомство с современным искусством Казахстана в частных галереях и студиях художников.",
    route: [
      { name: "Галерея Has Sanat", detail: "Классики и современники." },
      { name: "TSE Art Destination", detail: "Актуальное искусство и перформансы." },
      { name: "Студия локального художника", detail: "Личное общение с творцом." }
    ]
  },
  {
    id: 20,
    title: "Зимняя сказка: Катание в степи",
    cat: "Загородные поездки",
    badge: "Зима",
    badgeClass: "teal",
    image: "https://images.unsplash.com/photo-1418985991508-e47386d96a71?auto=format&fit=crop&w=800&q=80",
    price: "28 000 ₸",
    time: "4 часа",
    transport: "Снегоход/Сани",
    desc: "Настоящая зимняя экзотика: катание на санях, запряженных собаками или снегоходах по бескрайним просторам.",
    route: [
      { name: "Этно-аул", detail: "Знакомство с породой Тазы." },
      { name: "Прогулка по снегу", detail: "Драйв и адреналин." },
      { name: "Чаепитие в теплой юрте", detail: "Традиционные сладости и тепло очага." }
    ]
  }
];

const GUIDE_DATA = [
  {
    id: 1,
    name: "Дарья А.",
    role: "Старший гид, историк",
    image: "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=400&h=400&fit=crop&crop=face",
    specialization: "Архитектура и история",
    languages: "Русский, Английский, Казахский",
    experience: "9 лет",
    rating: 4.9,
    reviews: 150,
    bio: "Дарья знает историю каждого кирпича в старом городе. Она специализируется на архивных исследованиях и может рассказать о секретах зданий, которых уже нет на карте."
  },
  {
    id: 2,
    name: "Алексей С.",
    role: "Гастро-эксперт, этнограф",
    image: "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=400&h=400&fit=crop&crop=face",
    specialization: "Гастротуры и традиции",
    languages: "Русский, Казахский",
    experience: "7 лет",
    rating: 4.8,
    reviews: 98,
    bio: "Алексей считает, что путь к сердцу города лежит через его кухню. Он знает лучшие места с аутентичным бешбармаком и может провести мастер-класс по приготовлению кумыса."
  },
  {
    id: 3,
    name: "Андрей К.",
    role: "Фотограф, арт-гид",
    image: "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=400&h=400&fit=crop&crop=face",
    specialization: "Фото- и арт-маршруты",
    languages: "Русский, Английский",
    experience: "5 лет",
    rating: 5.0,
    reviews: 72,
    bio: "Андрей покажет вам Астану через объектив. Он знает все 'инстаграмные' локации и поможет сделать идеальные кадры, попутно рассказывая о современном искусстве столицы."
  },
  {
    id: 4,
    name: "Елена Ж.",
    role: "Педагог, детский гид",
    image: "https://images.unsplash.com/photo-1438761681033-6461ffad8d80?w=400&h=400&fit=crop&crop=face",
    specialization: "Детские квесты и семейные туры",
    languages: "Русский, Казахский",
    experience: "10 лет",
    rating: 4.9,
    reviews: 210,
    bio: "Елена превращает обычную прогулку в захватывающее приключение. Её экскурсии-квесты обожают дети, а родители ценят за познавательность и безопасность."
  },
  {
    id: 5,
    name: "Максим Р.",
    role: "Эксперт по эко-туризму",
    image: "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=400&h=400&fit=crop&crop=face",
    specialization: "Природа и загородные туры",
    languages: "Русский, Английский",
    experience: "6 лет",
    rating: 4.7,
    reviews: 85,
    bio: "Максим — ваш проводник в мир дикой природы. Бурабай, Коргалжын и степные просторы — его стихия. Профессиональный альпинист и любитель бердвотчинга."
  },
  {
    id: 6,
    name: "Сауле М.",
    role: "Культуролог",
    image: "https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=400&h=400&fit=crop&crop=face",
    specialization: "Музеи и современная культура",
    languages: "Казахский, Русский, Турецкий",
    experience: "8 лет",
    rating: 4.9,
    reviews: 124,
    bio: "Сауле мастерски соединяет древние легенды с современными культурными трендами. Она лучший гид по Национальному музею и театру Астана Опера."
  }
];

// Common UI Elements
const commonUI = {
  initHeader() {
    const header = document.getElementById('header');
    if (!header) return;
    window.addEventListener('scroll', () => {
      header.classList.toggle('scrolled', window.scrollY > 80);
    });
  },

  initProgressBar() {
    const progressBar = document.getElementById('progress-bar');
    if (!progressBar) return;
    window.addEventListener('scroll', () => {
      const doc = document.documentElement;
      const scrolled = doc.scrollTop / (doc.scrollHeight - doc.clientHeight);
      progressBar.style.width = (scrolled * 100) + '%';
    });
  },

  initAnimations() {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(e => {
        if (e.isIntersecting) {
          e.target.style.opacity = '1';
          e.target.style.transform = 'translateY(0)';
        }
      });
    }, { threshold: 0.1 });

    document.querySelectorAll('.tour-card, .guide-card, .review-card, .cat-item, .feature, .season, .number-item').forEach(el => {
      el.style.opacity = '0';
      el.style.transform = 'translateY(30px)';
      el.style.transition = 'all 0.6s cubic-bezier(0.165, 0.84, 0.44, 1)';
      observer.observe(el);
    });
  }
};

// Modal System
const tourModal = {
  overlay: document.getElementById('modalOverlay'),
  closeBtn: document.getElementById('modalClose'),

  init() {
    if (this.closeBtn) {
      this.closeBtn.onclick = () => this.close();
    }
    if (this.overlay) {
      this.overlay.onclick = (e) => {
        if (e.target === this.overlay) this.close();
      };
    }
  },

  open(id) {
    const tour = TOUR_DATA.find(t => t.id === id);
    if (!tour || !this.overlay) return;

    document.getElementById('modalImg').src = tour.image;
    document.getElementById('modalCat').innerText = tour.cat;
    document.getElementById('modalTitle').innerText = tour.title;
    document.getElementById('modalDesc').innerText = tour.desc;
    document.getElementById('modalPrice').innerHTML = tour.price + "<span>/чел</span>";

    const routeHtml = tour.route.map(item => `
      <div class="route-item">
        <h4>${item.name}</h4>
        <p>${item.detail}</p>
      </div>
    `).join('');
    document.getElementById('modalRoute').innerHTML = routeHtml;

    this.overlay.classList.add('active');
    document.body.style.overflow = 'hidden';
  },

  close() {
    if (this.overlay) {
      this.overlay.classList.remove('active');
      document.body.style.overflow = 'auto';
    }
  }
};

// Global Init
document.addEventListener('DOMContentLoaded', () => {
  commonUI.initHeader();
  commonUI.initProgressBar();
  tourModal.init();
});

// Helper for card generation
function createTourCard(tour) {
  return `
    <div class="tour-card" onclick="tourModal.open(${tour.id})">
      <div class="card-img">
        <img src="${tour.image}" alt="${tour.title}" loading="lazy">
        ${tour.badge ? `<span class="card-badge ${tour.badgeClass || 'teal'}">${tour.badge}</span>` : ''}
      </div>
      <div class="card-body">
        <div class="card-cat">${tour.cat}</div>
        <h3>${tour.title}</h3>
        <div class="card-meta">
          <span>⏳ ${tour.time}</span>
          <span>🚗 ${tour.transport}</span>
        </div>
        <div class="card-footer">
          <div class="card-price">${tour.price}<span>/чел</span></div>
          <div class="card-arrow">→</div>
        </div>
      </div>
    </div>
  `;
}
