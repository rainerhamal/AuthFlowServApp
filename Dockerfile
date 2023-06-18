FROM python:3.11

RUN pip install pipenv

WORKDIR /app

COPY Pipfile Pipfile.lock ./

RUN pipenv install --system

COPY . .

CMD ["python", "manage.py", "runserver"]