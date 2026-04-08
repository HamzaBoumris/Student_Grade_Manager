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
