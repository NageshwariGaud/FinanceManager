import sqlite3
from database import connect_db
import hashlib

def hash_password(password):
    """Hash the password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username, password):
    """Register a new user with a username and password."""
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)",(username, hash_password(password)))
        conn.commit()
        print("User registered successfully.")
    except sqlite3.IntegrityError:
        print("Error: Username already exists.")
    finally:
        conn.close()

def login_user(username, password):
    """Authenticate the user with username and password."""
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", 
                   (username, hash_password(password)))
    user = cursor.fetchone()
    conn.close()
    if user:
        print("Login successful!")
        return user[0]  # Return user_id
    else:
        print("Login failed. Check your username and password.")
        return None