# Управление сотрудниками

## Способы добавления/изменения сотрудников

### 1. Через веб-интерфейс (самый простой)

**Добавить сотрудника:**
1. Войдите как владелец (admin/admin123)
2. Перейдите: http://localhost:8000/staff/employees/
3. Нажмите "Добавить сотрудника"
4. Выберите пользователя из списка (или создайте нового через админку)
5. Заполните данные:
   - Тип оплаты (оклад/почасовая)
   - Ставка
   - Дата найма
   - Статус (активен/неактивен)
6. Сохраните

**Изменить сотрудника:**
1. В списке сотрудников нажмите кнопку редактирования (карандаш)
2. Измените нужные поля
3. Сохраните

### 2. Через админ-панель Django

1. Откройте: http://localhost:8000/admin/
2. Войдите как владелец
3. Раздел "Персонал" → "Сотрудники"
4. Нажмите "Добавить сотрудника" или выберите существующего для редактирования

### 3. Через скрипт (программно)

**Добавить сотрудника:**
```bash
python add_employee.py --username ivan --first_name Иван --role admin --salary_rate 500
```

**Изменить сотрудника:**
```bash
python add_employee.py --username ivan --edit --salary_rate 600
```

**Параметры:**
- `--username` - логин пользователя (обязательно)
- `--first_name` - имя сотрудника
- `--role` - роль (owner/admin, по умолчанию: admin)
- `--salary_type` - тип оплаты (salary/hourly, по умолчанию: hourly)
- `--salary_rate` - ставка/оклад (по умолчанию: 0)
- `--edit` - режим редактирования
- `--is_active` - активен (true/false)

### 4. Через Django shell

**Открыть shell:**
```bash
python manage.py shell
```

**Добавить сотрудника:**
```python
from apps.accounts.models import User
from apps.staff.models import Employee
from django.utils import timezone

# Создать пользователя
user = User.objects.create_user(
    username='ivan',
    first_name='Иван',
    role='admin',
    email='ivan@club.local'
)
user.set_password('123456')
user.save()

# Создать сотрудника
employee = Employee.objects.create(
    user=user,
    salary_type='hourly',
    salary_rate=500,
    hire_date=timezone.now().date(),
    is_active=True
)
```

**Изменить сотрудника:**
```python
from apps.staff.models import Employee

employee = Employee.objects.get(user__username='ivan')
employee.salary_rate = 600
employee.save()
```

**Удалить сотрудника:**
```python
employee = Employee.objects.get(user__username='ivan')
employee.delete()  # Удалит сотрудника, но не пользователя
# или
employee.user.delete()  # Удалит и пользователя, и сотрудника
```

### 5. Прямое редактирование базы данных (не рекомендуется)

Если используете SQLite:
```bash
sqlite3 db.sqlite3
```

Затем SQL команды:
```sql
-- Посмотреть всех сотрудников
SELECT * FROM staff_employee;

-- Изменить ставку
UPDATE staff_employee SET salary_rate = 600 WHERE id = 1;
```

## Важные моменты

1. **Связь с пользователем**: Каждый сотрудник должен быть связан с пользователем (User)
2. **Роль**: Сотрудники обычно имеют роль "admin", владелец - "owner"
3. **Пароль по умолчанию**: При создании через скрипт пароль устанавливается как "123456" - его нужно сменить
4. **Удаление**: При удалении сотрудника пользователь остается в системе, но теряет связь с Employee

## Примеры использования скрипта

```bash
# Добавить сотрудника с окладом
python add_employee.py --username petr --first_name Петр --salary_type salary --salary_rate 30000

# Добавить сотрудника с почасовой оплатой
python add_employee.py --username maria --first_name Мария --salary_type hourly --salary_rate 250

# Изменить ставку существующего сотрудника
python add_employee.py --username valya --edit --salary_rate 300

# Деактивировать сотрудника
python add_employee.py --username danil --edit --is_active false
```

