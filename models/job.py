# models/job.py
from database.database import Database

class Job:
    def __init__(self, description, status="Job Created"):
        self.description = description
        self.status = status

    def save(self):
        db = Database().get_connection()
        cursor = db.cursor()
        cursor.execute("INSERT INTO jobs (description, status) VALUES (?, ?)", (self.description, self.status))
        db.commit()

    @staticmethod
    def get_all():
        db = Database().get_connection()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM jobs")
        return cursor.fetchall()