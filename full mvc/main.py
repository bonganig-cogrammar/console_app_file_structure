import os
import sqlite3

from views.expense_view import ExpenseView
from views.income_view import IncomeView

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

    expense = ExpenseView()
    income_view = IncomeView()


    if choice == 1:
        expense.create_expense()
    elif choice == 2:        
        expense.show_expenses()
    elif choice == 3:
        income_view.create_income()
    elif choice == 4:
        income_view.show_income()
    else:
        print("Invalid choice. Please try again.")
    

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


if __name__ == "__main__":
    create_database()

    display_menu()
    choice = int(input("Enter your choice: "))
    select_option(choice)