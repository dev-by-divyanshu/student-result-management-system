from student import add_student, view_students
from marks import enter_marks, view_marks
from result import show_result, show_all_results

def menu():
    while True:
        print("\n1. Add Student")
        print("2. Enter Marks")
        print("3. View Marks")
        print("4. Show Result")
        print("5. View All Students")
        print("6. Show All Results")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            enter_marks()
        elif choice == "3":
            view_marks()
        elif choice == "4":
            show_result()
        elif choice == "5":
            view_students()
        elif choice == "6":
            show_all_results()
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid option.")

menu()