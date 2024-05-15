# LITRevu

## Description du projet:
  Le but de ce projet et de créer une MVP pour une application permettant à une communauté d'utilisateurs de consulter ou de solliciter une critique de livres à la demande.
  
## Fonctionnalités du programme:
  Ce programme permet:
    - se connecter et s’inscrire 
    - le site ne doit pas être accessible à un utilisateur non connecté
    - consulter un flux contenant les derniers tickets et les commentaires des utilisateurs qu'il suit, classés par ordre chronologique, les plus récents en premier 
    - créer des critiques en réponse à des tickets
    - créer des critiques qui ne sont pas en réponse à un ticket. Dans le cadre d'un processus en une étape, l'utilisateur créera un ticket puis un commentaire en réponse à son propre ticket
    - voir, modifier et supprimer ses propres tickets et commentaires
    - suivre les autres utilisateurs en entrant leur nom d'utilisateur
    - voir qui il suit et suivre qui il veut ainsi que de cesser de suivre un utilisateur
    
## Pré-requis:
   - Language de programmation:
      Python3
   - Module utilisés:
      - Django 4
   - Le fichier **requirements.txt** permet l'installation des modules nécessaires.

## Installation:
   - Créer un dossier à la racine du projet.
   - Copier et dézipper l' archive dans le dossier ou utiliser la commande "git clone".
   - Ouvrir une console et se placer dans le dossier.
   - Créer un environnement virtuel grâce à la commande " py -m venv env".
   - Activer l'environnent virtuel avec la commande : "source env/Scripts/activate".(Mac)
   - Installer les packages nécessaires avec la commande : " pip install -r requirements.txt".

## Utilisation:
   - Exécuter le programme soit en tapant "py manage.py" dans la console ou au travers d'un éditeur de code.
   - Dans le terminal, tapez: "python manage.py runserver" pour lancer le serveur local.
   - Dans votre navigateur internet , rendez vous à l' adresse:" http://127.0.0.1:8000/" pour acceder au site
