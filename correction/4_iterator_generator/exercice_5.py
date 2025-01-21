import sys
from memory_profiler import profile

@profile
def avec_liste(n):
    return [i**2 for i in range(n)]

@profile
def avec_generateur(n):
    for i in range(n):
        yield i**2

n = 10**6

print("Avec liste:")
liste = avec_liste(n)
print(f"Taille en mémoire: {sys.getsizeof(liste)} bytes")

print("\nAvec générateur:")
gen = avec_generateur(n)
print(f"Taille en mémoire: {sys.getsizeof(gen)} bytes")


for i, val in enumerate(liste):
    if i >= 5: break
    print(val)

for i, val in enumerate(gen):
    if i >= 5: break
    print(val)

# La liste stocke tous les éléments en mémoire (plusieurs MB pour n=10^6)
# Le générateur ne prend que quelques bytes car il calcule les valeurs à la demande
# Dans les deux cas, nous n'utilisons que les 5 premiers éléments


# C'est particulièrement utile quand:
# - Vous travaillez avec de grandes séquences
# - Vous ne nécessitez pas tous les éléments en même temps
# - Vous voulez économiser de la mémoire
# - Vous traitez des flux de données (streaming)
# - Vous avez des calculs coûteux qui ne sont peut-être pas tous nécessaires.