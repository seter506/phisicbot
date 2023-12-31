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

    #вывод не подтвержденных клиентов
    def get_unconf_clients(self):
        with self.connect:
            result=self.cursor.execute("SELECT id, name, last_name, klass,id_tel FROM clients WHERE confirm=0").fetchall()
            return result

    def conf_ok_client(self, id_tel):
        with self.connect:
            self.cursor.execute("UPDATE clients SET confirm=True WHERE id_tel=?",(id_tel,))