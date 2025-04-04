from util.db_util import connect_db
from exceptions.DatabaseException import DatabaseException
from exceptions.CourseNotFoundException import CourseNotFoundException
from exceptions.TeacherNotFoundException import TeacherNotFoundException
from exceptions.PaymentException import PaymentException
from exceptions.StudentNotFoundException import StudentNotFoundException
from dao.StudentDAO import StudentDAO
from dao.TeacherDAO import TeacherDAO
from dao.CourseDAO import CourseDAO
from dao.EnrollmentDAO import EnrollmentDAO
from dao.PaymentDAO import PaymentDAO

def main():
    while True:
        print("\nStudent Information System:")
        print("1. Enroll Student in Course")
        print("2. Update Student Info")
        print("3. Make Payment")
        print("4. Display Student Info")
        print("5. Get Enrolled Courses")
        print("6. Get Payment History")
        print("7. Assign Teacher to Course")
        print("8. Update Course Info")
        print("9. Display Course Info")
        print("10. Get Enrollments")
        print("11. Get Teacher")
        print("12. Get Student from Enrollment")
        print("13. Get Course from Enrollment")
        print("14. Update Teacher Info")
        print("15. Display Teacher Info")
        print("16. Get Assigned Courses")
        print("17. Get Student from Payment")
        print("18. Get Payment Amount")
        print("19. Get Payment Date")
        print("20. Generate Enrollment Report")
        print("21. Generate Payment Report")
        print("22. Calculate Course Statistics")
        print("23. Exit")

        choice = input("Enter: ")

        try:
            if choice == "1":
                student_id = input("Enter Student ID: ")
                course_id = input("Enter Course ID: ")
                EnrollmentDAO.enroll_student(student_id, course_id)
                print("Student enrolled successfully.")
            elif choice == "2":
                student_id = input("Enter Student ID: ")
                first_name = input("Enter First Name: ")
                last_name = input("Enter Last Name: ")
                dob = input("Enter Date of Birth (Y-M-D): ")
                email = input("Enter Email: ")
                phone = input("Enter Phone Number: ")
                StudentDAO.update_student_info(student_id, first_name, last_name, dob, email, phone)
                print("Student information updated successfully.")
            elif choice == "3":
                student_id = input("Enter Student ID: ")
                amount = float(input("Enter Payment Amount: "))
                PaymentDAO.make_payment(student_id, amount)
                print("Payment recorded successfully.")
            elif choice == "4":
                student_id = input("Enter Student ID: ")
                student_info = StudentDAO.get_student(student_id)
                print(f"ID: {student_info['StudentID']}, Name: {student_info['FirstName']} {student_info['LastName']}")
                print(f"Email: {student_info['Email']}, Phone: {student_info['PhoneNumber']}")
            elif choice == "5":
                student_id = input("Enter Student ID: ")
                courses = StudentDAO.get_enrolled_courses(student_id)
                for course in courses:
                    print(f"Course ID: {course[0]}, Name: {course[1]}")
            elif choice == "6":
                student_id = input("Enter Student ID: ")
                payments = StudentDAO.get_payment_history(student_id)
                for payment in payments:
                    print(f"Payment ID: {payment['PaymentID']}, Amount: {payment['Amount']}, Date: {payment['PaymentDate']}")
            elif choice == "7":
                teacher_id = input("Enter Teacher ID: ")
                course_id = input("Enter Course ID: ")
                CourseDAO.assign_teacher(teacher_id, course_id)
                print("Teacher assigned successfully.")
            elif choice == "8":
                course_id = input("Enter Course ID: ")
                course_code = input("Enter Course Code: ")
                course_name = input("Enter Course Name: ")
                CourseDAO.update_course_info(course_id, course_code, course_name)
                print("Course information updated successfully.")
            elif choice == "9":
                course_id = input("Enter Course ID: ")
                course_info = CourseDAO.get_course(course_id)
                print(f"Course ID: {course_info[0]}, Name: {course_info[1]}, Code: {course_info[2]}")
            elif choice == "10":
                course_id = input("Enter Course ID: ")
                enrollments = CourseDAO.get_enrollments(course_id)
                for enrollment in enrollments:
                    print(f"Enrollment ID: {enrollment[0]}, Student ID: {enrollment[1]}")
            elif choice == "11":
                course_id = input("Enter Course ID: ")
                teacher = CourseDAO.get_teacher(course_id)
                print(f"Assigned Teacher: {teacher}")
            elif choice == "12":
                enrollment_id = input("Enter Enrollment ID: ")
                student = EnrollmentDAO.get_student(enrollment_id)
                print(f"Student ID: {student}")
            elif choice == "13":
                enrollment_id = input("Enter Enrollment ID: ")
                course = EnrollmentDAO.get_course(enrollment_id)
                print(f"Course ID: {course}")
            elif choice == "14":
                teacher_id = input("Enter Teacher ID: ")
                name = input("Enter Name: ")
                email = input("Enter Email: ")
                expertise = input("Enter Expertise: ")
                TeacherDAO.update_teacher_info(teacher_id, name, email, expertise)
                print("Teacher information updated successfully.")
            elif choice == "15":
                teacher_id = input("Enter Teacher ID: ")
                teacher_info = TeacherDAO.get_teacher(teacher_id)
                print(f"Teacher ID: {teacher_info['TeacherID']}, Name: {teacher_info['Name']}")
            elif choice == "16":
                teacher_id = input("Enter Teacher ID: ")
                courses = TeacherDAO.get_assigned_courses(teacher_id)
                for course in courses:
                    print(f"Course ID: {course[0]}, Name: {course[1]}")
            elif choice == "17":
                payment_id = input("Enter Payment ID: ")
                student_id = PaymentDAO.get_student_from_payment(payment_id)
                print(f"Student ID: {student_id}")
            elif choice == "18":
                payment_id = input("Enter Payment ID: ")
                amount = PaymentDAO.get_payment_amount(payment_id)
                print(f"Payment Amount: {amount}")
            elif choice == "19":
                payment_id = input("Enter Payment ID: ")
                payment_date = PaymentDAO.get_payment_date(payment_id)
                print(f"Payment Date: {payment_date}")
            elif choice == "20":
                course_id = input("Enter Course ID: ")
                report = EnrollmentDAO.generate_enrollment_report(course_id)
                print(report)
            elif choice == "21":
                student_id = input("Enter Student ID: ")
                report = PaymentDAO.generate_payment_report(student_id)
                print(report)
            elif choice == "22":
                course_id = input("Enter Course ID: ")
                stats = CourseDAO.calculate_course_statistics(course_id)
                print(f"Total Enrollments: {stats['Total Enrollments']}")
                print(f"Total Payments Received: {stats['Total Payments Received']}")
            elif choice == "23":
                print("Exiting Student Information System.")
                break
            else:
                print("Invalid choice. Please try again.")
        except (DatabaseException, StudentNotFoundException, TeacherNotFoundException, CourseNotFoundException, PaymentException) as e:
            print(f"Error: {str(e)}")

main()
