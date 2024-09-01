import sys
import os
import unittest

# Add parent directory to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from DataPersistence import HabitTrackerDB
from Completions import Completions


class TestCompletions(unittest.TestCase):
    def setUp(self):
        self.db = HabitTrackerDB()
        self.db.clear_tables()
        self.db.fill_tables()
        self.completions = Completions(self.db)

    def tearDown(self):
        self.db.close()

    def test_add_completion(self):
        habit_id = 1
        completion_date = '2024-08-01'
        self.completions.add_completion(habit_id, completion_date)
        completion = self.completions.get_completion(1)
        self.assertIsNotNone(completion)
        self.assertEqual(completion[1], habit_id)
        self.assertEqual(completion[2], completion_date)

    def test_get_completion(self):
        completion = self.completions.get_completion(1)
        self.assertIsNotNone(completion)

    def test_get_longest_streak(self):
        habit_id = 1
        start_date, end_date, length = self.completions.get_longest_streak(habit_id)
        self.assertIsNotNone(start_date)
        self.assertIsNotNone(end_date)
        self.assertIsNotNone(length)

    def test_update_completion(self):
        completion_id = 1
        habit_id = 2
        completion_date = '2024-08-02'
        self.completions.update_completion(completion_id, habit_id, completion_date)
        completion = self.completions.get_completion(completion_id)
        self.assertEqual(completion[1], habit_id)
        self.assertEqual(completion[2], completion_date)

    def test_delete_completion(self):
        completion_id = 1
        self.completions.delete_completion(completion_id)
        completion = self.completions.get_completion(completion_id)
        self.assertIsNone(completion)

if __name__ == '__main__':
    unittest.main()