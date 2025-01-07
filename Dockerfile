
FROM python:3.11


WORKDIR /code


COPY ./requirements.txt /code/requirements.txt

COPY ./app/config.yaml /code/config.yaml
COPY ./app/logging.conf /code/logging.conf
RUN pip install --no-cache-dir -r /code/requirements.txt


COPY ./app /code/app

EXPOSE 80


CMD ["fastapi", "run", "app/main.py", "--port", "80"]