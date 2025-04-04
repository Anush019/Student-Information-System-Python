class Teacher:
    def __init__(self, TeacherID, Name, Email, Expertise):
        self.TeacherID = TeacherID
        self.Name = Name
        self.Email = Email
        self.Expertise = Expertise
        self.AssignedCourses = []

    def AssignCourse(self, course):
        if course in self.AssignedCourses:
            return f"Already assigned to {course.CourseName}"

        self.AssignedCourses.append(course)
        course.AssignedTeacher = self
        return f"Assigned {course.CourseName} to {self.Name}"

    def GetAssignedCourses(self):
        return self.AssignedCourses
