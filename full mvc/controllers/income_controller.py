from repo.database_connection import DatabaseConnection
from models.income import Income

class IncomeController(DatabaseConnection):
    
    def create(self, income: Income):
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
                    income.to_tuple())
        
    def get_incomes(self):
        '''
        Get all income records from the database

        returns:
            None
        '''

        incomes = self.get_all("income")
        income_list = []

        for income in incomes:
            income_obj = Income(id=income[0], name=income[1], type=income[2], amount=income[3])
            income_list.append(income_obj)

        return income_list

    
    def get_income(self, id):
        '''
        Get a specific income record from the database

        params:
            id (int): the id of the income record

        returns:
            None        
        '''
        income = self.get("income", id)

        income_obj = Income(id=income[0], name=income[1], type=income[2], amount=income[3])
        return income_obj

    def delete_income(self, id):
        '''
        removes an income record from the database 

        params: 
            id (int): the id of the income record

        returns:
            None        
                
        '''
        self.delete("income", id)