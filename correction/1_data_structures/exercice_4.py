def shallow_copy(obj):
    if isinstance(obj, (int, float, str, bool, type(None))):
        return obj
    
    if isinstance(obj, list):
        return list(obj)
    
    if isinstance(obj, tuple):
        return tuple(obj)
    
    if isinstance(obj, dict):
        return dict(obj)
    
    if isinstance(obj, set):
        return set(obj)
    
    raise TypeError(f"Le type {type(obj)} n'est pas supporté pour la shallow copy")

def deep_copy(obj):
    if isinstance(obj, (int, float, str, bool, type(None))):
        return obj
    
    if isinstance(obj, list):
        return [deep_copy(item) for item in obj]
    
    if isinstance(obj, tuple):
        return tuple(deep_copy(item) for item in obj)
    
    if isinstance(obj, dict):
        return {deep_copy(key): deep_copy(value) for key, value in obj.items()}
    
    if isinstance(obj, set):
        return {deep_copy(item) for item in obj}
    
    raise TypeError(f"Le type {type(obj)} n'est pas supporté pour la deep copy")


if __name__ == "__main__":
    original = {
        'liste': [1, [2, 3], 4],
        'dict': {'a': 1, 'b': [5, 6]},
        'tuple': (7, [8, 9]),
        'set': {10, 11, (12, 13)}
    }

    print("1. Test de la shallow copy")
    shallow = shallow_copy(original)
    original['liste'][1][0] = 'modifié'
    print("Original après modification:", original['liste'])
    print("Shallow copy après modification:", shallow['liste'])

    print("\n2. Test de la deep copy")
    deep = deep_copy(original)
    original['liste'][1][0] = 'modifié encore'
    print("Original après modification:", original['liste'])
    print("Deep copy après modification:", deep['liste'])


    print("\n3. Utilisation du module copy")
    import copy
    
    module_shallow = copy.copy(original)
    print("Module shallow copy:", type(module_shallow))
    
    module_deep = copy.deepcopy(original)
    print("Module deep copy:", type(module_deep))

    print("\n4. Utilisation des méthodes .copy()")
    liste_copy = original['liste'].copy()
    dict_copy = original['dict'].copy()
    set_copy = original['set'].copy()