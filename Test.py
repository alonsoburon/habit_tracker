import unittest
import os
import sys

# Add the 'tests' directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'tests')))

# Import test cases from the 'tests' directory
from tests.test_analytics import TestAnalytics
from tests.test_completions import TestCompletions
from tests.test_dataPersistence import TestHabitTrackerDB
from tests.test_habit import TestHabit
from tests.test_user import TestUser


# Create a test suite
suite = unittest.TestSuite()

# Add the test cases to the suite
suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestAnalytics))
suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestCompletions))
suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestHabitTrackerDB))
suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestHabit))
suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestUser))

# Run the test suite
runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)

# Print the test results
print(f'Total tests run: {result.testsRun}')
print(f'Failures: {len(result.failures)}')
print(f'Errors: {len(result.errors)}')