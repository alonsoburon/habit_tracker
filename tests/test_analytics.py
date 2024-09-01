import sys
import os
import unittest

# Add parent directory to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from DataPersistence import HabitTrackerDB
from Analytics import Analytics


class TestAnalytics(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.db = HabitTrackerDB(':memory:')  # Use in-memory database for testing
        cls.db.fill_tables()
        cls.analytics = Analytics(cls.db)

    @classmethod
    def tearDownClass(cls):
        cls.db.close()

    def test_getAllHabits(self):
        user_id = 1  # Assuming Test_User_1 has id 1
        habits = self.analytics.getAllHabits(user_id)
        self.assertEqual(len(habits), 10)  # 5 daily + 5 weekly habits

    def test_getHabitsByPeriodicity(self):
        user_id = 1
        daily_habits = self.analytics.getHabitsByPeriodicity(user_id, 'daily')
        weekly_habits = self.analytics.getHabitsByPeriodicity(user_id, 'weekly')
        self.assertEqual(len(daily_habits), 5)
        self.assertEqual(len(weekly_habits), 5)

    def test_getLongestStreakAllHabits(self):
        user_id = 1
        longest_streaks = self.analytics.getLongestStreakAllHabits(user_id)
        self.assertEqual(len(longest_streaks), 10)  # One streak for each habit
        for streak in longest_streaks.values():
            self.assertIn('start_date', streak)
            self.assertIn('end_date', streak)
            self.assertIn('length', streak)

    def test_getLongestStreakForHabit(self):
        # Assuming the first habit has id 1
        habit_id = 1
        streak = self.analytics.getLongestStreakForHabit(habit_id)
        self.assertIsNotNone(streak)
        self.assertEqual(len(streak), 3)  # start_date, end_date, length

    def test_getLongestStreaksForAllPeriodicities(self):
        user_id = 1
        all_streaks = self.analytics.getLongestStreaksForAllPeriodicities(user_id)
        self.assertIn('daily', all_streaks)
        self.assertIn('weekly', all_streaks)
        self.assertEqual(len(all_streaks['daily']), 5)
        self.assertEqual(len(all_streaks['weekly']), 5)

if __name__ == '__main__':
    unittest.main()