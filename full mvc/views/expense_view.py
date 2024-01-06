from controllers.expenses_controller import ExpenseController
from models.expenses import Expense

class ExpenseView():

    def __init__(self) -> None:
        self.expense_obj = ExpenseController()

    def show_expenses(self):
        expenses = self.expense_obj.get_expenses()

        for expense in expenses:        
            print(f"ID: {expense[0]}", f"Title: {expense[1]}", f"Description: {expense[2]}", sep="\n")
            print("-"*40)

    def create_expense(self):
        name = input("Expense Name: ")
        description = input("Expense Description: ")
        amount = input("Expense Amount: ")

        expense = Expense(name, description, amount)

        self.expense_obj.create(expense)
