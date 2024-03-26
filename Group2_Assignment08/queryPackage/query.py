#query.py

import pyodbc
# We will put the query here- with the summary, filter, and joins
#it will replace the SELECT statement we currently have

def query_of_data():
    '''
    
    '''

    conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=lcb-sql.uccob.uc.edu\\nicholdw;' #make sure you have two backslashes
                      'Database=GroceryStoreSimulator;'
                      'uid=IS4010Login;'  # make sure you have a semicolon between the parameters
                      'pwd=P@ssword2')
# Submit a query to the SQL Server instance and store the results in the cursor object

    cursor = conn.cursor()
    cursor.execute("SELECT TOP (1) tEmpl.FirstName, tEmpl.LastName, tStore.State, SUM(tTransactionType.TransactionTypeID) AS TotalTransactions FROM tStore INNER JOIN tTransaction ON tStore.StoreID = tTransaction.StoreID INNER JOIN tTransactionType ON tTransaction.TransactionTypeID = tTransactionType.TransactionTypeID INNER JOIN tEmpl ON tTransaction.EmplID = tEmpl.EmplID WHERE tStore.State = 'OH' GROUP BY tEmpl.FirstName, tEmpl.LastName, tStore.State ORDER BY TotalTransactions DESC")
    EmplList = []
    for row in cursor:
        EmplList.append(row.FirstName.strip())
        EmplList.append(row.LastName.strip())
        EmplList.append(row.State.strip())
        EmplList.append(row.TotalTransactions)
        print(EmplList)
