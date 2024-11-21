import sqlite3
import pandas as pd



'''Purpose of cursor, connect, sql queries, commit, close'''
'''1.connect- establish a connection between db
   2.cursor- created from connection obj
   3. sql queries are interface through which we can 
   4. pushes the data into the db
   5.'''


'''create db, create tables, insert rows/records, fetch rows/records, update a row/record, delete a row/record'''

def main():
    # conn = sqlite3.connect('enterprise.db')  # DB is created in the current directory
    # curs = conn.cursor()
    # #puprose to create a cursor?/
    # # curs.execute('''
    # #                     CREATE TABLE employees
    # #                     (
    # #                         emp_id INT PRIMARY_KEY,
    # #                         emp_name VARCHAR(20),
    # #                         emp_email VARCHAR(20)
    # #                     )
    # #      ''')
    #
    # # # # insert data
    # # curs.execute('INSERT INTO employees VALUES(1, "Arun", "arun@company.org")')
    # # curs.execute('INSERT INTO employees VALUES(2, "Aditya", "aditya@company.org")')
    # # curs.execute('INSERT INTO employees VALUES(3, "Ashish", "ashish@company.org")')
    # # curs.execute('INSERT INTO employees VALUES(4, "Ankur", "ankur@company.org")')
    #
    # conn.commit()
    # curs.close()


    ### import csv into DB
    conn = sqlite3.connect('brain.db')
    curs = conn.cursor()

    df_data = pd.read_csv('~/PYTHON_LAB/Lab28/brain_size.csv', sep=';', na_values=".")
    df_data.to_sql('brain_size', conn, if_exists='replace', index=False)

    conn.commit()
    curs.close()
    conn.close()

    #execute sql queries

    conn = sqlite3


if __name__ == '__main__':
    main()