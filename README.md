Сервис рассылок
Разработан на django rest framework с django-rq и rq-scheduler
Установка и запуск

Склонировать репозиторий с Gitlab:
git clone git@gitlab.com:iesambaev/mailing_service.git

Перейти в директорию проекта

Создать виртуальное окружение:
python -m venv venv

Активировать окружение:
source\venv\bin\activate

В файле .env заполнить необходимые данные: TOKEN = '<your token>'

Установка зависимостей:
pip install -r requirements.txt

Создать и применить миграции в базу данных:
python manage.py makemigrations
python manage.py migrate

Запустить сервер
python manage.py runserver

Запустить worker
    python manage.py rqworker --with-scheduler
    для mac os: OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES python manage.py rqworker --with-scheduler

Запуск тестов
python manage.py test


Установка проекта с помощью docker-compose

1.Склонировать репозиторий с Gitlab
git clone git@gitlab.com:iesambaev/mailing_service.git

Перейти в директорию проекта

2.В файле .env заполнить необходимые данные: 
TOKEN = '<your token>'

3.Запустить контейнеры
sudo docker-compose up -d

4.Остановка работы контейнеров
sudo docker-compose stop


http://0.0.0.0:8000/api/ - api проекта
    
http://0.0.0.0:8000/api/clients/ - клиенты
    
http://0.0.0.0:8000/api/mailings/ - рассылки
    
http://0.0.0.0:8000/api/mailings/fullinfo/ - общая статистика по всем рассылкам
    
http://0.0.0.0:8000/api/mailings//info/ - детальная статистика по конкретной рассылке
    
http://0.0.0.0:8000/api/messages/ - сообщения
    
http://0.0.0.0:8000/docs/ - docs проекта
    
http://0.0.0.0:8000/admin/ - админ панель сервиса
    
http://0.0.0.0:8000/admin/django-rq/ - панель управления рассылок
