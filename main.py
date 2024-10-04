from getpass import getpass
from user import register_user, login_user
from transaction import add_transaction, view_transactions, delete_transaction
from budget import set_budget, check_budget_exceeded
from report_generator import generate_monthly_report, generate_yearly_report
from backup_restore import backup_database, restore_database
import datetime

def main():
    print("Welcome to the Personal Finance Management Application!")
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Backup Database")
        print("4. Restore Database")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            username = input("Enter a new username: ")
            password = getpass("Enter a new password: ")
            register_user(username, password)

        elif choice == '2':
            username = input("Enter your username: ")
            password = getpass("Enter your password: ")
            user_id = login_user(username, password)

            if user_id:
                while True:
                    print("\n--- Main Menu ---")
                    print("1. Add Income/Expense")
                    print("2. View Transactions")
                    print("3. Delete Transaction")
                    print("4. Set Budget")
                    print("5. Check Budget Status")
                    print("6. Generate Monthly Report")
                    print("7. Generate Yearly Report")
                    print("8. Logout")

                    user_choice = input("Select an option: ")
                    if user_choice == '1':
                        amount = float(input("Enter the amount: "))
                        category = input("Enter the category (e.g., Food, Rent, Salary): ")
                        type = input("Enter type (income/expense): ").lower()
                        date = str(datetime.date.today())
                        description = input("Enter a description: ")

                        add_transaction(user_id, amount, category, type, date, description)

                    elif user_choice == '2':
                        transactions = view_transactions(user_id)
                        print("\n--- Your Transactions ---")
                        for trans in transactions:
                            print(trans)

                    elif user_choice == '3':
                        trans_id = int(input("Enter the Transaction ID to delete: "))
                        delete_transaction(trans_id)

                    elif user_choice == '4':
                        category = input("Enter category for the budget: ")
                        amount = float(input("Enter the budget amount: "))
                        set_budget(user_id, category, amount)

                    elif user_choice == '5':
                        category = input("Enter category to check budget status: ")
                        check_budget_exceeded(user_id, category)

                    elif user_choice == '6':
                        month = int(input("Enter the month (1-12): "))
                        year = int(input("Enter the year (e.g., 2024): "))
                        generate_monthly_report(user_id, month, year)

                    elif user_choice == '7':
                        year = int(input("Enter the year (e.g., 2024): "))
                        generate_yearly_report(user_id, year)

                    elif user_choice == '8':
                        print("Logged out successfully.")
                        break

                    else:
                        print("Invalid option. Please try again.")

        elif choice == '3':
            # Backup Database
            backup_file = input("Enter the backup file name (or press Enter to use default 'finance_manager_backup.db'): ") or 'finance_manager_backup.db'
            backup_database(backup_file)

        elif choice == '4':
            # Restore Database
            backup_file = input("Enter the backup file name to restore (default 'finance_manager_backup.db'): ") or 'finance_manager_backup.db'
            restore_database(backup_file)

        elif choice == '5':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

main()

