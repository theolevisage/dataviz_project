# Dataviz' project

This is a datavision project.

## Run project
Pour pouvoir lancer le projet il faut au préalable avoir installé `docker` et `docker-compose`.<br>
Il faut ensuite ouvrir un terminal et entrer la commande suivante :
```shell
docker-compose up
```
> **_NOTE:_**  Vous devrez peut être executer la commande précédé `sudo` si vous n'avez pas ajouté votre utilisateur au groupe docker

##  Architecture
_Schéma d'architecture_ 
![archi](https://user-images.githubusercontent.com/59962729/159161412-d6f5875a-1b5f-49a3-ab37-ba83afb04dd7.png)

Notre solution est composée de cinq unités de production connectées par un système de socket avec un collecteur de données. <br>
Ces deux parties sont réalisées en python. Le collecteur enregistre les données en base. <br><br>

D'un autre côté une API en node.js est connectée à notre base de données, elle permet de ne pas exposer notre connexion à la base de données dans le navigateur et donc d'en limiter l'accès.<br>
Cette API est requêtée par un front en vue.js qui tourne sur un serveur Nginx.<br><br>

Pour plus de détails sur chacune des parties qui compose l'architecture détaillée dans le schéma ci-dessus, se référer au README présent dans le dossier correspondant : 
 - U<sub>n</sub> => UniteProd https://github.com/theolevisage/dataviz_project/tree/main/UniteProd
 - Python collector => Collecteur https://github.com/theolevisage/dataviz_project/tree/main/Collecteur
 - Mariadb SGDB => MariaDB https://github.com/theolevisage/dataviz_project/tree/main/MariaDB
 - API Node.js => API https://github.com/theolevisage/dataviz_project/tree/main/API
 - Front running on Nginx => Nginx/front_dataviz_js https://github.com/theolevisage/dataviz_project/tree/main/Nginx/front_dataviz_js


