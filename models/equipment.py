from database.database import Database

class Equipment:
    @staticmethod
    def save(customer_id, type, serial_number):
        db = Database().get_connection()
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO equipment (customer_id, type, serial_number) VALUES (?, ?, ?)",
            (customer_id, type, serial_number)
        )
        db.commit()
