
Personal Finance Management Application

Welcome to the Personal Finance Management Application! This application helps you manage your personal finances by allowing you to register, log in, track transactions, set budgets, generate reports, and backup or restore your financial data.

Features

- User Registration & Login: Secure user authentication using usernames and passwords.
- Transaction Management: 
  - Add income or expenses with details.
  - View a list of transactions.
  - Delete specific transactions.
- Budgeting: Set budgets for different categories and check if you are within your budget.
- Reporting: Generate monthly and yearly financial reports to track your spending habits.
- Backup & Restore: Safeguard your data with backup and restore functionalities.

Requirements

- Python 3.x
- Required modules (see below)

Installation

1. Clone this repository:
   git clone <repository-url>
   cd <repository-directory>
   

2. Install necessary dependencies (if any). You may need to create a virtual environment:
   python -m venv venv
   source venv/bin/activate
   On Windows use "venv\Scripts\activate"


4. (Optional) Install any required packages using pip:
   pip install -r requirements.txt
   
Usage

1. Run the application:
   python main.py
   

2. Follow the prompts in the terminal to:
   - Register a new user.
   - Login to your account.
   - Manage your transactions, budgets, and reports.
   - Backup or restore your database.

Dependencies

- `getpass: For secure password input.
- Custom modules:
  - user: Handles user registration and login.
  - transaction: Manages adding, viewing, and deleting transactions.
  - budget: Handles budget setting and checking.
  - report_generator: Generates monthly and yearly reports.
  - backup_restore: Manages database backup and restoration.

Happy budgeting!
