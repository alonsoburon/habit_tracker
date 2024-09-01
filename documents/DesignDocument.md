# Command Line Habit Tracker - Design Document

## 1. Project Overview
This CLI Habit tracker is a Python-based app that allows users to track their habits through a text-based user interface (TUI). Users can create habits, mark them as complete, and view analytics about their progress.

## 2. Core Components

<img src="https://mermaid.ink/svg/pako:eNp1kctqwzAQRX9FaJ10050XBT_iONAs2iYrKYuJPbFFbNnVo2BC_r1ypYAo7SzEnHuvHmhutB4bpAltFUwdeX3nkrjS9uyFAYR8mmavLpWyw3F38oyy4dK3fs3YUaMKbs4qOAsTqGD5OEw9GjFKHbQN20mDCmojvnCP0ga99DsPzrmiKrIgb1kqoZ-NqB8HVEx_9sLg8yl-RUrW6xeyiSGLIY-hiKGMYRtudUBy6Hsd53-p4chyUd8sKoGagGzIHiS06DPV46-yOPXjhIfn_xnFXwZd0QGVG1DjxndbgpyaDgfkNHFtA-rKKZd3lwNrxo9Z1jQxyuKKqtG2HU0u0GtHdmrAYCHAjXwI6v0bh1GZNA" alt="" width="auto" height="500" >

## 3. Database
SQLite3 is used as the database for this project. It's a lightweight, serverless, and self-contained relational database engine that doesn't require a separate server process or configuration.

<img src="https://mermaid.ink/svg/pako:eNqdUsFugzAM_ZXI5_YHuK60myqhamPSDkhVRjywSggyyQFR_n3JgII6bYf6Etl-fn523ENuFEIEyDuSBUud1cLbe4vcin50gr0kaXyIXwUpcTqKDE5MWnInjthlsMDS-CMVzhfXUqOHJcaKxFXVjBnG51l-kn2Y_w_uW15hmzM1lkx9l2mQySjKyXZ3mZxRhoKdtPhbVZjo7KXtg7S9YaSiXkubxnoyuqkw0Dwy2wwrw3L-67aIvvVbZA_rD7xet1vTz-uOPN3MMYUmwFr4iIINaGQtSfnj-JklA1uixgwCQEm-BKrB46Sz5q2rc4gsO9wAG1eUEH3JqvWea5TXNh3XFB2-AR2Cvf0" alt="" width="auto" height="500">

## 4. Class Attributes and Methods

### 4.1 InteractiveMenu
Attributes:
- `title: str`
- `options: list`
- `selected: int`

Methods:
- `__init__(self, title, options)`
- `get_formatted_options(self)`
- `create_layout(self)`
- `create_style(self)`
- `create_keybindings(self)`
- `run(self)`

### 4.2 HabitTrackerDB
Attributes:
- `conn: sqlite3.Connection`

Methods:
- `__init__(self, db_name='habit_tracker.d`b')
- `create_tables(self)`
- `clear_tables(self)`
- `fill_tables(self)`
- `close(self)`

### 4.3 Analytics
Attributes:
- `habit: HabitModule`
- `completions: CompletionsModule`

Methods:
- `__init__(self, db)`
- `getAllHabits(self, user_id)`
- `getHabitsByPeriodicity(self, user_id, periodici`ty)
- `getLongestStreakAllHabits(self, user_id)`
- `getLongestStreakForHabit(self, habit_id)`
- `getLongestStreaksForAllPeriodicities(self, user_id)`

### 4.4 Completions
Attributes:
- `db: HabitTrackerDB`

Methods:
- `__init__(self, db)`
- `add_completion(self, habit_id, completionDate)`
- `get_completion(self, completion_id)`
- `get_longest_streak(self, habit_id)`
- `update_completion(self, completion_id, habit_id, completionDate)`
- `delete_completion(self, completion_id)`

### 4.5 Habit
Attributes:
- `db: HabitTrackerDB`

Methods:
- `__init__(self, db)`
- `add_habit(self, name, description, periodicity, creationDate, user_id)`
- `get_habit(self, habit_id)`
- `get_habits(self, user_id)`
- `get_habits_by_periodicity(self, user_id, periodicity)`
- `get_habits_by_user(self, user_id)`
- `update_habit(self, habit_id, name, description, periodicity, creationDate)`
- `delete_habit(self, habit_id)`

### 4.6 User
Attributes:
- `db: HabitTrackerDB`

Methods:
- `__init__(self, db)`
- `add_user(self, username)`
- `get_user(self, user_id)`
- `get_users(self)`
- `update_user(self, user_id, username)`
- `delete_user(self, user_id)`

## 5. External Libraries
- **SQLite3**: Included in Python, used for database operations
- **Colorama**: Used for easier terminal coloring
- **prompt_toolkit**: Used for interactive arrow-key oriented TUI

## 6. Installation and Usage
To install the Command Line Habit Tracker:
1. Ensure Python 3.7+ is installed on your system
2. Clone the repository or download the source code at https://github.com/alonsoburon/habit_tracker.git
3. Install required libraries: `pip install colorama prompt_toolkit`
4. Run `main.py` to start the application

To use the application:
1. Navigate menus using *arrow keys*
2. Select options with the *Enter* key
3. Follow on-screen prompts to manage *users*, *habits*, and view *analytics*
4. Use the debug menu for clearing and filling the db with fake data