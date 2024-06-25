import sqlite3


class DBManager:

    def __init__(self, dbpath):
        self.path_to_db = dbpath

    def __enter__(self):
        self.connection = sqlite3.connect(self.path_to_db)
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()
