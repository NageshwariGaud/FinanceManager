import datetime
from database import connect_db

def set_budget(user_id, category, amount):
    """Set a monthly budget for a specific category."""
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS budgets (
                        budget_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_id INTEGER,
                        category TEXT,
                        amount REAL,
                        date TEXT,
                        FOREIGN KEY(user_id) REFERENCES users(user_id)
                    )''')
    
    cursor.execute("INSERT INTO budgets (user_id, category, amount, date) VALUES (?, ?, ?, ?)",
                   (user_id, category, amount, str(datetime.date.today())))
    conn.commit()
    conn.close()
    print(f"Budget set for {category} category successfully.")

def check_budget_exceeded(user_id, category):
    """Check if the user has exceeded their budget for a given category."""
    conn = connect_db()
    cursor = conn.cursor()

    # Get the total expenses for the given category and current month
    cursor.execute('''SELECT SUM(amount) 
                      FROM transactions 
                      WHERE user_id=? AND category=? AND type='expense' AND strftime('%m', date) = strftime('%m', DATE('now'))''', 
                      (user_id, category))
    total_expense = cursor.fetchone()[0] or 0  # Handle NoneType if no expenses found
    # Get the set budget for the given category
    cursor.execute("SELECT amount FROM budgets WHERE user_id=? AND category=? AND strftime('%m', date) = strftime('%m', DATE('now'))", 
                   (user_id, category))
    budget = cursor.fetchone()

    conn.close()

    if budget and total_expense > budget[0]:
        print(f"Alert: You have exceeded your budget for {category} by {total_expense - budget[0]:.2f}.")
    else:
        print(f"You are within the budget for {category}.")
