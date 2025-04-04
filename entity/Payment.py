class Payment:
    payment_list = []

    def __init__(self, PaymentID, Student, Amount, PaymentDate):
        self.PaymentID = PaymentID
        self.Student = Student
        self.Amount = Amount
        self.PaymentDate = PaymentDate
