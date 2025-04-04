class TeacherNotFoundException(Exception):
    def __init__(self, message="Teacher not found"):
        self.message = message
        super().__init__(self.message)
