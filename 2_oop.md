# Exercice 1: Classes et Objets


1. Créez une classe `Car` avec les attributs suivants:
- `brand` (marque de la voiture)
- `model` (modèle de la voiture)
  
2. Puis ajoutez une méthode `display_info` qui affiche les informations complètes de la voiture.

3. Instanciez deux objets `Car` avec des marques et des modèles différents.
4. Appelez `display_info` pour afficher leurs informations.


# Exercice 2: Attributs et méthodes

1. Ajoutez un attribut `year` (année de fabrication) à la classe `Car`.
2. Ajoutez une méthode `age` qui calcule l’âge de la voiture en fonction de l'année actuelle.


# Exercice 3

1. Ajoutez une méthode `get_odometer` permettant de retourner le kilométrage de la voiture.
2. Ajoutez une méthode `drive` permettant d'ajouter une distance (en kilomètres) au kilométrage de la voiture.
3. Empêchez l’ajout d’une distance négative dans la méthode drive (et donc le kilométrage).

4. Affichez le kilométrage initial.
5. Ajoutez une distance de 150 km et affichez le nouveau kilométrage.
6. Essayez d'ajouter une distance négative et observez l'erreur.
7. Essayez d'afficher l'odometer en utilisant directement l'attribut. Qu'observe-t-on ?


Attention: Le kilométrage de doit pas pouvoir être modifié en dehors de la méthode drive.



# Exercice 4: Propriétés
1. Ajoutez une propriété `price` (prix) à la classe `Car`. Le prix doit pouvoir être lu et modifié. En revanche, il ne peut être inférieur à 0.
2. Définissez une nouvelle voiture avec un prix.
3. Affichez le prix. Modifiez le prix. Affichez le à nouveau.
4. Essayez d'attribuer une valeur négative et observer le résultat.


# Exercice 5: Héritage
1. Créez une classe enfant `ElectricCar` qui hérite de `Car`. Ajoutez à ElectricCar:
- Un attribut `battery_capacity` (capacité de la batterie, en kWh).
- Une méthode `charge_time()` qui calcule le temps de recharge complet (supposez une vitesse de charge de 50 kW).
2. Instanciez une voiture électrique.
3. Affichez le temps de recharge.


# Exercice 6

1. Ajoutez une méthode `start_engine()` à la classe `Car` et `ElectricCar`.
- Pour Car, la méthode affiche : "Le moteur thermique démarre."
- Pour ElectricCar, elle affiche : "Le moteur électrique démarre."

2. Appelez la méthode `start_engine` sur une voiture classique et une voiture électrique.


# Exercice 7: Variables de classe

1. Imaginons que nous souhaitons connaître le nombre de voiture produite. Modifiez la classe `Car` pour connaître le nombre de voiture produite à tout moment.
2. Créez 2 voitures. afficher le nombre de voiture total. Puis créez cette fois-ci une voiture électrique et affichez à nouveau le nombre voiture total.

# Exercice 8: Méthodes de classe

1. Ajoutez une méthode de classe `get_total_cars()` qui retourne le nombre total de voitures créées.
2. Appelez la méthode get_total_cars() après avoir créé plusieurs voitures.


# Exercice 9: Méthodes statiques

1. Ajoutez une méthode statique `convert_miles_to_km` pour convertir une distance en miles en kilomètres (1 mile = 1.60934 km).
2. Appelez la méthode statique avec différentes valeurs en miles sans instancier d'objet.

# Exercice 10: Variables de classe

Ajoutez les fonctionnalités suivantes à la classe Car :

- Une variable de classe `total_distance` pour suivre la distance totale parcourue par toutes les voitures.
- Une méthode de classe `get_total_distance()` pour retourner cette distance.
- Une méthode statique `calculate_fuel_needed(distance, fuel_efficiency)` pour calculer le carburant nécessaire pour parcourir une distance donnée (efficacité en litres par km).


# Exercice 11: Abstraction et Polymorphisme

1. Créez une classe abstraite `Vehicle` avec:
- Une méthode abstraite `calculate_cost_per_km()`
- Une méthode abstraite `get_max_range()`
- Une méthode concrète `display_range()` qui affiche l'autonomie maximale du véhicule

2. Modifiez la classe `Car` pour hériter de `Vehicle`:
- `calculate_cost_per_km()` doit retourner le coût au km (consommation * prix du carburant)
- `get_max_range()` doit retourner l'autonomie maximale (capacité du réservoir / consommation)
- Ajoutez les attributs nécessaires (consommation, capacité du réservoir, prix du carburant)

3. Modifiez la classe `ElectricCar` pour hériter de `Vehicle`:
- `calculate_cost_per_km()` doit retourner le coût au km (consommation électrique * prix du kWh)
- `get_max_range()` doit retourner l'autonomie maximale (capacité de la batterie / consommation)
- Ajoutez les attributs nécessaires (consommation électrique, prix du kWh)

4. Créez une liste de véhicules contenant une voiture thermique et une voiture électrique
5. Parcourez la liste et affichez pour chaque véhicule:
   - Son type
   - Son coût au kilomètre
   - Son autonomie maximale