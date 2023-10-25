# Chapitre 3 : Création d'un Smart Contrat "Loterie"

Dans ce troisième chapitre, nous allons explorer la création d'un contrat intelligent de loterie sur une blockchain. La loterie est un exemple classique d'utilisation des contrats intelligents pour créer une application de jeu décentralisée. Le contrat que nous allons créer permettra aux participants de miser une somme d'argent en ETH et de tenter leur chance pour remporter le jackpot.

## Contrat de Loterie en Solidity

Le contrat de loterie est écrit en Solidity, un langage de programmation spécifiquement conçu pour créer des contrats intelligents sur la blockchain. Ce contrat permet aux participants de miser une somme d'argent en ETH et de tenter leur chance pour remporter le jackpot.

**Explication du contrat de loterie** :

- Le contrat "Loterie" permet au gestionnaire (manager) de créer une loterie et de superviser son fonctionnement.

- Les joueurs peuvent participer en utilisant la fonction `enter()`. Ils doivent miser une somme minimale de 0.01 ether pour participer.

- Une fois que suffisamment de joueurs ont rejoint la loterie, le gestionnaire peut déclencher la fonction `triggerWinner()` pour choisir un gagnant de manière aléatoire. Le gagnant reçoit tout l'ETH accumulé dans la cagnotte.

- Le contrat utilise une fonction pour générer un nombre aléatoire basé sur divers paramètres, notamment le bloc actuel, l'horodatage et la liste des joueurs.

- Le contrat comprend des modificateurs pour restreindre certaines opérations aux seuls gestionnaires.

- Enfin, le contrat peut être réinitialisé pour permettre de nouvelles participations.

Maintenant que nous avons introduit le contrat de loterie, nous allons explorer comment déployer ce contrat et interagir avec lui dans les prochaines sections de ce tutoriel.

Vous pouvez consulter le code source complet du contrat de loterie en Solidity dans le fichier [loto.sol](./chapitre3/loto.sol).