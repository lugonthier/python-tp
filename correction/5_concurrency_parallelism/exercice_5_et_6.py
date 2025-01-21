import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

urls = [
    "https://fr.wikipedia.org/wiki/Henry_Cavill",
    "https://fr.wikipedia.org/wiki/Ben_Affleck",
    "https://fr.wikipedia.org/wiki/Gal_Gadot",
    "https://fr.wikipedia.org/wiki/Henry_Cavill",
    "https://fr.wikipedia.org/wiki/Ben_Affleck",
    "https://fr.wikipedia.org/wiki/Gal_Gadot",
    "https://fr.wikipedia.org/wiki/Henry_Cavill",
    "https://fr.wikipedia.org/wiki/Ben_Affleck",
    "https://fr.wikipedia.org/wiki/Gal_Gadot",
    "https://fr.wikipedia.org/wiki/Henry_Cavill",
    "https://fr.wikipedia.org/wiki/Ben_Affleck",
    "https://fr.wikipedia.org/wiki/Gal_Gadot",
    "https://fr.wikipedia.org/wiki/Henry_Cavill",
    "https://fr.wikipedia.org/wiki/Ben_Affleck",
    "https://fr.wikipedia.org/wiki/Gal_Gadot",
    "https://fr.wikipedia.org/wiki/Henry_Cavill",
    "https://fr.wikipedia.org/wiki/Ben_Affleck",
    "https://fr.wikipedia.org/wiki/Henry_Cavill",
    "https://fr.wikipedia.org/wiki/Ben_Affleck",
    "https://fr.wikipedia.org/wiki/Gal_Gadot",
    "https://fr.wikipedia.org/wiki/Henry_Cavill",
    "https://fr.wikipedia.org/wiki/Ben_Affleck",
    "https://fr.wikipedia.org/wiki/Gal_Gadot",
    "https://fr.wikipedia.org/wiki/Henry_Cavill",
    "https://fr.wikipedia.org/wiki/Ben_Affleck",
    "https://fr.wikipedia.org/wiki/Gal_Gadot",
    "https://fr.wikipedia.org/wiki/Henry_Cavill",
    "https://fr.wikipedia.org/wiki/Ben_Affleck",
    "https://fr.wikipedia.org/wiki/Gal_Gadot",
    "https://fr.wikipedia.org/wiki/Henry_Cavill",
    "https://fr.wikipedia.org/wiki/Ben_Affleck",
    "https://fr.wikipedia.org/wiki/Gal_Gadot",
    "https://fr.wikipedia.org/wiki/Henry_Cavill",
    "https://fr.wikipedia.org/wiki/Ben_Affleck",
    "https://fr.wikipedia.org/wiki/Henry_Cavill",
    "https://fr.wikipedia.org/wiki/Ben_Affleck",
    "https://fr.wikipedia.org/wiki/Gal_Gadot",
    "https://fr.wikipedia.org/wiki/Henry_Cavill",
    "https://fr.wikipedia.org/wiki/Ben_Affleck",
    "https://fr.wikipedia.org/wiki/Gal_Gadot",
    "https://fr.wikipedia.org/wiki/Henry_Cavill",
    "https://fr.wikipedia.org/wiki/Ben_Affleck",
    "https://fr.wikipedia.org/wiki/Gal_Gadot",
    "https://fr.wikipedia.org/wiki/Henry_Cavill",
    "https://fr.wikipedia.org/wiki/Ben_Affleck",
    "https://fr.wikipedia.org/wiki/Gal_Gadot",
    "https://fr.wikipedia.org/wiki/Henry_Cavill",
    "https://fr.wikipedia.org/wiki/Ben_Affleck",
    "https://fr.wikipedia.org/wiki/Gal_Gadot",
    "https://fr.wikipedia.org/wiki/Henry_Cavill",
    "https://fr.wikipedia.org/wiki/Ben_Affleck",
    "https://fr.wikipedia.org/wiki/Henry_Cavill",
    "https://fr.wikipedia.org/wiki/Ben_Affleck",
    "https://fr.wikipedia.org/wiki/Gal_Gadot",
    "https://fr.wikipedia.org/wiki/Henry_Cavill",
    "https://fr.wikipedia.org/wiki/Ben_Affleck",
    "https://fr.wikipedia.org/wiki/Gal_Gadot",
    "https://fr.wikipedia.org/wiki/Henry_Cavill",
    "https://fr.wikipedia.org/wiki/Ben_Affleck",
    "https://fr.wikipedia.org/wiki/Gal_Gadot",
    "https://fr.wikipedia.org/wiki/Henry_Cavill",
    "https://fr.wikipedia.org/wiki/Ben_Affleck",
    "https://fr.wikipedia.org/wiki/Gal_Gadot",
    "https://fr.wikipedia.org/wiki/Henry_Cavill",
    "https://fr.wikipedia.org/wiki/Ben_Affleck",
    "https://fr.wikipedia.org/wiki/Gal_Gadot",
    "https://fr.wikipedia.org/wiki/Henry_Cavill",
    "https://fr.wikipedia.org/wiki/Ben_Affleck",
    "https://fr.wikipedia.org/wiki/Henry_Cavill",
    "https://fr.wikipedia.org/wiki/Ben_Affleck",
    "https://fr.wikipedia.org/wiki/Gal_Gadot",
    "https://fr.wikipedia.org/wiki/Henry_Cavill",
    "https://fr.wikipedia.org/wiki/Ben_Affleck",
    "https://fr.wikipedia.org/wiki/Gal_Gadot",
    "https://fr.wikipedia.org/wiki/Henry_Cavill",
    "https://fr.wikipedia.org/wiki/Ben_Affleck",
    "https://fr.wikipedia.org/wiki/Gal_Gadot",
    "https://fr.wikipedia.org/wiki/Henry_Cavill",
    "https://fr.wikipedia.org/wiki/Ben_Affleck",
    "https://fr.wikipedia.org/wiki/Gal_Gadot",
    "https://fr.wikipedia.org/wiki/Henry_Cavill",
    "https://fr.wikipedia.org/wiki/Ben_Affleck",
    "https://fr.wikipedia.org/wiki/Gal_Gadot",
    "https://fr.wikipedia.org/wiki/Henry_Cavill",
    "https://fr.wikipedia.org/wiki/Ben_Affleck",
]

def load_url(index: int) -> bytes:
    """Fetch the content of a URL."""
    try:
        with urllib.request.urlopen(urls[index], timeout=20) as conn:
            return conn.read()
    except Exception as e:
        print(f"Error loading URL {urls[index]}: {e}")
        return b""


if __name__ == "__main__":
    n_jobs = len(urls)
    print("n_jobs", n_jobs)
    start_time = time.time()
    results_sequential = [load_url(i) for i in range(n_jobs)]
    end_time = time.time()
    print(f"Serial execution time: {end_time - start_time:.2f} seconds")

    # Exercice 5
    for n_threads in [2, 4]:
        start_time = time.time()
        with ThreadPoolExecutor(max_workers=n_threads) as executor:
            results = executor.map(load_url, range(n_jobs))
        end_time = time.time()
        print(
            f"multithreading avec {n_threads} threads, temps total: {end_time - start_time:.2f} secondes"
        )

    # Exercice 6
    for n_processes in [2, 4]:
        start_time = time.time()
        with ProcessPoolExecutor(max_workers=n_processes) as executor:
            results = executor.map(load_url, range(n_jobs))
        end_time = time.time()
        print(
            f"multiprocessing avec {n_processes} processus, temps total: {end_time - start_time:.2f} secondes"
        )
