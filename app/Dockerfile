FROM python:3.12

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

COPY . /app/

EXPOSE 8000

ENV PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE=core.settings \
    DJANGO_SECRET_KEY=your-secret-key

CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]