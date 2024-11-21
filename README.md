# **Docker Compose**

## Запуск приложения

git clone git@github.com:python-dev-blog/docker-compose-demo.git
cd dfrsite
docker-compose up


### Запуск контейнеров

docker inspect - запускает все сервисы и контейнеры на основе вашего docker-compose.yml файла
docker-compose up -d - запускает все контейнеры в фоновом режиме (не блокирует консоль)
docker-compose up postgres> - запускает определенный сервис (вместо postgres подставьте нужный)
docker-compose --profile dev up - запускает только те контейнеры, которые относятся к профилю dev
docker-compose start - запускает остановленные контейнеры
docker-compose build - собирает образы
docker-compose up --build - запускает и одновременно пересобирает образы, если они были изменены с момента последнего запуска или если они еще не были созданы
docker-compose restart - перезапустить контейнеры

## Остановка контейнеров

docker-compose down - останавливает и удаляет все контейнеры и сети, созданные с помощью docker-compose up
docker-compose down --remove-orphans - если какие-либо контейнеры остаются после остановки всех сервисов, которые изначально их создали, то эти оставшиеся контейнеры также будут удалены
docker-compose down --volumes - останавливает контейнеры и удаляет связанные с ними volumes
docker-compose stop - останавливает контейнеры, созданные с помощью docker-compose up, без их удаления

### Состояние контейнеров

docker-compose logs - просмотреть логи
docker logs <container_name> - посмотреть логи конкретного контейнера
docker-compose ps - просмотреть статус запущенных контейнеров
docker-compose top - отображает информцию о процессах внутри контейнеров
docker inspect <container_id> - показывает json с настройками контейнера и его состоянием

### Масштабирование

docker-compose up -d --scale <service_name>=<num_instances> - масштабирует количество запущенных контейнеров для указанного сервиса
Выполнение команд внутри контейнера
docker-compose exec <container_id> <command> - позволяет выполнять команды внутри контейнера, например docker exec 7cbde5a06bbb pytest api/tests.py
docker exec -it <container_id> /bin/sh - открыть консоль контейнера

Based on:
https://www.youtube.com/watch?v=0uLDObuutFs&t=1007s
https://github.com/python-dev-blog/docker-compose-demo


## Проект в рамках вакансии на Python Developer / Разработчик Python для работы на маркетплейсах

Обязанности: 
Ваша задача — разработка API для сбора данных о товарах с маркетплейса Wildberries и их хранения в базе данных. 
Необходимо реализовать два эндпоинта API с использованием Python, Django, DRF, PostgreSQL, Celery, Redis и Docker.

Технические требования:

**Python 3.10+
Django
Django Rest Framework (DRF)
PostgreSQL
Celery
Redis
Docker
Задание:**

### API для получения информации о товаре:

Эндпоинт должен принимать артикул товара Wildberries, например: 206021772 (ссылка на товар: https://www.wildberries.ru/catalog/111111111/detail.aspx).
На основе артикулы необходимо запускать задачу Celery, которая будет собирать как можно больше информации о товаре (например, остатки, склады, на которых есть остатки, цена и другие данные). 
Эти данные должны быть сохранены в базу данных.
Структуру базы данных для хранения этой информации вам нужно разработать самостоятельно.
API для вывода списка товаров:
Эндпоинт должен выводить список товаров с информацией о каждом товаре, полученной в результате работы первого эндпоинта.
Дополнительные требования:
Ваше решение должно быть загружено в репозиторий на GitHub.
В репозитории должен быть файл с инструкцией по установке и запуску проекта (например, в README.md).