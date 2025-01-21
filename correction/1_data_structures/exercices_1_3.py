

# Exercice 1

## Déterminer le type des données
# Écrire une fonction identifier_type(data) qui prend un argument et retourne son type.

#### CORRECTION ####

def identifier_type(data):
    return type(data).__name__


#### END CORRECTION ####


print(identifier_type(42))  # int
print(identifier_type("Hello"))  # str
print(identifier_type([1, 2, 3]))  # list


# Exercice 2
# Question : Que va afficher ce code ? Écrivez votre prédiction en commentaire
# avant de l'exécuter, puis expliquez le résultat.

x = 10
y = x
print(f"1. Valeur initiale de x : {x}")
print(f"2. Valeur initiale de y : {y}")

# Modifions y. Que va-t-il se passer pour x ?
y = 20
print(f"3. Nouvelle valeur de y : {y}")
print(f"4. Valeur de x après modification de y : {x}")

# Questions à se poser :
# 1. Pourquoi x garde sa valeur initiale ?
# 2. Si on modifie y, pourquoi x n'est pas affecté ?
# 3. Que signifie l'immutabilité dans ce contexte ?


a = [1, 2, 3]  # Une liste
b = a
b.append(4)
print(f"5. Liste a : {a}")
print(f"6. Liste b : {b}")

# Comparez ce comportement avec celui des nombres.
# Quelle est la différence ?



# Exercice 3

# En python, le mot clé `is` est utilisé pour vérifier si deux variables pointent vers le même objet en mémoire.
# Alors que le mot clé `==` est utilisé pour vérifier si deux variables ont la même valeur.

x = [1, 2, 3]
y = x
z = [1, 2, 3]
print(x is y)  # ?
print(x is z)  # ?
print(x == z)  # ?

# Question : Que va afficher ce code ? Écrivez votre prédiction en commentaire
# avant de l'exécuter, puis expliquez le résultat.



# Exercice 4
# Un tuple en Python est considéré comme **immutable**, mais cette notion mérite d'être nuancée :
# Un tuple est immutable dans le sens où :
# - On ne peut pas ajouter ou supprimer des éléments
# - On ne peut pas remplacer des éléments
# - Sa structure ne peut pas être modifiée après création
mon_tuple = (1, 2, 3)

mon_tuple[0] = 10   
mon_tuple.append(4)

# Cependant, si un tuple contient des objets mutables (comme des listes), ces objets peuvent être modifiés :
t = ([1, 2], [3, 4])
t[0].append(99)
print(t) 

# Les tuples sont immuables, mais s'ils contiennent des objets mutables (comme des listes), ces objets peuvent être modifiés.