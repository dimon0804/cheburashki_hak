# Используем официальный Python образ
FROM python:3.10-slim

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Устанавливаем зависимости для установки Poetry
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python3 - && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Добавляем Poetry в PATH
ENV PATH="/root/.local/bin:$PATH"

# Копируем файлы зависимостей Poetry
COPY pyproject.toml poetry.lock ./

# Устанавливаем зависимости проекта
RUN poetry install --no-root --only main

# Копируем исходный код проекта
COPY . .

# Указываем команду для запуска приложения
CMD ["poetry", "run", "python", "main.py"]
