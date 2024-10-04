from database import connect_db
import datetime

def generate_monthly_report(user_id, month, year):
    """Generate a report for a given month and year for the user."""
    conn = connect_db()
    cursor = conn.cursor()

    # Query for transactions in the given month and year
    cursor.execute('''SELECT type, SUM(amount) 
                      FROM transactions 
                      WHERE user_id=? AND strftime('%m', date) = ? AND strftime('%Y', date) = ?
                      GROUP BY type''', (user_id, f"{month:02}", str(year)))
    report = cursor.fetchall()
    income, expenses = 0, 0
    for row in report:
        if row[0] == 'income':
            income += row[1]
        elif row[0] == 'expense':
            expenses += row[1]

    conn.close()
    savings = income - expenses
    print(f"\n--- Monthly Report for {month}/{year} ---")
    print(f"Total Income: {income}")
    print(f"Total Expenses: {expenses}")
    print(f"Savings: {savings}")
    return income, expenses, savings

def generate_yearly_report(user_id, year):
    """Generate a yearly report for the user."""
    conn = connect_db()
    cursor = conn.cursor()
     # Query for transactions in the given year
    cursor.execute('''SELECT type, SUM(amount) 
                      FROM transactions 
                      WHERE user_id=? AND strftime('%Y', date) = ?
                      GROUP BY type''', (user_id, str(year)))
    report = cursor.fetchall()

    income, expenses = 0, 0
    for row in report:
        if row[0] == 'income':
            income += row[1]
        elif row[0] == 'expense':
            expenses += row[1]

    conn.close()
    savings = income - expenses
    print(f"\n--- Yearly Report for {year} ---")
    print(f"Total Income: {income}")
    print(f"Total Expenses: {expenses}")
    print(f"Savings: {savings}")
    return income, expenses, savings