import sqlite3

def connect_db():
    """Connect to the SQLite3 database and return the connection."""
    conn = sqlite3.connect('finance_manager.db')
    return conn

def create_tables():
    """Create necessary tables for users and transactions."""
    conn = connect_db()
    cursor = conn.cursor()

    # Create Users Table
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT NOT NULL UNIQUE,
                        password TEXT NOT NULL
                    )''')

    # Create Transactions Table
    cursor.execute('''CREATE TABLE IF NOT EXISTS transactions (
                        transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_id INTEGER,
                        amount REAL,
                        category TEXT,
                        type TEXT,  -- 'income' or 'expense'
                        date TEXT,
                        description TEXT,
                        FOREIGN KEY(user_id) REFERENCES users(user_id)
                    )''')
    
    conn.commit()
    conn.close()

# Call the function to create tables
if __name__ == '__main__':
    create_tables()
