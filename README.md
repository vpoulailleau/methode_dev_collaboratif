# Méthode de développement collaboratif

## Projet

Vous devrez prévoir un code qui permet de répondre au jeu suivant : https://github.com/vpoulailleau/crystal_trucks

Contraintes :
* Python 3.10 sur PC
* Coopération avec git sur GitHub
  * Par équipe de 4
  * Par des pull requests

Votre code interagira sous forme de fichiers textes avec l'interface du jeu (`TODO prévoir stdin ?`), en respectant les règles à disposition dans le dépôt. Vous pouvez utiliser `game.py` qui est fourni, afin de générer les cartes à résoudre.
<<<<<<< HEAD

```python3
>>> import game
>>> game.init_game(4)
trucks: 6
width: 28
height: 11

### Grid ###
2   2 1          22       2 
1   21       2  2      111 1
  1    2 222   2       2    
  2     121 11       1  1   
 222   21221 2 11112    2 2 
21 11 21  1  2 22221 21  2  
 1   2   222     22 2    122
 2 112      1 1121 1 2   1 1
   12 1 1   1    11 1 2 1112
2  1 1  1112 1 12   211 22  
1  1  21       2  2    2  1 
### End Grid ###

Start!
```

Il est possible de capturer le résultat des `print` pour les traiter ensuite, avec `redirect_stdout` par exemple (https://stackoverflow.com/a/40984270/12199445).
=======
>>>>>>> refactoring

```python3
>>> import game
>>> game.init_game(4)
trucks: 6
width: 28
height: 11

### Grid ###
2   2 1          22       2 
1   21       2  2      111 1
  1    2 222   2       2    
  2     121 11       1  1   
 222   21221 2 11112    2 2 
21 11 21  1  2 22221 21  2  
 1   2   222     22 2    122
 2 112      1 1121 1 2   1 1
   12 1 1   1    11 1 2 1112
2  1 1  1112 1 12   211 22  
1  1  21       2  2    2  1 
### End Grid ###

Start!
```

Il est possible de capturer le résultat des `print` pour les traiter ensuite, avec `redirect_stdout` par exemple (https://stackoverflow.com/a/40984270/12199445).

## Algorithme

Allez d'abord au plus simple, afin d'avoir très vite un projet fonctionnel :
* pilotez un seul camion avec une double boucle sur les X et les Y, en creusant si un cristal est disponible
* pilotez ensuite un seul camion en allant au cristal le plus proche
* pilotez ensuite plusieurs camions qui collaborent

## Intégration continue

Mise en place de tests unitaires et d'intégration, joués en automatique sur GitHub à chaque pull request.

Mise en place de qualimétrie (flake8 ? black ?)

## Évaluation

* Présentation orale par équipe (30 minutes)
  * Présentation de la structure du code et des algorithmes principaux
  * Présentation de la méthodologie de test
  * Présentation de la qualimétrie
  * Présentation de l'automatisation (intégration continue)
  * Compétition : mesures des scores sur quelques cartes, pour avoir un meilleur score que les autres équipes
  * Note de groupe
