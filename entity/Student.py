from datetime import datetime
from Enrollment import Enrollment
from Payment import Payment

class Student:
    def __init__(self, StudentID, FirstName, LastName, DateOfBirth, Email, PhoneNumber):
        self.StudentID = StudentID
        self.FirstName = FirstName
        self.LastName = LastName
        self.DateOfBirth = DateOfBirth
        self.Email = Email
        self.PhoneNumber = PhoneNumber
        self.Enrollments = []
        self.Payments = []

    def EnrollInCourse(self, course):
        if any(enrollment.Course == course for enrollment in self.Enrollments):
            return "Already Enrolled in this Course"

        new_enrollment = Enrollment(len(Enrollment.enrollment_list) + 1, self, course, datetime.today())
        Enrollment.enrollment_list.append(new_enrollment)
        self.Enrollments.append(new_enrollment)
        course.Enrollments.append(new_enrollment)
        return "Course Enrolled Successfully"

    def UpdateStudentInfo(self, FirstName=None, LastName=None, DateOfBirth=None, Email=None, PhoneNumber=None):
        if FirstName:
            self.FirstName = FirstName
        if LastName:
            self.LastName = LastName
        if DateOfBirth:
            self.DateOfBirth = DateOfBirth
        if Email:
            self.Email = Email
        if PhoneNumber:
            self.PhoneNumber = PhoneNumber

    def MakePayment(self, Amount):
        new_payment = Payment(len(Payment.payment_list) + 1, self, Amount, datetime.today())
        Payment.payment_list.append(new_payment)
        self.Payments.append(new_payment)
        return "Payment Recorded Successfully"

    def DisplayStudentInfo(self):
        return (f"Student ID: {self.StudentID}\n"
                f"First Name: {self.FirstName}\n"
                f"Last Name: {self.LastName}\n"
                f"Date of Birth: {self.DateOfBirth}\n"
                f"Email ID: {self.Email}\n"
                f"Phone Number: {self.PhoneNumber}")

    def GetEnrolledCourses(self):
        return [enrollment.Course for enrollment in self.Enrollments]

    def GetPaymentHistory(self):
        return self.Payments
