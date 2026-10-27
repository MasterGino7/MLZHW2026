FROM python:3.10-slim

WORKDIR /app

RUN pip install --no-cache-dir pipenv

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --skip-lock

RUN pip install --no-cache-dir "numpy>=2.0.0"

COPY ["predict.py", "churn-model.bin", "./"]

EXPOSE 9696

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "predict:app"]