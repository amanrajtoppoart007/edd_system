from database.database import Database

class Technician:
    def __init__(self, name, expertise, id=None):
        self.name = name
        self.expertise = expertise
        self.id = id

    def save(self):
        db = Database().get_connection()
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO technicians (name, expertise) VALUES (?, ?)",
            (self.name, self.expertise)
        )
        db.commit()
        self.id = cursor.lastrowid
        return self.id

    @staticmethod
    def get_all():
        db = Database().get_connection()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM technicians")
        return cursor.fetchall()
