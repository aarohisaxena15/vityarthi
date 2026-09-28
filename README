# Student Management System

A Python-based Student Management System developed using Python and MySQL. The project is designed to manage student information, marks, attendance, and generate student performance reports through a modular and database-driven system.

## Features

* Add student details
* Store student name, roll number, email, course, and semester
* View student information
* Search students using roll number
* Update student details
* Delete student records
* Add marks for multiple subjects
* Calculate total marks
* Calculate percentage
* Generate grades
* Sort marks
* Search for marks
* Record subject-wise attendance
* Calculate attendance percentage
* Display attendance status
* Generate student performance reports
* MySQL database integration
* Input validation
* Exception handling
* Uses `student_id` to connect student, marks, and attendance records

## Technologies Used

* Python
* MySQL
* PyMySQL

## Project Structure

```text
Student-Management-System/
│
├── main.py
├── students.py
├── marks.py
├── attendance.py
├── report.py
├── database.py
└── README.md
```

## Module Description

### 1. main.py

The main module controls the entire application.

It provides the main menu and allows the user to access different modules.

Main options include:

* Student Management
* Marks Management
* Attendance Management
* Report Generation
* Exit

### 2. students.py

This module manages student information.

It stores:

* Student ID
* Student Name
* Roll Number
* Email
* Course
* Semester

The roll number is unique for every student.

Student records can be added, viewed, searched, updated, and deleted.

### 3. marks.py

This module manages student marks.

The user enters the student's roll number. The program finds the corresponding `student_id` from the students table.

The module allows the user to:

* Enter marks
* Display marks
* Calculate total
* Calculate percentage
* Generate grade
* Sort marks
* Search for a particular mark

Marks are validated so that values must be between 0 and 100.

### 4. attendance.py

This module manages student attendance.

The user enters the student's roll number and provides attendance details for different subjects.

The module allows the user to:

* Enter total classes
* Enter attended classes
* Calculate attendance percentage
* Display attendance
* Sort attendance
* Search for a subject
* Display attendance status

Attendance values are validated to prevent invalid data.

### 5. report.py

This module generates a complete student performance report.

The user enters the student's roll number.

The report displays:

* Student ID
* Name
* Roll Number
* Email
* Course
* Semester
* Subject-wise marks
* Total marks
* Percentage
* Grade
* Subject-wise attendance
* Attendance percentage
* Attendance status

### 6. database.py

This module creates the MySQL database and required tables.

The database contains:

* `students`
* `marks`
* `attendance`

Foreign keys are used to connect marks and attendance records with the correct student.

## Database Structure

### Students Table

```text
student_id
name
roll_no
email
course
semester
```

### Marks Table

```text
mark_id
student_id
subject
marks
```

### Attendance Table

```text
id
student_id
subject
total_classes
attended_classes
```

The `student_id` connects the student's personal information with their marks and attendance.

## Student Identification

The system uses the student's roll number to identify a student.

For example:

```text
Enter student roll number: 24
```

The program searches the `students` table and obtains the corresponding `student_id`.

The `student_id` is then used internally to store and retrieve marks and attendance.

This ensures that academic records are associated with the correct student.

## Marks Calculation

The total marks are calculated using:

```text
Total = Sum of all subject marks
```

Percentage is calculated using:

```text
Percentage = Total Marks / Number of Subjects
```

### Grade System

```text
90 and above  → A
75 - 89       → B
60 - 74       → C
50 - 59       → D
Below 50      → F
```

## Attendance Calculat
