"""
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
"""

import time
import threading
from concurrent.futures import ThreadPoolExecutor

def ma_fonction(message, duration):
    print(f"{message} Début du traitement\n")
    time.sleep(duration)
    print(f"{message} Fin du traitement\n")

if __name__ == "__main__":
    start_seq = time.time()
    ma_fonction("Tâche A (séquentiel)", 2)
    ma_fonction("Tâche B (séquentiel)", 2)
    end_seq = time.time()

    print(f"\nTemps total séquentiel : {end_seq - start_seq:.2f} secondes\n")


    # Avec threading
    start_time = time.time()
    thread_a = threading.Thread(target=ma_fonction, args=("Tâche A (thread)", 2))
    thread_b = threading.Thread(target=ma_fonction, args=("Tâche B (thread)", 2))

    thread_a.start()
    thread_b.start()

    thread_a.join()
    thread_b.join()

    end_time = time.time()

    print(f"Temps total multithreading : {end_time - start_time:.2f} secondes")
    
    # Avec concurrent.futures
    start_time = time.time()
    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(ma_fonction, "Tâche A (thread)", 2)
        executor.submit(ma_fonction, "Tâche B (thread)", 2)

    end_time = time.time()

    print(f"Temps total multithreading : {end_time - start_time:.2f} secondes")
