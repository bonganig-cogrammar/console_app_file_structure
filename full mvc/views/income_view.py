from controllers.expenses_controller import IncomeController
from models.income import Income

class IncomeView():

    def __init__(self) -> None:
        self.income_obj = IncomeController()

    def show_incomes(self):
        incomes = self.income_obj.get_incomes()

        for income in incomes:        
            print(f"ID: {income[0]}", f"Title: {income[1]}", f"Type: {income[2]}", sep="\n")
            print("-"*40)
            

    def create_income(self):
        name = input("Expense Name: ")
        type = input("Expense Description: ")
        amount = input("Expense Amount: ")

        income = Income(name, type, amount)

        self.income_obj.create(income)
