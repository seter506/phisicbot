import sqlite3

class DataBase:
    def __init__(self,file):
        self.connect=sqlite3.connect(file)
        self.cursor=self.connect.cursor()

    def create_table(self):
        with self.connect:
            query="""
            CREATE TABLE IF NOT EXISTS clients(
            id INTEGER PRIMARY KEY,
            id_tel VARCHAR(10),
            name VARCHAR(30),
            last_name VARCHAR(30),
            klass VARCHAR(3),
            confirm BOOLEAN DEFAULT False
            )
            """
            self.cursor.executescript(query)

    def client_exists(self, client_id_tel):
        with self.connect:
            result = self.cursor.execute("SELECT id_tel FROM clients WHERE id_tel=?", (client_id_tel,)).fetchone()
            if result:
                return True
            else:
                return False

    # добавление клиента в базу
    def add_client(self, client_id_tel, client_name, client_last_name, client_klass):
        with self.connect:
           val = [client_id_tel, client_name, client_last_name, client_klass]
           self.cursor.execute("INSERT INTO clients(id_tel, name, last_name, klass) VALUES(?,?,?,?)", val)

    # проверка подтвержденного клиента
    def client_confirm(self, client_id_tel):
        with self.connect:
            result = self.cursor.execute("SELECT confirm FROM clients WHERE id_tel=?", (client_id_tel,)).fetchone()
            if result==None:
                return -1
            else:
                return result[0]