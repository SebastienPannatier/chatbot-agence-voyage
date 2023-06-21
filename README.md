# Projet de travail de diplôme : Utilisation des graphes de connaissances pour améliorer l'interaction utilisateur-chatbot

## Aperçu
Ce projet de travail de diplôme, réalisé dans le cadre de ma formation à l'ESIG, se concentre sur l'utilisation des graphes de connaissances pour améliorer l'interaction entre les utilisateurs et les chatbots. Le but principal de ce projet est de développer un chatbot pour une agence de voyage qui tirera parti des graphes de connaissances afin de fournir des réponses précises et pertinentes aux utilisateurs.

Le code source de ce projet est hébergé dans le référentiel Git intitulé "chatbot-agence-voyage". Ce référentiel contient toutes les ressources nécessaires pour comprendre, développer et exécuter le chatbot.

## Fonctionnalités clés
- Analyse sémantique des requêtes utilisateur : Le chatbot utilise des techniques d'analyse sémantique pour comprendre les intentions des utilisateurs et extraire les entités clés dans leurs requêtes.
- Construction du graphe de connaissances : Un graphe de connaissances est créé en utilisant des ontologies ou des bases de données existantes sur le domaine du voyage. Ce graphe permet de représenter les connaissances et les relations entre les entités du domaine.
- Requêtes basées sur le graphe de connaissances : Le chatbot utilise le graphe de connaissances pour effectuer des recherches et récupérer des informations spécifiques sur les les hôtels et les restaurants.
- Suggestions contextuelles : Le chatbot utilise le contexte de la conversation pour fournir des suggestions pertinentes à l'utilisateur, basées sur les choix précédents ou les préférences enregistrées.

## Structure du référentiel
Le référentiel "chatbot-agence-voyage" est organisé de la manière suivante :
```
- /sources : Ce répertoire contient les données de la base de connaissances ainsi que son schéma et son script d'insertion.
- /chatbot : Ce répertoire contient le code source principal du chatbot, y compris les modules de traitement du langage naturel et la logique de conversation.
```

## Prérequis
Avant de pouvoir exécuter le chatbot, assurez-vous d'avoir les éléments suivants :

- Python 3.9.11 installée sur votre système.
- Rasa 3.5.5 installé dans un environement virtuel ou sur votre système.
- Les données nécessaires au fonctionnement du chatbot (disponibles dans le répertoire `/sources`).

## Guide d'installation et d'exécution
Pour installer et exécuter le chatbot sur votre système, veuillez suivre les étapes ci-dessous :

1. Clonez ce référentiel Git sur votre machine locale :
```
git clone https://github.com/SebastienPannatier/chatbot-agence-voyage
```

2. Accédez au répertoire du chatbot :
```
cd chatbot
```
3. Exécutez le bot :
```
python -m rasa shell
```
## Auteurs
- Pannatier Sébastien

## Licence
Ce projet est sous licence MIT. Consultez le fichier `LICENSE` pour plus d'informations.

## Remerciements
je tiens à remercier tous ceux qui ont apporté leur soutien pendant la réalisation de ce projet.

Merci et bon voyage avec notre chatbot !