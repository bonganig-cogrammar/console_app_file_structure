from database_connection import DatabaseConnection


class Income(DatabaseConnection):
    
    def create(self, name, type, amount):
        '''
        add the users income to the database.

        params: 
            name (string): the name for the income 
            type (string): the type of income
            amount (int): the amount of the income
        returns:
            None
        '''

        self.insert(f"INSERT INTO income (name, type, amount) VALUES (?, ?, ?)", 
                    (name, type, amount))
        
    def get_incomes(self):
        '''
        Get all income records from the database

        returns:
            None
        '''
        return self.get_all("income")
    
    def get_income(self, id):
        '''
        Get a specific income record from the database

        params:
            id (int): the id of the income record

        returns:
            None        
        '''
        return self.get("income", id)

    def delete_income(self, id):
        '''
        removes an income record from the database 

        params: 
            id (int): the id of the income record

        returns:
            None        
                
        '''
        self.delete("income", id)