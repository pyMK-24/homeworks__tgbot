import sqlite3

class Database:
    def __init__(self, path: str):
        self.path = path
    
    def create_table(self):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            conn.execute("""
                         CREATE TABLE IF NOT EXISTS reviews(
                             id INTEGER PRIMARY KEY AUTOINCREMENT,
                             name TEXT,
                             phone_number TEXT,
                             rate INTEGER,
                             extra_comments TEXT
                             )""")
            
            conn.execute("""
                         CREATE TABLE IF NOT EXISTS dishes(
                             id INTEGER PRIMARY KEY AUTOINCREMENT,
                             name TEXT,
                             price INTEGER,
                             description TEXT,
                             category TEXT,
                             option TEXT
                             )""")
            
    def save_review(self, data: dict):
        with sqlite3.connect(self.path) as conn:
            conn.execute(
                """INSERT INTO reviews (name,phone_number,rate,extra_comments)
                   VALUES(?,?,?,?)""",
                (data["name"],data["phone_number"],data["rate"],data["extra_comments"])
            )
            
    def save_dish(self, data: dict):
        with sqlite3.connect(self.path) as conn:
            conn.execute("""
                         INSERT INTO dishes (name,price,description,category,option)
                         VALUES(?,?,?,?,?)""",
                         (data["name"],data["price"],data["description"],data["category"],data["option"])
                         )