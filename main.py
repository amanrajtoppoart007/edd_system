# Directory: edd_system

# main.py
from controllers.app_controller import AppController

if __name__ == "__main__":
    print("EDD Technologies Repair System")
    app = AppController()
    app.run()


# Placeholder Files (to be implemented later)
# models/technician.py
# models/administrator.py
# models/job.py
# models/equipment.py
# services/notification_service.py
# services/supplier_manager.py
# utils/exceptions.py
# utils/menu.py
# tests/test_jobs.py

# Each of these files will follow similar structure: class-based logic with DB integration where needed.
