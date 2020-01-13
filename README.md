# tutorial-docker-django-celery

Simple django, docker and celery project written for learning purpouses

### Setup

Clone repository

    git clone https://github.com/mauriciolongato/femama-app.git

Run docker-compose
    
    sudo docker-compose up

Grant permission to postgres-data directory

    sudo chown -R $USER:$USER .
    
Set django - makemigrations, migrate and admin
    
    docker-compose exec web python manage.py makemigrations
    docker-compose exec web python manage.py migrate
    docker-compose exec web python manage.py createsuperuser
