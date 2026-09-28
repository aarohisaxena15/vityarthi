# Student Management System

## 📌 Project Overview

The **Student Management System** is a Python-based college project
developed to manage student information, marks, attendance, and student
reports.

The application uses **Python** for the program logic and **MySQL** for
storing student data permanently. **PyMySQL** is used to establish the
connection between Python and MySQL.

The project follows a modular approach, where different tasks are
divided into separate Python files. It demonstrates important
programming concepts such as functions, loops, conditional statements,
lists, searching, sorting, modular programming, database connectivity,
SQL queries, and CRUD operations.

------------------------------------------------------------------------

## 🎯 Objectives

The main objectives of this project are:

-   To maintain student information digitally.
-   To store and retrieve student records using MySQL.
-   To manage student marks.
-   To calculate total marks and percentage.
-   To generate grades automatically.
-   To manage student attendance.
-   To calculate attendance percentage.
-   To check attendance eligibility.
-   To generate student reports.
-   To demonstrate Python modular programming and database connectivity.

------------------------------------------------------------------------

## 🚀 Features

### Student Management

-   Add new student records.
-   View student records.
-   Search student records.
-   Update student information.
-   Delete student records.

### Marks Management

-   Enter student marks.
-   Calculate total marks.
-   Calculate percentage.
-   Generate grades automatically.
-   Search marks using roll number.
-   Sort marks.

### Attendance Management

-   Enter total classes.
-   Enter attended classes.
-   Calculate attendance percentage.
-   Check attendance eligibility.
-   Search attendance records.

### Report Management

-   Generate student reports.
-   Retrieve student information from MySQL.
-   Display marks and academic performance.
-   Display attendance information.
-   Display grade and eligibility information.

### Database Management

-   Connect Python with MySQL.
-   Store records permanently.
-   Retrieve records using SQL queries.
-   Update and delete database records.

------------------------------------------------------------------------

## 🛠️ Technologies Used

  Technology   Purpose
  ------------ ---------------------------
  Python       Application development
  MySQL        Database management
  PyMySQL      Python-MySQL connectivity
  VS Code      Development environment
  Git          Version control
  GitHub       Project repository

------------------------------------------------------------------------

## 📂 Project Structure

``` text
Student-Management-System/
│
├── main.py
├── database.py
├── student.py
├── marks.py
├── attendance.py
├── report.py
├── requirements.txt
└── README.md
```

------------------------------------------------------------------------

## 📄 Module Description

### 1. `main.py`

This is the main module of the application.

It provides the main menu and connects the different modules of the
project.

Responsibilities:

-   Display the main menu.
-   Take user choices.
-   Open Student Management.
-   Open Marks Management.
-   Open Attendance Management.
-   Open Report Management.
-   Exit the application.

------------------------------------------------------------------------

### 2. `database.py`

This module manages the connection between Python and MySQL.

It contains the common database connection function used by other
modules.

Example:

``` python
from database import get_connection

con = get_connection()
cur = con.cursor()
```

Keeping the connection code in a separate module avoids repeating the
same database connection code in every file.

------------------------------------------------------------------------

### 3. `student.py`

This module manages student information.

Typical student information includes:

-   Student ID
-   Name
-   Roll Number
-   Email
-   Course
-   Semester

The module can perform operations such as:

-   Add student
-   View student
-   Search student
-   Update student
-   Delete student

------------------------------------------------------------------------

### 4. `marks.py`

This module manages student marks.

Functions include:

-   Add marks
-   Calculate total
-   Calculate percentage
-   Generate grade
-   Search marks
-   Sort marks

The grade is generated according to the percentage calculated from the
entered marks.

------------------------------------------------------------------------

### 5. `attendance.py`

This module manages student attendance.

Functions include:

-   Add attendance
-   Calculate attendance percentage
-   Check attendance eligibility
-   Search attendance records

The attendance percentage is calculated using:

``` text
Attendance Percentage =
(Classes Attended / Total Classes) × 100
```

------------------------------------------------------------------------

### 6. `report.py`

This module generates student reports.

It retrieves information from the database and displays relevant student
information such as:

-   Student details
-   Marks
-   Total marks
-   Percentage
-   Grade
-   Attendance
-   Attendance percentage
-   Attendance status

