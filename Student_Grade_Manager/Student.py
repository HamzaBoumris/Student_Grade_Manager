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