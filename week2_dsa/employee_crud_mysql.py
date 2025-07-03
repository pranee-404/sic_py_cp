import pymysql
def connectDb():
    connection = None
    try:
        connection = pymysql.connect(host='localhost',user='root', password='love',
        database='db1',port=3306)
        print('database connected')
    except:
        print('database connection failed')
    return connection

def disconnectDb(connection):
    try:
        connection.close()
        print('db disconnected')
    except:
        print('db disconnection failed')

def create_db():
    query = 'create database IF NOT EXISTS db1'
    connection = connectDb()
    try: 
        cursor = connection.cursor()
        cursor.execute(query)
        print('db created')
        cursor.close()
        disconnectDb(connection)
    except:
        print('db creation failed')

def create_table():
    query = 'create table IF NOT EXISTS employees(id int primary key auto_increment, ' \
    'name varchar(50) not null, designation varchar(30), phone_number bigint unique, ' \
    'salary float, commission float default(0), years_of_experience tinyint, ' \
    'technology	varchar(30)	not null)'
    connection = connectDb()
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        print('Table created')
        cursor.close()
        disconnectDb(connection)
    except:
        print('Table creation failed')

def read_all_employees():
    query = 'select * from employees'
    connection = connectDb()
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        print('All rows retrieved')
        
        cursor.close()
        disconnectDb(connection)
    except:
        print('Rows retrieval failed')

connection = connectDb()
read_all_employees()

#connection.close()