------------------------------------------------------------------------

## 🗄️ Database

The project uses **MySQL** as its database.

### Database Name

``` text
college_project
```

### Main Tables

``` text
students
marks
attendance
```

The `students` table stores student information.

The `marks` table stores student marks and academic results.

The `attendance` table stores attendance information.

------------------------------------------------------------------------

## 🧱 Database Relationship

The general relationship between the modules and database can be
represented as:

``` text
                 Student Management System
                           |
             -----------------------------
             |             |             |
          Students        Marks       Attendance
             |             |             |
             --------------|--------------
                           |
                     MySQL Database
                           |
                        Reports
```

Student records are identified using the student's roll number or
student ID depending on the operation.

------------------------------------------------------------------------

## 📋 Requirements

Before running the project, install the following:

-   Python 3.x
-   MySQL Server
-   MySQL client or MySQL Workbench
-   PyMySQL
-   VS Code (recommended)

------------------------------------------------------------------------

## 📦 Installation

### Step 1: Install Python

Download and install Python 3.x.

Check whether Python is installed:

``` bash
python --version
```

------------------------------------------------------------------------

### Step 2: Install MySQL

Install MySQL Server and make sure the MySQL service is running.

You can use MySQL Workbench to manage the database.

------------------------------------------------------------------------

### Step 3: Install PyMySQL

Open the terminal in the project folder and run:

``` bash
pip install pymysql
```

------------------------------------------------------------------------

### Step 4: Install Requirements

If the project contains `requirements.txt`, run:

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

## ⚙️ Database Setup

Open MySQL Workbench or the MySQL command line.

Create the database:

``` sql
CREATE DATABASE college_project;
```

Select the database:

``` sql
USE college_project;
```

Create the required tables according to the SQL structure used by the
project.

The main tables are:

``` text
students
marks
attendance
```

------------------------------------------------------------------------

## 🔌 Database Configuration

Open:

``` text
database.py
```

Configure the MySQL connection.

Example:

``` python
import pymysql

def get_connection():
    con = pymysql.connect(
        host="localhost",
        user="root",
        password="YOUR_PASSWORD",
        database="college_project"
    )

    return con
```

Replace:

``` text
YOUR_PASSWORD
```

with your local MySQL password.

### ⚠️ Security

Do **not** upload your real MySQL password to GitHub.

For a public repository, use environment variables or another secure
configuration method instead of hardcoding passwords.

------------------------------------------------------------------------

## ▶️ Running the Project

Open the project folder in VS Code.

Run the main program:

``` bash
python main.py
```

If your main file has a different name, run that file instead.

------------------------------------------------------------------------

## 🖥️ Main Menu

When the program starts, the main menu provides access to the different
modules.

Example:

``` text
================================
     COLLEGE MANAGEMENT SYSTEM
================================

1. Student Management
2. Marks Management
3. Attendance Management
4. Report
5. Exit
```

Select an option by entering its corresponding number.

------------------------------------------------------------------------

## 🔄 Working Flow

The overall working flow of the project is:

``` text
Start
  |
  v
Main Menu
  |
  +-------------------+
  |                   |
  v                   v
Student            Marks
Management         Management
  |                   |
  |                   |
  +---------+---------+
            |
            v
       Attendance
       Management
            |
            v
          Report
            |
            v
      MySQL Database
            |
            v
      Display Result
            |
            v
      Return to Menu
            |
            v
           Exit
```

------------------------------------------------------------------------

## 🧮 Marks Calculation

The total marks are calculated as:

``` text
Total = Sum of all subject marks
```

The percentage is calculated as:

``` text
Percentage = Total Marks / Number of Subjects
```

The project then uses the percentage to generate a grade.

Example:

``` text
Marks:
80, 85, 90, 75, 88

Total:
418

Percentage:
83.6%

Grade:
B
```

------------------------------------------------------------------------

## 📊 Attendance Calculation

Attendance percentage is calculated using:

``` text
Attendance Percentage =
(Attended Classes / Total Classes) × 100
```

For example:

``` text
Total Classes = 100
Classes Attended = 85

Attendance Percentage = 85%
```

The project can then determine whether the student meets the required
attendance level.

------------------------------------------------------------------------

## 🔎 Searching

