.. Oclettings documentation master file, created by
   sphinx-quickstart on Wed Jul 17 14:18:12 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

======================================
Welcome to Oclettings's documentation!
======================================

Orange County Lettings est une agence de location immobilière. Sur le site, vous pouvez consulter plusieurs lieux de location ainsi que les profils des utilisateurs.

.. image:: images/lettings.png
   :alt: Orange County Lettings

Les technologies
----------------

Il s'agit d'une application écrite avec Django en langage Python. Les données sont stockées dans la base de données SQLite3.

Les différents outils utilisés pour le développement et le déploiement de cette application sont :
  - Github Actions pour la gestion de projet, le tableau des problèmes et les jalons 
  - Visual Studio Code pour le développement
  - Git pour le stockage du code et le contrôle de version
  - Sentinelle pour surveiller les performances du site
  - Docker et Docker Desktop pour la conteneurisation de code
  - GitHub actions pour l'intégration et la livraison continue de code
  - Lire la documentation, pour publier la documentation
  - AWS en tant qu'exécuteur pour le processus CI-CD
  - AWS EC2 pour le déploiement sur une url publique

.. toctree::
   :maxdepth: 3
   :caption: Table des matières:

   project_description
   installation
   quickstart
   base_de_données
   developpement
   guide_utilisation
   deploiement

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
