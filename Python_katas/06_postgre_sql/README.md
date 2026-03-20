# use postgres=# \l for listing all databases

# to use any databases -
- postgres=# \c demodb
- You are now connected to database "demodb" as user "postgres".
- demodb=#

# To create database:
- demodb=# create database test;
- CREATE DATABASE

# To delete database:
- demodb=# drop database test;
- DROP DATABASE

# To create table:
- student=# CREATE TABLE students(name text,number int,age int);
- CREATE TABLE
- student=# \d (for showing tables)



# Inserting values to table
- student=# INSERT INTO students(name,number,age) VALUES('Sam',12,20);
- INSERT 0 1
- student=# INSERT INTO students(name,number,age) VALUES('Jake',22,20);
- INSERT 0 1
- student=#

# Showing databases:
>>> student=# SELECT * FROM students;
name | number | age
Sam  | 12     | 20
Jake | 22     | 20
(2 rows)

>>>student=# SELECT name FROM students;
name
Sam
Jake
(2 rows)

>>>student=# SELECT * FROM students WHERE number=12;
name | number | age
Sam  | 12     | 20
(1 row)
student=#

# To create virtual environment into vs code 

>>:\Users\Krishanth\Desktop\Visual_Studio> virtualenv env

# To activate environment:
>>> :\Users\Krishanth\Desktop\Visual_Studio>cd env
:\Users\Krishanth\Desktop\Visual_Studio\env>cd scripts
:\Users\Krishanth\Desktop\Visual_Studio\env\Scripts>activate_



# To connect python script to the postgre sql

> import psycopg2

> conn = psycopg2.connect(dbname="postgres", user="postgres",password="demo123",host="localhost",port="5433")

> cursor = conn.cursor()

> cursor.execute('''create table employees(Name Text, ID int, Age int);''')

> print('Table created successfully')

> conn.commit()

> conn.close()