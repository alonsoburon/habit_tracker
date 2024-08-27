class User:
    """
    This class is responsible for managing the Users table in the database.
    It sends queries to the database. db is dependency injected from the HabitTrackerDB class.
    """

    def __init__(self, db):
        self.db = db

    def add_user(self, username):
        with self.db.conn:
            self.db.conn.execute('INSERT INTO Users (username) VALUES (?)', (username,))

    def get_user(self, user_id):
        cursor = self.db.conn.cursor()
        cursor.execute('SELECT * FROM Users WHERE id = ?', (user_id,))
        return cursor.fetchone()
    
    def get_users(self):
        cursor = self.db.conn.cursor()
        cursor.execute('SELECT * FROM Users')
        return cursor.fetchall()
    
    def update_user(self, user_id, username):
        with self.db.conn:
            self.db.conn.execute('UPDATE Users SET username = ? WHERE id = ?', (username, user_id))

    def delete_user(self, user_id):
        with self.db.conn:
            self.db.conn.execute('DELETE FROM Users WHERE id = ?', (user_id,))