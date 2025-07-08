# Exception :  Exception is a event that disrupts the normal of a program's execution.
#              It signifies that an error or unexpected situation has occurred during the runtime.

def handle_exception():
    try:
        num1 = 10
        num2 = 'Hello'
        print(num1+num2)

        print("Good Morning")
    except Exception as e:
        #print(e)
        print("Can not add string with number")

#handle_exception()
#print("Good Morning")



def handle_raise_exception():
    try:
        num1 = 10
        num2 = 'Hello'
        print(num1+num2)

        print("Good Morning")
    except Exception as e:
        print("Can not add string with number")
        raise e

handle_raise_exception()
print("Good Morning")

