from database.database import Database

class Job:
    def __init__(self, description, status="Job Created", technician_id=None,equipment_id=None, id=None):
        self.description = description
        self.status = status
        self.technician_id = technician_id
        self.equipment_id = equipment_id
        self.id = id

    def save(self):
        db = Database().get_connection()
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO jobs (description, status, technician_id,equipment_id) VALUES (?, ?, ? ,?)",
            (self.description, self.status, self.technician_id)
        )
        db.commit()
        self.id = cursor.lastrowid
        return self.id

    @staticmethod
    def get_all():
        db = Database().get_connection()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM jobs")
        return cursor.fetchall()

    @staticmethod
    def get_by_technician(technician_id):
        db = Database().get_connection()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM jobs WHERE technician_id = ?", (technician_id,))
        return cursor.fetchall()
