import psycopg2

# connect
conn = psycopg2.connect(
    dbname="demo",
    user="postgres",
    password="viru",
    host="localhost",
    port="1800"
)
cursor = conn.cursor()

# 1) create table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS employee(
        Name TEXT,
        ID   INT PRIMARY KEY,
        Age  INT
    );
''')
print("Table created successfully")

# 2) insert data
cursor.execute(
    "INSERT INTO employee (Name, ID, Age) VALUES (%s, %s, %s);",
    ("Viru", 1, 23)
)
cursor.execute(
    "INSERT INTO employee (Name, ID, Age) VALUES (%s, %s, %s);",
    ("Aditya", 2, 21)
)
print("Rows inserted")

# 3) select data
cursor.execute("SELECT * FROM employee;")
rows = cursor.fetchall()
print("All employees:")
for row in rows:
    print(row)

# 4) update data
cursor.execute(
    "UPDATE employee SET Age = %s WHERE ID = %s;",
    (24, 1)
)
print("Row updated")

# 5) delete data
cursor.execute(
    "DELETE FROM employee WHERE ID = %s;",
    (2,)
)
print("Row deleted")

# 6) show final table
cursor.execute("SELECT * FROM employee;")
print("Final data:")
for row in cursor.fetchall():
    print(row)

# commit and close
conn.commit()
cursor.close()
conn.close()
print("Connection closed")
