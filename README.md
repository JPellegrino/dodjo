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

## Les tests : ukemi du programmeur

### Brise-chute

Dans le contexte des arts martiaux, voici la définition de __ukemi__ d'après ma copine Wikipédia:
> Un ukemi est un brise-chute contrôlé qui sert à tomber sans se faire mal. 

<p align="center">
  <img src="./assets/ukemi.jpg"/>
</p>
<p align="center">
  <em>Brisage de chute en cours... Veuillez patienter...</em>
</p>

Alors qu'au judo, je pratique les ukemi depuis mon enfance; j'ai appris bien tardivement à employer les tests "contrôlés" en programmation.
  
Avant, je "testais" mon code en vérifiant "visuellement" que les résultats produits "convenaient". Ainsi quand je lançais mes scripts, trois cas se présentaient:
1. un message d'erreur apparaissait : je lisais le message, je tentais une correction, je relançais le script et je bouclais.
2. pas de message d'erreur et tout me semblait correct : je passais à la suite de mon travail.
3. pas de message d'erreur mais un résultat me chiffonnait: souvent je me disais "C'est bizarre, ça marchait tout à l'heure..." 

Dans le dernier cas, je m'arrachais quelques cheveux quand je m'apercevais que j'avais fait une "modif vite fait quelque part" dans le code qui s'avérait être la source à tous mes maux !!!

Par ailleurs, lorsque je reprenais du code de quelqu'un d'autre (en fait souvent une ancienne version de moi-même :scream:), j'avais **peur de tout casser** : de "faire du mal" au programme et à moi-même. Vous sentez l'analogie avec les ukemi arriver ?

Un des atouts du test contrôlé en programmation c'est de pouvoir se planter sans se faire mal.

Un exemple basique consiste à tester une fonction en comparant sa sortie avec ce que j'attends d'elle pour un jeu de paramètres donné.  Voici un exemple, pour ceux qui développent en Python:

Dans un fichier judo.py, j'écris la "coquille" de la fonction que je souhaite développer:
```python
def ippon_seoi_nage(attaquant:Judoka, défenseur:Judoka) -> Score:
    " Calcule le score marqué par le judoka attaquant"
    pass
```

Dans un autre fichier, le test:
```python
from judo import ippon_seoi_nage

def test_ippon_seoi_nage():
    # Je prépare les combatants
    attaquant = Judoka(grade="noire")
    defenseur = Judoka(grade="blanche")

    # Je calcule
    score = ippon_seoi_nage(attaquant:Judoka, defenseur:Judoka)

    # Je "contrôle" que le résultat est bien celui pour lequel j'implémente ma fonction
    assert score == Score("Ippon")
```

J'exécute le test (en général j'utilise ``pytest``). Et là ... bah ça foire! Mais c'est normal car la fonction ``ippon_seoi_nage`` n'a pas d'implémentation pour le moment !

Allez, on se relève et on reprend le combat ! A vous d'imaginer une implémentation qui fera **passer le test au vert** (c'est pas du green washing, enfin je ne crois pas...). 

Cette méthodologie, "coquille puis test puis implémentation", porte le nom de TDD pour *Test Driven Design*. Dans les faits, j'implémente souvent la fonction avant le test mais penser au test en amont permet de mieux clarifier ce que l'on attend d'elle.

Maintenant plus d'arrachage de cheveux (enfin presque...) ! Dès que je touche à du code, je relance mes tests. Cela permet de détecter immédiatement si une partie ne fonctionne plus **comme attendue**. 

### Intention et preuve de bonne foi

Aujourd'hui, lorsque je découvre ou que je revois du code, je commence par regarder les tests. En effet, les tests vont naturellement indiquer ce que les auteurs du code avaient l'intention de faire. De plus, si l'exécution des tests se déroulent sans erreur cela "prouve" que le programme "fonctionne".

Donc aujourd'hui, je ne me repose plus sur la parole de celles ou ceux qui ont programmé et qui cherchent à me convaincre en disant "ça marchait sur ma machine", voire à faire les yeux du chat botté pour m'amadouer. Non, non, non!  Je lis et j'exécute les tests. Un point c'est tout. Un point c'est toi. (Zazie! Rends-moi le clavier !)

### Un premier pas sur le Chemin

Malgré leur apparente simplicité, les tests ont énormément de vertus. Ils m'ont poussé à écrire du code "testable" et m'ont amené un peu plus vers la *Programmation Fonctionnelle*. Ils m'ont ouvert la voie à tout un panel de techniques sophistiquées, que je vais tenter de vous partager ensuite, qui permettent de mieux maîtriser son code toute en gardant la flexibilité de pouvoir le modifier sans peur de tout casser.

Faites donc vous aussi, ce premier pas sur la Voie. Hajime !

## Programmation Fonctionnelle



## Sujet à traiter:
- TDD
- Programmation Fonctionnelle
- DDD
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
