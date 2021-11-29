Create Project
    
    S.O.: Linux Ubuntu 20.04
    Python version: 3.8.10

## command code
    mkdir python_project_api

    cd python_project_api

    virtualenv -p python3 env
    . env/bin/activate

    pip install -r requirements.txt

    django-admin startproject project
    cd project/
    django-admin startapp api

## make migration
python3 manage.py makemigrations api --name users --empty

## exec migration
python3 manage.py migrate

## show migrations
python3 manage.py showmigrations api

## revert migration
python3 manage.py migrate api 0001