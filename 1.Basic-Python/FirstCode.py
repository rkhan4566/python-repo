# SQL And SQLite:-
#SQL (Structured Query Language) is a standard language for managing and manipulating relational databases.
#SQLite is a self-contained, serverless, and zero-configuration database engine that is widely used for embedded database systems.
#In this lesson, we will cover the basics of SQL and SQLite, including creating databases, tables, and performing various SQL operations.

import sqlite3

# connect and SQLite database
connection=sqlite3.connect('example.db')
print(connection)

cursor=connection.cursor()
#create a table
cursor.execute('''
Create Table If Not Exists employees(
    id integer primary key,
    name text not null,
    age integer,
    department text
    ) 
''')
#commit the changes
connection.commit()


###          1.  

cursor.execute('''
select * from employees
     
''')

#insert the data in sqlite table
cursor.execute('''
insert into employees(name,age,department)
               values('rehan',19,'EEE')
''')

cursor.execute('''
insert into employees(name,age,department)
               values('abutalha',19,'EE')
''')

cursor.execute('''
insert into employees(name,age,department)
               values('rkhan',19,'CSE')
''')

#commit the changes
connection.commit()

#query the data from the table
cursor.execute('select * from employees')
rows=cursor.fetchall()

#print the query data
for row in rows:
    print(row)


###             2.

#update the data into table
cursor.execute('''
UPDATE employees 
set age=20
where name is "rehan"             
''')

connection.commit()

#delete the data from the table
cursor.execute('''
delete from employees
               where name is "abutalha"

''')

#query the data from the table
cursor.execute('select * from employees')
rows=cursor.fetchall()

#print the query data
for row in rows:
    print(row)

###            3.

import sqlite3
#working with sales data
##connection to an SQLlite data base
connection=sqlite3.connect('sales_data.db')
cursor=connection.cursor()

#reate a table from sales data
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY,
    date TEXT NOT NULL,
    product TEXT NOT NULL,
    sales INTEGER,
    region TEXT
)
""")

# Insert data into the sales table
sales_data = [
    ('2023-01-01', 'Product1', 100, 'North'),
    ('2023-01-02', 'Product2', 200, 'South'),
    ('2023-01-03', 'Product1', 150, 'East'),
    ('2023-01-04', 'Product3', 250, 'West'),
    ('2023-01-05', 'Product2', 300, 'North')
]

cursor.executemany('''
insert into sales (date,product,sales,region)
                   values(?,?,?,?)

''',sales_data)

connection.commit()

cursor.execute('select * from sales')
rows=cursor.fetchall()

#print the query data
for row in rows:
    print(row)

#closed the connection
connection.close()
