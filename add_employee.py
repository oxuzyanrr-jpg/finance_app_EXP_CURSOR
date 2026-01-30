"""
Скрипт для добавления/изменения сотрудника через командную строку

Использование:
    python add_employee.py --username имя --first_name Имя --role admin
    python add_employee.py --username имя --edit --salary_rate 500
"""

import os
import django
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.accounts.models import User
from apps.staff.models import Employee
from django.utils import timezone

def add_employee(username, first_name=None, role='admin', salary_type='hourly', salary_rate=0):
    """Добавить нового сотрудника"""
    # Создаем или получаем пользователя
    user, created = User.objects.get_or_create(
        username=username,
        defaults={
            'first_name': first_name or username,
            'role': role,
            'email': f"{username}@club.local"
        }
    )
    
    if created:
        user.set_password('123456')
        user.save()
        print(f'[OK] Создан пользователь: {user.username}')
    else:
        print(f'[EXISTS] Пользователь уже существует: {user.username}')
        if first_name:
            user.first_name = first_name
            user.save()
            print(f'[UPDATED] Обновлено имя: {first_name}')
    
    # Создаем или получаем сотрудника
    employee, emp_created = Employee.objects.get_or_create(
        user=user,
        defaults={
            'salary_type': salary_type,
            'salary_rate': salary_rate,
            'hire_date': timezone.now().date(),
            'is_active': True
        }
    )
    
    if emp_created:
        print(f'[OK] Создан сотрудник: {user.get_full_name() or user.username}')
    else:
        print(f'[EXISTS] Сотрудник уже существует: {user.get_full_name() or user.username}')
    
    return employee

def edit_employee(username, **kwargs):
    """Изменить существующего сотрудника"""
    try:
        user = User.objects.get(username=username)
        employee = user.employee
    except User.DoesNotExist:
        print(f'[ERROR] Пользователь {username} не найден')
        return None
    except Employee.DoesNotExist:
        print(f'[ERROR] Сотрудник для пользователя {username} не найден')
        return None
    
    # Обновляем поля сотрудника
    if 'salary_rate' in kwargs:
        employee.salary_rate = kwargs['salary_rate']
    if 'salary_type' in kwargs:
        employee.salary_type = kwargs['salary_type']
    if 'is_active' in kwargs:
        employee.is_active = kwargs['is_active']
    
    employee.save()
    print(f'[UPDATED] Обновлен сотрудник: {user.get_full_name() or user.username}')
    return employee

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("""
Использование:
    
Добавить сотрудника:
    python add_employee.py --username имя --first_name Имя --role admin --salary_rate 500
    
Изменить сотрудника:
    python add_employee.py --username имя --edit --salary_rate 600
    
Параметры:
    --username      Логин пользователя (обязательно)
    --first_name    Имя сотрудника
    --role          Роль (owner/admin, по умолчанию: admin)
    --salary_type   Тип оплаты (salary/hourly, по умолчанию: hourly)
    --salary_rate   Ставка/оклад (по умолчанию: 0)
    --edit          Режим редактирования
    --is_active     Активен (true/false)
        """)
        sys.exit(1)
    
    # Парсинг аргументов
    args = {}
    i = 1
    while i < len(sys.argv):
        if sys.argv[i].startswith('--'):
            key = sys.argv[i][2:]
            if i + 1 < len(sys.argv) and not sys.argv[i + 1].startswith('--'):
                args[key] = sys.argv[i + 1]
                i += 2
            else:
                args[key] = True
                i += 1
        else:
            i += 1
    
    username = args.get('username')
    if not username:
        print('[ERROR] Укажите --username')
        sys.exit(1)
    
    if args.get('edit'):
        # Режим редактирования
        edit_kwargs = {}
        if 'salary_rate' in args:
            edit_kwargs['salary_rate'] = float(args['salary_rate'])
        if 'salary_type' in args:
            edit_kwargs['salary_type'] = args['salary_type']
        if 'is_active' in args:
            edit_kwargs['is_active'] = args['is_active'].lower() == 'true'
        
        edit_employee(username, **edit_kwargs)
    else:
        # Режим добавления
        add_employee(
            username=username,
            first_name=args.get('first_name'),
            role=args.get('role', 'admin'),
            salary_type=args.get('salary_type', 'hourly'),
            salary_rate=float(args.get('salary_rate', 0))
        )

