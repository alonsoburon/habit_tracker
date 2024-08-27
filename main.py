from TUI import clear_screen, print_header, main_menu, manage_users, manage_habits, view_analytics, debug_menu
from colorama import Fore, Style

def main():
    while True:
        try:
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
        except KeyboardInterrupt:
            print(Fore.YELLOW + "\nReturning to the main menu...")

if __name__ == "__main__":
    main()