from storage import load_data

def calculate_result(m):
    total = 0
    for i in range(1, 6):
        total += int(m[i])

    percentage = total / 5

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    cgpa = round(percentage / 9.5, 2)

    return total, percentage, grade, cgpa


def show_result():
    reg = input("Enter registration number: ")

    students = load_data("students.txt")
    marks = load_data("marks.txt")

    student = None
    for s in students:
        if s[0] == reg:
            student = s
            break

    if student is None:
        print("Student not found.")
        return

    markrow = None
    for m in marks:
        if m[0] == reg:
            markrow = m
            break

    if markrow is None:
        print("Marks not entered.")
        return

    total, per, grade, cgpa = calculate_result(markrow)

    print("\n--- Result ---")
    print("Name:", student[1])
    print("Semester:", student[2])
    print("Stream:", student[3])
    print("Total:", total)
    print("Percentage:", per)
    print("Grade:", grade)
    print("CGPA:", cgpa)


def show_all_results():
    students = load_data("students.txt")
    marks = load_data("marks.txt")

    print("\nReg No | Name | Percentage | Grade | CGPA")
    print("------------------------------------------")

    for s in students:
        reg = s[0]
        markrow = None
        for m in marks:
            if m[0] == reg:
                markrow = m
                break

        if markrow:
            _, per, grade, cgpa = calculate_result(markrow)
            print(reg, "|", s[1], "|", per, "|", grade, "|", cgpa)
        else:
            print(reg, "|", s[1], "| No Marks")