from database_connection import DatabaseConnection


class Expense(DatabaseConnection):    

    def create(self, expense, description, amount):
        '''
        create a new expense record in the database 

        params:
            expense (str): the name of the expense
            description (str): the description of the expense
            amount (float): the amount of the expense

        returns:
            None        
                                            
        '''
        
        self.insert(f"INSERT INTO expenses (name, description, amount) VALUES (?, ?, ?)", 
                    (expense, description, amount))
        
    def get_expenses(self):
        '''
        get all expense records from the database 

        params:
            None

        returns:
            None        
                                
        '''
        return self.get_all("expenses")


    def get_expense(self, id):
        '''
        get a specific expense record from the database

        params:
            id (int): the id of the expense record

        returns:
            None        
                            
        '''
        return self.get("expenses", id)
    
    def delete_expense(self, id):
        '''
        removes an expense record from the database 

        params: 
            id (int): the id of the expense record

        returns:
            None        
                
        '''
        self.delete("expenses", id)