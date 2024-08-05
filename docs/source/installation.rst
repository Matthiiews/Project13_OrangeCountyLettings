============
Installation
============

Ces étapes décrivent comment installer votre environnement de développement.

Cloner le dépôt GitHub
----------------------

.. code-block:: shell

   git clone https://github.com/Matthiiews/Project13_OrangeCountyLettings.git .

Créer l'environnement virtuel
-----------------------------

Un environnement virtuel est un répertoire qui contient une installation isolée de Python ainsi qu'un ensemble de paquets spécifiques à ce projet. Cela permet de :

  - Isoler les dépendances du projet des autres projets.
  - Faciliter la gestion des versions des paquets.
  - Éviter les conflits de versions entre les projets.

 - mkdir.venv
 - renommer le fichier .env.example en .env
 - ou python -m venv .venv
 - modifier les valeurs des variables pour les adapter à votre configuration (voir « Lier le projet à Sentry » pour la configuration de Sentry)
 - activer l'environnement sous windows : ./.venv/Scripts/activate
 - activer l'environnement sous Linux / mac os : source .venv/bin/activate
    
Lier le projet à Sentry
-----------------------

Sentry est une plateforme qui signale automatiquement les erreurs et les exceptions du projet. Elle permet également de surveiller les performances.

  - Créer un compte Sentry
  - Créer un projet avec la plateforme
  - Récupérez la clé DSN et intégrez-la dans votre fichier ''.env''
  - Connectez-vous à votre compte Sentry pour afficher les journaux récupérés par Sentry
  
Lancer le site
--------------

 - python manage.py runserver
 - allez à http://localhost:8000 avec votre navigateur
 - confirmer que le site fonctionne et qu'il est possible de naviguer à travers les différentes pages