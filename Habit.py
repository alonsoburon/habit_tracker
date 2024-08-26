class Habit:
    """
    This class is responsible for managing the Habits table in the database.
    """
    def __init__(self, db):
        self.db = db

    def add_habit(self, name, description, periodicity, creationDate, user_id):
        with self.db.conn:
            self.db.conn.execute('''
                INSERT INTO Habits (name, description, periodicity, creationDate, user_id)
                VALUES (?, ?, ?, ?, ?)
            ''', (name, description, periodicity, creationDate, user_id))

    def get_habit(self, habit_id):
        cursor = self.db.conn.cursor()
        cursor.execute('SELECT * FROM Habits WHERE id = ?', (habit_id,))
        return cursor.fetchone()

    def get_habits(self, user_id):
        cursor = self.db.conn.cursor()
        cursor.execute('SELECT * FROM Habits WHERE user_id = ?', (user_id,))
        return cursor.fetchall()

    def get_habits_by_periodicity(self, user_id, periodicity):
        cursor = self.db.conn.cursor()
        cursor.execute('SELECT * FROM Habits WHERE user_id = ? AND periodicity = ?', (user_id, periodicity))
        return cursor.fetchall()

    def get_habits_by_user(self, user_id):
        return self.get_habits(user_id)
    
    def update_habit(self, habit_id, name, description, periodicity, creationDate):
        with self.db.conn:
            self.db.conn.execute('''
                UPDATE Habits
                SET name = ?, description = ?, periodicity = ?, creationDate = ?
                WHERE id = ?
            ''', (name, description, periodicity, creationDate, habit_id))

    def delete_habit(self, habit_id):
        with self.db.conn:
            self.db.conn.execute('DELETE FROM Habits WHERE id = ?', (habit_id,))