The project uses searching concepts to find student-related information.

For example, a student can be searched using:

``` text
Roll Number
```

The program sends an SQL query to the MySQL database and retrieves the
matching record.

------------------------------------------------------------------------

## 🔢 Sorting

Sorting concepts are demonstrated in the marks module.

Marks can be arranged in ascending order to demonstrate the sorting
concept.

Example:

``` text
Before:
85, 62, 91, 74, 80

After sorting:
62, 74, 80, 85, 91
```

------------------------------------------------------------------------

## 🧩 Python Concepts Used

This project demonstrates several Python concepts studied in programming
courses.

### Basic Python

-   Variables
-   Data types
-   Input and output
-   Operators
-   Expressions

### Control Statements

-   `if`
-   `elif`
-   `else`

### Loops

-   `for`
-   `while`

### Functions

-   Function definition
-   Function calls
-   Parameters and arguments
-   Return values

### Data Structures

-   Lists
-   Tuples
-   Strings

### Modular Programming

The project is divided into multiple Python modules:

``` text
main.py
database.py
student.py
marks.py
attendance.py
report.py
```

### Database Programming

-   SQL queries
-   `INSERT`
-   `SELECT`
-   `UPDATE`
-   `DELETE`
-   `COMMIT`
-   Database connections

### Searching and Sorting

-   Searching student records
-   Searching marks
-   Sorting marks

------------------------------------------------------------------------

## 🧪 Testing

The project can be tested using different inputs.

### Student Testing

Test cases include:

-   Adding a valid student
-   Searching for an existing student
-   Searching for a non-existing student
-   Updating student information
-   Deleting a student

### Marks Testing

Test cases include:

-   Entering valid marks
-   Calculating total
-   Calculating percentage
-   Generating grade
-   Searching marks
-   Sorting marks

### Attendance Testing

Test cases include:

-   Entering valid attendance
-   Calculating attendance percentage
-   Checking eligibility
-   Searching attendance

### Database Testing

Test the following:

-   Database connection
-   Data insertion
-   Data retrieval
-   Data update
-   Data deletion

------------------------------------------------------------------------

## ❗ Error Handling

The project validates user inputs wherever required.

Examples include:

-   Invalid menu choices
-   Invalid marks
-   Invalid attendance values
-   Invalid student information
-   Database connection errors
-   Records that do not exist

Appropriate messages are displayed when invalid input is entered.

------------------------------------------------------------------------

## 🔐 Data Security

The project uses a local MySQL database for storing student information.

Database credentials should not be exposed in a public GitHub
repository.

For future improvements, environment variables can be used to store:

``` text
DB_HOST
DB_USER
DB_PASSWORD
DB_NAME
```

A `.env` file should be added to `.gitignore` so that sensitive
credentials are not uploaded.

------------------------------------------------------------------------

## 📈 Future Enhancements

The project can be extended with additional features such as:

-   Admin login
-   Student login
-   Password authentication
-   Subject-wise marks
-   Subject-wise attendance
-   Fee management
-   Timetable management
-   Faculty management
-   Search and filter options
-   PDF report generation
-   Excel report generation
-   Graphical User Interface using Tkinter
-   Web-based interface
-   Dashboard with charts
-   Email notifications
-   Cloud database support

------------------------------------------------------------------------

## 🎓 Learning Outcomes

After completing this project, the following concepts are demonstrated:

1.  Designing a modular Python application.
2.  Creating and using Python functions.
3.  Using loops and conditional statements.
4.  Working with lists and other data structures.
5.  Implementing searching and sorting.
6.  Connecting Python with MySQL.
7.  Executing SQL queries using PyMySQL.
8.  Performing CRUD operations.
9.  Validating user input.
10. Organizing a complete Python project into multiple modules.

------------------------------------------------------------------------

## 📌 Project Information

  Information            Details
  ---------------------- ---------------------------
  Project Name           Student Management System
  Programming Language   Python
  Database               MySQL
  Database Connector     PyMySQL
  IDE                    Visual Studio Code
  Project Type           College Academic Project

------------------------------------------------------------------------

## 👨‍💻 Author

**Student Management System**

Developed as a college academic project using Python and MySQL.

------------------------------------------------------------------------

## 📜 License

This project is created for educational and academic purposes.
