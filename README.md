
# Docker Compose

## Запуск приложения

1. **Клонирование репозитория**


   ```bash
   git clone https://github.com/rafalskypavel/WildberriesParser_DjangoDocker.git
   ```

2. **Переход в папку с проектом**


   ```bash
   cd dfrsite
   ```

3. **Запуск приложения с Docker Compose**


   ```bash
   docker-compose up
   ```

---

## Запуск контейнеров

- **Запуск всех сервисов и контейнеров**:
  ```bash
  docker-compose up
  ```

- **Запуск контейнеров в фоновом режиме**:
  ```bash
  docker-compose up -d
  ```

- **Запуск конкретного сервиса** (например, `postgres`):
  ```bash
  docker-compose up postgres
  ```

- **Запуск контейнеров для профиля `dev`**:
  ```bash
  docker-compose --profile dev up
  ```

- **Запуск остановленных контейнеров**:
  ```bash
  docker-compose start
  ```

- **Сборка образов**:
  ```bash
  docker-compose build
  ```

- **Запуск и пересборка образов**:
  ```bash
  docker-compose up --build
  ```

- **Перезапуск контейнеров**:
  ```bash
  docker-compose restart
  ```

---

## Остановка контейнеров

- **Остановка и удаление всех контейнеров и сетей**:
  ```bash
  docker-compose down
  ```

- **Удаление оставшихся контейнеров**:
  ```bash
  docker-compose down --remove-orphans
  ```

- **Остановка и удаление volumes**:
  ```bash
  docker-compose down --volumes
  ```

- **Остановка контейнеров без их удаления**:
  ```bash
  docker-compose stop
  ```

---

## Состояние контейнеров

- **Просмотр логов контейнеров**:
  ```bash
  docker-compose logs
  ```

- **Просмотр логов конкретного контейнера**:
  ```bash
  docker logs <container_name>
  ```

- **Просмотр статуса контейнеров**:
  ```bash
  docker-compose ps
  ```

- **Информация о процессах внутри контейнера**:
  ```bash
  docker-compose top
  ```

- **Настройки и состояние контейнера**:
  ```bash
  docker inspect <container_id>
  ```

---

## Масштабирование

- **Масштабирование количества контейнеров для сервиса**:
  ```bash
  docker-compose up -d --scale <service_name>=<num_instances>
  ```

---

## Выполнение команд внутри контейнера

- **Выполнение команд в контейнере**:
  ```bash
  docker-compose exec <container_id> <command>
  ```

- **Открытие консоли контейнера**:
  ```bash
  docker exec -it <container_id> /bin/sh
  ```

---

## Ресурсы

- **Видео**: [Docker Compose Demo](https://www.youtube.com/watch?v=0uLDObuutFs&t=1007s)
- **Исходный код**: [GitHub - docker-compose-demo](https://github.com/python-dev-blog/docker-compose-demo)

---

# Проект: Python Developer для работы на маркетплейсах

## Обязанности:
- Разработка API для сбора данных о товарах с маркетплейса Wildberries и их хранения в базе данных.
- Реализация двух эндпоинтов API с использованием Python, Django, DRF, PostgreSQL, Celery, Redis и Docker.

## Технические требования:
- Python 3.10+
- Django
- Django Rest Framework (DRF)
- PostgreSQL
- Celery
- Redis
- Docker

## Задание:

1. **API для получения информации о товаре**:
   - Эндпоинт принимает артикул товара Wildberries.
   - Запускает задачу Celery для сбора информации (остатки, склады, цена и т.д.).
   - Сохраняет эти данные в базе данных.

2. **API для вывода списка товаров**:
   - Эндпоинт выводит список товаров с информацией, полученной от первого эндпоинта.

## Дополнительные требования:
- Решение должно быть загружено в репозиторий на GitHub.
- В репозитории должен быть файл с инструкцией по установке и запуску проекта (например, README.md).
