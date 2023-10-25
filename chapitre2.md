# Chapitre 2 : Création d'un Smart Contrat "Hello World"

Dans ce deuxième chapitre, nous allons explorer en détail la création et le déploiement d'un smart contrat "Hello World" sur une blockchain. Ce contrat est écrit en Solidity, un langage de programmation pour les contrats intelligents, et il sera déployé à l'aide de Web3, une bibliothèque Python pour interagir avec la blockchain.

## Contrat "Hello World" en Solidity

Le contrat "Hello World" en Solidity est un exemple simple de contrat intelligent. Voici son code :

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract HelloWorld {
    string public welcomeMessage = "Hello, World!";

    function getWelcomeMessage() public view returns (string memory) {
        return welcomeMessage;
    }

    function setWelcomeMessage(string memory newMessage) public {
        welcomeMessage = newMessage;
    }
}
```


## Explication du contrat :

Le contrat s'appelle "HelloWorld" et est défini avec la directive pragma solidity ^0.8.0;, indiquant la version du compilateur Solidity.

Il contient une variable publique welcomeMessage qui stocke le message de bienvenue par défaut, initialisé à "Hello, World!".

Le contrat possède deux fonctions :

getWelcomeMessage(): Cette fonction est de type "view", ce qui signifie qu'elle ne modifie pas l'état de la blockchain. Elle renvoie le message de bienvenue actuel.
setWelcomeMessage(string memory newMessage): Cette fonction permet de mettre à jour le message de bienvenue. Elle prend un nouveau message en entrée et le stocke dans la variable welcomeMessage.

## Déploiement du Contrat avec Web3

Pour déployer ce contrat sur une blockchain, nous allons utiliser Web3, une bibliothèque Python qui nous permet d'interagir avec la blockchain. Voici un aperçu des étapes de déploiement :

1 - Configuration de Web3 : Nous devons configurer Web3 pour qu'il se connecte à une blockchain donnée en spécifiant l'URL du nœud RPC, le gestionnaire de portefeuille, et la clé privée.

2 - Chargement du Contrat : Nous chargeons le contrat à partir de son ABI (Interface Binaire Abstraite) et de son bytecode, généralement stockés dans un fichier de métadonnées.

3 - Construction de la Transaction de Déploiement : Nous construisons une transaction pour déployer le contrat. Cette transaction inclut des détails tels que l'expéditeur, la valeur, le prix du gaz, et le numéro de séquence.

4 - Estimation du Coût en Gaz : Avant de soumettre la transaction, nous estimons le coût en gaz nécessaire pour le déploiement.

5 - Envoi de la Transaction : Nous signons la transaction avec la clé privée et l'envoyons à la blockchain.

6 - Réception de la Confirmation : Nous attendons la confirmation de la transaction et récupérons l'adresse du contrat déployé.

Note : Les détails spécifiques du script de déploiement sont disponibles ici.

Félicitations ! Vous avez appris comment créer un contrat intelligent "Hello World" en Solidity et le déployer sur une blockchain à l'aide de Web3. Vous pouvez maintenant interagir avec ce contrat pour lire et mettre à jour le message de bienvenue.
