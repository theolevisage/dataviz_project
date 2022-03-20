# JS Front for datavision
A datavision project using vue.js, vue-router and vuetify

## état actuel

### Cas d'utilisation

_Schéma de cas d'utilisation_<br>
![usecase](https://user-images.githubusercontent.com/59962729/159162405-385dd415-6e29-40c6-8632-d1034823e8ed.png)

Nous avons réalisé un premier cas d'utilisation, un utilisateur doit pouvoir paramètrer les données qu'il visualise en ciblant:
 - Une unité de production et l'ensemble de ses automates
 - Un automate en particulier dans une unité de production
 - Toutes les données des unités de production (tous les automates)

_NB: Il y a une donnée redondante dans le diagramme de cas d'utilisation, en effet "tous les automates" ou "toutes les unités de production" correspondent à la même donnée_

## évolutions

Intégrer la librairie `axios` pour effectuer les requêtes sur l'API.<br>
D'autres paramètres devront être renseignés par l'utilisateur afin de cibler des informations en particulier (température cuve, température extérieur, ph, k+, ...)

Ce projet peut être lancé de manière autonome en suivant la procédure ci-dessous :
## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```
> **_NOTE:_** Pensez à changer les paramètres de connexion à la base de données si vous utilisez le projet indépendamment. 
