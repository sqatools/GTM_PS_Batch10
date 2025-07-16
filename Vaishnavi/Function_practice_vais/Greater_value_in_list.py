def greater(*args):
    second_value=0
    first_value = 0
    list1=0
    for i in args:
        if isinstance(i,list):
            len1=len(i)
            print(len1)
            for k in range(0, len1):
                first_value = i[k]
                if first_value > second_value:
                    greater_value = first_value
                    second_value = first_value
                else:
                    greater_value = second_value
            print(greater_value)
        elif isinstance(i,float):
            continue

#greater(1, 2, 3,[1040,2445,106,3234,3546,3,9,25,790,45],12.6)

def verify_login(**kwargs):
    db_user = 'user1'
    db_pass = 'user@12345'
    if db_user == kwargs['username'] and db_pass == kwargs['password']:
        print("login successful")
    else:
        print("Invalid credentials")

#verify_login(username='user5',password='user@12345')