- En python, le mot clé `is` est utilisé pour vérifier si deux variables pointent vers le même objet en mémoire.
- Alors que le mot clé `==` est utilisé pour vérifier si deux variables ont la même valeur.


# Exercice 1

1. Écrire une fonction `identifier_type(data)` qui prend un argument et retourne son type.


2. Que vont afficher les appels à la fonction:
```python
print(identifier_type(42)) # ?
print(identifier_type("Hello")) # ?
print(identifier_type([1, 2, 3])) # ?
```

3. Vérifier votre prédiction en testant la fonction.

# Exercice 2
1. Que va va afficher le code suivant:
```python
x = 10
y = x
print(f"Valeur de x : {x}") # ?
print(f"Valeur de y : {y}") # ?
```

2. Vérifier votre prédiction en testant le code.
3. Modifions y. Que va-t-il se passer pour x et pourquoi ?

```python
y = 20
```


4. Vérifier votre prédiction en testant le code.


# Exercice 3


1. Prenons maintenant une liste. 
Que va afficher le code suivant ?

```python
a = [1, 2, 3]
b = a
b.append(4)

print(f"Liste a : {a}")
print(f"Liste b : {b}")
```
1. Vérifier votre prédiction en testant le code.
2. Comparez ce comportement avec celui des nombres.
Quelle est la différence et pourquoi ?

# Exercice 4

1. Que va afficher le code suivant et pourquoi ?

```python
x = [1, 2, 3]
y = x
z = [1, 2, 3]

print(x is y)  # ?
print(x is z)  # ?
print(x == z)  # ?
```
2. Vérifier votre prédiction en executant le code.


# Exercice 5: Tuple mutable or not ?

Déterminer si un tuple ( exemple: (1, 2, 3) ) est mutable ou non.


# Exercice 6

1. Définissez une fonction `add_item` qui :
   - Prend une chaîne de caractères `item` à ajouter.
   - Possède un paramètre par défaut `items=[]` (un argument par défaut mutable).
   - Ajoute `item` à `items`.
   - Retourne la liste mise à jour.

2. Exécutez la fonction avec différentes valeurs de item et observez le résultat.

3. Observez la sortie. Qu’est-ce que vous remarquez ?


# Exercice 7

Comprendre et implémenter les copies en Python

1. Créez une fonction `shallow_copy(obj)` qui effectue une copie superficielle :
   - Doit gérer les types de base (int, float, str, bool, None)
   - Doit gérer les listes, tuples, dictionnaires et sets
   - Testez avec des structures imbriquées pour montrer le comportement de la copie superficielle

2. Créez une fonction `deep_copy(obj)` qui effectue une copie profonde :
   - Doit gérer les types de base
   - Doit gérer les listes, tuples, dictionnaires et sets
   - Doit copier récursivement les structures imbriquées
   - Testez avec des structures imbriquées pour montrer le comportement de la copie profonde

3. Montrez comment réaliser ces mêmes opérations avec :
   - Le module `copy` (import copy)
   - Les méthodes .copy() des objets