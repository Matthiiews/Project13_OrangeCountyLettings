# Utiliser une image officielle de Python comme image de base
FROM python:3.11.4-slim-buster

# Définir certaines variables d'environnement
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Ajouter des variables d'environnement pour la production
ENV DJANGO_SETTINGS_MODULE=oc_lettings_site.settings
ENV DJANGO_DATABASE_NAME=oc_lettings_site
ENV DEBUG_VALUE=True

# Créez un répertoire nommé dans l’image Docker
# RUN mkdir /app

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Installer les dépendances
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Installer et configurer tzdata pour le fuseau horaire Europe/Paris
RUN apt-get update && DEBIAN_FRONTEND="noninteractive" TZ="Europe/Paris" apt-get install -y tzdata

# Copier les fichiers de l'application dans le conteneur
COPY . .

# Exposer le port sur lequel l'application va tourner
EXPOSE 8000

# Commande pour lancer l'application avec Gunicorn
#  CMD ["gunicorn", "--bind=0.0.0.0:8000", "oc_lettings_site.wsgi"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]