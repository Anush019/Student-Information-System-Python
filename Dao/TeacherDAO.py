from util.db_util import connect_db
from exceptions.DatabaseException import DatabaseException
from exceptions.TeacherNotFoundException import TeacherNotFoundException

class TeacherDAO:

    def add_teacher(name, email, expertise):
        try:
            conn = connect_db()
            cursor = conn.cursor()
            sql = """insert into Teachers (Name, Email, Expertise) 
                        values (%s, %s, %s)"""
            cursor.execute(sql, (name, email, expertise))
            conn.commit()
            return cursor.lastrowid
        except Exception as e:
            raise DatabaseException(f"Error adding teacher: {str(e)}")
        finally:
            conn.close()


    def update_teacher_info(teacher_id, name, email, expertise):
        try:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("""
                update Teachers
                set Name = %s, Email = %s, Expertise = %s
                where TeacherID = %s
            """, (name, email, expertise, teacher_id))
            conn.commit()
            if cursor.rowcount == 0:
                raise TeacherNotFoundException("Teacher not found")
        except Exception as e:
            raise DatabaseException(f"Error updating teacher info: {str(e)}")
        finally:
            conn.close()


    def get_assigned_courses(teacher_id):
        try:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("""
                select CourseID, CourseName from Courses where TeacherID = %s
            """, (teacher_id,))
            return cursor.fetchall()
        except Exception as e:
            raise DatabaseException(f"Error fetching assigned courses: {str(e)}")
        finally:
            conn.close()


    def get_teacher(teacher_id):
        try:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("select TeacherID, Name, Email, Expertise from Teachers where TeacherID = %s", (teacher_id,))
            teacher = cursor.fetchone()
            if not teacher:
                raise TeacherNotFoundException("Teacher not found")
            return {
                "TeacherID": teacher[0],
                "Name": teacher[1],
                "Email": teacher[2],
                "Expertise": teacher[3]
            }
        except Exception as e:
            raise DatabaseException(f"Error fetching teacher: {str(e)}")
        finally:
            conn.close()