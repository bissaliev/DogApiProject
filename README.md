# DogApiProject

Проект представляет собой RESTful API для управления данными о собаках и породах собак, реализованный на Django и Django REST Framework (DRF). API позволяет создавать, получать, обновлять и удалять записи о собаках и породах, включая дополнительные вычисляемые данные, такие как средний возраст собак породы и количество собак.

## Основные компоненты

- **Модели**: `Dog` и `Breed`, определённые в `dogs/models.py`.
- **Сериализаторы**: `DogCreateSerializer`, `DogReadSerializer`, `BreedSerializer` в `api/serializers.py`.
- **Вьюсеты**: `DogViewSet` и `BreedViewSet` в `api/views.py` для обработки CRUD-операций.
- **Кастомные QuerySet**: Реализованы в `dogs/querysets.py` с использованием подзапросов для оптимизации.
- **Маршрутизация**: Использует DRF-роутеры в `api/urls.py`.
- **Контейнеризация**: Поддержка Docker и Docker Compose.

## Стек

- Python 3.12
- PostgreSQL 15
- Docker (опционально)
- Django 5.1
- Django Rest Framework 3.15

## Установка и запуск

### Локальная установка

1. Клонируйте репозиторий:

    ```bash
    git clone git@github.com:bissaliev/DogApiProject.git
    cd DogApiProject/
    ```

2. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

3. Настройте переменные окружения в .env (см. .env.example)

4. Примените миграции:

    ```bash
    python manage.py migrate
    ```

5. Загрузить фикстуры для моделей `Breed`, `Dog`:

    ```bash
    python manage.py loaddata fixtures/breeds.json
    python manage.py loaddata fixtures/dogs.json
    ```

6. Запустите сервер:

    ```bash
    python manage.py runserver
    ```

### Использование `Docker`

1. Убедитесь, что `Docker` и `Docker Compose` установлены.
2. Скопируйте `.env.example` в `.env` и настройте переменные.
3. Запустите контейнеры:

    ```bash
    docker-compose up --build
    ```

4. Примените миграции в контейнере:

    ```bash
    docker-compose exec web python manage.py migrate
    ```

5. Загрузить фикстуры для моделей `Breed`, `Dog`:

    ```bash
    docker-compose exec web python manage.py loaddata fixtures/breeds.json
    docker-compose exec web python manage.py loaddata fixtures/dogs.json
    ```

API будет доступно по адресу <http://localhost:8000/api/v1/>.

## Структура проекта

- `dogs/` — приложение с моделями, кастомными QuerySet и админкой.
- `api/` — приложение с сериализаторами, вьюсетами и URL-маршрутами.
- `.env` — файл с переменными окружения.
- `Dockerfile` — сборка образа приложения.
- `docker-compose.yml` — конфигурация сервисов (Django + PostgreSQL).

## API Эндпоинты

### Собаки (`/api/dogs/`)

- `GET /api/dogs/`: Получить список собак с аннотацией среднего возраста породы.

  - Ответ:

      ```json
      [
        {
          "id": 1,
          "name": "Rex",
          "age": 7,
          "breed": "Labrador",
          "gender": "Male",
          "color": "Коричневый",
          "favorite_food": "food",
          "favorite_toy": "toy",
          "avg_breed_age": 5
        }
      ]
      ```

- `POST /api/dogs/`: Создать собаку.

  - Запрос:

    ```json
    {
        "name": "Max",
        "age": 6,
        "breed": 2,
        "gender": "Male",
        "color": "Черный",
        "favorite_food": "food",
        "favorite_toy": "toy"
    }
    ```

- `GET /api/dogs/<id>/`: Получить собаку с количеством собак той же породы.
  - Ответ:

    ```json
    {
        "id": 1,
        "name": "Rex",
        "age": 7,
        "breed": "Labrador",
        "gender": "Male",
        "color": "Коричневый",
        "favorite_food": "food",
        "favorite_toy": "toy",
        "count_breed_dogs": 4
    }
    ```

- `PUT /api/dogs/<id>/`: Обновить собаку.
  - Запрос:

    ```json
    {
        "name": "Update Max",
        "age": 6,
        "breed": 2,
        "gender": "Male",
        "color": "Черный",
        "favorite_food": "food",
        "favorite_toy": "toy"
    }
    ```

- `DELETE /api/dogs/<id>/`: Удалить собаку.

### Породы (`/api/breeds/`)

- `GET /api/breeds/`: Получить список пород с количеством собак.
  - Ответ:

    ```json
    [
        {
            "id": 1,
            "name": "Labrador",
            "size": "Large",
            "friendliness": 5,
            "trainability": 1,
            "shedding_amount": 2,
            "exercise_needs": 1,
            "count_dogs": 4
        }
    ]
    ```

- `POST /api/breeds/`: Создать породу.
  - Запрос:

    ```json
    {
        "name": "Labrador",
        "size": "Large",
        "friendliness": 5,
        "trainability": 1,
        "shedding_amount": 2,
        "exercise_needs": 1,
    }
    ```

- `GET /api/breeds/<id>/`: Получить породу.
  - Ответ:

    ```json
    {
        "id": 1,
        "name": "Labrador",
        "size": "Large",
        "friendliness": 5,
        "trainability": 1,
        "shedding_amount": 2,
        "exercise_needs": 1,
        "count_dogs": 4
    }
    ```

- `PUT /api/breeds/<id>/`: Обновить породу.
  - Запрос:

      ```json
      {
          "name": "Update Labrador",
          "size": "Large",
          "friendliness": 5,
          "trainability": 1,
          "shedding_amount": 2,
          "exercise_needs": 1,
      }
      ```

- `DELETE /api/breeds/<id>/`: Удалить породу.
