import sqlite3
import pandas as pd


def main():

     #DB/store is a way to store data
'''Relational DB- MySQl, Sqlite, Oracle, SQL-server, PostgreSQL
    -contains a bunch of tables, table consist of rows and columns
No-SQL DB-

Graph DB
Vector DB-recent Db, storing numbers as vector'''


'''SQL stands for structured query language, talks to the DB programmatically, like an interface between user and DB'''
'''No-SQL DB, eg: mongo-DB, cassandra-DB'''

# SCHEMA A WAY TO DEFINE A DATABASE, COLUMNS AND ROWS IN IT
'''DDl-Data definition language, defines schema
Data manipulation'''

conn = sqlite3.connect('enterprise.db')  # DB is created in the current directory
curs = conn.cursor()
curs.execute('''
                    CREATE TABLE employees
                    (
                        emp_id INT PRIMARY_KEY,
                        emp_name VARCHAR(20),
                        emp_email VARCHAR(20)
                    )
     ''')



if __name__ == '__main__':
    main()