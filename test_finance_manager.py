import unittest
from user import register_user, login_user
from transaction import add_transaction, view_transactions
from budget import set_budget, check_budget_exceeded
from database import connect_db, create_tables

class TestFinanceManager(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Create test database tables before all tests."""
        create_tables()

    def test_user_registration_and_login(self):
        """Test user registration and login functionality."""
        username, password = 'testuser', 'testpassword'
        register_user(username, password)
        user_id = login_user(username, password)
        self.assertIsNotNone(user_id, "User login failed after registration.")

    def test_add_transaction(self):
        """Test adding a transaction."""
        user_id = 1
        add_transaction(user_id, 500, 'Food', 'expense', '2024-01-01', 'Lunch')
        transactions = view_transactions(user_id)
        self.assertTrue(len(transactions) > 0, "Transaction not added successfully.")

    def test_set_and_check_budget(self):
        """Test setting and checking budget."""
        user_id = 1
        set_budget(user_id, 'Food', 1000)
        check_budget_exceeded(user_id, 'Food')  # Should be within budget

    @classmethod
    def tearDownClass(cls):
        """Clean up by deleting all test data."""
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS users")
        cursor.execute("DROP TABLE IF EXISTS transactions")
        cursor.execute("DROP TABLE IF EXISTS budgets")
        conn.commit()
        conn.close()

if __name__ == '_main_':
    unittest.main()