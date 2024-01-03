import sqlite3

class DatabaseConnection():
        
    def insert(self, query: str, params: tuple):
        '''
        write the values to the database 

        params:
            query (string): The insert SQL query
            parmas (tuple): The values to be inserted

        returns:
            None
        '''
        with sqlite3.connect('database.db') as db:
            cursor = db.cursor()
            cursor.execute(query, (params))

    def get_all(self, table: str):
        '''
        Get all the records from the database

        params:
            table (string): The table name

        returns:
            None
        '''
        with sqlite3.connect('database.db') as db:
            cursor = db.cursor()
            data = cursor.execute(f"SELECT * FROM {table}").fetchall()            
            return data

    def get(self, table: str, id: str):
        '''
        Get a single record from the database

        params:
            table (string): The table name
            id (string): The record id

        returns:
            None
        '''
        with sqlite3.connect('database.db') as db:
            cursor = db.cursor()
            data = cursor.execute(f"SELECT * FROM {table} WHERE id = ? ", (id,))
            return data.fetchone()
        
    def delete(self, table: str, id: str):
        '''
        Delete a single record from the database

        params:
            table (string): The table name
            id (string): The record id

        returns:
            None
        '''
        with sqlite3.connect('database.db') as db:
            cursor = db.cursor()
            cursor.execute(f"DELETE FROM {table} WHERE id = ?", (id,))    

