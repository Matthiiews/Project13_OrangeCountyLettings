# Utiliser une image officielle de Python comme image de base
FROM python:3.11-slim

# Définir certaines variables d'environnement
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Ajouter des variables d'environnement pour la production
ENV DJANGO_SETTINGS_MODULE=oc_lettings_site.settings_production
ENV DJANGO_DATABASE_NAME=oc_lettings_site

# Créez un répertoire nommé dans l’image Docker
# RUN mkdir /app

# Définir le répertoire de travail dans le conteneur
WORKDIR  /usr/src/app

# Installer les dépendances
COPY ./requirements.txt  /usr/src/app/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copier les fichiers de l'application dans le conteneur
COPY  . /usr/src/app/

# Exposer le port sur lequel l'application va tourner
EXPOSE 8000

# Commande pour lancer l'application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
