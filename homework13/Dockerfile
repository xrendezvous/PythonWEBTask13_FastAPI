FROM python:3.12

WORKDIR /app

COPY . /app

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

EXPOSE 8000

ENV NAME World

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
