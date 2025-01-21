# Exercice 0: Séquentiel

Créez une fonction prenant 2 arguments:
- message
- duration

La fonction devra:
1. Afficher le `message` suivi du texte `Début du traitement`.
2. Attendre `duration` secondes.
3. afficher le `message` suivi du text `Fin du traitement`.

Exemple:
```python
mafonction('Tâche A', 2)
Tâche A: Début du traitement
Tâche A: Fin du traitement
```

Une fois la fonction construite, exécutez la 2 fois de suite avec des messages différents. Mesurez le temps total d'exécution du programme.


# Exercice 1: Multithreading

Reprendre la fonction que vous avez crée précédemment.

1. utilisez le module `threading` pour créer 2 threads afin d'exécuter les 2 appels de fonction en **concurrences** tout en mesurant le temps total d'exécution du programme.

L'exemple ci dessous montre comment créer un thread:
```python
threading.Thread(
  target=mafonction,
  args=(
    # Les arguments de la fonction
  )
)
```
Pour démarrer un thread, utilisez la méthode `start`.

Pour attendre que tout les threads se terminent, appelez la méthode `join`.


2. Le module `threading` n'est pas le seul moyen de faire du multithreading en Python. Il existe aussi le module `concurrent.futures` qui est beaucoup utilisez.

Reproduisez le programme avec cette fois-ci le module `concurrent.futures`.


# Exercice 2: Multiprocessing

Reprendre la fonction que vous avez crée précédemment.

1. utilisez le module `multiprocessing` pour créer 2 processus afin d'exécuter les 2 appels de fonction en **parallèle** tout en mesurant le temps total d'exécution du programme.

L'exemple ci dessous montre comment créer un processus:
```python
multiprocessing.Process(
  target=mafonction,
  args=(
    # Les arguments de la fonction
  )
)
```
Pour démarrer un processus, utilisez la méthode `start`.

Pour attendre que tout les processus se terminent, appelez la méthode `join`.


2. Le module `multiprocessing` n'est pas le seul moyen de faire du multithreading en Python. Il existe aussi le module `concurrent.futures` qui est beaucoup utilisez.

Reproduisez le programme avec cette fois-ci le module `concurrent.futures`.


# Exercice 3: Finalement, que choisir ?

- Créez une fonction `cpu_heavy_task` qui prend un argument `x` et qui calcule la somme des nombres de 0 à 10^x.
- Exécutez cette fonction avec x=8, 4 fois de suite en séquentiel, puis en parallèle avec les 2 méthodes vues précédemment.
- Mesurez le temps d'exécution de chaque méthode.
- Comparez les résultats.

# Exercice 4: Les threads et la concurrence

Essayer de démontrer expérimentalement que les threads ne sont pas parallèles.

Par exemple, vous pouvez tracer la répartition des temps d'exécution des opérations au sein des threads.


# Exercice 5: Quand le multithreading est efficace ?

Dans cet exercice, nous allons tester l'efficacité du multithreading pour les opérations I/O bound (entrées/sorties).

1. Créez une fonction `load_url(index: int)` qui:
   - Prend en paramètre un index correspondant à une URL dans une liste prédéfinie
   - Télécharge le contenu de l'URL correspondante
   - Retourne le contenu

2. Créez une liste d'URLs (par exemple des pages Wikipédia)

3. Testez le téléchargement de toutes les URLs avec:
   - Une exécution séquentielle
   - Une exécution avec ThreadPoolExecutor en variant le nombre de threads (2, 4, 8)

4. Comparez les temps d'exécution


# Exercice 6: I/O bound et multiprocessing

1. Reproduire le programme de l'exercice 5 avec le module mais cette fois-ci en faisant du multiprocessing.
2. Comparez les temps d'exécution.

# Eexercice 7 asyncio


Avant de plonger dans l'exercice sur asyncio, voici les principales opérations que vous utiliserez :

## Fonctions de base
- `asyncio.run(coroutine)`: Point d'entrée principal pour exécuter une coroutine. Lance la boucle d'événements et gère son cycle de vie.
```python
async def main():
    await some_coroutine()

asyncio.run(main())
```

- `await`: Mot-clé pour suspendre l'exécution d'une coroutine jusqu'à ce que la coroutine attendue soit terminée.
```python
async def example():
    result = await some_async_function()
```

## Exécution concurrente
- `asyncio.gather(*coroutines)`: Exécute plusieurs coroutines simultanément et attend que toutes soient terminées.
```python
async def main():
    results = await asyncio.gather(
        coroutine1(),
        coroutine2(),
        coroutine3()
    )
    # results contient les résultats dans l'ordre des coroutines
```

- `asyncio.create_task(coroutine)`: Crée une tâche à partir d'une coroutine pour une exécution concurrente.
```python
async def main():
    task1 = asyncio.create_task(coroutine1())
    task2 = asyncio.create_task(coroutine2())
    await task1
    await task2
```


Dans cet exercice, nous allons explorer la programmation asynchrone avec asyncio pour gérer des opérations I/O bound de manière efficace.

1. Créez une fonction asynchrone `async def fetch_url(url: str)` qui:
   - Utilise `aiohttp` pour télécharger une URL de manière asynchrone
   - Retourne le contenu de la page
   - Affiche le temps de début et de fin du téléchargement

2. Créez une fonction asynchrone `async def main()` qui:
   - Prend une liste d'URLs (vous pouvez réutiliser celle de l'exercice 5)
   - Utilise `asyncio.gather()` pour télécharger toutes les URLs en parallèle
   - Mesure le temps total d'exécution

3. Comparez les performances avec:
   - L'approche séquentielle (exercice 5)
   - L'approche multithreading (exercice 5)
   - L'approche multiprocessing (exercice 6)
