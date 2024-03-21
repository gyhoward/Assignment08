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
    cursor.execute('SELECT * FROM tCountry')
    for row in cursor:
        print(row)