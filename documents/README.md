# Command Line Habit Tracker

![Habit Tracker Logo](Menu.png)

## Project Overview

This Command Line Habit Tracker is a Python-based app designed for a IU Internationale assignment.

It's a simple interface for creating habits, completing them and tracking those completions over time.

Key features:
- User management
- Habit creation and tracking
- Completion logging
- Analytics and streak tracking
- Interactive TUI

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [File Descriptions](#file-descriptions)
- [Database Structure](#database-structure)
- [Code Structure](#code-structure)
- [How To Use](#how-to-use)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/alonsoburon/habit-tracker.git
   cd habit-tracker
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate
   # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install colorama prompt_toolkit
   ```

## Usage

To run the Habit Tracker:

1. Navigate to the folder where you cloned it (should be named `./habit-tracker/`).
2. Run the main script:
   ```
   python main.py
   ```
3. Use the arrow keys to navigate the menus and press Enter to select an option.

## Files

- `main.py`: The entry point of the application. It initializes the main loop and handles the top-level menu.
- `TUI.py`: Contains the Text User Interface, including menu rendering and user input handling. Calls other classes' methods
- `Analytics.py`: Handles data analysis and reporting functions, using Habit and Completions methods.
- `DataPersistence.py`: Manages general database connections and operations, including debug methods.
- `InteractiveMenu.py`: Implements the interactive menu system using prompt_toolkit, handling user interaction.
- `User.py`: Contains the User class for sending & receiving user-related db queries.
- `Habit.py`: Contains the Habit class for managing habit-related db queries.
- `Completions.py`: Contains the Completions class, for sending and handling completions-related db queries.
- `slides.html`: Contains presentation slides for the project (not part of the main application).

## Database Structure

The application uses SQLite3 for data storage. The database consists of three main tables:

1. Users
2. Habits
3. Completions

![Database Structure](https://mermaid.ink/svg/pako:eNqdUsFugzAM_ZXI5_YHuK60myqhamPSDkhVRjywSggyyQFR_n3JgII6bYf6Etl-fn523ENuFEIEyDuSBUud1cLbe4vcin50gr0kaXyIXwUpcTqKDE5MWnInjthlsMDS-CMVzhfXUqOHJcaKxFXVjBnG51l-kn2Y_w_uW15hmzM1lkx9l2mQySjKyXZ3mZxRhoKdtPhbVZjo7KXtg7S9YaSiXkubxnoyuqkw0Dwy2wwrw3L-67aIvvVbZA_rD7xet1vTz-uOPN3MMYUmwFr4iIINaGQtSfnj-JklA1uixgwCQEm-BKrB46Sz5q2rc4gsO9wAG1eUEH3JqvWea5TXNh3XFB2-AR2Cvf0)

## Code Structure

The application follows a modular structure with clear separation of concerns:

![Code Structure](https://mermaid.ink/svg/pako:eNp1kctqwzAQRX9FaJ10050XBT_iONAs2iYrKYuJPbFFbNnVo2BC_r1ypYAo7SzEnHuvHmhutB4bpAltFUwdeX3nkrjS9uyFAYR8mmavLpWyw3F38oyy4dK3fs3YUaMKbs4qOAsTqGD5OEw9GjFKHbQN20mDCmojvnCP0ga99DsPzrmiKrIgb1kqoZ-NqB8HVEx_9sLg8yl-RUrW6xeyiSGLIY-hiKGMYRtudUBy6Hsd53-p4chyUd8sKoGagGzIHiS06DPV46-yOPXjhIfn_xnFXwZd0QGVG1DjxndbgpyaDgfkNHFtA-rKKZd3lwNrxo9Z1jQxyuKKqtG2HU0u0GtHdmrAYCHAjXwI6v0bh1GZNA)

## How To Use

1. Run `main.py` on your terminal
2. Use the arrow keys to navigate the menus
3. Use the Enter key to select an option
4. When done, Exit the program

### Menu:

1. **Manage Users**: Add, view, or delete users.
2. **Manage Habits**: Add new habits, view existing ones, or mark habits as complete.
3. **View Analytics**: View all habits, habits by periodicity, and longest streaks.
4. **Debug Menu**: Clear the database or fill it with dummy data for testing purposes.
