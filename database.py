import sqlite3

class Database:
    def __init__(self,path: str):
        self.path = path
        
    def create_tables(self):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            conn.execute("""
                        CREATE TABLE IF NOT EXISTS homeworks(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT,
                            number TEXT,
                            link TEXT
                        )""")
            
    def save_homework(self, data:dict):
        with sqlite3.connect(self.path) as conn:
            conn.execute("""
                         INSERT INTO homeworks (name,number,link)
                         VALUES (?,?,?)""",
                         (data["name"],data["number"],data["link"])
                         )