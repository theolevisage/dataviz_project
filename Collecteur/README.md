# Dataviz' project
## Collecteur
Ce conteneur reçoit les données des unités de production et envoie des requêtes d'insertion vers le conteneur Mariadb. 

## Etat actuel
Le conteneur est fonctionnel, il reçoit les données des différentes unités de production grâce à une connexion socket multi-thread.
Il reçoit tout d'abord les clés publiques des unités et les enregistre dans son trousseau de clé. Il envoie en retour sa clé publique.
Il reçoit ensuite les différentes données chiffrées produites par les unités.
Il les déchiffre avec sa clé privée, vérifie si l'unité est bannie ou non, vérifie la preuve de travail et envoie des requêtes d'insertion vers Mariadb si tout est bon.
Il envoie en retour à l'unité de production un message chiffré inidquant l'insertion des données et la date du fichier concernée.

## Evolutions
Des évolutions seront apportées dans le prochain cours afin de traiter les données avant leurs insertions.
