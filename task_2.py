students_math_results = [
    {"name": "Олександр", "scores": {"Calculus": 85, "Algebra": 90, "Discrete Math": 78}},
    {"name": "Марія", "scores": {"Calculus": 65, "Algebra": 55, "Discrete Math": 70}},
    {"name": "Іван", "scores": {"Calculus": 92, "Algebra": 88, "Discrete Math": 95}},
    {"name": "Анна", "scores": {"Calculus": 45, "Algebra": 60, "Discrete Math": 50}}
]
def get_successful_students(students_list,passing_score=60):
    successful_students = {}
    for student in students_list:
        name = student["name"]
        scores = student["scores"]
        is_successful = True
        for score in scores.values():
            if score < passing_score:
                is_successful = False
                break
        if is_successful:
            average_score = sum(scores.values())/len(scores.values())
            successful_students[name] = average_score
    return successful_students
result = get_successful_students(students_math_results)
print("список учів")
for name, average_score in result.items():
    print(f"{name}: {average_score}")




