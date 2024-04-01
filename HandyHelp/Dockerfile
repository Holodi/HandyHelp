# Використовуємо базовий образ Python
FROM python:3.9

# Встановлюємо залежності за допомогою pipenv
RUN pip install pipenv

# Встановлюємо залежності проекту
WORKDIR /app
COPY Pipfile Pipfile.lock /app/

# Копіюємо всі файли проекту в робочу директорію контейнера
COPY . /app/

# Команда для запуску сервера Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


