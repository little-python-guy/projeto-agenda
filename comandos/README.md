Iniciar um projeto Django

```
python -m venv venv
.venv/Scripts/activate
pip install django
django-admin startproject project .
python manage.py runserver
python manage.py startapp contact
```

Migrando a base de dados do Django

```
python manage.py makemigrations
python manage.py migrate
```

Criando e modificando a senha de um super usuário

```
python manage.py createsuperuser
python manage.py changepassword USERNAME
```
