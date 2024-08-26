from Habit import Habit as HabitModule

class Analytics:
    """
    This class is responsible for managing the Analytics of the Habits table in the database.
    """
    def __init__(self, db):
        self.habit = HabitModule(db)

    def getAllHabits(self, user_id):
        return self.habit.get_habits(user_id)

    def getHabitsByPeriodicity(self, user_id, periodicity):
        return self.habit.get_habits_by_periodicity(user_id, periodicity)

    def getLongestStreakAllHabits(self, user_id):
        habits = self.habit.get_habits(user_id)
        longest_streaks = {}
        for habit in habits:
            habit_id = habit[0]  # Assuming habit ID is the first element
            longest_streaks[habit_id] = self.habit.get_longest_streak(habit_id)
        return longest_streaks

    def getLongestStreakForHabit(self, habit_id):
        return self.habit.get_longest_streak(habit_id)