import sqlite3

def init_db():
    conn = sqlite3.connect("threats.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS threats (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        description TEXT NOT NULL,
                        risk_level TEXT)''')
    conn.commit()
    conn.close()
