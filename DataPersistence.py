import sqlite3

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

            # Insert habits
            self.conn.execute('''
                INSERT INTO Habits (name, description, periodicity, creationDate, user_id) VALUES
                ('Run', 'Run 5km', 'daily', '2021-01-01', ?),
                ('Read', 'Read a book', 'daily', '2021-01-01', ?),
                ('Study', 'Study for 1 hour', 'daily', '2021-01-01', ?)
            ''', (user_id_1, user_id_2, user_id_3))

            # Retrieve habit IDs
            cursor.execute('SELECT id FROM Habits WHERE name = ?', ('Run',))
            habit_id_1 = cursor.fetchone()[0]
            cursor.execute('SELECT id FROM Habits WHERE name = ?', ('Read',))
            habit_id_2 = cursor.fetchone()[0]
            cursor.execute('SELECT id FROM Habits WHERE name = ?', ('Study',))
            habit_id_3 = cursor.fetchone()[0]

            # Insert completions
            self.conn.execute('''
                INSERT INTO Completions (habit_id, completionDate) VALUES
                (?, '2021-01-01'),
                (?, '2021-01-02'),
                (?, '2021-01-03'),
                (?, '2021-01-01'),
                (?, '2021-01-02'),
                (?, '2021-01-01')
            ''', (habit_id_1, habit_id_1, habit_id_1, habit_id_2, habit_id_2, habit_id_3))

    def close(self):
        self.conn.close()