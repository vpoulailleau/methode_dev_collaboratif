# Méthode de développement collaboratif

## Projet

* Python 3.10 sur PC
* Coopération avec git sur GitHub
  * Par équipe de 4
  * Par des pull requests

Vous devrez prévoir un code qui permet de répondre au jeu suivant : https://github.com/vpoulailleau/crystal_trucks

Votre code interragira sous forme de fichiers textes avec l'interface du jeu (TODO prévoir stdin ?), en respectant les règles à disposition dans le dépôt. Vous pouvez utilisez `game.py` qui est fourni, afin de générer les cartes à résoudre.

## Algorithme

Allez d'abord au plus simple, afin d'avoir très vite un projet fonctionnel :
* pilotez un seul camion avec une double boucle sur les X et les Y
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
  * Compétition : mesures des scores sur quelques cartes, pour avoir un meilleur score que les autres équipes
  * Note de groupe
