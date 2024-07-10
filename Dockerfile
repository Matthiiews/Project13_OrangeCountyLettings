# Utiliser une image officielle de Python comme image de base
FROM python:3.11-slim

# Définir certaines variables d'environnement
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Ajouter des variables d'environnement pour la production
ENV DJANGO_SETTINGS_MODULE=oc_lettings_site.settings_production

# Créez un répertoire nommé dans l’image Docker
RUN mkdir /app

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Installer les dépendances
COPY ./requirements.txt ./app/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r ./app/requirements.txt

# Copier les fichiers de l'application dans le conteneur
COPY . /app/

# Exposer le port sur lequel l'application va tourner
EXPOSE 8000

# Commande pour lancer l'application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
