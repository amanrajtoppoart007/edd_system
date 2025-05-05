import sys
from models.customer import Customer
from models.equipment import Equipment
from models.job import Job
from models.administrator import Administrator
from models.technician import Technician
from database.database import Database

class AppController:
    def __init__(self):
        self.current_user = None
        self.db = Database()

    def run(self):
        while True:
            try:
                print("\n--- EDD Technologies ---")
                print("1. Login as Administrator")
                print("2. Login as Technician")
                print("3. Login as Customer")
                print("4. Exit")
                choice = input("Choose an option: ")
                if choice == '1':
                    name = input("Enter admin name: ")
                    self.current_user = Administrator(name)
                    self.admin_menu()
                elif choice == '2':
                    email = input("Enter technician email: ")
                    technician = Technician.find_by_email(email)
                    if technician:
                        self.current_user = technician
                        self.technician_menu()
                    else:
                        print("Technician not found.")
                elif choice == '3':
                    email = input("Enter your email: ")
                    customer = Customer.find_by_email(email)
                    if customer:
                        self.current_user = customer
                        self.customer_menu()
                    else:
                        print("Customer not found. Please register as walk-in.")
                elif choice == '4':
                    print("Goodbye!")
                    sys.exit()
                else:
                    print("Invalid option.")
            except KeyboardInterrupt:
                print("\n[!] Returning to main menu.")

    def admin_menu(self):
        while True:
            try:
                print("\n--- Admin Menu ---")
                print("1. Register Walk-in Customer")
                print("2. List All Jobs")
                print("3. Allocate Job to Technician")
                print("4. Add New Technician")
                print("5. Logout")
                choice = input("Choose an option: ")
                if choice == '1':
                    self.register_walkin_customer()
                elif choice == '2':
                    self.list_jobs()
                elif choice == '3':
                    self.allocate_job()
                elif choice == '4':
                    self.add_technician()
                elif choice == '5':
                    break
                else:
                    print("Invalid choice")
            except KeyboardInterrupt:
                print("\n[!] Returning to admin menu.")
                break


    def add_technician(self):
        try:
            name = input("Enter technician name: ")
            email = input("Enter technician email: ")
            expertise = input("Enter technician expertise: ")
            technician = Technician(name,email, expertise)
            technician.save()
            print(f"Technician '{name}' with '{email}' added successfully.")
        except Exception as e:
            print(f"[!] Error adding technician: {e}")

    def register_walkin_customer(self):
        try:
            name = input("Enter customer name: ")
            email = input("Enter email: ")
            equipment_type = input("Enter equipment type: ")
            serial = input("Enter serial number: ")

            customer = Customer(name, email)
            customer_id = customer.save()

            Equipment.save(customer_id, equipment_type, serial)
            print(f"Customer {name} and equipment details saved.")
        except Exception as e:
            print(f"Error while registering customer: {e}")

    def list_jobs(self):
        jobs = Job.get_all()
        for job in jobs:
            print(f"Job ID: {job[0]}, Description: {job[1]}, Status: {job[2]}")

    def allocate_job(self):
        try:
            equipment_id = input("Enter equipment ID to allocate job: ")
            technician_id = input("Enter technician ID to allocate job: ")
            description = input("Enter job description: ")
            job = Job(description, technician_id=technician_id,equipment_id=equipment_id)
            job.save()
            print(f"Job created with ID: {job.id}")
        except Exception as e:
            print(f"Error while allocating job: {e}")

    def technician_menu(self):
        while True:
            try:
                print("\n--- Technician Menu ---")
                print("1. List Jobs Assigned to Me")
                print("2. Logout")
                choice = input("Choose an option: ")
                if choice == '1':
                    self.list_jobs_for_technician()
                elif choice == '2':
                    break
                else:
                    print("Invalid choice")
            except KeyboardInterrupt:
                print("\n[!] Returning to technician menu.")
                break

    def list_jobs_for_technician(self):
        try:
            technician_id = self.current_user.get_id()
            jobs = Job.get_by_technician(technician_id)
            if jobs:
                for job in jobs:
                    print(f"Job ID: {job[0]}, Description: {job[1]}, Status: {job[2]}")
            else:
                print("No jobs assigned to you.")
        except Exception as e:
            print(f"Error while listing jobs: {e}")

    def customer_menu(self):
        while True:
            try:
                print("\n--- Customer Menu ---")
                print("1. Book Equipment Repair")
                print("2. Logout")
                choice = input("Choose an option: ")
                if choice == '1':
                    self.book_equipment_repair()
                elif choice == '2':
                    break
                else:
                    print("Invalid choice")
            except KeyboardInterrupt:
                print("\n[!] Returning to customer menu.")
                break

    def book_equipment_repair(self):
        try:
            equipment_type = input("Enter equipment type: ")
            serial = input("Enter serial number: ")
            customer_id = self.current_user.get_id()
            Equipment.save(customer_id, equipment_type, serial)
            print("Equipment registered for repair.")
        except Exception as e:
            print(f"Error while booking equipment: {e}")
