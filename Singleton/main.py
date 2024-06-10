from Singleton import Singleton
import sqlite3

class DatabaseConnection(Singleton):
    _connection = None  


    def __init__(self):
        if self._connection is None:
            self._connection = sqlite3.connect("users.db")


    def execute_query(self, query):
        cursor = self._connection.cursor()
        cursor.execute(query)
        self._connection.commit()


    def close(self):
        self._connection.close()


db1 = DatabaseConnection()
db1.execute_query("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")

db2 = DatabaseConnection()
db2.execute_query("INSERT INTO users (name) VALUES ('Alice')")

print(db1 is db2)
db1.close()
db2.close()