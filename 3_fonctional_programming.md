# Programmation Fonctionnelle en Python - Exercices Pratiques
# Exercice 1: *args
1. Créez une fonction `concatenate_lists(*args)` qui:
   - Prend un nombre variable de listes en argument
   - Combine toutes les listes en une seule
   - Élimine les doublons
   - Trie le résultat
2. Testez avec différentes combinaisons de listes.

# Exercice 2: **kwargs
1. Créez une fonction `create_student_report(**kwargs)` qui:
   - Accepte des paires clé-valeur représentant matière:note
   - Calcule la moyenne générale
   - Identifie la meilleure et la pire note
   - Retourne un dictionnaire avec ces statistiques
2. Testez avec différents cas.

# Exercice 3: Combinaison de *args et **kwargs

1. Créez une fonction `analyze_student_groups(*args, **kwargs)` qui:
   - Prend en arguments positionnels (*args) plusieurs listes d'étudiants
   - Prend en arguments nommés (**kwargs) les seuils de notation (ex: excellent=18, bien=14, moyen=10)
   - Pour chaque groupe d'étudiants:
     * Calcule la moyenne
     * Compte le nombre d'étudiants par niveau
     * Identifie le meilleur étudiant
   - Retourne un rapport comparatif des groupes


# Exercice 4: Fonctions Lambda et Map
1. Créez une liste de nombres et utilisez une fonction lambda avec `map()` pour:
   - Doubler chaque nombre
   - Convertir chaque nombre en string
   - Calculer le carré de chaque nombre
2. Convertissez les résultats en liste et affichez-les

# Exercice 5: Filter
1. À partir d'une liste de nombres, utilisez `filter()` avec une lambda pour:
   - Garder uniquement les nombres pairs
   - Garder les nombres supérieurs à une valeur donnée
   - Garder les nombres qui sont des carrés parfaits
2. Affichez les résultats filtrés

# Exercice 6: Reduce
1. Utilisez `reduce()` pour:
   - Calculer la somme d'une liste de nombres
   - Trouver le plus grand nombre d'une liste
   - Concaténer une liste de strings
2. Comparez avec les fonctions built-in équivalentes (sum, max)

# Exercice 7: Fonctions d'Ordre Supérieur
1. Créez une fonction `apply_operations` qui prend une liste et une liste de fonctions en paramètre
2. La fonction doit appliquer chaque fonction successivement aux éléments
3. Testez avec différentes opérations (multiplication, division, puissance)


4. Réécrivez-la de manière pure
5. Créez une version qui isole les effets secondaires


# Exercice 8: Décorateurs Simples
1. Créez un décorateur qui:
   - Mesure le temps d'exécution d'une fonction
   - Affiche les arguments passés à une fonction
   - Met en cache les résultats (memoization)
2. Appliquez ces décorateurs à différentes fonctions

# Exercice 9: Décorateurs avec Arguments
1. Créez un décorateur qui accepte des arguments pour:
   - Limiter le nombre d'appels à une fonction
   - Retry une fonction en cas d'erreur
   - Logger les appels avec un niveau de verbosité configurable


# Exercice 10: Fusion OOP et Programmation Fonctionnelle
1. Reprenez la classe abstraite `Vehicle` et ses enfants `Car` et `ElectricCar`

2. Implémentez des décorateurs utiles:
   - Un décorateur `retry(max_attempts=3, delay=1)` qui réessaie une opération en cas d'échec (ex: calcul de coût avec API externe)
   - Un décorateur `rate_limit(calls=100, period=60)` qui limite le nombre d'appels à une méthode par période
   - Un décorateur `validate_args` qui vérifie les types et valeurs des arguments (ex: prix > 0, capacité > 0)
   - Un décorateur `measure_performance` qui trace le temps d'exécution


3. Implémentez une hiérarchie de classes en évitant la duplication de code grâce à `*args` et `**kwargs`:
   - Modifiez `Vehicle` pour accepter les attributs communs
   - Créez une classe `Car` avec ses attributs spécifiques
   - Créez une classe `ElectricCar` avec ses attributs spécifiques
   - Créez une classe `HybridCar` qui hérite de `Car` et `ElectricCar`


# Exercice 11: Fonctions Pures vs Impures
1. Identifiez pourquoi la fonction suivante est impure:

```python
total = 0
def add_to_total(x):
global total
total += x
return total
```
