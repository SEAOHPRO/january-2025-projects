from all_actions import *

def welcome_message():
    print("""
    **********************************************
               Welcome to Expense Tracker         
    **********************************************
    Track your daily expenses, stay on budget, and gain insights into your spending habits!
    With this program, you can:
          
    1. Add your expenses with details like category, name, date, and price.
    2. View a summary of all your expenses.
    3. Filter expenses by category or date.
    4. Set a budget and monitor if you're staying within it.
    5. Visualize your spending with easy-to-read graphs.
          
            Start managing your finances today!
    "**********************************************\n""")
    
    return input("Please choose a number to form an action: ")
action = welcome_message()

if   action == 1: 
    op_purchase()

elif action == 2:
    # factor = input("choose factor do search: ")
    # value  = input(f"{factor}: ")
    # search(factor, value)
    pass