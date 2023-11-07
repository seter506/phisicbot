import sqlite3

class DataBase:
    def __init__(self,file):
        self.connect=sqlite3.connect(file)
        self.cursor=self.connect.cursor()

    