# Dataviz' project
## Collecteur
Ce conteneur reçoit les données des unités de production et envoie des requêtes d'insertion vers le conteneur Mariadb. 

## Etat actuel
Le conteneur est fonctionnel, il raeçoit les données des différentes unités de production grâce à une connexion multisocket.
Il convertit ces données puis envoie des requêtes sql d'insertion vers Mariadb.

## Evolutions
Des évolutions seront apportées dans le prochain cours afin de traiter les données avant leurs insertions.
