# AnFristPost
Consiste na criação do primeiro Blog para demostração no Curso WTTD. pela Indagação  "Você já criou seu blog hoje?"

## Como rodar o projeto?

* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.

##-Usando-Linux
```
No Terminal
git clone https://github.com/vladetec/AnFristPost.git
cd AnFristPost
python3 -m venv env
source env/bin/activate
pip install -U pip wheel setuptools
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate
python manage.py createsuperuser --email admin@example.com --username admin
python manage.py runserver
```
##-Caso-Windows
```
cmd
git clone https://github.com/vladetec/AnFristPost.git
cd AnFristPost
python -m venv env
cd env/Scripts
activate
pip install -U pip wheel setuptools
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Links - Tecnologias Utilitarias

[Python](https://www.python.org/)
[Django](https://www.djangoproject.com/)
[Django-Rest-Framework](https://www.django-rest-framework.org/)
[Insomnia](https://insomnia.rest/download/)
[Db-Browser](https://sqlitebrowser.org/)
[PostgresSQL](https://www.postgresql.org/)
[Templates](https://html5up.net/)
[VsCode](https://code.visualstudio.com/)
[PyCharm](https://www.jetbrains.com/pt-br/pycharm/)
[emmet](https://emmet.io/)
[Python-Dcouple](https://github.com/henriquebastos/python-decouple)