# models/customer.py

from database.database import Database

class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def save(self):
        db = Database().get_connection()
        cursor = db.cursor()
        cursor.execute("INSERT INTO customers (name, email) VALUES (?, ?)", (self.name, self.email))
        db.commit()
        return cursor.lastrowid

    @staticmethod
    def find_by_email(email):
        db = Database().get_connection()
        cursor = db.cursor()
        cursor.execute("SELECT id, name, email FROM customers WHERE email = ?", (email,))
        row = cursor.fetchone()
        if row:
            return Customer(row[1], row[2])  # name, email
        return None
