class Completions:
    """
    This class is responsible for managing the Completions table in the database.
    It sends queries to the database. db is dependency injected from the HabitTrackerDB class
    """
    def __init__(self, db):
        self.db = db

    def add_completion(self, habit_id, completionDate):
        with self.db.conn:
            self.db.conn.execute('INSERT INTO Completions (habit_id, completionDate) VALUES (?, ?)', (habit_id, completionDate))

    def get_completion(self, completion_id):
        cursor = self.db.conn.cursor()
        cursor.execute('SELECT * FROM Completions WHERE id = ?', (completion_id,))
        return cursor.fetchone()

    def get_longest_streak(self, habit_id):
        cursor = self.db.conn.cursor()
        cursor.execute('''
            WITH HabitCompletions AS (
                SELECT 
                    C.habit_id,
                    H.periodicity,
                    C.completionDate,
                    DATE(C.completionDate, 
                        CASE 
                            WHEN H.periodicity = 'daily' THEN '-' || (ROW_NUMBER() OVER (PARTITION BY C.habit_id ORDER BY C.completionDate) - 1) || ' days'
                            WHEN H.periodicity = 'weekly' THEN '-' || (ROW_NUMBER() OVER (PARTITION BY C.habit_id ORDER BY C.completionDate) - 1) * 7 || ' days'
                        END
                    ) AS streak_start
                FROM 
                    Completions C
                JOIN 
                    Habits H ON C.habit_id = H.id
                WHERE 
                    C.habit_id = ?
            )
            SELECT 
                MIN(completionDate) AS start_date,
                MAX(completionDate) AS end_date,
                COUNT(*) AS length
            FROM 
                HabitCompletions
            GROUP BY 
                habit_id, streak_start
            ORDER BY 
                length DESC
            LIMIT 1;
        ''', (habit_id,))
        return cursor.fetchone()

    def update_completion(self, completion_id, habit_id, completionDate):
        with self.db.conn:
            self.db.conn.execute('''
                UPDATE Completions
                SET habit_id = ?, completionDate = ?
                WHERE id = ?
            ''', (habit_id, completionDate, completion_id))

    def delete_completion(self, completion_id):
        with self.db.conn:
            self.db.conn.execute('DELETE FROM Completions WHERE id = ?', (completion_id,))
