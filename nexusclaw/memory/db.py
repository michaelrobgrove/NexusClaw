import sqlite3
from typing import Any, Dict, List

class MemoryDB:
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self._create_tables()

    def _create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS preferences (
                user_id TEXT,
                key TEXT,
                value TEXT,
                confidence REAL,
                PRIMARY KEY (user_id, key)
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS patterns (
                user_id TEXT,
                pattern TEXT,
                score REAL,
                PRIMARY KEY (user_id, pattern)
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS outcomes (
                user_id TEXT,
                outcome TEXT,
                timestamp INTEGER
            )
        ''')
        self.conn.commit()

    def upsert_preference(self, user_id: str, key: str, value: str, confidence: float):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO preferences (user_id, key, value, confidence) VALUES (?, ?, ?, ?)
            ON CONFLICT(user_id, key) DO UPDATE SET value=excluded.value, confidence=excluded.confidence
        ''', (user_id, key, value, confidence))
        self.conn.commit()

    def get_preferences(self, user_id: str) -> Dict[str, Any]:
        cursor = self.conn.cursor()
        cursor.execute('SELECT key, value FROM preferences WHERE user_id = ?', (user_id,))
        return {row[0]: row[1] for row in cursor.fetchall()}

    # Additional methods for patterns and outcomes can be added similarly

# Example usage:
# db = MemoryDB('memory.db')
# db.upsert_preference('user1', 'language', 'en', 0.9)
# prefs = db.get_preferences('user1')
# print(prefs)
