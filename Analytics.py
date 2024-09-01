from Habit import Habit as HabitModule
from Completions import Completions as CompletionsModule

class Analytics:
    """
    This class is responsible for managing the Analytics of the Habits table in the database.
    It calls functions from the Habit class and runs analytics on the data.
    """
    def __init__(self, db):
        self.habit = HabitModule(db)
        self.completions = CompletionsModule(db)

    def getAllHabits(self, user_id):
        return self.habit.get_habits(user_id)

    def getHabitsByPeriodicity(self, user_id, periodicity):
        return self.habit.get_habits_by_periodicity(user_id, periodicity)

    def getLongestStreakAllHabits(self, user_id):
        habits = self.habit.get_habits(user_id)
        longest_streaks = {}
        for habit in habits:
            habit_id = habit[0]  # Habit ID as first element in tuple
            streak_data = self.completions.get_longest_streak(habit_id)
            if streak_data:
                start_date, end_date, length = streak_data
                longest_streaks[habit_id] = {
                    "start_date": start_date,
                    "end_date": end_date,
                    "length": length
                }
        return longest_streaks

    def getLongestStreakForHabit(self, habit_id):
        return self.completions.get_longest_streak(habit_id)
    
    def getLongestStreaksForAllPeriodicities(self, user_id):
        periodicity_options = ["daily", "weekly"]
        all_longest_streaks = {}

        for periodicity in periodicity_options:
            habits = self.habit.get_habits_by_periodicity(user_id, periodicity)
            longest_streaks = {}  # Dictionary to store longest streaks for each habit
            for habit in habits:
                habit_id = habit[0]  # Habit ID as first element in tuple
                streak_data = self.completions.get_longest_streak(habit_id)  # Get longest streak data for habit
                if streak_data:
                    start_date, end_date, length = streak_data
                    longest_streaks[habit_id] = {
                        "start_date": start_date,
                        "end_date": end_date,
                        "length": length
                    }
            all_longest_streaks[periodicity] = longest_streaks  # Store the longest streaks for the current periodicity

        return all_longest_streaks  # Return dictionary of longest streaks for each periodicity
    