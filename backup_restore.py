import sqlite3
import shutil
from database import connect_db

def backup_database(backup_file='finance_manager_backup.db'):
    """Create a backup of the current database."""
    conn = connect_db()
    with open(backup_file, 'w') as backup:
        for line in conn.iterdump():
            backup.write(f'{line}\n')
    conn.close()
    print(f"Database backup created successfully as '{backup_file}'.")

def restore_database(backup_file='finance_manager_backup.db'):
    """Restore the database from a backup file."""
    conn = connect_db()
    cursor = conn.cursor()

    # Delete all current data in the database
    cursor.execute("DROP TABLE IF EXISTS users")
    cursor.execute("DROP TABLE IF EXISTS transactions")
    cursor.execute("DROP TABLE IF EXISTS budgets")
    conn.commit()

    # Restore from the backup file
    with open(backup_file, 'r') as backup:
        sql_script = backup.read()
        cursor.executescript(sql_script)
    conn.commit()
    conn.close()
    print(f"Database restored successfully from '{backup_file}'.")