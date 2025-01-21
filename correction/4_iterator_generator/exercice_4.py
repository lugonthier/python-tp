nombres = range(1, 11)

carres_liste = [x**2 for x in nombres]
print(carres_liste) 

carres_gen = (x**2 for x in nombres)
print(carres_gen) 
print(list(carres_gen)) 

pairs_gen = (x for x in nombres if x % 2 == 0)