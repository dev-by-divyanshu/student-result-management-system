from storage import load_data, save_data

def add_student():
    reg = input("Enter registration number: ")
    name = input("Enter name: ")
    sem = input("Enter semester: ")
    stream = input("Enter stream: ")

    students = load_data("students.txt")

    for s in students:
        if s[0] == reg:
            print("Student already exists.")
            return

    students.append([reg, name, sem, stream])
    save_data("students.txt", students)
    print("Student added.")

def view_students():
    students = load_data("students.txt")

    if not students:
        print("No students found.")
        return

    print("\n--- Students ---")
    for s in students:
        print(s)