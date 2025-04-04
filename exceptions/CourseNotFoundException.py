class CourseNotFoundException(Exception):
    def __init__(self, message="Course not found"):
        self.message = message
        super().__init__(self.message)
