import unittest
import os
import sys

# Add parent directory to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from DataPersistence import HabitTrackerDB

class TestHabitTrackerDB(unittest.TestCase):
    def setUp(self):
        self.db = HabitTrackerDB(db_name=':memory:')

    def tearDown(self):
        self.db.close()

    def test_create_tables(self):
        self.db.create_tables()

        # Check if the tables were created
        cursor = self.db.conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = [table[0] for table in cursor.fetchall()]
        self.assertIn('Users', tables)
        self.assertIn('Habits', tables)
        self.assertIn('Completions', tables)

    def test_clear_tables(self):
        self.db.create_tables()
        self.db.fill_tables()

        # Check if the tables are not empty
        cursor = self.db.conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM Users")
        self.assertGreater(cursor.fetchone()[0], 0)
        cursor.execute("SELECT COUNT(*) FROM Habits")
        self.assertGreater(cursor.fetchone()[0], 0)
        cursor.execute("SELECT COUNT(*) FROM Completions")
        self.assertGreater(cursor.fetchone()[0], 0)

        self.db.clear_tables()

        # Check if the tables are empty
        cursor.execute("SELECT COUNT(*) FROM Users")
        self.assertEqual(cursor.fetchone()[0], 0)
        cursor.execute("SELECT COUNT(*) FROM Habits")
        self.assertEqual(cursor.fetchone()[0], 0)
        cursor.execute("SELECT COUNT(*) FROM Completions")
        self.assertEqual(cursor.fetchone()[0], 0)

    def test_fill_tables(self):
        self.db.create_tables()
        self.db.fill_tables()

        # Check if the tables are filled with data
        cursor = self.db.conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM Users")
        self.assertEqual(cursor.fetchone()[0], 3)
        cursor.execute("SELECT COUNT(*) FROM Habits")
        self.assertEqual(cursor.fetchone()[0], 30)
        cursor.execute("SELECT COUNT(*) FROM Completions")
        self.assertGreater(cursor.fetchone()[0], 0)

if __name__ == '__main__':
    unittest.main()