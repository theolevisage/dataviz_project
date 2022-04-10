# Dataviz' project
## MariaDB
Ce conteneur stocke les données envoyées par le Collecteur. 

## Etat actuel
A la création du conteneur, la base "datas" et les tables "production_unit", "automat" et "anomaly" sont créées si elles n'existent pas.
"production_unit" contient les noms des unités de production et un booléen de banissement.
"automat" contient les données envoyées par le collecteur provenant des différentes unités.
"anomaly" contiendra les données erronées.


Exemple de données insérées :
![image](https://user-images.githubusercontent.com/47949408/159161835-28d87d4d-f8a3-42ba-a666-4a030ca653c6.png)


