# Student Result Management System

A simple Python project to manage students using registration number, semester, and stream. It stores marks for five subjects, calculates total, percentage, grade, and CGPA, and saves all data in text files using a basic ‘|’ format. Easy, beginner-friendly, and ideal for first-year students.

---

## 📌 Features
- Add student using Registration Number
- View all students
- Enter marks for 5 subjects
- View marks of a student
- Calculate:
  - Total Marks
  - Percentage
  - Grade
  - CGPA
- Show result of a student
- Show result of all students

---

## 📁 Project Structure

main.py      → Main menu and program flow                                                                                                                                                                           student.py   → Add student, view students                                                                                                                                                                    marks.py     → Enter and view marks                                                                                                                                                                                 result.py    → Result calculation and display                                                                                                                                                                     storage.py   → Simple text file read/write                                                                                                                                                                          students.txt → Stores registration number, name, semester, stream                                                                                                                                                 marks.txt    → Stores marks of 5 subjects

---

## 🧾 Student Data Format
Stored in students.txt as:

registration_number | name | semester | stream

Example:

101 | Rahul | 1st Semester | CSE

---

## 📝 Marks Data Format
Stored in marks.txt as:

registration_number | sub1 | sub2 | sub3 | sub4 | sub5

Example:

101 | 85 | 90 | 78 | 88 | 92

---

## ▶ How to Run
1. Keep all .py files in one folder.
2. Open terminal / CMD in that folder.
3. Run:

python main.py

The program will create:
- students.txt
- marks.txt

These store student and marks data permanently.

---

## 🧠 How Result is Calculated

### ✔ Total

total = sum of 5 subject marks

### ✔ Percentage

percentage = total / 5

### ✔ Grade
- A+ → 90 and above  
- A  → 80–89  
- B  → 70–79  
- C  → 60–69  
- D  → 50–59  
- F  → below 50  

### ✔ CGPA

cgpa = percentage / 9.5

---

## 🎯 Purpose of the Project
- Practice basic Python  
- Learn multi-file programs  
- Understand simple file handling  
- Create a working result management system  
- Suitable for first-year B.Tech CSE submissions  

---

## 👤 Author
Divyanshu Kumar  
B.Tech CSE – 1st Year  
VIT Bhopal University


---
