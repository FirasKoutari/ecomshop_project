# Utilise l'image officielle de Python comme image de base
FROM python:3.12.3-alpine

# Définit le répertoire de travail dans le conteneur
WORKDIR /app

# Copie le fichier requirements.txt dans le répertoire de travail
COPY requirements.txt .

# Installe les dépendances Python
RUN pip install -r requirements.txt

# Copie tout le contenu de votre projet Django dans le répertoire de travail
COPY . .

# Définit les variables d'environnement nécessaires
ENV PYTHONUNBUFFERED 1

# Expose le port que Django utilise par défaut
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "127.0.0.0:8000"]