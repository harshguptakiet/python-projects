students = [
    {'name': 'John', 'math': 85, 'science': 92, 'english': 78},
    {'name': 'Marie', 'math': 90, 'science': 88, 'english': 95},
    {'name': 'Steve', 'math': 76, 'science': 85, 'english': 80},
    {'name': 'Alice', 'math': 89, 'science': 94, 'english': 91}
]
def aggregate_students(students):
    score_dict = []
    math_sum = 0
    science_sum=0
    english_sum =0
    for student in students:
        math_sum = math_sum+student['math']
        science_sum = science_sum+student['science']
        english_sum = english_sum+student['english']
    score_dict.append(english_sum)
    score_dict.append(science_sum)
    score_dict.append(math_sum)
    return score_dict
result = {}
result = aggregate_students(students)
print(result)

