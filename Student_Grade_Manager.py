import json
import os

DATA_FILE = "data.json"
#----Storage------
def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)
#----Student------
def add_student(data, name):
    if name in data:
        print("Student already exists.")
        return
    data[name] = {}
    print(f"Student {name} added.")


def delete_student(data, name):
    if name not in data:
        print("Student not found.")
        return
    del data[name]
    print(f"Student {name} deleted.")
#----Grades------
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
#----Display------
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
#----Main Menu------
def menu():
    data = load_data()

    while True:
        print("""
1. Add student
2. Delete student
3. Add grade
4. Show students
5. Class average
6. Top student
7. Exit
""")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Student name: ")
            add_student(data, name)

        elif choice == "2":
            name = input("Student name: ")
            delete_student(data, name)

        elif choice == "3":
            name = input("Student name: ")
            subject = input("Subject: ")
            try:
                grade = float(input("Grade (0-20): "))
                add_grade(data, name, subject, grade)
            except ValueError:
                print("Invalid grade.")
        elif choice == "4":
            show_students(data)

        elif choice == "5":
            avg = calculate_class_average(data)
            print(f"Class average: {avg:.2f}")

        elif choice == "6":
            result = get_top_student(data)
            if result:
                student, avg = result
                print(f"Top student: {student} ({avg:.2f})")
            else:
                print("No data available.")

        elif choice == "7":
            save_data(data)
            print("Data saved. Exiting...")
            break

        else:
            print("Invalid choice.")
if __name__ == "__main__":
    menu()