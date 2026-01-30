# Структура проекта CyberHub Manager

## Основные директории

```
cyberhub_manager/
├── manage.py                 # Django management script
├── requirements.txt           # Python зависимости
├── .env.example              # Пример файла с переменными окружения
├── README.md                 # Основная документация
├── SETUP.md                  # Инструкция по установке
├── .gitignore                # Игнорируемые файлы для Git
│
├── config/                   # Основная конфигурация Django
│   ├── __init__.py
│   ├── settings.py           # Настройки проекта
│   ├── urls.py               # Главный URL router
│   ├── wsgi.py               # WSGI конфигурация
│   └── asgi.py               # ASGI конфигурация
│
├── apps/                     # Django приложения
│   ├── accounts/             # Аутентификация и пользователи
│   │   ├── models.py         # Модель User с ролями
│   │   ├── views.py          # Представления (логин, логаут, смена пароля)
│   │   ├── forms.py          # Формы аутентификации
│   │   ├── decorators.py     # Декораторы для проверки ролей
│   │   ├── urls.py           # URL маршруты
│   │   └── admin.py          # Админ-панель
│   │
│   ├── finances/             # Модуль финансов
│   │   ├── models.py         # Income, Expense, категории
│   │   ├── views.py          # CRUD операции, отчеты, экспорт
│   │   ├── forms.py          # Формы для доходов/расходов
│   │   ├── services.py       # Бизнес-логика расчетов
│   │   ├── urls.py           # URL маршруты
│   │   └── admin.py          # Админ-панель
│   │
│   ├── staff/                # Модуль персонала
│   │   ├── models.py         # Employee, Shift, WorkTime
│   │   ├── views.py          # CRUD сотрудников, смены, зарплата
│   │   ├── forms.py          # Формы для сотрудников и смен
│   │   ├── services.py       # Расчет зарплаты, статистика
│   │   ├── urls.py           # URL маршруты
│   │   └── admin.py          # Админ-панель
│   │
│   ├── dashboard/            # Главная страница
│   │   ├── views.py          # Дашборды для Owner и Admin
│   │   └── urls.py           # URL маршруты
│   │
│   └── integrations/         # Интеграция с внешним API
│       ├── club_api.py       # Клиент для работы с API клубного ПО
│       ├── tasks.py          # Celery задачи для синхронизации
│       ├── views.py          # Ручная синхронизация
│       └── urls.py           # URL маршруты
│
├── templates/                # HTML шаблоны
│   ├── base.html             # Базовый шаблон
│   ├── accounts/             # Шаблоны аутентификации
│   ├── dashboard/            # Шаблоны дашборда
│   ├── finances/             # Шаблоны финансов
│   ├── staff/                # Шаблоны персонала
│   └── integrations/         # Шаблоны интеграций
│
├── static/                   # Статические файлы (CSS, JS, изображения)
├── media/                    # Загруженные файлы (чеки, документы)
└── staticfiles/              # Собранные статические файлы (после collectstatic)
```

## Основные модели данных

### accounts.User
- Расширенная модель пользователя Django
- Поля: username, email, password, role (Owner/Admin), created_at

### finances.Income
- Доходы
- Поля: amount, category, date, description, source_type (API/Manual), created_by

### finances.Expense
- Расходы
- Поля: amount, category, date, description, receipt_file, created_by

### finances.IncomeCategory / ExpenseCategory
- Категории доходов и расходов
- Поля: name, description

### staff.Employee
- Сотрудники
- Поля: user (OneToOne), salary_type (оклад/почасовая), salary_rate, hire_date, is_active

### staff.Shift
- Смены
- Поля: employee, start_time, end_time, status, notes, created_by

### staff.WorkTime
- Учет рабочего времени
- Поля: shift, actual_hours, confirmed, confirmed_by

## Роли пользователей

### Owner (Владелец)
- Полный доступ ко всем функциям
- Финансовые отчеты и аналитика
- Управление персоналом
- Настройки системы

### Admin (Администратор)
- Просмотр своих смен
- Просмотр своего графика
- Просмотр своей зарплаты
- Ограниченный доступ

## API интеграция

Модуль `integrations` позволяет:
- Получать данные о доходах с компьютеров через REST API
- Периодически синхронизировать данные (Celery)
- Обрабатывать ошибки и логировать операции

## Безопасность

- Хеширование паролей (PBKDF2)
- Защита от SQL-инъекций (ORM Django)
- Защита от XSS (автоматическое экранирование)
- CSRF защита
- Разграничение доступа по ролям

