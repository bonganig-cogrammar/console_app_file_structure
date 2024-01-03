# Simple Version
This shows a simple way to break the code up

`main.py`
- Handles the user input and prints out the user outputs
- This is the main entry point of the application and connects to all of the other files

`expenses.py` `income.py`
- This is the controller that handles the user input and talks to the `database_connection.py` file to read and write from the database
- Inherits from the `database_connection.py`

`database_connection.py`
- Directly connects to the database and performs the queries.

# Full MVC
This file breaks the files up further by adding views for each controller and models for each controller.

`main.py`
- Entry point for the application, connects to the different views
- Performs any other application operations

`models/`
- These are the models that represent the database objects
- This will be used to pass data between the controller and the view, reducing the number of paramters that are passed when using the controller

`views`
- Handles the input and output for the user
- connects to the controllers

`controller/`
- The controllers that perform operations on each database object
- inherit and connect to the database class

`repo/`
- Holds database services


