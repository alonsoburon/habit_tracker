import unittest
from datetime import datetime
import os
import sys

# Add parent directory to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from User import User
from DataPersistence import HabitTrackerDB

class TestUser(unittest.TestCase):
    def setUp(self):
        self.db = HabitTrackerDB(':memory:')
        self.user = User(self.db)

    def tearDown(self):
        self.db.close()

    def test_add_user(self):
        self.user.add_user('Test_User')
        user = self.user.get_user(1)
        self.assertIsNotNone(user)
        self.assertEqual(user[1], 'Test_User')

    def test_get_user(self):
        self.user.add_user('Test_User')
        user = self.user.get_user(1)
        self.assertIsNotNone(user)
        self.assertEqual(user[1], 'Test_User')

    def test_get_users(self):
        self.user.add_user('Test_User_1')
        self.user.add_user('Test_User_2')
        self.user.add_user('Test_User_3')
        users = self.user.get_users()
        self.assertEqual(len(users), 3)
        self.assertEqual(users[0][1], 'Test_User_1')
        self.assertEqual(users[1][1], 'Test_User_2')
        self.assertEqual(users[2][1], 'Test_User_3')

    def test_update_user(self):
        self.user.add_user('Test_User')
        self.user.update_user(1, 'Updated_Test_User')
        user = self.user.get_user(1)
        self.assertEqual(user[1], 'Updated_Test_User')

    def test_delete_user(self):
        self.user.add_user('Test_User')
        self.user.delete_user(1)
        user = self.user.get_user(1)
        self.assertIsNone(user)

if __name__ == '__main__':
    unittest.main()