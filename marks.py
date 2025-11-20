from storage import load_data, save_data

def enter_marks():
    reg = input("Enter registration number: ")

    students = load_data("students.txt")
    found = False
    for s in students:
        if s[0] == reg:
            found = True
            break

    if not found:
        print("Student not found.")
        return

    print("Enter marks for 5 subjects:")
    m1 = input("Subject 1: ")
    m2 = input("Subject 2: ")
    m3 = input("Subject 3: ")
    m4 = input("Subject 4: ")
    m5 = input("Subject 5: ")

    marks = load_data("marks.txt")

    updated = False
    for i, m in enumerate(marks):
        if m[0] == reg:
            marks[i] = [reg, m1, m2, m3, m4, m5]
            updated = True
            break

    if not updated:
        marks.append([reg, m1, m2, m3, m4, m5])

    save_data("marks.txt", marks)
    print("Marks saved.")

def view_marks():
    reg = input("Enter registration number: ")

    marks = load_data("marks.txt")

    for m in marks:
        if m[0] == reg:
            print("Marks:", m)
            return

    print("Marks not found.")