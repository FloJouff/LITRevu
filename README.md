# LITRevu

## Description du projet:
  Le but de ce projet est de créer une application permettant à une communauté d'utilisateurs de consulter et/ou de demander des critiques littéraires.
  
## Fonctionnalités de l'application:
  Cette application permet aux utilisateurs :
    - de se connecter, se déconnecter et de s’inscrire sur le site.
    (Le reste du contenu du site n'est accessible qu'aux utilisateurs connectés)
    - de consulter un flux contenant les derniers tickets et les commentaires des utilisateurs qu'il suit, classés par ordre antichronologique.
    - de créer des critiques en réponse à des tickets
    - de créer de nouvelles critiques . Dans le cadre d'un processus en une étape, l'utilisateur créera un ticket puis un commentaire en réponse à son propre ticket
    - de voir, modifier et supprimer ses propres tickets et commentaires.
    - de suivre les autres utilisateurs en entrant leur nom d'utilisateur.
    - de voir la liste des utilisateurs qu'il suit et qui le suivent.
    - de bloquer un utilisateurs et de voir la liste des utlisateurs bloqués.
    
## Pré-requis:
   - Language de programmation:
      Python 3+
   - Module utilisé:
      - Django 5
   - Le fichier **requirements.txt** permet l'installation des modules nécessaires.

## Etapes d'installation:

#### Installer Python

L’installation de Python est très simple ! Rendez-vous sur [python.org](https://www.python.org/downloads/), choisissez votre système d’exploitation (Mac/Windows, etc.) et cliquez sur le bouton de téléchargement pour installer Python sur votre ordinateur.

Si vous utilisez Windows, pensez à bien cocher la case "Add to path" pour ajouter Python aux variables d'environnement.

#### Faire une copie du repository.

A partir du lien GitHub: https://github.com/FloJouff/LITRevu, créer un clone du projet en local sur votre ordinateur

#### Création de l'environnement virtuel

Depuis votre terminal, à la racine du projet, créer un environnement virtuel, afin d'y installer uniquement les paquets Python nécessaires à l'exécution du script.

    $ python -m venv env

#### Activation de l'environnement virtuel

A partir du terminal, taper la commande suivante:

    $ source env/bin/activate (pour MacOs, Linux)
    $ env\scripts\activate (pour Windows)

#### Installation des paquets Python nécessaires à l'execution du code:

Le fichier --requirements.txt-- a été cloné à partir du repository GitHub.
A partir du terminal, taper la commande suivante:

    $ pip install -r requirements.txt

Une fois l'installation terminée, taper la commande suivante pour vous assurer de l'installation correcte des modules requis:

    $ pip freeze

## Utilisation:
   - Exécuter le programme en tapant "py manage.py" dans la console ou à l'aide d'un éditeur de code.
   - Dans le terminal, tapez: 
      $ python manage.py runserver 
      pour lancer le serveur local.
   - Dans votre navigateur, rendez vous à l' adresse:" http://127.0.0.1:8000/" pour acceder au site.
