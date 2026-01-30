# Инструкция по загрузке на GitHub

## Шаг 1: Создайте репозиторий на GitHub

1. Перейдите на https://github.com
2. Войдите в свой аккаунт
3. Нажмите кнопку "+" в правом верхнем углу → "New repository"
4. Заполните:
   - **Repository name**: `cyberhub-manager` (или любое другое имя)
   - **Description**: "Веб-приложение для управления компьютерным клубом"
   - **Visibility**: Public или Private (на ваш выбор)
   - **НЕ** ставьте галочки на "Initialize with README", "Add .gitignore", "Choose a license" (у нас уже есть эти файлы)
5. Нажмите "Create repository"

## Шаг 2: Подключите локальный репозиторий к GitHub

После создания репозитория GitHub покажет вам команды. Выполните их в терминале:

```bash
# Добавьте remote репозиторий (замените YOUR_USERNAME на ваш GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/cyberhub-manager.git

# Или если используете SSH:
# git remote add origin git@github.com:YOUR_USERNAME/cyberhub-manager.git

# Переименуйте ветку в main (если нужно)
git branch -M main

# Загрузите код на GitHub
git push -u origin main
```

## Альтернативный способ (через GitHub CLI)

Если у вас установлен GitHub CLI:

```bash
gh repo create cyberhub-manager --public --source=. --remote=origin --push
```

## Важно!

- Файл `.env` с секретными ключами **НЕ** будет загружен (он в .gitignore)
- База данных `db.sqlite3` **НЕ** будет загружена (она в .gitignore)
- Все остальные файлы проекта будут загружены

## После загрузки

Ваш код будет доступен по адресу:
`https://github.com/YOUR_USERNAME/cyberhub-manager`
