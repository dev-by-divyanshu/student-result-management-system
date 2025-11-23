# Project Statement: Student Result Management System

> *Project Definition Document*
> A Python-based Console Application using File Handling

## 1. Introduction
The *Student Result Management System* is a lightweight, modular Python application designed to digitize the academic record-keeping process. It serves as a foundational project for understanding software development, focusing on data persistence using file handling without relying on external database engines.

## 2. Problem Statement
In many introductory scenarios, student records are managed manually or through disconnected systems. This leads to:
* Difficulty in calculating complex metrics like CGPA manually.
* Data loss when programs are not persistent (data disappears after closing the code).
* Lack of organized structure in basic programming projects.

## 3. Proposed Solution
This project proposes a *CLI (Command Line Interface)* based application that:
1.  *Modularizes Logic:* Separates code into distinct files (student.py, marks.py, result.py) for better maintainability.
2.  *Ensures Persistence:* Uses simple text files (students.txt, marks.txt) to store data permanently.
3.  *Automates Grading:* Automatically computes Totals, Percentages, Grades, and CGPA based on input scores.

## 4. Functional Requirements
The system is designed to perform the following core functions:

### A. Student Management
* *Registration:* Ability to add new students with a unique Registration Number, Name, Semester, and Stream.
* *View:* Display a list of all registered students.
* *Storage:* Data is saved in students.txt.

### B. Marks Management
* *Entry:* Input marks for 5 distinct subjects mapped to a student's Registration Number.
* *Storage:* Marks are saved in marks.txt.

### C. Result Processing
* *Calculation:* The system automatically processes raw marks to generate:
    * *Total Marks:* Sum of 5 subjects.
    * *Percentage:* (Total / 5).
    * *CGPA:* (Percentage / 9.5).
* *Grading:* Assigns letter grades (A+ to F) based on fixed percentage thresholds.

## 5. Technical Specifications

### Technology Stack
* *Language:* Python 3.x
* *Interface:* Command Line / Terminal
* *Database:* Flat Text Files (.txt)
* *External Libraries:* None (Standard Library only)

### Code Structure
The project follows a modular architecture:
1.  **main.py**: Handles the main menu and program flow.
2.  **storage.py**: Manages low-level file Read/Write operations.
3.  **student.py**: Logic for student registration and display.
4.  **marks.py**: Logic for inputting and retrieving marks.
5.  **result.py**: Logic for mathematical calculations (CGPA/Grade).

## 6. Grading Logic
The system implements the following logic for academic evaluation:

| Percentage Range | Grade |
| :--- | :--- |
| 90 and above | *A+* |
| 80 – 89 | *A* |
| 70 – 79 | *B* |
| 60 – 69 | *C* |
| 50 – 59 | *D* |
| Below 50 | *F* |

* *CGPA Formula:* CGPA = Percentage / 9.5

## 7. Conclusion
This project demonstrates the practical application of Python programming concepts, specifically *File I/O, **Modular Programming, and **Data Processing*. It provides an efficient, lightweight solution for managing student results in a text-based environment.

---
*Submitted By:*
* *Name:* Divyanshu Kumar
* *Course:* B.Tech CSE (1st Year)
* *Institution:* VIT Bhopal University
