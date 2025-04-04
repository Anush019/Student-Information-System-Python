from util.db_util import connect_db
from exceptions.DatabaseException import DatabaseException
from exceptions.CourseNotFoundException import CourseNotFoundException

class CourseDAO:
    def assign_teacher(course_id, teacher_id):
        try:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("update Courses set TeacherID = %s where CourseID = %s", (teacher_id, course_id))
            conn.commit()
            if cursor.rowcount == 0:
                raise CourseNotFoundException("Course not found")
        except Exception as e:
            raise DatabaseException(f"Error assigning teacher to course: {str(e)}")
        finally:
            conn.close()


    def update_course_info(course_id, course_code, course_name):
        try:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("update Courses set CourseCode = %s, CourseName = %s where CourseID = %s", (course_code, course_name, course_id))
            conn.commit()
            if cursor.rowcount == 0:
                raise CourseNotFoundException("Course not found")
        except Exception as e:
            raise DatabaseException(f"Error updating course info: {str(e)}")
        finally:
            conn.close()


    def get_course(course_id):
        try:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("select CourseID, CourseName, CourseCode from Courses where CourseID = %s", (course_id,))
            course = cursor.fetchone()
            if not course:
                raise CourseNotFoundException("Course not found")
            return course
        except Exception as e:
            raise DatabaseException(f"Error fetching course: {str(e)}")
        finally:
            conn.close()


    def get_teacher(course_id):
        try:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("select TeacherID from Courses where CourseID = %s", (course_id,))
            teacher = cursor.fetchone()
            if not teacher or teacher[0] is None:
                raise CourseNotFoundException("No teacher assigned to this course")
            return teacher[0]
        except Exception as e:
            raise DatabaseException(f"Error fetching teacher for course: {str(e)}")
        finally:
            conn.close()


    def get_enrollments(course_id):
        try:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("select s.StudentID, s.FirstName, s.LastName from Enrollments e join Students s ON e.StudentID = s.StudentID where e.CourseID = %s ", (course_id,))
            return cursor.fetchall()
        except Exception as e:
            raise DatabaseException(f"Error fetching enrollments: {str(e)}")
        finally:
            conn.close()

    def calculate_course_statistics(course_id):
        try:
            conn = connect_db()
            cursor = conn.cursor()

            cursor.execute("select count(*) from enrollments where courseid = %s", (course_id,))
            num_enrollments = cursor.fetchone()[0]

            cursor.execute("""
                select coalesce(sum(p.amount), 0) 
                from payments p 
                join enrollments e on p.studentid = e.studentid 
                where e.courseid = %s
            """, (course_id,))
            total_payments = cursor.fetchone()[0]

            return {
                "Total Enrollments": num_enrollments,
                "Total Payments Received": total_payments
            }
        except Exception as e:
            raise DatabaseException(f"Error calculating course statistics: {str(e)}")
        finally:
            conn.close()