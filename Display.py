def show_students(data):
    if not data:
        print("No students available.")
        return

    for student, subjects in data.items():
        avg = calculate_average(data, student)
        print(f"\n{student}:")
        for sub, grade in subjects.items():
            print(f"  {sub}: {grade}")
        print(f"  Average: {avg:.2f}")