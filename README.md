# Quickstart

Установить Docker

https://docs.docker.com/compose/install/


Запуск

    docker-compose build
    docker-compose up -d
    docker-compose exec web python manage.py migrate
    docker-compose exec web python manage.py createsuperuser

http://localhost:8000/ - документация API (Swagger UI)

http://localhost:8000/admin/ - админ. панель
