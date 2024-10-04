from database import connect_db

def add_transaction(user_id, amount, category, type, date, description):
    """Add a new income or expense transaction."""
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO transactions (user_id, amount, category, type, date, description) VALUES (?, ?, ?, ?, ?, ?)", 
                   (user_id, amount, category, type, date, description))
    conn.commit()
    conn.close()
    print(f"{type.capitalize()} added successfully.")

def view_transactions(user_id):
    """View all transactions for the logged-in user."""
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM transactions WHERE user_id=?", (user_id,))
    transactions = cursor.fetchall()
    conn.close()
    return transactions

def delete_transaction(transaction_id):
    """Delete a specific transaction by its ID."""
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM transactions WHERE transaction_id=?", (transaction_id,))
    conn.commit()
    conn.close()
    print("Transaction deleted successfully.")