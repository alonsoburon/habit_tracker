import os
import time
from User import User as UserModule
from Habit import Habit as HabitModule
from Completions import Completions as CompletionsModule
from colorama import init, Fore, Style
from prompt_toolkit import Application
from prompt_toolkit.layout.containers import HSplit, Window
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.styles import Style as PromptStyle
from prompt_toolkit.layout import Layout, HSplit, Window
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.widgets import Box, Frame
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

class InteractiveMenu:
    """
    This class is our interactive menu for our TUI, it will display a list of options and allow the user to select one.
    """
    def __init__(self, title, options):
        self.title = title
        self.options = options
        self.selected = 0

    def get_formatted_options(self):
        result = []
        for i, option in enumerate(self.options):
            if i == self.selected:
                result.append(('class:selected', f'> {option}\n'))
            else:
                result.append(('', f'  {option}\n'))
        return result

    def create_layout(self):
        return Layout(
            HSplit([
                Box(
                    body=Window(height=1, content=FormattedTextControl(self.title), align="center"),
                    padding=1,
                    style="class:title"
                ),
                Frame(
                    body=Window(content=FormattedTextControl(self.get_formatted_options)),
                    title="Options",
                    style="class:options-frame"
                )
            ])
        )

    def create_style(self):
        return PromptStyle([
            ('selected', '#CCCC11 bold'),
        ])

    def create_keybindings(self):
        kb = KeyBindings()

        @kb.add('up')
        def _(event):
            self.selected = (self.selected - 1) % len(self.options)

        @kb.add('down')
        def _(event):
            self.selected = (self.selected + 1) % len(self.options)

        @kb.add('enter')
        def _(event):
            event.app.exit(result=self.selected)

        return kb

    def run(self):
        application = Application(
            layout=self.create_layout(),
            key_bindings=self.create_keybindings(),
            style=self.create_style(),
            full_screen=True
        )
        return application.run()

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
def main():
    while True:
        clear_screen()
        print(Fore.CYAN + Style.BRIGHT + print_header())
        choice = main_menu()

        if choice == 0:
            manage_users()
        elif choice == 1:
            manage_habits()
        elif choice == 2:
            view_analytics()
        elif choice == 3:
            debug_menu()
        elif choice == 4:
            print(Fore.YELLOW + "\n👋 Thank you for using Alonso's Habit Tracker! Goodbye! 🌟")
            break

if __name__ == "__main__":
    main()