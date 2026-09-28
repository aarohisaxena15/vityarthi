import pymysql


# Database connection
con = pymysql.connect(
    host="localhost",
    user="root",
    password="97139713",
    database="college_project"
)

cur = con.cursor()


# Add marks
def add_marks():

    roll_no = input("Enter student roll number: ").strip()

    if roll_no == "":
        print("Roll number cannot be empty.")
        return None, None

    cur.execute(
        "SELECT student_id FROM students WHERE roll_no = %s",
        (roll_no,)
    )

    student = cur.fetchone()

    if student is None:
        print("Student not found.")
        return None, None

    student_id = student[0]

    marks = []

    # Number of subjects
    while True:

        try:
            n = int(input("Enter number of subjects: "))

            if n <= 0:
                print("Number of subjects must be greater than 0.")
            else:
                break

        except ValueError:
            print("Invalid input. Enter a whole number.")

    # Enter marks
    for i in range(n):

        subject = input(f"Enter subject {i + 1} name: ").strip()

        while subject == "":
            print("Subject name cannot be empty.")
            subject = input(f"Enter subject {i + 1} name: ").strip()

        while True:

            try:
                mark = float(
                    input(f"Enter marks for {subject}: ")
                )

                if mark < 0:
                    print("Marks cannot be negative.")

                elif mark > 100:
                    print("Marks cannot be greater than 100.")

                else:
                    marks.append((subject, mark))
                    break

            except ValueError:
                print("Invalid input. Please enter a number.")

    # Save each subject mark
    for subject, mark in marks:

        cur.execute(
            """
            INSERT INTO marks
            (student_id, subject, marks)
            VALUES (%s, %s, %s)
            """,
            (student_id, subject, mark)
        )

    con.commit()

    print("Marks added successfully.")

    return roll_no, marks


# Calculate total
def calculate_total(marks):

    total = 0

    for subject, mark in marks:
        total += mark

    return total


# Calculate percentage
def calculate_percentage(marks):

    if len(marks) == 0:
        return 0

    total = calculate_total(marks)

    return total / len(marks)


# Generate grade
def calculate_grade(percentage):

    if percentage >= 90:
        return "A"

    elif percentage >= 75:
        return "B"

    elif percentage >= 60:
        return "C"

    elif percentage >= 50:
        return "D"

    else:
        return "F"


# Sort marks
def sort_marks(marks):

    sorted_marks = marks.copy()

    sorted_marks.sort(key=lambda x: x[1])

    return sorted_marks


# Search mark
def search_mark(marks):

    while True:

        try:
            mark = float(input("Enter mark to search: "))
            break

        except ValueError:
            print("Invalid input. Enter a number.")

    found = False

    for subject, value in marks:

        if value == mark:
            print("Mark found in", subject)
            found = True

    if not found:
        print("Mark not found.")


# Display marks
def display_marks(roll_no, marks):

    total = calculate_total(marks)
    percentage = calculate_percentage(marks)
    grade = calculate_grade(percentage)

    print("\n----- MARKS DETAILS -----")
    print("Roll Number:", roll_no)

    for subject, mark in marks:
        print(subject, ":", mark)

    print("Total:", total)
    print("Percentage:", round(percentage, 2), "%")
    print("Grade:", grade)


# Marks menu
def marks_menu():

    roll_no, marks = add_marks()

    if marks is None:
        return

    while True:

        print("\n----- MARKS MENU -----")
        print("1. Display marks")
        print("2. Sort marks")
        print("3. Search mark")
        print("4. Total and percentage")
        print("5. Exit")

        try:

            choice = int(input("Enter your choice: "))

            if choice == 1:
                display_marks(roll_no, marks)

            elif choice == 2:
                print("\nSorted marks:")

                for subject, mark in sort_marks(marks):
                    print(subject, ":", mark)

            elif choice == 3:
                search_mark(marks)

            elif choice == 4:

                print("Total:", calculate_total(marks))
                print(
                    "Percentage:",
                    round(calculate_percentage(marks), 2),
                    "%"
                )

            elif choice == 5:
                print("Exiting marks module...")
                break

            else:
                print(
                    "Invalid choice. "
                    "Please enter a number from 1 to 5."
                )

        except ValueError:
            print(
                "Invalid input. "
                "Please enter a number from 1 to 5."
            )


if __name__ == "__main__":
    marks_menu()
