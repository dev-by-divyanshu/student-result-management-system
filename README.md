# 🏫 Student Result Management System (Python + CSV)

A simple Python-based project that manages students, stores their marks, and automatically calculates *Total Marks, **Percentage, **Grade, and **CGPA*.  
Data is stored using *CSV files*, making the project lightweight, portable, and perfect for beginners.

---

## ⭐ Features

### 👨‍🎓 Student Management
- Add student  
- View all students  
- Search student  
- Update student  
- Delete student  

### 📝 Marks Management
- Enter marks for *5 subjects*  
- Update existing marks  
- View marks of a student  
- View all marks  

### 📊 Result Management
- Calculate:
  - Total Marks (out of 500)
  - Percentage
  - Grade (A+, A, B, C, D, F)
  - CGPA (percentage / 9.5)
- View result for one student  
- View result summary for all students  

---

## 🗂 Project Structure

main.py          - Main menu and navigation
student.py       - Student CRUD operations
marks.py         - Marks entry & view
results.py       - Result calculation (Total, Percentage, Grade, CGPA)
storage.py       - CSV read/write functions
utils.py         - Validation and helper functions
students.csv     - Auto-created student data
marks.csv        - Auto-created marks data
README.md        - Project documentation
statement.md     - Problem statement & scope

---

## ⚙ Technologies Used
- Python 3  
- CSV File Storage  
- Built-in Libraries: csv, os, time

---

## 🧠 Calculation Logic

### 🎓 Percentage

percentage = total_marks / 5

### 🏆 Grade Criteria
| Percentage | Grade |
|-----------|--------|
| ≥ 90      | A+     |
| 80–89     | A      |
| 70–79     | B      |
| 60–69     | C      |
| 50–59     | D      |
| < 50      | F      |

### 🎯 CGPA

CGPA = percentage / 9.5

---

## ▶ How to Run the Project

### Step 1: Install Python  
Make sure Python 3 is installed.

### Step 2: Open Terminal / CMD in Project Folder

### Step 3: Run the Program

python main.py

---

## 📁 CSV Files Used

### students.csv
Stores:
- Roll Number  
- Name  
- Class  
- Section  

### marks.csv
Stores:
- Roll Number  
- Marks for 5 subjects  

Both files are created automatically when the project runs.

---

## 🔍 Sample Output

Result for Rohan Sharma (Roll: 102) Marks: 85, 76, 92, 88, 74 Total: 415 / 500 Percentage: 83.0% Grade: A CGPA: 8.73 / 10

---

## 🚀 Future Enhancements
- Add GUI using Tkinter  
- Store data in SQLite/MySQL  
- Export results to PDF  
- Create web version using Flask  

---

## 👨‍💻 Author
*Divyanshu Kumar*  
VIT Bhopal University  
Python – Build Your Own Project  

---
