import sqlite3
import datetime
import random

class HabitTrackerDB:
    """
    This class is responsible for managing the database connection and creating the tables.
    Also it has debug methods to clear the tables, fill them with dummy data and close the connection.
    """

    def __init__(self, db_name='habit_tracker.db'):
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS Users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL
                )
            ''')
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS Habits (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    description TEXT,
                    periodicity TEXT,
                    creationDate TEXT,
                    user_id INTEGER,
                    FOREIGN KEY(user_id) REFERENCES Users(id)
                )
            ''')
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS Completions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    habit_id INTEGER,
                    completionDate TEXT,
                    FOREIGN KEY(habit_id) REFERENCES Habits(id)
                )
            ''')

    def clear_tables(self):
        with self.conn:
            self.conn.execute('DELETE FROM Users')
            self.conn.execute('DELETE FROM Habits')
            self.conn.execute('DELETE FROM Completions')

    def fill_tables(self):
        with self.conn:
            # Insert users
            self.conn.execute('''
                INSERT INTO Users (username) VALUES
                ('Test_User_1'),
                ('Test_User_2'),
                ('Test_User_3')
            ''')

            # Retrieve user IDs
            cursor = self.conn.cursor()
            cursor.execute('SELECT id FROM Users WHERE username = ?', ('Test_User_1',))
            user_id_1 = cursor.fetchone()[0]
            cursor.execute('SELECT id FROM Users WHERE username = ?', ('Test_User_2',))
            user_id_2 = cursor.fetchone()[0]
            cursor.execute('SELECT id FROM Users WHERE username = ?', ('Test_User_3',))
            user_id_3 = cursor.fetchone()[0]

            # Define pre-defined habits
            daily_habits = [
                ("Exercise", "Daily exercise routine"),
                ("Read", "Read a book for 30 minutes"),
                ("Meditate", "Meditate for 10 minutes"),
                ("Study", "Study a new topic for 1 hour"),
                ("Journal", "Write in your journal")
            ]

            weekly_habits = [
                ("Grocery Shopping", "Do the weekly grocery shopping"),
                ("Clean House", "Clean the house"),
                ("Laundry", "Do the laundry"),
                ("Call Family", "Call a family member"),
                ("Plan Week", "Plan the upcoming week")
            ]

            # Insert habits
            start_date = datetime.date(2024, 8, 1)
            
            for user_id in [user_id_1, user_id_2, user_id_3]:
                for habit, description in daily_habits:
                    self.conn.execute('''
                        INSERT INTO Habits (name, description, periodicity, creationDate, user_id)
                        VALUES (?, ?, 'daily', ?, ?)
                    ''', (habit, description, start_date, user_id))

                for habit, description in weekly_habits:
                    self.conn.execute('''
                        INSERT INTO Habits (name, description, periodicity, creationDate, user_id)
                        VALUES (?, ?, 'weekly', ?, ?)
                    ''', (habit, description, start_date, user_id))

            # Retrieve all habit IDs
            cursor.execute('SELECT id, periodicity FROM Habits')
            habits = cursor.fetchall()

            # Insert completions for 4 weeks, 80% of the time
            for i in range(28):  # 28 days
                current_date = start_date + datetime.timedelta(days=i) # Add i days to start_date
                for habit_id, periodicity in habits:
                    if periodicity == 'daily':
                        # Complete daily habits approximately 80% of the time
                        if random.random() < 0.8:
                            self.conn.execute('''
                                INSERT INTO Completions (habit_id, completionDate)
                                VALUES (?, ?)
                            ''', (habit_id, current_date))
                    elif periodicity == 'weekly' and i % 7 == 0:
                        # Complete weekly habits approximately 80% of the time
                        if random.random() < 0.8:
                            self.conn.execute('''
                                INSERT INTO Completions (habit_id, completionDate)
                                VALUES (?, ?)
                            ''', (habit_id, current_date))
        self.conn.commit()
    def close(self):
        self.conn.close()