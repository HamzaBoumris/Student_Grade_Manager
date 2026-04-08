def add_grade(data, name, subject, grade):
    if name not in data:
        print("Student not found.")
        return

    if grade < 0 or grade > 20:
        print("Grade must be between 0 and 20.")
        return

    data[name][subject] = grade
    print(f"Added grade {grade} for {name} in {subject}.")


def calculate_average(data, name):
    if name not in data or not data[name]:
        return 0

    grades = data[name].values()
    return sum(grades) / len(grades)

def calculate_class_average(data):
    if not data:
        return 0

    averages = [calculate_average(data, student) for student in data if data[student]]
    if not averages:
        return 0
    return sum(averages) / len(averages)


def get_top_student(data):
    if not data:
        return None

    best_student = None
    best_avg = -1

    for student in data:
        avg = calculate_average(data, student)
        if avg > best_avg:
            best_avg = avg
            best_student = student

    return best_student, best_avg