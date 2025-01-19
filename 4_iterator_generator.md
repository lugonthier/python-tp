# Exercice 1: Itérateur
1. Créez trois collections différentes : une liste, un tuple et un dictionnaire avec des données de votre choix
2. Pour chaque collection :
   - Récupérez son itérateur avec la fonction iter()
   - Utilisez la fonction next() pour parcourir quelques éléments
   - Gérez la fin de l'itération avec try/except StopIteration
3. Pour le dictionnaire, montrez comment itérer sur :
   - les clés
   - les valeurs
   - les paires clé-valeur

# Exercice 2: Itérateur de Fibonacci
1. Créez une classe FibonacciIterator qui prend en paramètre le nombre n d'éléments à générer
2. Implémentez les méthodes __iter__ et __next__
3. La classe doit :
   - Garder en mémoire les deux derniers nombres calculés
   - Retourner les nombres de la suite de Fibonacci jusqu'à la position n
   - Lever StopIteration une fois n atteint
4. Testez votre itérateur avec différentes valeurs de n


# Exercice 3: Générateur de nombres premiers
1. Écrivez une fonction premiers_generator(limite) qui :
   - Prend en paramètre une limite supérieure
   - Utilise yield pour générer les nombres premiers jusqu'à cette limite
2. Implémentez une fonction auxiliaire est_premier(n) qui vérifie si un nombre est premier
3. Testez votre générateur avec différentes limites
4. Comparez le code avec une version qui utiliserait une liste


# Exercice 4: Compréhension de liste vs Expression génératrice
1. Créez une séquence de nombres de 1 à 10
2. Écrivez :
   - Une compréhension de liste qui calcule les carrés de ces nombres
   - Une expression génératrice qui fait la même chose
3. Ajoutez un filtrage pour ne garder que les nombres pairs
4. Comparez :
   - La syntaxe des deux approches
   - L'affichage direct des résultats
   - L'utilisation en boucle

# Exercice 5: Comparaison de mémoire et performance

1. Installez le module memory_profiler (pip install memory_profiler)
2. Créez deux fonctions qui produisent la même séquence (par exemple, les carrés des nombres) :
   - Une qui retourne une liste
   - Une qui utilise yield
3. Utilisez ces fonctions avec un grand nombre d'éléments (ex: 10^6)
4. Comparez :
   - L'espace mémoire utilisé (avec sys.getsizeof ou memory_profiler)
   - Le temps de création
   - Le comportement lors de l'utilisation partielle des données


# Exercice 6: Générateur de fichiers
1. Créez un fichier de test avec un grand nombre de lignes
2. Écrivez une fonction qui lit le fichier ligne par ligne
3. Comparez le temps de lecture avec une liste et un générateur
4. Utilisez memory_profiler pour comparer l'utilisation de la mémoire
