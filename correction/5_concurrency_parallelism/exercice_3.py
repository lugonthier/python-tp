"""
- Créez une fonction `cpu_heavy_task` qui prend un argument `x` et qui calcule la somme des nombres de 0 à 10^x.
- Exécutez cette fonction avec x=8, 4 fois de suite en séquentiel, puis 4 fois en parallèle avec les 2 méthodes vues précédemment.
- Mesurez le temps d'exécution de chaque méthode.
- Comparez les résultats.
"""


import time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

def cpu_heavy_task(x):
    start = time.time()
    sum(range(10**x))
    stop = time.time()
    return start, stop


if __name__ == "__main__":
    
    N = 4
    start_time = time.time()
    results_sequential = [cpu_heavy_task(8) for _ in range(N)]
    end_time = time.time()
    print(f"Temps total sequential : {end_time - start_time:.2f} secondes\n")
    
    start_time = time.time()
    with ThreadPoolExecutor(max_workers=4) as executor:
        results = executor.map(cpu_heavy_task, [8]*N)
    end_time = time.time()
    
    for i, result in enumerate(results):
        print(f"Temps total thread {i}: {result[1] - result[0]:.2f} secondes")
    print(f"Temps total multithreading : {end_time - start_time:.2f} secondes\n")

    start_time = time.time()
    with ProcessPoolExecutor(max_workers=4) as executor:
        results = executor.map(cpu_heavy_task, [8]*N)
    end_time = time.time()

    for i, result in enumerate(results):
        print(f"Temps total processus {i}: {result[1] - result[0]:.2f} secondes")
    print(f"Temps total multiprocessing : {end_time - start_time:.2f} secondes\n")
