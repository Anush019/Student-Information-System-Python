from util.db_util import connect_db
from exceptions.DatabaseException import DatabaseException
from exceptions.StudentNotFoundException import StudentNotFoundException

class StudentDAO:
    def add_student(first_name, last_name, dob, email, phone):
        try:
            conn = connect_db()
            cursor = conn.cursor()
            sql = """insert into Students (FirstName, LastName, DateOfBirth, Email, PhoneNumber) 
                        values (%s, %s, %s, %s, %s)"""
            cursor.execute(sql, (first_name, last_name, dob, email, phone))
            conn.commit()
            return cursor.lastrowid
        except Exception as e:
            raise DatabaseException(f"Error adding student: {str(e)}")
        finally:
            conn.close()

    def enroll_in_course(student_id, course_id):
        try:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("""
                insert into Enrollments (StudentID, CourseID, EnrollmentDate)
                values (%s, %s, NOW())
            """, (student_id, course_id))
            conn.commit()
        except Exception as e:
            raise DatabaseException(f"Error enrolling student: {str(e)}")
        finally:
            conn.close()


    def update_student_info(student_id, first_name, last_name, date_of_birth, email, phone):
        try:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("""
                update Students
                set FirstName = %s, LastName = %s, DateOfBirth = %s, Email = %s, PhoneNumber = %s
                where StudentID = %s
            """, (first_name, last_name, date_of_birth, email, phone, student_id))
            conn.commit()
            if cursor.rowcount == 0:
                raise StudentNotFoundException("Student not found")
        except Exception as e:
            raise DatabaseException(f"Error updating student info: {str(e)}")
        finally:
            conn.close()


    def get_enrolled_courses(student_id):
        try:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("""
                select c.CourseID, c.CourseName from Enrollments e
                join Courses c ON e.CourseID = c.CourseID
                where e.StudentID = %s
            """, (student_id,))
            return cursor.fetchall()
        except Exception as e:
            raise DatabaseException(f"Error fetching enrolled courses: {str(e)}")
        finally:
            conn.close()


    def get_student(student_id):
        try:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute(
                "select StudentID, FirstName, LastName, Email, PhoneNumber from Students where StudentID = %s",
                (student_id,))
            student = cursor.fetchone()
            if not student:
                raise StudentNotFoundException("Student not found")
            return {
                "StudentID": student[0],
                "FirstName": student[1],
                "LastName": student[2],
                "Email": student[3],
                "PhoneNumber": student[4]
            }
        except Exception as e:
            raise DatabaseException(f"Error fetching student: {str(e)}")
        finally:
            conn.close()


    def get_payment_history(student_id):
        try:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("select PaymentID, Amount, PaymentDate from Payments where StudentID = %s", (student_id,))
            payments = cursor.fetchall()
            return [{
                "PaymentID": payment[0],
                "Amount": payment[1],
                "PaymentDate": payment[2]
            } for payment in payments]
        except Exception as e:
            raise DatabaseException(f"Error fetching payment history: {str(e)}")
        finally:
            conn.close()