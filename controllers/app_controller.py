import sys
from models.administrator import Administrator
from models.technician import Technician
from models.customer import Customer
from models.job import Job

class AppController:
    def __init__(self):
        self.current_user = None

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
                    name = input("Enter technician name: ")
                    self.current_user = Technician(name)
                    self.technician_menu()
                elif choice == '3':
                    name = input("Enter customer name: ")
                    email = input("Enter email: ")
                    self.current_user = Customer(name, email)
                    self.customer_menu()
                elif choice == '4':
                    print("Goodbye!")
                    sys.exit()
                else:
                    print("Invalid option!")
            except KeyboardInterrupt:
                print("\n[!] KeyboardInterrupt detected. Returning to main menu.\n")


    def admin_menu(self):
        while True:
            print("\n--- Admin Menu ---")
            print("1. Register Walk-in Customer")
            print("2. List All Jobs")
            print("3. Logout")
            choice = input("Choose an option: ")
            if choice == '1':
                self.current_user.register_walkin_customer()
            elif choice == '2':
                self.list_jobs()
            elif choice == '3':
                break
            else:
                print("Invalid choice")

    def technician_menu(self):
        print("Technician functionality not implemented yet.")
        input("Press Enter to return...")

    def customer_menu(self):
        print("Customer functionality not implemented yet.")
        input("Press Enter to return...")

    def list_jobs(self):
        jobs = Job.get_all()
        for job in jobs:
            print(f"Job ID: {job[0]}, Description: {job[1]}, Status: {job[2]}")
