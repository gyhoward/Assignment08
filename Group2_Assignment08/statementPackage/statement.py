#statement.py

# Name: Josh Halbakken
# email:halbakjc@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date: 3/28/2024
# Course/Section: IS4010
# Semester/Year: Spring 2024
# Brief Description of the assignment: make a query and print statement with output
# Brief Description of what this module does: This module contains our print statement which calls to our query
# Citations:
# Anything else that's relevant:

#This is just testing that we can make a print statement work.
#replace hello with our fact statement
from queryPackage.query import *

def print_statement():
    '''
    Factual statement relating to data
    @return A print statement about our query
    ''' 
    print(f"the employee with the most refunds is {result[0]}{result[1]}with {result[3]} refunds")
    '''for FirstName, LastName, State, TotalTransactions in EmplList:
        print("the employee with most refunds is ") ''' 