class EnrollmentException(Exception):
    def __init__(self, message="Enrollment operation failed"):
        self.message = message
        super().__init__(self.message)
