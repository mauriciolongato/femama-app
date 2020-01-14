# femama-app


### Setup do ambiente de desenvolvimento


Clone o repositório

    git clone https://github.com/mauriciolongato/femama-app.git

Rode o docker-compose-dev
    
    sudo docker-compose -f docker-compose-dev.yml up

De permissão para o diretório .postgres-data e .static-volume 

    sudo chown -R $USER:$USER .
    
Setup do django - makemigrations, migrate and admin
    
    docker-compose -f docker-compose-dev.yml exec web python manage.py makemigrations
    docker-compose -f docker-compose-dev.yml exec web python manage.py migrate
    docker-compose -f docker-compose-dev.yml exec web python manage.py createsuperuser


Acesse: http://127.0.0.1:8000/admin


### Setup do ambiente de produção

Antes da descrição do processo de deploy, esse site foi muito útil! (valeu a referencia)
https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/

Clone o repositório

    git clone https://github.com/mauriciolongato/femama-app.git

Rode o docker-compose-prod
    
    sudo docker-compose -f docker-compose-prod.yml up

De permissão para o diretório .postgres-data e .static-volume 

    sudo chown -R $USER:$USER .
    
Setup do django - makemigrations, migrate and admin
    
    docker-compose -f docker-compose-prod.yml exec web python manage.py makemigrations
    docker-compose -f docker-compose-prod.yml exec web python manage.py migrate
    docker-compose -f docker-compose-prod.yml exec web python manage.py createsuperuser


Acesse: http://127.0.0.1:1337/admin