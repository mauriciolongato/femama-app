# tutorial-docker-django-celery

Simple django, docker and celery project written for learning purpouses

### Setup

Clone repository

    git clone https://github.com/mauriciolongato/tutorial-docker-django-celery.git

Run docker-compose
    
    sudo docker-compose up

Grant permission to postgres-data directory

    sudo chown -R $USER:$USER .
    
Set django - makemigrations, migrate and admin
    
    docker-compose run web python manage.py makemigrations
    docker-compose run web python manage.py migrate
    docker-compose run web python manage.py createsuperuser