# Dataviz' project
## UniteProd
Ce conteneur génère des données pour une unité de production. 

## Etat actuel
Le conteneur est fonctionnel, il génère des données alétoires dans les bornes définies.
Cette génération a lieu toutes les minutes.
Les données sont envoyées au conteneur Collecteur via une connection socket.
L'envoie des données est fonctionnel.
Le numéro de l'unité de production provient du fichier docker-compose.yml dans le dossier parent.

## Evolutions
Rendre les numéros des types d'automates paramétrables pour chaque unité de production, à la manière du numéro d'unité de production. 
