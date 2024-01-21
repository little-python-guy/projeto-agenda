# Projeto Agenda (com Django Web Framework)

Projeto feito no curso de Python do instrutor Luiz Otávio (link para o curso na
Udemy: [https://www.udemy.com/course/python-3-do-zero-ao-avancado/](url))

## Ferramentas utilizadas
- Visual Code Studio;
- Python 3.11.1
- Django Web Framework;
- Pillow (para trabalhar com imagens);
- Faker (para preencher a base de dados);
- SQLite3 e PostgreSQL (base de dados);
- Google Cloud Platform (para o servidor);
- Máquina Virtual (Linux - Ubuntu 20.04 LTS);
- Gunicorn (configuração do servidor);
- Nginx (configuração do protocolo HTTP).

## Iniciar um projeto Django

```
python -m venv venv
.venv/Scripts/activate
pip install django
django-admin startproject project .
python manage.py runserver
python manage.py startapp contact
```

## Migrando a base de dados do Django

```
python manage.py makemigrations
python manage.py migrate
```

## Criando e modificando a senha de um super usuário

```
python manage.py createsuperuser
python manage.py changepassword USERNAME
```

## Trabalhando com o model do Django

```python

# Importe o módulo
from contact.models import Contact

# Cria um contato (Lazy - sem salvar na página de admin)
# Retorna o contato
contact = Contact(**fields)

# Salva o contato na página de contatos em admin
contact.save()

# Cria um contato (Não Lazy)
# Retorna o contato
contact = Contact.objects.create(**fields)

# Seleciona um contato com id 10
# Retorna o contato
contact = Contact.objects.get(pk=10) # pk = primary key

# Edita um contato
# Retorna o contato
contact.field_name1 = 'Novo valor 1'
contact.field_name2 = 'Novo valor 2'
contact.save()

# Apaga um contato
# Depende da base de dados, geralmente retorna o número
# de valores manupulados na base de dados
contact.delete()

# Seleciona todos os contatos ordenando por id (ordem decrescente)
# Retorna QuerySet[]
contacts = Contact.objects.all().order_by('-id')

# Seleciona contatos usando filtros (Lazy)
# Retorna QuerySet[]
contacts = Contact.objects.filter(**filters).order_by('-id')

```
