# main.py

import pymysql
import students
import marks
import attendance
import report

while True:

    print("========== MAIN MENU ==========")
    print("1. Student Management")
    print("2. Marks Management")
    print("3. Attendance Management")
    print("4. Reports")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        students.student_menu()

    elif choice == "2":
        marks.marks_menu()

    elif choice == "3":
        attendance.attendance_menu()

    elif choice == "4":
        report.report_menu()

    elif choice == "5":
        print("Program ended.")
        break

    else:
        print("Invalid choice.")














