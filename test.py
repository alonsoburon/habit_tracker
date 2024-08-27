import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
import sys

class TestHabitTracker(unittest.TestCase):
    def setUp(self):
        # Redirect stdout to capture print statements
        self.held_stdout = StringIO()
        sys.stdout = self.held_stdout

    def tearDown(self):
        # Reset stdout
        sys.stdout = sys.__stdout__

    @patch('builtins.input', side_effect=['0', '1', '2', '3', '4'])
    @patch('InteractiveMenu.InteractiveMenu.run', side_effect=[0, 1, 2, 3, 4])
    def test_main_menu(self, mock_input, mock_menu_run):
        from TUI import main_menu
        main_menu()
        output = self.held_stdout.getvalue()
        self.assertIn("Main Menu:", output)

    @patch('builtins.input', side_effect=['0', '1', '2'])
    @patch('InteractiveMenu.InteractiveMenu.run', side_effect=[0, 1, 2])
    def test_debug_menu(self, mock_input, mock_menu_run):
        from TUI import debug_menu
        debug_menu()
        output = self.held_stdout.getvalue()
        self.assertIn("Debug Menu:", output)

    @patch('builtins.input', side_effect=['testuser'])
    @patch('InteractiveMenu.InteractiveMenu.run', side_effect=[0, 1, 2, 3])
    def test_manage_users(self, mock_input, mock_menu_run):
        from TUI import manage_users
        manage_users()
        output = self.held_stdout.getvalue()
        self.assertIn("User testuser added successfully!", output)

    @patch('builtins.input', side_effect=['testhabit', 'test description'])
    @patch('InteractiveMenu.InteractiveMenu.run', side_effect=[0, 0, 1, 2, 3])
    def test_manage_habits(self, mock_input, mock_menu_run):
        from TUI import manage_habits
        manage_habits()
        output = self.held_stdout.getvalue()
        self.assertIn("Habit 'testhabit' added successfully!", output)

    @patch('InteractiveMenu.InteractiveMenu.run', side_effect=[0, 0, 1, 2, 3])
    def test_view_analytics(self, mock_menu_run):
        from TUI import view_analytics
        view_analytics()
        output = self.held_stdout.getvalue()
        self.assertIn("Analytics:", output)

    @patch('InteractiveMenu.InteractiveMenu.run', side_effect=[4])
    def test_exit(self, mock_menu_run):
        from TUI import main
        with self.assertRaises(SystemExit):
            main()

if __name__ == '__main__':
    unittest.main()