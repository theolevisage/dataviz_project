# Dataviz' project
## UnitProd
Ce conteneur génère des données pour une unité de production. 

## Etat actuel
Le conteneur est fonctionnel, il génère des données alétoires dans les bornes définies.
Cette génération a lieu toutes les minutes.
Les données sont envoyées au conteneur Collecteur via une connection socket.
L'envoie des données est fonctionnel.
Le numéro de l'unité de production provient du fichier docker-compose.yml dans le dossier parent.

## Evolutions
Rendre les numéros des types d'automates paramétrables pour chaque unité de production, à la manière du numéro d'unité de production. 

## Sécurité
Le premier échange entre les unités de production et le collecteur sert à l'échange des clés assymétriques, les échanges suivants sont chiffrés avec les clés RSA ainsi récupérées.
Les clés sont gérées avec GPG

_Diagramme d'activité_
![archi](https://cdn.discordapp.com/attachments/900310417862189136/962698350342316062/production_unit_diagram.drawio.png)

