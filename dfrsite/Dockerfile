# Используем минимальный образ Python 3.12
FROM python:3.12-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем только необходимые файлы, сначала requirements.txt, затем весь код
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальной код
COPY . /app/

# Запускаем миграции, создание суперпользователя и сбор статики
CMD python manage.py makemigrations \
    && python manage.py migrate \
    && python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='root').exists() or User.objects.create_superuser('root', 'root@example.com', '1234')" \
    && python manage.py collectstatic --no-input \
    && gunicorn dfrsite.wsgi:application --bind 0.0.0.0:8000

