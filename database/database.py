import sqlite3

class Database:
    _connection = None  # Singleton connection

    def __init__(self):
        if Database._connection is None:
            Database._connection = sqlite3.connect("edd_system.db")
            self.create_tables()

    def create_tables(self):
        cursor = Database._connection.cursor()
        
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

        # Create jobs table (with equipment_id, technician_id, and job_cost)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS jobs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                equipment_id INTEGER NOT NULL,
                technician_id INTEGER,
                description TEXT NOT NULL,
                status TEXT NOT NULL,
                job_cost REAL DEFAULT 0,
                FOREIGN KEY(equipment_id) REFERENCES equipment(id),
                FOREIGN KEY(technician_id) REFERENCES technicians(id)
            )
        ''')
        
        # Create technicians table
        cursor.execute('''CREATE TABLE IF NOT EXISTS technicians (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            expertise TEXT NOT NULL
        )''')

        # Create suppliers table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS suppliers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                part_type TEXT NOT NULL,
                location TEXT NOT NULL
            )
        ''')


        Database._connection.commit()

    def get_connection(self):
        return Database._connection
