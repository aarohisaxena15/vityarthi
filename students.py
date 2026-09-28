import pymysql


con = pymysql.connect(host="localhost", user="root", password="97139713", database="college_project")
cur = con.cursor()

# Add Student
def add_student():
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    email = input("Enter email: ")
    course = input("Enter course: ")
    semester = int(input("Enter semester: "))

    query = """
    INSERT INTO students
    (name, roll_no, email, course, semester)
    VALUES (%s, %s, %s, %s, %s)
    """

    try:
        cur.execute(query, (name, roll_no, email, course, semester))
        con.commit()
        print("Student added successfully!")

    except pymysql.IntegrityError:
        print("Roll number already exists.")

    


# View Students
def view_students():
    cur.execute("SELECT * FROM students")

    students = cur.fetchall()

    if len(students) == 0:
        print("No students found.")

    else:
        print("\n---------- STUDENT RECORDS ----------")

        for student in students:
            print("Student ID :", student[0])
            print("Name       :", student[1])
            print("Roll No    :", student[2])
            print("Email      :", student[3])
            print("Course     :", student[4])
            print("Semester   :", student[5])
            print("-------------------------------------")

    


# Search Student
def search_student():
    roll_no = input("Enter roll number to search: ")

    query = "SELECT * FROM students WHERE roll_no = %s"

    cur.execute(query, (roll_no,))

    student = cur.fetchone()

    if student:
        print("\nStudent Found")
        print("Student ID :", student[0])
        print("Name       :", student[1])
        print("Roll No    :", student[2])
        print("Email      :", student[3])
        print("Course     :", student[4])
        print("Semester   :", student[5])

    else:
        print("Student not found.")

    


# Update Student
def update_student():
    roll_no = input("Enter roll number to update: ")

    cur.execute(
        "SELECT * FROM students WHERE roll_no = %s",
        (roll_no,)
    )

    student = cur.fetchone()

    if student:
        name = input("Enter new name: ")
        email = input("Enter new email: ")
        course = input("Enter new course: ")
        semester = int(input("Enter new semester: "))

        query = """
        UPDATE students
        SET name = %s,
            email = %s,
            course = %s,
            semester = %s
        WHERE roll_no = %s
        """

        cur.execute(
            query,
            (name, email, course, semester, roll_no)
        )

        con.commit()

        print("Student updated successfully!")

    else:
        print("Student not found.")

    


# Delete Student
def delete_student():
    roll_no = input("Enter roll number to delete: ")

    query = "DELETE FROM students WHERE roll_no = %s"

    cur.execute(query, (roll_no,))

    if cur.rowcount > 0:
        con.commit()
        print("Student deleted successfully!")

    else:
        print("Student not found.")



def student_menu():

    while True:
        print("\n===== STUDENT MANAGEMENT =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            break

        else:
            print("Invalid choice.")