class DatabaseException(Exception):
    def __init__(self, message="Database operation failed"):
        self.message = message
        super().__init__(self.message)
