"""
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
"""

import os
import time
import multiprocessing
from concurrent.futures import ProcessPoolExecutor

def ma_fonction(message, duration):
    print(f"{message} Début du traitement\n")
    time.sleep(duration)
    print(f"{message} Fin du traitement\n")


if __name__ == "__main__":
    print(f"Nombre de coeurs : {os.cpu_count()}")
    
    
    # Avec multiprocessing
    start_time = time.time()
    process_a = multiprocessing.Process(target=ma_fonction, args=("Tâche A (process)", 2))
    process_b = multiprocessing.Process(target=ma_fonction, args=("Tâche B (process)", 2))

    process_a.start()
    process_b.start()

    process_a.join()
    process_b.join()

    end_time = time.time()

    print(f"Temps total multiprocessing : {end_time - start_time:.2f} secondes")
    
    
    # Avec concurrent.futures

    start_time = time.time()
    with ProcessPoolExecutor(max_workers=2) as executor:
        executor.submit(ma_fonction, "Tâche A (process)", 2)
        executor.submit(ma_fonction, "Tâche B (process)", 2)

    end_time = time.time()

    print(f"Temps total multiprocessing : {end_time - start_time:.2f} secondes")
