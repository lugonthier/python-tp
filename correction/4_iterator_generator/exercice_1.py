def exercice_iterateurs():
    ma_liste = [1, 2, 3, 4, 5]
    mon_tuple = ('a', 'b', 'c')
    mon_dict = {'x': 1, 'y': 2, 'z': 3}
    
    iter_liste = iter(ma_liste)
    iter_tuple = iter(mon_tuple)
    iter_dict = iter(mon_dict)
    
    print(next(iter_liste)) 
    print(next(iter_liste)) 
    
    try:
        while True:
            print(next(iter_tuple))
    except StopIteration:
        print("Fin de l'itérateur")
        
    print(list(iter_dict)) 
    print(list(iter(mon_dict.values()))) 
    print(list(iter(mon_dict.items()))) 
    
if __name__ == "__main__":
    exercice_iterateurs()