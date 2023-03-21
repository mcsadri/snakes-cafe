"""
Snakes Cafe is a command line utility which will mimic the functionality of a point of sale restaurant system using
basic Python tools and understanding of the basics of the language.

Feature Tasks and Requirements:
* When run, the program should print an intro message and the menu for the restaurant
* The restaurant’s menu should include appetizers, entrees, desserts, and beverages.
* The program should prompt the user for an order
* When a user enters an item, the program should print an acknowledgment of their input
* The program should tell the user how to exit
* The program’s content should match included sample exactly
    * Actually, there’s one tiny spot that should be different - see if you can spot it.
    * The > character represents user input line and should be printed out with a trailing space.

Stretch Goals:
* Print out a summary of complete order.
* Only allow ordering items on the menu.
* Allow ordering items not on menu but give custom reply.
"""

menu = """**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**                                  **
**   To see the menu, type "menu"   **
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************"""

prompt = """
****************************************
** What else would you like to order? **
****************************************"""

order = {
    "Wings": 0,
    "Cookies": 0,
    "Spring Rolls": 0,
    "Salmon": 0,
    "Steak": 0,
    "Meat Tornado": 0,
    "A Literal Garden": 0,
    "Ice Cream": 0,
    "Cake": 0,
    "Pie": 0,
    "Coffee": 0,
    "Tea": 0,
    "Unicorn Tears": 0
}

order_completed = False

def main():
    """
    doodah
    """
    print(menu)
    while order_completed == False:

        ordered_item = input ("> ")
        if ordered_item in order:
            order.update({order: sum()})
            print(ordered_item)
        else:
            print("that's not a valid option")
        print(prompt)



main()

