from util.db_util import connect_db
from dao.StudentDAO import StudentDAO
from exceptions.DatabaseException import DatabaseException
from exceptions.StudentNotFoundException import StudentNotFoundException
from exceptions.PaymentException import PaymentException

class PaymentDAO:
    def get_student(payment_id):
        try:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("""
            select s.StudentID, s.FirstName, s.LastName
            from Payments p
            join Students s on p.StudentID = s.StudentID
            where p.PaymentID = %s
            """, (payment_id,))
            student = cursor.fetchone()
            if not student:
                raise StudentNotFoundException("Student associated with this payment not found")
            return student
        except Exception as e:
            raise DatabaseException(f"Error fetching student: {str(e)}")
        finally:
            conn.close()


    def get_payment_amount(payment_id):
        try:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("select Amount from Payments where PaymentID = %s", (payment_id,))
            amount = cursor.fetchone()
            if not amount:
                raise PaymentException("Payment amount not found")
            return amount[0]
        except Exception as e:
            raise DatabaseException(f"Error fetching payment amount: {str(e)}")
        finally:
            conn.close()


    def get_payment_date(payment_id):
        try:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("select PaymentDate FROM Payments where PaymentID = %s", (payment_id,))
            date = cursor.fetchone()
            if not date:
                raise PaymentException("Payment date not found")
            return date[0]
        except Exception as e:
            raise DatabaseException(f"Error fetching payment date: {str(e)}")
        finally:
            conn.close()


    def make_payment(student_id, amount):
        try:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("""
                        insert into Payments (StudentID, Amount, PaymentDate)
                        values (%s, %s, NOW())
                    """, (student_id, amount))
            conn.commit()
        except Exception as e:
            raise PaymentException(f"Error processing payment: {str(e)}")
        finally:
            conn.close()


    def get_student_from_payment(payment_id):
        try:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("select StudentID from Payments where PaymentID = %s", (payment_id,))
            student = cursor.fetchone()
            if not student:
                raise PaymentException("Payment not found")
            return student[0]
        except Exception as e:
            raise DatabaseException(f"Error fetching student from payment: {str(e)}")
        finally:
            conn.close()

    def generate_payment_report(student_id):
        try:
            payments = StudentDAO.get_payment_history(student_id)
            if not payments:
                return f"No payments found for Student {student_id}."

            report = [f"Payment Report for Student {student_id}:"]
            for payment in payments:
                report.append(
                    f"Payment ID: {payment['PaymentID']}, Amount: {payment['Amount']}, Date: {payment['PaymentDate']}")
            return "\n".join(report)
        except Exception as e:
            raise DatabaseException(f"Error fetching payment report: {str(e)}")