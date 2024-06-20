@echo off

rem Création des migrations pour chaque application
python manage.py makemigrations ProductsApp
python manage.py makemigrations PaymentApp
python manage.py makemigrations MainApp
python manage.py makemigrations AuthenticationApp
python manage.py makemigrations CartApp


rem Application des migrations
python manage.py migrate

rem Démarrage du serveur de développement
python manage.py runserver