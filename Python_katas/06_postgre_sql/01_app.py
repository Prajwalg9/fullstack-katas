import psycopg2
conn = psycopg2.connect(dbname="demo", user="postgres",password="viru",host="localhost",port="1800")
cursor = conn.cursor()
cursor.execute('''create table if not exists employee(Name Text, ID int, Age int);''')
print('Table created successfully')
conn.commit()
conn.close()


