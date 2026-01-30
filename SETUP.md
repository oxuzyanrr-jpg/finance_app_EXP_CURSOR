# Инструкция по первому запуску

## Шаг 1: Установка зависимостей

```bash
# Создайте виртуальное окружение
python -m venv venv

# Активируйте виртуальное окружение
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Установите зависимости
pip install -r requirements.txt
```

## Шаг 2: Настройка базы данных

1. Установите PostgreSQL, если еще не установлен
2. Создайте базу данных:
```sql
CREATE DATABASE cyberhub_db;
CREATE USER postgres WITH PASSWORD 'postgres';
GRANT ALL PRIVILEGES ON DATABASE cyberhub_db TO postgres;
```

## Шаг 3: Настройка переменных окружения

Создайте файл `.env` в корне проекта на основе `.env.example`:

```env
SECRET_KEY=django-insecure-change-this-in-production
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

DB_NAME=cyberhub_db
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432

CLUB_API_URL=
CLUB_API_KEY=
CLUB_API_SYNC_INTERVAL=3600
```

## Шаг 4: Применение миграций

```bash
python manage.py makemigrations
python manage.py migrate
```

## Шаг 5: Создание суперпользователя

```bash
python manage.py createsuperuser
```

Введите логин, email и пароль. После создания пользователя:

1. Зайдите в админ-панель: http://localhost:8000/admin/
2. Найдите созданного пользователя в разделе "Пользователи"
3. Установите роль "Владелец" (Owner) для этого пользователя

## Шаг 6: Создание категорий доходов и расходов

После первого входа в систему, создайте категории для доходов и расходов через админ-панель или через интерфейс приложения.

Примеры категорий доходов:
- Игровое время (автоматически) - создается автоматически при синхронизации
- Бар
- Продажа товаров
- Другое

Примеры категорий расходов:
- Аренда
- Коммунальные услуги
- Зарплаты
- Закупка товаров
- Реклама
- Другое

## Шаг 7: Создание сотрудников

1. Создайте пользователей для сотрудников через админ-панель или через интерфейс
2. Назначьте им роль "Администратор" (Admin)
3. В разделе "Сотрудники" создайте запись сотрудника, привязав к пользователю
4. Установите тип оплаты (оклад или почасовая ставка) и ставку

## Шаг 8: Запуск сервера

```bash
python manage.py runserver
```

Откройте браузер и перейдите на http://localhost:8000/

## Настройка интеграции с клубным ПО (опционально)

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
# В отдельном терминале
celery -A config worker -l info

# В другом терминале
celery -A config beat -l info
```

## Полезные команды

```bash
# Создать миграции
python manage.py makemigrations

# Применить миграции
python manage.py migrate

# Создать суперпользователя
python manage.py createsuperuser

# Собрать статические файлы
python manage.py collectstatic

# Запустить сервер разработки
python manage.py runserver

# Открыть Django shell
python manage.py shell
```

## Решение проблем

### Ошибка подключения к базе данных
- Проверьте, что PostgreSQL запущен
- Убедитесь, что данные в `.env` правильные
- Проверьте, что база данных создана

### Ошибка импорта модулей
- Убедитесь, что виртуальное окружение активировано
- Проверьте, что все зависимости установлены: `pip install -r requirements.txt`

### Ошибка миграций
- Удалите все файлы в папках `migrations` (кроме `__init__.py`)
- Выполните `python manage.py makemigrations` заново
- Примените миграции: `python manage.py migrate`

