==========================
Processus de développement
==========================

Exécutez le site localement avec Django
---------------------------------------

  - démarrer l'environnement virtuel [1]_
  - python manage.py collectstatic
  - python manage.py runserver
  - allez à http://localhost:8000 avec votre navigateur
  - allez sur http://localhost:8000/admin pour accéder au panneau d'administration
    vous pouvez vous connecter avec l'utilisateur admin et le mot de passe Abc1234 !
  - allez sur http://localhost:8000/sentry-debug/ pour générer une ZeroDivisionError et vérifier votre compte Sentry

Exécutez le site localement via Docker
--------------------------------------

Créer un compte dockerhub
- installer docker desktop
- récupérer l'image docker pour exécuter l'application localement : docker pull slb59/lettings
- assurez-vous que le serveur local n'est pas en cours d'exécution
- lancer le serveur : docker compose -f compose/docker-compose.yml up -d
- le site devrait fonctionner de la même manière avec les mêmes URL, comme si vous utilisiez la procédure locale
- Pour arrêter le serveur sans supprimer les ressources créées : docker compose stop, et pour l'arrêter en détruisant toutes les      ressources créées : docker compose down
  
.. [1]	En définissant la variable DEBUG dans le fichier .env sur true, vous pouvez afficher la barre d'outils de débogage

Contrôle de qualité
-------------------

Linting
---------

- Activer l'environnement virtuel
- Flake8 est un wrapper autour de ces outils :

   - PyFlakes
   - style de code pycode
   - Scénario de McCabe de Ned Batchelder
    
   .. code-block:: shell

      flake8

isort
-----

- isort est un utilitaire/bibliothèque Python permettant de trier les importations par ordre alphabétique et de les séparer automatiquement en sections et par type
   .. code-block:: shell
      
      isort . --check

black
-----

- black est le formateur de code Python sans compromis.
   .. code-block:: shell
      
      black . --check

pylint
------

- pylint est un analyseur de code statique pour Python 2 ou 3.
   .. code-block:: shell

      pylint . --recursive=y > logs/pylint.txt
  
   alors vous pouvez vérifier le fichier logs/pylint.txt

Pytest
------

- Le framework pytest facilite l'écriture de tests unitaires
   .. code-block:: shell
      
      pytest

Vous pouvez vérifier la couverture des tests avec :
   .. code-block:: shell

      pytest --cov=. --cov-report=html

puis vérifiez le résultat dans htmlcov.index.html

Vous pouvez également consulter le rapport HTML logs/pytest-report.html avec :
    .. code-block:: shell

       pytest --html=logs/pytest-report.html