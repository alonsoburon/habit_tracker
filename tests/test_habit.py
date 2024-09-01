import unittest
from datetime import datetime
import os
import sys

# Add parent directory to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Habit import Habit
from DataPersistence import HabitTrackerDB

class TestHabit(unittest.TestCase):
    def setUp(self):
        self.db = HabitTrackerDB(':memory:')
        self.habit = Habit(self.db)

    def tearDown(self):
        self.db.close()

    def test_add_habit(self):
        name = "Exercise"
        description = "Daily exercise routine"
        periodicity = "daily"
        creation_date = datetime.now().strftime('%Y-%m-%d')
        user_id = 1

        self.habit.add_habit(name, description, periodicity, creation_date, user_id)

        habit = self.habit.get_habit(1)
        self.assertIsNotNone(habit)
        self.assertEqual(habit[1], name)
        self.assertEqual(habit[2], description)
        self.assertEqual(habit[3], periodicity)
        self.assertEqual(habit[4], creation_date)
        self.assertEqual(habit[5], user_id)

    def test_get_habit(self):
        name = "Exercise"
        description = "Daily exercise routine"
        periodicity = "daily"
        creation_date = datetime.now().strftime('%Y-%m-%d')
        user_id = 1

        self.habit.add_habit(name, description, periodicity, creation_date, user_id)

        habit = self.habit.get_habit(1)
        self.assertIsNotNone(habit)
        self.assertEqual(habit[1], name)
        self.assertEqual(habit[2], description)
        self.assertEqual(habit[3], periodicity)
        self.assertEqual(habit[4], creation_date)
        self.assertEqual(habit[5], user_id)

    def test_get_habits(self):
        self.db.fill_tables()

        habits = self.habit.get_habits(1)
        self.assertEqual(len(habits), 10)

        habits = self.habit.get_habits(2)
        self.assertEqual(len(habits), 10)

        habits = self.habit.get_habits(3)
        self.assertEqual(len(habits), 10)

    def test_get_habits_by_periodicity(self):
        self.db.fill_tables()

        daily_habits = self.habit.get_habits_by_periodicity(1, 'daily')
        self.assertEqual(len(daily_habits), 5)

        weekly_habits = self.habit.get_habits_by_periodicity(1, 'weekly')
        self.assertEqual(len(weekly_habits), 5)

    def test_update_habit(self):
        name = "Exercise"
        description = "Daily exercise routine"
        periodicity = "daily"
        creation_date = datetime.now().strftime('%Y-%m-%d')
        user_id = 1

        self.habit.add_habit(name, description, periodicity, creation_date, user_id)

        new_name = "Workout"
        new_description = "Intense workout session"
        new_periodicity = "weekly"
        new_creation_date = datetime.now().strftime('%Y-%m-%d')

        self.habit.update_habit(1, new_name, new_description, new_periodicity, new_creation_date)

        habit = self.habit.get_habit(1)
        self.assertEqual(habit[1], new_name)
        self.assertEqual(habit[2], new_description)
        self.assertEqual(habit[3], new_periodicity)
        self.assertEqual(habit[4], new_creation_date)

    def test_delete_habit(self):
        name = "Exercise"
        description = "Daily exercise routine"
        periodicity = "daily"
        creation_date = datetime.now().strftime('%Y-%m-%d')
        user_id = 1

        self.habit.add_habit(name, description, periodicity, creation_date, user_id)

        self.habit.delete_habit(1)

        habit = self.habit.get_habit(1)
        self.assertIsNone(habit)

if __name__ == '__main__':
    unittest.main()