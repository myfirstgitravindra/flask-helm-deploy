FROM python:3.11-slim
WORKDIR /app

COPY docker/prod/requirements.txt .
RUN python -m pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY app/ ./app

EXPOSE 5000

ENV FLASK_APP=app:create_app
ENV FLASK_ENV=production
ENV FLASK_RUN_HOST=0.0.0.0

CMD ["flask", "run"]
