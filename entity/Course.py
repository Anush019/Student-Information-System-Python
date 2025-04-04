class Course:
    def __init__(self, CourseID, CourseName, CourseCode, AssignedTeacher=None):
        self.CourseID = CourseID
        self.CourseName = CourseName
        self.CourseCode = CourseCode
        self.AssignedTeacher = AssignedTeacher
        self.Enrollments = []

    def AssignTeacher(self, teacher):
        self.AssignedTeacher = teacher
        return f"Teacher {teacher.Name} assigned to {self.CourseName}"

    def GetEnrollments(self):
        return [enrollment.Student for enrollment in self.Enrollments]
