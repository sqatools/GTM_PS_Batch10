# 07/07/2025 Session - Absent

import sqlite3
from faker import Faker
fk = Faker()

def create_database(db_name = 'student_database.db'):
    con = sqlite3.connect(db_name)
    return con

def create_table(table_query):
    connect = create_database()
    connect.execute(table_query)
    connect.close()

# create_table_query = """create table student(name char[20], email char[20], phone char[20],address char[50])"""
# create_table(create_table_query)


def insert_data_to_table(insert_query):
    connect = create_database()
    connect.execute(insert_query)
    connect.commit()
    connect.close()

# insert_query = """insert into student(name, email, phone, address) values('Aradhya','aaru@gmail.com','7878787887','Delhi')"""
# print(insert_query)
# insert_data_to_table(insert_query)

# for i in range(50):
#     name = fk.user_name()
#     email = fk.email()
#     phone = fk.phone_number()
#     address = fk.address()
# insert_query = f"""insert into student(name, email, phone, address) values('{name}','{email}','{phone}','{address}')"""
# print(insert_query)
# insert_data_to_table(insert_query)

def run_select_query(select_query):
    con = create_database()
    data = con.execute(select_query)
    return data

# select_data_query = """select * from student"""
"""
data = run_select_query(select_data_query)
print(data)
for val in data:
    print(val)
"""
select_data_query2 = """select * from student where phone='284-573-7004x2397'"""
data = run_select_query(select_data_query2)
print(data)
for val in data:
    print(val)

select_data_query3 = """select name from student where phone='284-573-7004x2397'"""
data = list(run_select_query(select_data_query3))
print(data)
print(data[0][0])
assert data[0][0] == 'christophertorres'
