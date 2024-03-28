#query.py

# Name: Alyssa Battaglia
# email:battagaa@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date: 3/28/2024
# Course/Section: IS4010
# Semester/Year: Spring 2024
# Brief Description of the assignment: make a query and print statement with output
# Brief Description of what this module does: This module contains the SQL query
# Citations:
# Anything else that's relevant:

import pyodbc
# We will put the query here- with the summary, filter, and joins
#it will replace the SELECT statement we currently have


    

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=lcb-sql.uccob.uc.edu\\nicholdw;' #make sure you have two backslashes
                      'Database=GroceryStoreSimulator;'
                      'uid=IS4010Login;'  # make sure you have a semicolon between the parameters
                      'pwd=P@ssword2')
# Submit a query to the SQL Server instance and store the results in the cursor object

cursor = conn.cursor()
    
cursor.execute("SELECT TOP (1) tEmpl.FirstName, tEmpl.LastName, tStore.State, SUM(tTransactionType.TransactionTypeID) AS TotalTransactions FROM tStore INNER JOIN tTransaction ON tStore.StoreID = tTransaction.StoreID INNER JOIN tTransactionType ON tTransaction.TransactionTypeID = tTransactionType.TransactionTypeID INNER JOIN tEmpl ON tTransaction.EmplID = tEmpl.EmplID WHERE tStore.State = 'OH' GROUP BY tEmpl.FirstName, tEmpl.LastName, tStore.State ORDER BY TotalTransactions DESC")
result = cursor.fetchone()
EmplList = ()
for row in cursor:
        EmplList.append(row.FirstName.strip())
        EmplList.append(row.LastName.strip())
        EmplList.append(row.State.strip())
        EmplList.append(row.TotalTransactions)
        print(EmplList)
        
