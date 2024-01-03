from repo.database_connection import DatabaseConnection
from models.expenses import Expense


class ExpenseController(DatabaseConnection):    

    def create(self, expense: Expense):
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
                    expense.to_tuple())
        
    def get_expenses(self):
        '''
        get all expense records from the database 

        params:
            None

        returns:
            None        
                                
        '''
        expenses = self.get_all("expenses")
        expense_list = []

        for expense in expenses:
            expense_obj = Expense(id=expense[0], name=expense[1], description=expense[2], amount=expense[3])
            expense_list.append(expense_obj)

        return expense_list


    def get_expense(self, id):
        '''
        get a specific expense record from the database

        params:
            id (int): the id of the expense record

        returns:
            None        
                            
        '''
        expense =  self.get("expenses", id)

        expense_obj = Expense(id=expense[0], name=expense[1], description=expense[2], amount=expense[3])
        return expense_obj  
    
    def delete_expense(self, id):
        '''
        removes an expense record from the database 

        params: 
            id (int): the id of the expense record

        returns:
            None        
                
        '''
        self.delete("expenses", id)