# CyberHub Manager

Веб-приложение для управления компьютерным клубом. Система предназначена для учета финансов (доходы/расходы), интеграции с игровым клиентом для сбора статистики, управления персоналом (графики, зарплата) и разграничения прав доступа между владельцами и администраторами.

## Технологический стек

- **Backend**: Django 4.2
- **Frontend**: Django Templates + Bootstrap 5
- **База данных**: PostgreSQL
- **Дополнительно**: Django REST Framework, Celery (опционально), pandas, openpyxl

## Функциональность

### Модули системы:

1. **Аутентификация и авторизация**
   - Вход по логину и паролю
   - Разделение интерфейса по ролям (Владелец/Админ)
   - Смена пароля

2. **Финансы**
   - Учет доходов (автоматически через API и вручную)
   - Учет расходов с категориями
   - Загрузка чеков/документов
   - Отчеты и аналитика (только для Владельца)
   - Экспорт в Excel/CSV

3. **Персонал**
   - Управление сотрудниками (CRUD)
   - График смен (календарный вид)
   - Учет рабочего времени
   - Расчет зарплаты
   - Ведомость на выплату

4. **Интеграция**
   - Получение данных о доходах с компьютеров через API клубного ПО
   - Периодическая синхронизация (Celery)

## Установка и настройка

### Требования

- Python 3.10+
- PostgreSQL 12+
- Redis (для Celery, опционально)

### Шаги установки

1. Клонируйте репозиторий или создайте проект

2. Создайте виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# или
venv\Scripts\activate  # Windows
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

4. Создайте файл `.env` на основе `.env.example` и настройте переменные окружения:
```bash
SECRET_KEY=your-secret-key-here
DEBUG=True
DB_NAME=cyberhub_db
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432
CLUB_API_URL=https://your-club-api-url.com
CLUB_API_KEY=your-api-key
```

5. Создайте базу данных PostgreSQL:
```sql
CREATE DATABASE cyberhub_db;
```

6. Выполните миграции:
```bash
python manage.py makemigrations
python manage.py migrate
```

7. Создайте суперпользователя (владельца):
```bash
python manage.py createsuperuser
```

После создания суперпользователя, зайдите в админ-панель и установите роль "Владелец" для созданного пользователя.

8. Запустите сервер разработки:
```bash
python manage.py runserver
```

## Настройка интеграции с клубным ПО

1. Укажите URL API и ключ в `.env`:
```
CLUB_API_URL=https://your-club-api-url.com/api
CLUB_API_KEY=your-api-key
```

2. API должен возвращать данные в формате:
```json
[
    {
        "date": "2024-01-15",
        "amount": 1500.00,
        "computer_id": 1,
        "description": "Игровое время"
    }
]
```

3. Для периодической синхронизации настройте Celery (опционально):
```bash
celery -A config worker -l info
celery -A config beat -l info
```

## Роли пользователей

### Владелец (Owner)
- Полный доступ ко всем функциям
- Финансовые отчеты и аналитика
- Управление персоналом
- Настройки системы

### Администратор (Admin)
- Просмотр своих смен
- Просмотр своего графика
- Просмотр своей зарплаты
- Ограниченный доступ к финансовым данным

## Структура проекта

```
cyberhub_manager/
├── manage.py
├── requirements.txt
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── apps/
│   ├── accounts/          # Аутентификация
│   ├── finances/          # Финансы
│   ├── staff/             # Персонал
│   ├── dashboard/         # Дашборд
│   └── integrations/      # Интеграции
├── static/                # Статические файлы
├── media/                 # Загруженные файлы
└── templates/             # HTML шаблоны
```

## Разработка

### Создание миграций
```bash
python manage.py makemigrations
python manage.py migrate
```

### Создание суперпользователя
```bash
python manage.py createsuperuser
```

### Запуск тестов
```bash
python manage.py test
```

### Сбор статических файлов
```bash
python manage.py collectstatic
```

## Лицензия

Проект разработан для внутреннего использования.

## Контакты

Разработчик: Оксзян Реваз Рамазович

