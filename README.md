# 🛒 Sarafan Backend Test Task

[![Django](https://img.shields.io/badge/Django-6.0.2-092E20?style=for-the-badge&logo=django)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/DRF-3.16.1-red?style=for-the-badge&logo=django)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-4169E1?style=for-the-badge&logo=postgresql)](https://www.postgresql.org/)
[![JWT](https://img.shields.io/badge/JWT-Auth-000000?style=for-the-badge&logo=json-web-tokens)](https://jwt.io/)

API для интернет-магазина с категориями, товарами и корзиной пользователя. 
Проект выполнен в рамках тестового задания  "Сарафан".

## ✨ Возможности

- 📁 **Категории и подкатегории** (с вложенностью и пагинацией)
- 📦 **Товары** с изображениями в 3-х размерах
- 🛍️ **Корзина пользователя** с подсчетом сумм
- 🔐 **JWT авторизация**
- 🖼️ **Админка** для управления контентом

## 🛠️ Технологии

```
🐍 Python 3.13
🌶️ Django 6.0
🎛️ Django REST Framework 3.16
🔐 JWT Authentication
🐘 PostgreSQL 16
📦 Poetry
```

## 🚀 Быстрый старт

### 1. Клонирование
```bash
git clone <url-вашего-репозитория>
cd sarafan_backend
```

### 2. Установка зависимостей
```bash
poetry install
poetry shell
```

### 3. Настройка базы данных PostgreSQL
```sql
CREATE DATABASE sarafan_db;
```

### 4. Создайте файл `.env`
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
DB_NAME=sarafan_db
DB_USER=postgres
DB_PASSWORD=your-password
DB_HOST=localhost
DB_PORT=5432
```

### 5. Миграции и запуск
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## 📚 API Документация

### 🔐 Аутентификация

<details>
<summary><b>Получение токена</b></summary>

**Request:**
```http
POST /api/token/
Content-Type: application/json

{
    "username": "admin",
    "password": "your-password"
}
```

**Response:**
```json
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc...",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```
</details>

<details>
<summary><b>Обновление токена</b></summary>

```http
POST /api/token/refresh/
Content-Type: application/json

{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```
</details>

### 📁 Категории (публичные)

<details>
<summary><b>GET /api/categories/</b></summary>

```http
GET /api/categories/
```

**Response:**
```json
{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "name": "Электроника",
            "slug": "elektronika",
            "image": null,
            "subcategories": [
                {
                    "id": 1,
                    "name": "Смартфоны",
                    "slug": "smartfony",
                    "image": null,
                    "category": 1,
                    "products": [ ]
                }
            ]
        }
    ]
}
```
</details>

### 📦 Товары (публичные)

<details>
<summary><b>GET /api/products/</b></summary>

```http
GET /api/products/
```

**Response:**
```json
{
    "id": 1,
    "name": "iPhone 17 Pro Max",
    "slug": "iphone-17-pro-max",
    "price": "1000000.00",
    "description": "",
    "subcategory": 1,
    "images": [
        {
            "id": 1,
            "image": {
                "full": "/media/products/iphone.jpg",
                "thumbnail": "/media/products/thumbnail_iphone.jpg",
                "medium": "/media/products/medium_iphone.jpg",
                "large": "/media/products/large_iphone.jpg"
            }
        }
    ]
}
```
</details>

### 🛒 Корзина (требуется JWT)

<details>
<summary><b>➕ Добавить товар</b></summary>

```http
POST /api/cart/add_item/
Authorization: Bearer <access_token>
Content-Type: application/json

{
    "product_id": 1,
    "quantity": 2
}
```
</details>

<details>
<summary><b>📋 Просмотр корзины</b></summary>

```http
GET /api/cart/
Authorization: Bearer <access_token>
```

**Response:**
```json
{
    "id": 1,
    "items": [ ],
    "total_items": 4,
    "total_price": 4000000.0
}
```
</details>

<details>
<summary><b>✏️ Изменить количество</b></summary>

```http
POST /api/cart/update_quantity/
Authorization: Bearer <access_token>
Content-Type: application/json

{
    "item_id": 1,
    "quantity": 5
}
```
</details>

<details>
<summary><b>🗑️ Удалить товар</b></summary>

```http
DELETE /api/cart/remove_item/
Authorization: Bearer <access_token>
Content-Type: application/json

{
    "item_id": 1
}
```
</details>

<details>
<summary><b>🧹 Очистить корзину</b></summary>

```http
DELETE /api/cart/clear/
Authorization: Bearer <access_token>
```
</details>

## 🎯 Задание №1: Последовательность

```python
def sequence(n):
    """Выводит первые n элементов последовательности 1223334444..."""
    result = []
    num = 1
    while len(result) < n:
        result.extend([num] * min(num, n - len(result)))
        num += 1
    return result

print(sequence(10))  # [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
```

## 📁 Структура проекта

```
sarafan_backend/
├── config/              # Настройки проекта
├── products/            # Приложение с товарами
│   ├── models.py        # Category, Subcategory, Product, ProductImage
│   ├── serializers.py   # Сериализаторы
│   ├── views.py         # ViewSets
│   └── admin.py         # Админка
├── cart/                 # Приложение корзины
│   ├── models.py        # Cart, CartItem
│   ├── serializers.py   # Сериализаторы с подсчетом сумм
│   └── views.py         # ViewSet с кастомными actions
├── media/                # Загруженные изображения
├── manage.py
├── pyproject.toml        # Зависимости (Poetry)
└── .env                  # Переменные окружения
```

## ✅ Выполненные требования

- [x] Категории и подкатегории в админке
- [x] Slug и изображения у категорий
- [x] Связь подкатегорий с родителями
- [x] API категорий с подкатегориями и пагинацией
- [x] CRUD продуктов в админке
- [x] Изображения товаров в 3-х размерах
- [x] API продуктов с пагинацией
- [x] Корзина: добавление, изменение, удаление
- [x] Подсчет количества и суммы в корзине
- [x] Очистка корзины
- [x] Публичный доступ к категориям и товарам
- [x] Приватный доступ к корзине (только свои)
- [x] JWT авторизация
- [x] Задание №1 (последовательность)

## 📄 Лицензия

Проект распространяется под [лицензией MIT](LICENSE)

---
## 👨‍💻 Разработчик

### Василий - tanec_991@mail.ru


<div align="center">
  <sub>Тестовое задание "Сарафан"</sub>
  <br>
  <sub>⭐ Не забудьте поставить звезду, если проект понравился!</sub>
</div>