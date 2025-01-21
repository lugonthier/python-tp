"""
Essayer de démontrer expérimentalement que les threads ne sont pas parallèles.

Par exemple, vous pouvez tracer la répartition des temps d'exécution des opérations au sein des threads.
"""
import time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from typing import List


import numpy as np
import matplotlib.pyplot as plt

def live_tracker(x: int) -> List[float]:
    reference = time.time()
    timings = [time.time() - reference for _ in range(10**x)] 
    return timings


def visualize_live_runtimes(results: List[List[float]], title: str) -> None:
    for i, exp in enumerate(results):
        plt.scatter(exp, np.full(len(exp), i), alpha=0.8, color="red", edgecolors="none", s=1)
    plt.grid(axis="x")
    plt.ylabel("Tasks")
    ytks = range(len(results))
    plt.yticks(ytks, [f"job {i}" for i in ytks])
    plt.xlabel("Seconds")
    plt.title(title)


if __name__ == "__main__":
    
    with ThreadPoolExecutor(max_workers=4) as executor:
        results_multithreading = executor.map(live_tracker, [6, 6, 6, 6])
    
    with ProcessPoolExecutor(max_workers=4) as executor:
        results_multiprocessing = executor.map(live_tracker, [6, 6, 6, 6])
        
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    visualize_live_runtimes(list(results_multithreading), "multithreading")

    plt.subplot(1, 2, 2)
    visualize_live_runtimes(list(results_multiprocessing), "multiprocessing")

    plt.tight_layout()
    plt.show()
