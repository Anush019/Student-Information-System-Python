class PaymentException(Exception):
    def __init__(self, message="Payment operation failed"):
        self.message = message
        super().__init__(self.message)
