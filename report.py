
import pymysql


# Database connection
con = pymysql.connect(
    host="localhost",
    user="root",
    password="97139713",
    database="college_project"
)

cur = con.cursor()


# Generate Student Report
def generate_report():

    roll_no = input("Enter student roll number: ").strip()

    if roll_no == "":
        print("Roll number cannot be empty.")
        return

    # Get student details
    cur.execute(
        "SELECT * FROM students WHERE roll_no = %s",
        (roll_no,)
    )

    student = cur.fetchone()

    if student is None:
        print("Student not found.")
        return

    student_id = student[0]

    print("\n======================================")
    print("       STUDENT PERFORMANCE REPORT")
    print("======================================")

    print("Student ID :", student[0])
    print("Name       :", student[1])
    print("Roll No    :", student[2])
    print("Email      :", student[3])
    print("Course     :", student[4])
    print("Semester   :", student[5])


    # Get marks
    cur.execute(
        """
        SELECT subject, marks
        FROM marks
        WHERE student_id = %s
        """,
        (student_id,)
    )

    marks = cur.fetchall()

    print("\n------------- MARKS ------------------")

    if len(marks) == 0:

        print("No marks available.")

    else:

        total = 0
        valid_marks = 0

        for subject, mark in marks:

            try:
                mark = float(mark)

                if mark < 0 or mark > 100:
                    print(subject, ": Invalid marks")
                    continue

                print(subject, ":", mark)

                total += mark
                valid_marks += 1

            except (ValueError, TypeError):

                print(subject, ": Invalid marks")


        if valid_marks > 0:

            percentage = total / valid_marks

            if percentage >= 90:
                grade = "A"

            elif percentage >= 75:
                grade = "B"

            elif percentage >= 60:
                grade = "C"

            elif percentage >= 50:
                grade = "D"

            else:
                grade = "F"

            print("--------------------------------------")
            print("Total      :", total)
            print("Percentage :", round(percentage, 2), "%")
            print("Grade      :", grade)

        else:

            print("No valid marks available.")


    # Get attendance
    cur.execute(
        """
        SELECT subject, total_classes, attended_classes
        FROM attendance
        WHERE student_id = %s
        """,
        (student_id,)
    )

    attendance = cur.fetchall()

    print("\n----------- ATTENDANCE ----------------")

    if len(attendance) == 0:

        print("No attendance records available.")

    else:

        for subject, total_classes, attended_classes in attendance:

            try:

                total_classes = int(total_classes)
                attended_classes = int(attended_classes)

                if total_classes <= 0:
                    print("Subject :", subject)
                    print("Invalid total classes.")
                    print("--------------------------------------")
                    continue

                if attended_classes < 0 or attended_classes > total_classes:
                    print("Subject :", subject)
                    print("Invalid attendance data.")
                    print("--------------------------------------")
                    continue

                attendance_percentage = (
                    attended_classes / total_classes
                ) * 100

                if attendance_percentage >= 75:
                    status = "Good"
                else:
                    status = "Low"

                print("Subject :", subject)
                print(
                    "Attendance :",
                    round(attendance_percentage, 2),
                    "%"
                )
                print("Status :", status)
                print("--------------------------------------")

            except (ValueError, TypeError):

                print("Subject :", subject)
                print("Invalid attendance data.")
                print("--------------------------------------")



# Report Menu
def report_menu():

    while True:

        print("\n========== REPORT MODULE ==========")
        print("1. Generate Student Report")
        print("2. Back")

        try:

            choice = int(input("Enter your choice: "))

            if choice == 1:

                generate_report()

            elif choice == 2:

                print("Returning to main menu...")
                break

            else:

                print("Invalid choice. Please enter 1 or 2.")

        except ValueError:

            print("Invalid input. Please enter 1 or 2.")


# Run report module
if __name__ == "__main__":
    report_menu()

