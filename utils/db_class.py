import sqlite3

class DataBase:
    def __init__(self,file):
        self.connect=sqlite3.connect(file)
        self.cursor=self.connect.cursor()

    def create_table(self):
        with self.connect as db:
            query="""
            CREATE TABLE IF NOT EXISTS clients(
            id INTEGER PRIMARY KEY,
            id_tel VARCHAR(10),
            name VARCHAR(30),
            last_name VARCHAR(30)
            klass VARCHAR(3)
            )
            """
            self.cursor.executescript(query)