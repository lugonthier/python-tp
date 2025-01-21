def analyze_student_groups(*args, **kwargs):
    thresholds = {
        'excellent': kwargs.get('excellent', 18),
        'bien': kwargs.get('bien', 14),
        'moyen': kwargs.get('moyen', 10)
    }
    
    def evaluate_level(note):
        if note >= thresholds['excellent']:
            return 'excellent'
        elif note >= thresholds['bien']:
            return 'bien'
        elif note >= thresholds['moyen']:
            return 'moyen'
        return 'insuffisant'
    
    def analyze_group(group):
        if not group:
            return None
            
        average = sum(group) / len(group)
        best_score = max(group)
        
        level_count = {
            'excellent': 0,
            'bien': 0,
            'moyen': 0,
            'insuffisant': 0
        }
        for note in group:
            level = evaluate_level(note)
            level_count[level] += 1
            
        return {
            'average': round(average, 2),
            'best_score': best_score,
            'level_distribution': level_count
        }
    
    groups_analysis = {}
    for i, group in enumerate(args, 1):
        groups_analysis[f'Groupe {i}'] = analyze_group(group)
    
    return groups_analysis

if __name__ == "__main__":
    groupe_a = [19, 12, 15, 17, 13]
    groupe_b = [14, 13, 12, 15, 16]
    groupe_c = [18, 17, 18, 19, 15]

    result1 = analyze_student_groups(groupe_a, groupe_b, groupe_c)
    print("Analyse avec seuils par défaut:")
    print(result1)

    result2 = analyze_student_groups(
        groupe_a, groupe_b, groupe_c,
        excellent=16, bien=13, moyen=10
    )
    print("\nAnalyse avec seuils personnalisés:")
    print(result2)

    result3 = analyze_student_groups(
        groupe_a, [], groupe_c,
        excellent=17, bien=15, moyen=12
    )
    print("\nAnalyse avec un groupe vide:")
    print(result3)