import sqlite3

class Database:
    def __init__(self):
        self.connection = sqlite3.connect("edd_system.db")
        self.create_tables()

    def create_tables(self):
        cursor = self.connection.cursor()
        
        # Create customers table
        cursor.execute('''CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        )''')
        
        # Create equipment table
        cursor.execute('''CREATE TABLE IF NOT EXISTS equipment (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER,
            type TEXT NOT NULL,
            serial_number TEXT NOT NULL,
            FOREIGN KEY(customer_id) REFERENCES customers(id)
        )''')

        # Create jobs table
        cursor.execute('''CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            status TEXT NOT NULL,
            technician_id INTEGER,
            FOREIGN KEY(technician_id) REFERENCES technicians(id)
        )''')
        
        # Create technicians table
        cursor.execute('''CREATE TABLE IF NOT EXISTS technicians (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            expertise TEXT NOT NULL
        )''')

        self.connection.commit()

    def get_connection(self):
        return self.connection
