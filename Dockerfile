FROM python:3
ENV PYTHONUNBUFFERED 1
ENV DJANGO_ENV dev
ENV DOCKER_CONTAINER 1



WORKDIR /code/
COPY ./requirements.txt /code/requirements.txt
RUN pip install -r /code/requirements.txt
COPY . /code/

EXPOSE 8000
EXPOSE 6379