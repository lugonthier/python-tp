"""
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
"""


import time
def ma_fonction(message, duration):
    print(f"{message} Début du traitement\n")
    time.sleep(duration)
    print(f"{message} Fin du traitement\n")
    

start_seq = time.time()
ma_fonction("Tâche A (séquentiel)", 2)
ma_fonction("Tâche B (séquentiel)", 2)
end_seq = time.time()

print(f"\nTemps total séquentiel : {end_seq - start_seq:.2f} secondes\n")