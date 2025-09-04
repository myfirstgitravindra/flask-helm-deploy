FROM python:3.11-slim
WORKDIR /app

COPY docker/dev/requirements-dev.txt .
RUN python -m pip install --upgrade pip && pip install --no-cache-dir -r requirements-dev.txt

COPY app/ ./app

EXPOSE 5000

ENV FLASK_APP=app:create_app
ENV FLASK_ENV=development
ENV FLASK_RUN_HOST=0.0.0.0

CMD ["flask", "run"]
