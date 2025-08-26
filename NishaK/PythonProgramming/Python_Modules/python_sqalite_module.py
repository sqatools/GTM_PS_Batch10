import sqlite3
from faker import Faker
fk = Faker()


def create_data_base(db_name='student.db'):
    con = sqlite3.connect(db_name)
    return con


def create_a_table(table_query):
    connect = create_data_base()
    connect.execute(table_query)
    connect.close()


# create_table_query = """create table student(name char[20], email char[20], phone char[20], address char[50])"""
# create_a_table(create_table_query)


def insert_data_to_table(insert_query):
    connect = create_data_base()
    connect.execute(insert_query)
    connect.commit()
    connect.close()


# insert_query = """Insert into student(name, email, phone, address) values('Mohit', 'mohit@gmail.com', 787987983, 'Mumbai Boriwali')"""
# insert_data_to_table(insert_query)


# for i in range(50):
#   name = fk.user_name()
#   email = fk.email()
#   phone = fk.phone_number()
#   address = fk.address()
#   insert_query = f"""insert into student(name, email, phone, address) values('{name}', '{email}', '{phone}', '{address}')"""
#   insert_data_to_table(insert_query)


def run_select_query(select_query):
    con = create_data_base()
    data = con.execute(select_query)
    return data


# select_data_query = """select * from student"""
# data = run_select_query(select_data_query)
# print(data)
# for val in data:
#   print(val)


select_data_query2 = """select * from student where phone ='3472026236'"""
data = run_select_query(select_data_query2)
print(data)
for val in data:
    print(val)


select_data_query2 = """select name from student where phone='3472026236'"""
data = list(run_select_query(select_data_query2))
print(data[0][0])
assert data[0][0] == 'nrogers'
