
import pymysql


# Database connection
con = pymysql.connect(
    host="localhost",
    user="root",
    password="97139713",
    database="college_project"
)

cur = con.cursor()


# Add attendance
def add_attendance():

    roll_no = input("Enter student roll number: ").strip()

    if roll_no == "":
        print("Roll number cannot be empty.")
        return None, None

    # Find student
    cur.execute(
        "SELECT student_id FROM students WHERE roll_no = %s",
        (roll_no,)
    )

    student = cur.fetchone()

    if student is None:
        print("Student not found.")
        return None, None

    student_id = student[0]

    attendance = []

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

    # Enter attendance for each subject
    for i in range(n):

        subject = input(
            f"Enter subject {i + 1} name: "
        ).strip()

        while subject == "":
            print("Subject name cannot be empty.")

            subject = input(
                f"Enter subject {i + 1} name: "
            ).strip()

        # Total classes
        while True:

            try:
                total_classes = int(
                    input(
                        f"Enter total classes for {subject}: "
                    )
                )

                if total_classes <= 0:
                    print(
                        "Total classes must be greater than 0."
                    )
                else:
                    break

            except ValueError:
                print(
                    "Invalid input. Enter a whole number."
                )

        # Attended classes
        while True:

            try:
                attended_classes = int(
                    input(
                        f"Enter attended classes for {subject}: "
                    )
                )

                if attended_classes < 0:
                    print(
                        "Attended classes cannot be negative."
                    )

                elif attended_classes > total_classes:
                    print(
                        "Attended classes cannot be greater "
                        "than total classes."
                    )

                else:
                    break

            except ValueError:
                print(
                    "Invalid input. Enter a whole number."
                )

        attendance.append(
            (
                subject,
                total_classes,
                attended_classes
            )
        )

    # Save attendance in database
    for subject, total_classes, attended_classes in attendance:

        cur.execute(
            """
            INSERT INTO attendance
            (student_id, subject, total_classes, attended_classes)
            VALUES (%s, %s, %s, %s)
            """,
            (
                student_id,
                subject,
                total_classes,
                attended_classes
            )
        )

    con.commit()

    print("Attendance added successfully.")

    return roll_no, attendance


# Calculate attendance percentage
def calculate_percentage(total_classes, attended_classes):

    if total_classes <= 0:
        return 0

    return (
        attended_classes / total_classes
    ) * 100


# Calculate attendance status
def calculate_status(percentage):

    if percentage >= 75:
        return "Good"
    else:
        return "Low"


# Display attendance
def display_attendance(roll_no, attendance):

    print("\n----- ATTENDANCE DETAILS -----")
    print("Roll Number:", roll_no)

    for subject, total_classes, attended_classes in attendance:

        percentage = calculate_percentage(
            total_classes,
            attended_classes
        )

        status = calculate_status(percentage)

        print("\nSubject:", subject)
        print("Total Classes:", total_classes)
        print("Attended Classes:", attended_classes)
        print(
            "Attendance:",
            round(percentage, 2),
            "%"
        )
        print("Status:", status)


# Sort attendance
def sort_attendance(attendance):

    sorted_attendance = attendance.copy()

    sorted_attendance.sort(
        key=lambda x: calculate_percentage(x[1], x[2])
    )

    return sorted_attendance


# Search subject
def search_subject(attendance):

    subject = input(
        "Enter subject to search: "
    ).strip().lower()

    found = False

    for sub, total_classes, attended_classes in attendance:

        if sub.lower() == subject:

            percentage = calculate_percentage(
                total_classes,
                attended_classes
            )

            print("\nSubject found.")
            print("Subject:", sub)
            print("Total Classes:", total_classes)
            print("Attended Classes:", attended_classes)
            print(
                "Attendance:",
                round(percentage, 2),
                "%"
            )

            found = True

    if not found:
        print("Subject not found.")


# Attendance menu
def attendance_menu():

    roll_no, attendance = add_attendance()

    if attendance is None:
        return

    while True:

        print("----- ATTENDANCE MENU -----")
        print("1. Display attendance")
        print("2. Sort attendance")
        print("3. Search subject")
        print("4. Exit")

        try:

            choice = int(
                input("Enter your choice: ")
            )

            if choice == 1:

                display_attendance(
                    roll_no,
                    attendance
                )

            elif choice == 2:

                print("\nSorted Attendance:")

                sorted_data = sort_attendance(
                    attendance
                )

                for subject, total_classes, attended_classes in sorted_data:

                    percentage = calculate_percentage(
                        total_classes,
                        attended_classes
                    )

                    print(
                        subject,
                        ":",
                        round(percentage, 2),
                        "%"
                    )

            elif choice == 3:

                search_subject(attendance)

            elif choice == 4:

                print(
                    "Exiting attendance module..."
                )

                break

            else:

                print(
                    "Invalid choice. "
                    "Please enter a number from 1 to 4."
                )

        except ValueError:

            print(
                "Invalid input. "
                "Please enter a number from 1 to 4."
            )


# Run attendance module
if __name__ == "__main__":
    attendance_menu()





