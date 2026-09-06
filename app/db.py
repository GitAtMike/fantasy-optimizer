import sqlite3

def init_db(): # Initializes the database and creates the league_info table if it doesn't exist
    connection = sqlite3.connect("fantasy_optimizer.db")
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS league_info (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            week INTEGER UNIQUE,
            date TEXT,
            my_score REAL,
            opponent_score REAL,
            opponent_name TEXT,
            result TEXT
        )
    """)
    connection.commit()
    connection.close()

def log_result(week: int, date: str, my_score: float, opponent_score: float, opponent_name: str, result: str): # Logs the result of a matchup to the league_info table, updating the entry if it already exists for the given week
    connection = sqlite3.connect("fantasy_optimizer.db")
    cursor = connection.cursor()
    cursor.execute("""
        SELECT id FROM league_info WHERE week = ?
        """, (week,))
    existing_entry = cursor.fetchone()
    if existing_entry is None:
        cursor.execute("""
            INSERT INTO league_info(week, date, my_score, opponent_score, opponent_name, result)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (week, date, my_score, opponent_score, opponent_name, result))
    else:
        cursor.execute("""
            UPDATE league_info
            SET date = ?, my_score = ?, opponent_score = ?, opponent_name = ?, result = ?
            WHERE week = ?
        """, (date, my_score, opponent_score, opponent_name, result, week))
    connection.commit()
    connection.close()

def get_all_results(): # Retrieves all results from the league_info table
    connection = sqlite3.connect("fantasy_optimizer.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM league_info")
    results = cursor.fetchall()
    connection.close()
    return results

if __name__ == "__main__":
    init_db()
    print(get_all_results())