import os
import time
from User import User as UserModule
from Habit import Habit as HabitModule
from Completions import Completions as CompletionsModule
from colorama import init, Fore, Style
from InteractiveMenu import InteractiveMenu
from DataPersistence import HabitTrackerDB
from Analytics import Analytics

init(autoreset=True)

db = HabitTrackerDB()
analytics = Analytics(db)
User = UserModule(db)
Habit = HabitModule(db)
Completions = CompletionsModule(db)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    return f"""
🌟✨🌟✨🌟✨🌟✨🌟✨🌟✨🌟✨🌟✨🌟✨🌟✨🌟✨🌟✨🌟✨🌟✨🌟✨🌟

                   🎯 Alonso's Habit Tracker 🎯

🌟✨🌟✨🌟✨🌟✨🌟✨🌟✨🌟✨🌟✨🌟✨🌟✨🌟✨🌟✨🌟✨🌟✨🌟✨🌟
    """

def main_menu():
    menu = InteractiveMenu(
        "Main Menu:",
        ["👤 Manage Users", "🏋️ Manage Habits", "📊 View Analytics", "⚙️ Debug Menu", "🚪 Exit"]
    )
    return menu.run()

def manage_users():
    users = User.get_users()
    user_options = [f"ID: {user[0]}, Username: {user[1]}" for user in users]

    menu = InteractiveMenu(
        "👥 User Management:",
        ["➕ Add User", "🔍 View Users", "🗑️ Delete User", "↩️ Back to Main Menu"]
    )
    choice = menu.run()

    if choice == 0:
        username = input(Fore.CYAN + "Enter username: ")
        User.add_user(username)
        print(Fore.GREEN + f"✅ User {username} added successfully!")
    elif choice == 1:
        print(Fore.CYAN + "\nUsers:")
        for user in users:
            print(Fore.WHITE + f"ID: {user[0]}, Username: {user[1]}")
    elif choice == 2:
        user_delete_menu = InteractiveMenu(
            "Select a user to delete:",
            user_options
        )
        user_id = User.get_users()[user_delete_menu.run()][0]
        User.delete_user(user_id)
        print(Fore.GREEN + "✅ User deleted successfully!")
    elif choice == 3:
        return

    input(Fore.YELLOW + "\nPress Enter to continue...")

def manage_habits():
    users = User.get_users()
    user_options = [f"ID: {user[0]}, Username: {user[1]}" for user in users]
    
    menu = InteractiveMenu(
        "🏋️ Habit Management:",
        ["➕ Add Habit", "🔍 View Habits", "✅ Mark Habit as Complete", "↩️ Back to Main Menu"]
    )
    choice = menu.run()
    
    if choice == 0:
        user_id_menu = InteractiveMenu(
            "Select a user:",
            user_options
        )
        user_id = User.get_users()[user_id_menu.run()][0]
        
        name = input(Fore.CYAN + "Enter habit name: ")
        description = input(Fore.CYAN + "Enter habit description: ")
        
        periodicity_options = ["Daily", "Weekly"]
        periodicity_menu = InteractiveMenu(
            "Select periodicity:",
            periodicity_options
        )
        periodicity = periodicity_options[periodicity_menu.run()].lower()
        
        creation_date = time.strftime('%Y-%m-%d')
        Habit.add_habit(name, description, periodicity, creation_date, user_id)
        print(Fore.GREEN + f"✅ Habit '{name}' added successfully!")
    elif choice == 1:
        user_id_menu = InteractiveMenu(
            "Select a user:",
            user_options
        )
        user_id = User.get_users()[user_id_menu.run()][0]
        habits = Habit.get_habits_by_user(user_id)
        print(Fore.CYAN + "\nHabits:")
        for habit in habits:
            print(Fore.WHITE + f"ID: {habit[0]}, Name: {habit[1]}, Periodicity: {habit[3]}")
    elif choice == 2:
        user_id_menu = InteractiveMenu(
            "Select a user:",
            user_options
        )
        user_id = User.get_users()[user_id_menu.run()][0]
        habits = Habit.get_habits_by_user(user_id)
        habit_id_menu = InteractiveMenu(
            "Select a habit:",
            [f"ID: {habit[0]}, Name: {habit[1]}" for habit in habits]
        )
        habit_id = Habit.get_habits_by_user(user_id)[habit_id_menu.run()][0]
        completion_date = time.strftime('%Y-%m-%d')
        Completions.add_completion(habit_id, completion_date)
        print(Fore.GREEN + f"✅ Habit marked as complete for {completion_date}!")
    elif choice == 3:
        return
    
    input(Fore.YELLOW + "\nPress Enter to continue...")

def view_analytics():
    users = User.get_users()
    user_options = [f"ID: {user[0]}, Username: {user[1]}" for user in users]

    menu = InteractiveMenu(
        "📊 Analytics:",
        ["📈 View All Habits", "🔍 View Habits by Periodicity", "🏆 View Longest Streak", "↩️ Back to Main Menu"]
    )
    choice = menu.run()
    
    if choice == 0:
        user_id_menu = InteractiveMenu(
            "Select a user:",
            user_options
        )
        user_id = User.get_users()[user_id_menu.run()][0]
        habits = analytics.getAllHabits(user_id)
        print(Fore.CYAN + "\nAll Habits:")
        for habit in habits:
            print(Fore.WHITE + f"ID: {habit[0]}, Name: {habit[1]}, Periodicity: {habit[3]}")
    elif choice == 1:
        user_id_menu = InteractiveMenu(
            "Select a user:",
            user_options
        )
        user_id = User.get_users()[user_id_menu.run()][0]
        periodicity_options = ["Daily", "Weekly"]
        periodicity_menu = InteractiveMenu(
            "Select periodicity:",
            periodicity_options
        )
        periodicity = periodicity_options[periodicity_menu.run()].lower()
        habits = analytics.getHabitsByPeriodicity(user_id, periodicity)
        print(Fore.CYAN + f"\n{periodicity.capitalize()} Habits:")
        for habit in habits:
            print(Fore.WHITE + f"ID: {habit[0]}, Name: {habit[1]}")
    elif choice == 2:
        user_id_menu = InteractiveMenu(
            "Select a user:",
            user_options
        )
        user_id = User.get_users()[user_id_menu.run()][0]
        longest_streaks = analytics.getLongestStreakAllHabits(user_id)
        print(Fore.CYAN + "\nLongest Streaks:")
        for habit_id, streak in longest_streaks.items():
            habit = Habit.get_habit(habit_id)
            print(Fore.WHITE + f"Habit: {habit[1]}, Longest Streak: {streak} days")
    elif choice == 3:
        return
    
    input(Fore.YELLOW + "\nPress Enter to continue...")

def debug_menu():
    menu = InteractiveMenu(
        "Debug Menu:",
        ["🔥 Clear Database", "🧩 Fill Database with dummy data", "🚪 Exit"]
    )
    choice = menu.run()

    if choice == 0:
        db.clear_tables()
        print(Fore.GREEN + "✅ Database cleared successfully!")
    elif choice == 1:
        db.fill_tables()
        print(Fore.GREEN + "✅ Database filled with dummy data successfully!")
    elif choice == 2:
        return

    input(Fore.YELLOW + "\nPress Enter to continue...")