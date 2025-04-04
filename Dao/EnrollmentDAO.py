from util.db_util import connect_db
from exceptions.DatabaseException import DatabaseException
from exceptions.EnrollmentException import EnrollmentException

class EnrollmentDAO:
    def get_student(enrollment_id):
        try:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("""
            select s.StudentID, s.FirstName, s.LastName
            from Enrollments e
            join Students s on e.StudentID = s.StudentID
            where e.EnrollmentID = %s
            """, (enrollment_id,))
            student = cursor.fetchone()
            if not student:
                raise EnrollmentException("Student associated with this enrollment not found")
            return student
        except Exception as e:
            raise DatabaseException(f"Error fetching student: {str(e)}")
        finally:
            conn.close()

    def get_course(enrollment_id):
        try:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("""
            select c.CourseID, c.CourseName
            from Enrollments e
            join Courses c ON e.CourseID = c.CourseID
            where e.EnrollmentID = %s
            """, (enrollment_id,))
            course = cursor.fetchone()
            if not course:
                raise EnrollmentException("Course associated with this enrollment not found")
            return course
        except Exception as e:
            raise DatabaseException(f"Error fetching course: {str(e)}")
        finally:
            conn.close()


    def enroll_student(student_id, course_id):
        try:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("""
            insert into Enrollments (StudentID, CourseID, EnrollmentDate)
            values (%s, %s, NOW())
            """, (student_id, course_id))
            conn.commit()
            return cursor.lastrowid
        except Exception as e:
            raise DatabaseException(f"Error enrolling student: {str(e)}")
        finally:
            conn.close()

    def generate_enrollment_report(course_id):
        try:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("""
                   select S.StudentID, S.FirstName, S.LastName, S.Email 
                   from Enrollments E
                   join Students S on E.StudentID = S.StudentID
                   where E.CourseID = %s
               """, (course_id,))
            students = cursor.fetchall()

            if not students:
                return f"No students enrolled in Course {course_id}."

            report = [f"Enrollment Report for Course {course_id}:"]
            for student in students:
                report.append(f"ID: {student[0]}, Name: {student[1]} {student[2]}, Email: {student[3]}")
            return "\n".join(report)
        except Exception as e:
            raise DatabaseException(f"Error fetching enrollment report: {str(e)}")
        finally:
            conn.close()