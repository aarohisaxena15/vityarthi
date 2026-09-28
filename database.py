
import pymysql


# Connect to MySQL server
con = pymysql.connect(
    host="localhost",
    user="root",
    password="97139713"
)

cur = con.cursor()


# Create database
cur.execute(
    "CREATE DATABASE IF NOT EXISTS college_project"
)

cur.close()
con.close()


# Connect to college_project database
con = pymysql.connect(
    host="localhost",
    user="root",
    password="97139713",
    database="college_project"
)

cur = con.cursor()


# ---------------- STUDENTS TABLE ----------------

cur.execute("""
CREATE TABLE IF NOT EXISTS students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    roll_no VARCHAR(20) UNIQUE NOT NULL,
    email VARCHAR(100),
    course VARCHAR(50),
    semester INT
);
""")


# ---------------- MARKS TABLE ----------------

cur.execute("""
CREATE TABLE IF NOT EXISTS marks (
    mark_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    subject VARCHAR(100) NOT NULL,
    marks FLOAT NOT NULL,

    FOREIGN KEY (student_id)
    REFERENCES students(student_id)
    ON DELETE CASCADE
);
""")


# ---------------- ATTENDANCE TABLE ----------------

cur.execute("""
CREATE TABLE IF NOT EXISTS attendance (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    subject VARCHAR(100) NOT NULL,
    total_classes INT NOT NULL,
    attended_classes INT NOT NULL,

    FOREIGN KEY (student_id)
    REFERENCES students(student_id)
    ON DELETE CASCADE
);
""")


# Save changes
con.commit()

cur.close()
con.close()

