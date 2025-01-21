def create_student_report(**kwargs):
    if not kwargs:
        return {
            'average': 0,
            'best_subject': None,
            'worst_subject': None
        }
    
    average = sum(kwargs.values()) / len(kwargs)
    
    best_subject = max(kwargs.items(), key=lambda x: x[1])[0]
    worst_subject = min(kwargs.items(), key=lambda x: x[1])[0]
    
    return {
        'average': average,
        'best_subject': best_subject,
        'worst_subject': worst_subject
    }

report1 = create_student_report(math=18, physics=15, english=12)
print(report1)  

report2 = create_student_report(math=15)
print(report2)  

report3 = create_student_report(math=15, physics=15)
print(report3) 
