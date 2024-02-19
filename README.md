# Bienvenue au Dodjo !

<p align="center">
  <img src="./assets/welcome_dodjo.jpg"/>
</p>

Le Dodjo est en quelque sorte le chemin que j'arpente dans l'univers de la programmation.
Le Dodjo est mon expérience personnelle mais pourrait aussi être une voie pour d'autres : je vous la partage donc. 

Pourquoi Dodjo ? Parce que Dodjo, c'est beau. Parce que Dodjo, c'est rigolo.

## Avertissements
Comme toute chose dans notre univers, ce contenu est **impermanent**. 
Je modifie ces notes de façon continue en fonction des retours des lectrices et des lecteurs.

## Les tests: ukemi du programmeur

Dans le contexte des arts martiaux, voici la définition de __ukemi__ d'après mon copain Wikipédia:
```
Un ukemi est un brise-chute contrôlé qui sert à tomber sans se faire mal. 
```
<p align="center">
  <img src="./assets/ukemi.jpg"/>
</p>


Alors qu'au judo, je pratique les ukemi depuis mon enfance; j'ai appris bien tardivement à employer les tests "contrôlés" en programmation.
  
Avant, je "testais" mon code en vérifiant "visuellement" que les résultats produits "convenaient". Ainsi quand je lançais mes scripts, trois cas se présentaient:
1. un message d'erreur apparaissait : je lisais le message, je tentais une correction, je relançais le script et je bouclais.
2. pas de message d'erreur et tout me semblait correct : je passais à la suite de mon travail.
3. pas de message d'erreur mais un résultat me chiffonait: souvent je me disais "C'est bizarre, ça marchait toute à l'heure..." 

Dans le dernier cas, je m'arrachais quelques cheveux quand je m'apercevais que j'avais fait une "modif vite fait quelque part" dans le code qui s'avérait être la source à tous mes maux !!!

Par ailleurs, lorsque je reprenais du code de quelqu'un d'autre (en fait souvent une acienne version de moi-même :scream:), j'avais **peur de tout casser** : de "faire du mal" au programme et à moi-même. Vous sentez l'analogie avec les ukemi arriver ?

Un des atouts du test controlé en programmation c'est de pouvoir se planter sans se faire mal.

Un exemple basique consiste à tester une fonction en comparant sa sortie avec ce que j'attends d'elle pour un jeu de paramètres donné.  

Pour ceux qui développe en Python:
```python
def ippon_seoi_nage(attaquant:Judoka, défenseur:Judoka) -> Score:
    " Calcule le score marqué par le judoka attaquant"
    pass
```

 on peut utiliser ``pytest`` pour nous y aider.





## Sujet à traiter:
- TDD
- DDD
- Programmation Fonctionnelle
- Continuous Delivery
- Coding dojo
  
## Influences:
- Pierre-Emmanuel Bois (et la programmation asyncrhone)
- Jean-Baptiste Musso (et le Lean Software Manufacturing)
- Arjancodes (et les code smells)
- Dave Farley (et le continuous delivery)
- Martin Fowler (et l'agile)
- Bartoz Milewski (et la programmation fonctionnelle)

## Inspiration par-delà de la programmation:
- Richard Feynman (et la pédagogie du "take the world from another point of view") 
- Olivia Caramello (et les ponts entre les domaines mathématiques)
- Grothendieck (et la pensée de la pensée)
