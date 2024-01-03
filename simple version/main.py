import os
import sqlite3
from database_connection import DatabaseConnection
from expenses import Expense
from income import Income

def display_menu():
    '''
    Show the menu options
    '''
    print("1. Add expense\n"
        + "2. View and/or edit expenses\n"
        + "3. Add income\n"
        + "4. View and/or edit income\n"
        + "12. Quit")
    
def select_option(choice):
    '''
    Perform the users required operation
    '''
    if choice == 1:
        add_expense()
    elif choice == 2:
        view_expenses()
    elif choice == 3:
        add_income()
    elif choice == 4:
        view_income()    
    else:
        print("Invalid choice. Please try again.")

def add_expense():
    '''
    Create a new expense row in the databse
    '''
    expense_obj = Expense()

    expense = input("Expense Name: ")
    description = input("Expense Description: ")
    amount = input("Expense Amount: ")

    expense_obj.create(expense, description, amount)

def view_expenses():
    '''
    View all past expenses
    '''
    expense = Expense()

    expenses = expense.get_expenses()

    for expense in expenses:        
        print(f"ID: {expense[0]}", f"Title: {expense[1]}", f"Description: {expense[2]}", sep="\n")
        print("-"*40)

def create_database():
    '''
    Create a new database if there isn't one already 
    '''
    if os.path.isfile('database.db'):
        return
    
    with open("create_tables.sql") as file:
        scripts = file.read()

    with sqlite3.connect('database.db') as db:
        cursor = db.cursor()
        cursor.executescript(scripts)

def add_income():
    '''
    Create a new income record
    '''
    income = Income()

    name = input("Expense Name: ")
    type = input("Expense Description: ")
    amount = input("Expense Amount: ")

    income.create(name, type, amount)

def view_income():
    '''
    view all income items
    '''
    income = Income()

    incomes = income.get_incomes()

    for income in incomes:        
        print(f"ID: {income[0]}", f"Title: {income[1]}", f"Type: {income[2]}", sep="\n")
        print("-"*40)
            


if __name__ == "__main__":
    create_database()

    display_menu()
    choice = int(input("Enter your choice: "))
    select_option(choice)